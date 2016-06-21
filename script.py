#! /usr/bin/env python
import sys
from fabric.tasks import execute
from fabric.api import *
from termcolor import colored

# enable tab autocomplete (used for local path)
import readline, glob
def complete(text, state):
    return (glob.glob(text+'*')+[None])[state]
readline.set_completer_delims(' \t\n;')
readline.set_completer(complete)

'''
# run(command) - Run a shell command on a remote host.
# sudo(comand) - Run a shell command on a remote host, with superuser privileges.
# local(command) - Run a command on the local system.
# open_shell() - Opens an interactive shell on the remote system
# get(remote_path, local_path) - Download one or more files from a remote host.
# put(local_path, remote_path) - Upload one or more files to a remote host.
'''

##############   FUNCTIONS   ##########################


def check_hosts(): # Check each host to see if it's running
	with hide('running'):
		for host, result in execute(run_command, "uname -a", hosts=env.hosts).iteritems():
			if result != "Error":
				running_hosts[host] = result[:result.find("#")]
			else:
				running_hosts[host] = "Host Down"


def active_hosts(): # Show active hosts
	print "\nActive Hosts:"
	print colored("ID\tHost\t\t\tStatus","cyan")
	print colored("----\t---------------\t\t---------------------","green")
	flag = 0	
	for idx, host in enumerate(env.hosts):
		if running_hosts[host] != "Host Down":
			with hide('running'):
				uptime = execute(run_command, "uptime", hosts=host)[host]
			print str(idx)+"\t"+host+"\t"+uptime
			flag = 1
	if flag==0:
		print colored("No active hosts\n","red")
	print "\n"


def list_hosts(): # list all hosts
    	print "\n{0:5} | {1:30} | {2:15}".format("ID", "Host", "SysInfo")
    	print "-" * 60
    	for idx, host in enumerate(env.hosts):
        	print "{0:5} | {1:30} | {2}".format(idx, host, running_hosts[host])
    	print "\n"


def get_hosts(): # Used to get the hosts list. Choosed by user
    	selected_hosts = []
    	tmp = raw_input("Hosts id (0 1 2... / all) [default is all]: ")
    	if tmp == "" or tmp == "all":
		selected_hosts = env.hosts
	else:
    		for num in tmp.split(): 
        		selected_hosts.append(env.hosts[int(num)])
    	return selected_hosts


@parallel
def run_command(command): # Run a command against host/s
	try:
		with hide('running', 'stdout', 'stderr'):
			if command.strip()[0:5] == "sudo":
                		results = sudo(command)
            		else:
                		results = run(command)
    	except:
        	results = 'Error'
	return results
 

def download(): # Download file or folder
	remote_path = raw_input("Remote path: ")
	readline.parse_and_bind("tab: complete") # enable autocomplete		
	local_path = raw_input("Local path: ")
	readline.parse_and_bind('set disable-completion on') # disable autocomplete
	get(remote_path, local_path)


def upload(): # Upload file or folder
	readline.parse_and_bind("tab: complete") # enable autocomplete
	local_path = raw_input("Local path: ")
	readline.parse_and_bind('set disable-completion on') # disable autocomplete
	remote_path = raw_input("Remote path: ")
	remote_path_dir = remote_path[:remote_path.rfind("/")] # path till last '/'
	run('mkdir -p %s'%remote_path_dir) # create dir in path if needed			
	put(local_path, remote_path)


@parallel
def background_run(command):
    command = 'nohup %s &> /dev/null &' % command
    run(command, pty=False)

@parallel
def script_exec(local_path):
	put(local_path, "/tmp/script.fabric", mode=0755)
    	background_run('/tmp/script.fabric')



##############   MENU   ##########################


def menu():
   	for num, desc in enumerate(["List Hosts", "Active Hosts", "Update Hosts", "Run Command", "Open Shell", "File Upload", "File Download", "Script Exec", "Exit"]):
        	print "[" + str(num) + "] " + desc
    	try:        	
		choice = int(raw_input('\nC&C $> '))
   	except KeyboardInterrupt:
		print ""		
		sys.exit()		
	except:
		choice = 0
	return choice


def work(choice):
        list_hosts()
	if choice == 1:
		active_hosts()
	if choice == 2:
		check_hosts()
		print colored("Host List Updated\n","green")
        # run a command
        if choice == 3:
		cmd = raw_input("Command: ")
		# Execute the "run_command" task with the given command "cmd" on the selected hosts
		try:
			with hide('running'):
            			for host, result in execute(run_command, cmd, hosts=get_hosts()).iteritems():
                			print "\n[" + host + "]: " + cmd
                			print ('-' * 80) + '\n' + result + '\n'
		except KeyboardInterrupt:
			print ""			
			sys.exit()
		except:
			print colored("Invalid host id\n","red")        	
	# open a shell
        elif choice == 4:
        	host = int(raw_input("Host id: "))
		try:	           	 	
			execute(open_shell, host=env.hosts[host])
		except KeyboardInterrupt:
			print ""			
			sys.exit()			
		except:
			print colored("Invalid host id\n","red")
	# upload 	
	elif choice == 5:
		execute(upload, hosts=get_hosts())
		print colored("Upload Completed\n","green")		
	# download	
	elif choice == 6:	
		execute(download, hosts=get_hosts())
		print colored("Download Completed\n","green")
	# script exec
	elif choice == 7:
		hosts_list = get_hosts()
		readline.parse_and_bind("tab: complete")
		local_path = raw_input("Local path: ")
		readline.parse_and_bind('set disable-completion on')
		with hide('running','stdout'):
			execute(script_exec, local_path, hosts=hosts_list)
		print colored("Execution Completed\n","green")
		
		

##############   MAIN   ##########################


running_hosts={} # map

print "Loading hosts...\n"

fin = open("creds.txt", "r")
data = fin.readlines()
for line in data:
	try:
		host, password = line.strip().split()
	except Exception:
                host = line.strip()
                password = None
	if len(host.split(':')) == 1:
		host = host + ":22"
	env.hosts.append(host)
	if password is not None:
        	env.passwords[host] = password.strip()

env.skip_bad_hosts=True
env.timeout=2
env.warn_only=True
env.connection_attempts=1
check_hosts()
choice = menu()
while choice != 8:
	work(choice)
	choice = menu()
