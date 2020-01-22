import paramiko
from scp import SCPClient

import appsettings
from appsettings import useHostname

try:
	ssh_client = paramiko.SSHClient()
	ssh_client.set_missing_host_key_policy(paramiko.AutoAddPolicy())
	#ssh_client.connect(hostname='rpitablet.local', username='pi', password='paulina84')
	#ssh_client.connect(hostname=useHostname, username='CEX', password='rom25123012')
	ssh_client.connect(hostname=useHostname, username='ditsa', password='ditsanet')

	'''
	sftp = ssh_client.open_sftp()
	# This will remove a file
	sftp.remove("/home/pi/Documents/New.txt")
	# This will remove a folder
	sftp.rmdir("/home/pi/Documents/New")
	sftp.close()
	'''

	# SCPCLient takes a paramiko transport as an argument
	scp = SCPClient(ssh_client.get_transport())

	# This will copy a file
	#scp.get(remote_path='/home/ditsa/TestLogs/4-SGL.txt', local_path='')
	# This will copy a whole directory
	scp.get(remote_path='/home/ditsa/FormationDataFiles/', local_path='', recursive=True)
	#scp.get(remote_path='/Users/cex/TestLogs/', local_path='', recursive=True)

	scp.close()
	ssh_client.close()
except Exception as e:
	print("Error : " + str(e))