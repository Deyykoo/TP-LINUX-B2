# I. Partitionnement
## 1. LVM dès l'installation

🌞 Faites une install manuelle de Rocky Linux
```
[quentin@TP4 ~]$ lsblk
NAME        MAJ:MIN RM  SIZE RO TYPE MOUNTPOINTS
sda           8:0    0   40G  0 disk
├─sda1        8:1    0   21G  0 part
│ ├─rl-root 253:0    0   10G  0 lvm  /
│ ├─rl-swap 253:1    0    1G  0 lvm  [SWAP]
│ ├─rl-home 253:2    0    5G  0 lvm  /home
│ └─rl-var  253:3    0    5G  0 lvm  /var
└─sda2        8:2    0    1G  0 part /boot
sr0          11:0    1 1024M  0 rom
```
## 2. Scénario remplissage de partition
🌞 Remplissez votre partition /home
```
[quentin@TP4 ~]$ dd if=/dev/zero of=/home/quentin/bigfile bs=4M count=5000
dd: error writing '/home/quentin/bigfile': No space left on device
1171+0 records in
1170+0 records out
4911124480 bytes (4.9 GB, 4.6 GiB) copied, 48.5935 s, 115 MB/s
```
🌞 Constater que la partition est pleine
```
[quentin@TP4 ~]$ df -h
Filesystem           Size  Used Avail Use% Mounted on
devtmpfs             4.0M     0  4.0M   0% /dev
tmpfs                888M     0  888M   0% /dev/shm
tmpfs                356M  5.0M  351M   2% /run
/dev/mapper/rl-root  9.8G  1.1G  8.3G  12% /
/dev/sda2            974M  185M  722M  21% /boot
/dev/mapper/rl-home  4.9G  4.6G     0 100% /home
/dev/mapper/rl-var   4.9G  114M  4.5G   3% /var
tmpfs                178M     0  178M   0% /run/user/1000
```
🌞 Agrandir la partition
```
[quentin@TP4 ~]$ df -h
Filesystem           Size  Used Avail Use% Mounted on
devtmpfs             4.0M     0  4.0M   0% /dev
tmpfs                888M     0  888M   0% /dev/shm
tmpfs                356M  5.0M  351M   2% /run
/dev/mapper/rl-root  9.8G  1.1G  8.3G  12% /
/dev/sda2            2.0G  185M  1.7G  11% /boot
/dev/mapper/rl-home   22G   20G  1.1G  95% /home
/dev/mapper/rl-var   4.9G  114M  4.5G   3% /var
tmpfs                178M     0  178M   0% /run/user/1000
```
🌞 Remplissez votre partition /home
```
[quentin@TP4 ~]$ dd if=/dev/zero of=/home/quentin/bigfile bs=4M count=5000
dd: error writing '/home/quentin/bigfile': No space left on device
4308+0 records in
4307+0 records out
18065813504 bytes (18 GB, 17 GiB) copied, 64.7353 s, 245 MB/s
```
🌞 Utiliser ce nouveau disque pour étendre la partition /home de 40G
```
[quentin@TP4 ~]$ df -h
Filesystem           Size  Used Avail Use% Mounted on
devtmpfs             4.0M     0  4.0M   0% /dev
tmpfs                888M     0  888M   0% /dev/shm
tmpfs                356M  5.0M  351M   2% /run
/dev/mapper/rl-root  9.8G  1.1G  8.3G  12% /
/dev/sda2            974M  185M  722M  21% /boot
/dev/mapper/rl-home   45G   17G   26G  40% /home
/dev/mapper/rl-var   4.9G  114M  4.5G   3% /var
tmpfs                178M     0  178M   0% /run/user/1000
```
# II. Gestion de users
🌞 Gestion basique de users
```
[quentin@TP4 ~]$ cat /etc/group | grep -E "alice|bob|charlie|eve|backup"
alice:x:1002:
bob:x:1003:
charlie:x:1004:
eve:x:1005:
backup:x:1006:
admins:x:1007:alice,bob,charlie
``` 
🌞 La conf sudo doit être la suivante
```
%admins ALL=(ALL)       NOPASSWD: ALL
```
🌞 Le dossier /var/backup
```
[quentin@TP4 ~]$ sudo chmod 600 /var/backup/
```
🌞 Mots de passe des users, prouvez que
```
[quentin@TP4 ~]$ sudo passwd -S bob
bob PS 2025-01-13 0 99999 7 -1 (Password set, SHA512 crypt.)
```
🌞 User eve
```
[eve@localhost ~]$ sudo -u backup ls
ls: cannot open directory '.': Permission denied
[eve@localhost ~]$ sudo -u backup cat
Sorry, user eve is not allowed to execute '/bin/cat' as backup on localhost.localdomain.



[eve@localhost ~]$ sudo -l
User eve may run the following commands on localhost:
    (backup) /bin/ls
```
# III. Gestion du temps
🌞 Je vous laisse gérer le bail vous-mêmes
- déterminez quel service sur Rocky Linux est le client NTP par défaut
```
[quentin@TP4 ~]$ systemctl list-units -t service -a | grep chrony
  chronyd.service
                loaded    active   running NTP client/server
```
- demandez à ce service de se synchroniser sur les serveurs français du NTP Pool Project
```
fr.pool.ntp.org
```
- assurez-vous que vous êtes synchronisés sur l'heure de Paris
```
[quentin@TP4 ~]$ timedatectl
               Local time: Wed 2025-01-22 14:47:32 CET
           Universal time: Wed 2025-01-22 13:47:32 UTC
                 RTC time: Wed 2025-01-22 13:47:32
                Time zone: Europe/Paris (CET, +0100)
System clock synchronized: yes
              NTP service: active
          RTC in local TZ: no
```