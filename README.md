# Brute Force Login Simulator

## Description
This project simulates a brute force attack on a mock login form hosted on a local server. The script iterates through a list of passwords (wordlist) and attempts to log in using each password, logging the success or failure of each attempt. This project is intended for educational purposes to demonstrate the importance of securing web applications against brute force attacks.

## File Structure
- **mock_server/**: Contains the Flask server to host a mock login page.
- **brute_force.py**: The brute force simulation script.
- **wordlist.txt**: List of passwords for brute force attempts.
- **logs/login_attempts.log**: Log file for recording the results of each login attempt.

## How to Use
1. Navigate to the mock_server directory:
  cd mock_server

2. Start the Flask mock server:
  python app.py

Note: The server will start on http://127.0.0.1:5000 by default.

4. Prepare the Wordlist
  Open another terminal window, navigate back to the main project directory (where brute_force.py is located):
like this: cd /path/to/BruteForceLoginSimulator
   
5. Run the brute force script:
  python brute_force.py

7. Step 4: Check the Logs
  After the script finishes running, you can check the results of the login attempts in the logs/login_attempts.log file. This file will contain a record of each login attempt, including whether it was successful or failed.

## Requirements
Before you begin, ensure you have Python 3 installed on your system. You can download it from [python.org](https://www.python.org/downloads/).

Additionally, you will need to install the Flask library. You can do this using pip:
```bash
pip install Flask
