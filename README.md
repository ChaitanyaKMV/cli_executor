# CLI Executor Service

CLI Executor Service is a Python application that provides a REST API for executing command-line interface (CLI) commands on a remote machine via SSH.

The service allows users to send requests to an endpoint with the necessary information, including the IP address of the target machine, authentication credentials, and a list of commands to execute. The service establishes an SSH connection to the remote machine and executes the specified commands, returning the output as a JSON object.

## Prerequisites

To run the CLI Executor Service, you need to have the following dependencies installed:

- Python (version 3.6 or higher)
- Flask (install via `pip install flask`)
- Paramiko (install via `pip install paramiko`)

## Usage

1. Clone the repository to your local machine:


2. Navigate to the project directory:


3. Install the required dependencies:

pip install -r requirements.txt

4. Start the service:

python app.py

The service will be available at `http://localhost:5000/`.

## API Endpoints

The CLI Executor Service provides the following API endpoint:

- **POST** `/execute`

Execute CLI commands on a remote machine.

Request body parameters:
- `ip` (string): IP address of the target machine.
- `username` (string): Username for SSH authentication.
- `password` (string): Password for SSH authentication.
- `commands` (list): List of CLI commands to execute.

### Example request:
```json
{
 "ip": "192.168.1.100",
 "username": "admin",
 "password": "password123",
 "commands": [
   "command1",
   "command2",
   "command3"
 ]
}

### Example response:

[
  {
    "command": "command1",
    "stdout": "output of command1",
    "stderr": "error message (if any)"
  },
  {
    "command": "command2",
    "stdout": "output of command2",
    "stderr": "error message (if any)"
  },
  {
    "command": "command3",
    "stdout": "output of command3",
    "stderr": "error message (if any)"
  }
]

# Contributing
Contributions to the CLI Executor Service are welcome! If you find any issues or have suggestions for improvements, please open an issue or submit a pull request.

When contributing, please follow these guidelines:

Fork the repository and create a new branch for your contribution.
Make your changes and ensure they are properly tested.
Write clear and concise commit messages.
Submit a pull request explaining your changes.

# License
This project is licensed under the MIT License. See the LICENSE file for details.


Feel free to modify and customize this template to fit your specific project requirements.
