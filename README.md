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

   create a text file as `requirements.txt` and add above dependencies
   Do install using pip in one shot `pip install -r requirements.txt`

4. Start the service:

   python `app_name.py`

The service will be available at `http://localhost:5000/`.

[To run as a Service](#Run-cli_executor-as-a-backend-service)

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
```

### Example response:
```
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
```
## Run-cli_executor-as-a-backend-service
### On LINUX
To run the script as a service continuously and in the background, you can use a process manager like systemd (on Linux) or NSSM (on Windows). These process managers allow you to create and manage background services.

Here's an example of how to use systemd to run the script as a service on a Linux system:

1. Create a systemd service unit file. Open a terminal and run the following command to create a new service unit file:

   `sudo nano /etc/systemd/system/cli_executor.service`

2. Add the following content to the 'cli_executor.service' file:
   ```
   [Unit]
   Description=CLI Executor Service
   After=network.target

   [Service]
   ExecStart=/usr/bin/python3 /path/to/cli_executor.py
   WorkingDirectory=/path/to/
   StandardOutput=syslog
   StandardError=syslog
   SyslogIdentifier=cli_executor
   User=your_username
   Group=your_groupname

   [Install]
   WantedBy=multi-user.target
   ```
   Make sure to replace `/path/to/cli_executor.py` with the actual path to your Python script. 
   Adjust the User and Group values to match the user and group you want the service to run as.

3. Save the file and exit the text editor.

4. Enable and start the service. Run the following commands to enable the service and start it:

   ```
   sudo systemctl enable cli_executor
   sudo systemctl start cli_executor
   ```
   The service will now be running in the background. You can check the status of the service using sudo systemctl status cli_executor.

### On Windows, you can use NSSM (Non-Sucking Service Manager) to achieve a similar result. Here are the steps:

1. Download NSSM from the official website: https://nssm.cc/download. Choose the appropriate version for your system (32-bit or 64-bit).

2. Extract the NSSM executable (nssm.exe) to a directory of your choice.

3. Open a command prompt with administrator privileges and navigate to the directory where you extracted NSSM.

4. Install the script as a service by running the following command:

   `nssm install CLI_Executor "C:\path\to\python.exe" "C:\path\to\cli_executor.py"`

   Replace `C:\path\to\python.exe` with the actual path to your Python executable, and `C:\path\to\cli_executor.py` with the actual path to your Python script.
5. In the 'NSSM' GUI that opens, configure the service parameters as desired (e.g., set the startup directory, set the username and password, etc.). Click "Install service" to create the service.
6. Start the service by running the following command:

   `nssm start CLI_Executor`
   The service will now be running in the background. You can check the status of the service using nssm status CLI_Executor.
   With these steps, you can ensure that the script runs continuously as a background service, even if the console or terminal is closed.

# Contributing
Contributions to the CLI Executor Service are welcome! If you find any issues or have suggestions for improvements, please open an issue or submit a pull request.

When contributing, please follow these guidelines:

* Fork the repository and create a new branch for your contribution.
* Make your changes and ensure they are properly tested.
* Write clear and concise commit messages.
* Submit a pull request explaining your changes.

## About the Author

My name is Chaitanya, and I work as a Software Engineer specializing in Automation Testing. I have a keen interest in automating tasks and simplifying workflows. If you have any questions or suggestions related to this project, feel free to reach out.

Connect with me on LinkedIn: [Chaitanya Profile]([https://www.linkedin.com/in/your-linkedin-profile-url](https://www.linkedin.com/in/chaitanya-kumar-kakarla/))


## License

This project is licensed under the MIT License. See the [LICENSE](LICENSE) file for details.

Feel free to modify and customize this template to fit your specific project requirements.
