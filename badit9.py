import paramiko

hostname = "bandit.labs.overthewire.org"
port = 2220
username = "bandit9"
password = "UsvVyFSfZZWbi6wgC7dAFyFuR6jQQUhR"

cmd = "strings data.txt"
#connect to server
ssh = paramiko.SSHClient()
ssh.set_missing_host_key_policy(paramiko.AutoAddPolicy())
ssh.connect(hostname, port, username, password)
#connect to server
#read the readme in server and print
stdin, stdout, stderr = ssh.exec_command(cmd)
lines = stdout.readlines()
print(lines[0])