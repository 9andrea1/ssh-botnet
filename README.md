# ssh botnet c&c 
ssh botnet c&amp;c

'''shell
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
    0 | root@127.0.0.1:22              | Host Down
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
    0 | root@127.0.0.1:22              | Host Down
    1 | root@192.168.6.100:22          | Linux sk-srv16 3.11.0-18-generic 



Active Hosts:
ID	Host			Status
----	---------------		---------------------
1	root@192.168.6.100:22	10:33:34 up 211 days, 21:25,  1 user,  load average: 0.00, 0.01, 0.05


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
    0 | root@127.0.0.1:22              | Host Down
    1 | root@192.168.6.100:22          | Linux sk-srv16 3.11.0-18-generic 


Command: id
Hosts id (0 1 2... / all) [default is all]: 1

[root@192.168.6.100:22]: id
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
'''
