# ssh botnet 
add ssh credentials into 'creds.txt' file and run './script.py'

## Example
```shell
root@kali:~/script/ssh_botnet# ./script.py 
Loading hosts...

[0] List Hosts
[1] Active Hosts
[2] Update Hosts
[3] Run Command
[4] Open Shell
[5] File Upload
[6] File Download
[7] Script Exec
[8] Exit

C&C $> 0

ID    | Host                           | SysInfo        
------------------------------------------------------------
    0 | root@127.0.0.1:22              | Linux kali 4.0.0-kali1-amd64
    1 | root@192.168.6.100:22          | Linux sk-srv16 3.11.0-18-generic 


[0] List Hosts
[1] Active Hosts
[2] Update Hosts
[3] Run Command
[4] Open Shell
[5] File Upload
[6] File Download
[7] Script Exec
[8] Exit

C&C $> 1

ID    | Host                           | SysInfo        
------------------------------------------------------------
    0 | root@127.0.0.1:22              | Linux kali 4.0.0-kali1-amd64
    1 | root@192.168.6.100:22          | Linux sk-srv16 3.11.0-18-generic 


Active Hosts:
ID	    Host			        Status
----	---------------		    ---------------------
0	    root@127.0.0.1:22	    12:07:32 up  2:42,  3 users,  load average: 0.42, 0.29, 0.29
1	    root@192.168.6.100:22	12:07:33 up 227 days, 22:59,  1 user,  load average: 0.23, 0.06, 0.06


[0] List Hosts
[1] Active Hosts
[2] Update Hosts
[3] Run Command
[4] Open Shell
[5] File Upload
[6] File Download
[7] Script Exec
[8] Exit

C&C $> 3

ID    | Host                           | SysInfo        
------------------------------------------------------------
    0 | root@127.0.0.1:22              | Linux kali 4.0.0-kali1-amd64
    1 | root@192.168.6.100:22          | Linux sk-srv16 3.11.0-18-generic 


Command: id
Hosts id (0 1 2... / all) [default is all]: 

[root@192.168.6.100:22]: id
--------------------------------------------------------------------------------
uid=0(root) gid=0(root) groups=0(root)


[root@127.0.0.1:22]: id
--------------------------------------------------------------------------------
uid=0(root) gid=0(root) groups=0(root)

[0] List Hosts
[1] Active Hosts
[2] Update Hosts
[3] Run Command
[4] Open Shell
[5] File Upload
[6] File Download
[7] Script Exec
[8] Exit

C&C $> 4

ID    | Host                           | SysInfo        
------------------------------------------------------------
    0 | root@127.0.0.1:22              | Linux kali 4.0.0-kali1-amd64 
    1 | root@192.168.6.100:22          | Linux sk-srv16 3.11.0-18-generic 


Host id: 0
[root@127.0.0.1:22] Executing task 'open_shell'
Last login: Tue Jun 21 10:38:12 2016 from localhost
root@kali:~# id
uid=0(root) gid=0(root) groups=0(root)
root@kali:~#
```
