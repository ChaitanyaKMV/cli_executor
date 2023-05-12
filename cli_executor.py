from flask import Flask, request, jsonify
import paramiko

app = Flask(__name__)

@app.route('/execute', methods=['POST'])
def execute_commands():
    # Extract request data
    data = request.get_json()
    machine_ip = data.get('ip')
    username = data.get('username')
    password = data.get('password')
    commands = data.get('commands')

    if not machine_ip or not username or not password or not commands:
        return jsonify({'error': 'Missing required parameters.'}), 400

    try:
        # Establish SSH connection
        ssh = paramiko.SSHClient()
        ssh.set_missing_host_key_policy(paramiko.AutoAddPolicy())
        ssh.connect(machine_ip, username=username, password=password)

        results = []
        for command in commands:
            if not command:
                continue  # Skip empty commands

            try:
                # Execute command on the remote machine
                stdin, stdout, stderr = ssh.exec_command(command)

                # Read the output and error streams
                output = stdout.read().decode('utf-8').strip()
                error = stderr.read().decode('utf-8').strip()

                results.append({
                    'command': command,
                    'stdout': output,
                    'stderr': error
                })

            except paramiko.SSHException as e:
                results.append({
                    'command': command,
                    'stdout': '',
                    'stderr': f'SSHException: {str(e)}'
                })

        # Close the SSH connection
        ssh.close()

        return jsonify(results), 200

    except paramiko.AuthenticationException:
        return jsonify({'error': 'Authentication failed.'}), 401

    except paramiko.SSHException as e:
        return jsonify({'error': f'SSH connection failed: {str(e)}'}), 500

    except Exception as e:
        return jsonify({'error': f'An error occurred: {str(e)}'}), 500

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000)


#endpoint: http://localhost:5000/execute
#example request json body input
input_string = '''
{
  "ip": "remote_machine_ip",
  "username": "remote_username",
  "password": "remote_password",
  "commands": [
    "ls",
    "pwd"
  ]
}

'''
