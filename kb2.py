import paramiko

hostname = "bandit.labs.overthewire.org"
port = 2220
username = "bandit2"
password = "CV1DtqXWVFXTvM2F0k09SHz0YwRINYA9"

cmd = 'cat "spaces in this filename"'
#connect to server
ssh = paramiko.SSHClient()
ssh.set_missing_host_key_policy(paramiko.AutoAddPolicy())
ssh.connect(hostname, port, username, password)
#connect to server
#read the readme in server and print
stdin, stdout, stderr = ssh.exec_command(cmd)
lines = stdout.readlines()
print(lines) 