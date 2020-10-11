#Module required for ssh
import paramiko

cmd = 'cat *'
client = paramiko.SSHClient()
client.set_missing_host_key_policy(paramiko.WarningPolicy())
client.connect('bandit.labs.overthewire.org', username='bandit0', password='bandit0')
ssh_stdin, ssh_stdout, ssh_stderr = client.exec_command(cmd)

print("Your command: " + cmd + '\n')
print('Output: ')
print(ssh_stdout.read().decode())
