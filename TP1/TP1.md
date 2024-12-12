# I. Init
🌞 Ajouter votre utilisateur au groupe docker
```powershell
- commande : sudo usermod -aG docker quentin

    [quentin@TP1 ~]$ docker ps
    CONTAINER ID   IMAGE     COMMAND   CREATED   STATUS    PORTS     NAMES
```
🌞 Lancer un conteneur NGINX
```powershell
[quentin@TP1 ~]$ docker run -d -p 9999:80 nginx
82d795f14e05fa2fbc0fd25e48c7116ec9170ccb662e0e6bfcae9994c5cdb31c
```
🌞 Visitons
```powershell
[quentin@TP1 ~]$ docker ps🌞
CONTAINER ID   IMAGE     COMMAND                  CREATED         STATUS         PORTS
   NAMES
82d795f14e05   nginx     "/docker-entrypoint.…"   6 minutes ago   Up 6 minutes   0.0.0.0:9999->80/tcp, [::]:9999->80/tcp   priceless_satoshi



[quentin@TP1 ~]$ docker logs 82d795f14e05🌞
/docker-entrypoint.sh: /docker-entrypoint.d/ is not empty, will attempt to perform configuration
/docker-entrypoint.sh: Looking for shell scripts in /docker-entrypoint.d/
/docker-entrypoint.sh: Launching /docker-entrypoint.d/10-listen-on-ipv6-by-default.sh
10-listen-on-ipv6-by-default.sh: info: Getting the checksum of /etc/nginx/conf.d/default.conf
10-listen-on-ipv6-by-default.sh: info: Enabled listen on IPv6 in /etc/nginx/conf.d/default.conf
/docker-entrypoint.sh: Sourcing /docker-entrypoint.d/15-local-resolvers.envsh
/docker-entrypoint.sh: Launching /docker-entrypoint.d/20-envsubst-on-templates.sh
/docker-entrypoint.sh: Launching /docker-entrypoint.d/30-tune-worker-processes.sh
/docker-entrypoint.sh: Configuration complete; ready for start up
2024/12/11 15:05:47 [notice] 1#1: using the "epoll" event method
2024/12/11 15:05:47 [notice] 1#1: nginx/1.27.3
2024/12/11 15:05:47 [notice] 1#1: built by gcc 12.2.0 (Debian 12.2.0-14)
2024/12/11 15:05:47 [notice] 1#1: OS: Linux 5.14.0-427.13.1.el9_4.x86_64
2024/12/11 15:05:47 [notice] 1#1: getrlimit(RLIMIT_NOFILE): 1073741816:1073741816
2024/12/11 15:05:47 [notice] 1#1: start worker processes
2024/12/11 15:05:47 [notice] 1#1: start worker process 28



[quentin@TP1 ~]$ docker inspect -s 82d795f14e05🌞
[
    {
        "Id": "82d795f14e05fa2fbc0fd25e48c7116ec9170ccb662e0e6bfcae9994c5cdb31c",
        "Created": "2024-12-11T15:05:47.590288543Z",
        "Path": "/docker-entrypoint.sh",
        "Args": [
            "nginx",
            "-g",
            "daemon off;"
        ],
        "State": {
            "Status": "running",
            "Running": true,
            "Paused": false,
            "Restarting": false,
            "OOMKilled": false,
            "Dead": false,
            "Pid": 13945,
            "ExitCode": 0,
            "Error": "",
            "StartedAt": "2024-12-11T15:05:47.675047488Z",
            "FinishedAt": "0001-01-01T00:00:00Z"
        },
        "Image": "sha256:66f8bdd3810c96dc5c28aec39583af731b34a2cd99471530f53c8794ed5b423e",
        "ResolvConfPath": "/var/lib/docker/containers/82d795f14e05fa2fbc0fd25e48c7116ec9170ccb662e0e6bfcae9994c5cdb31c/resolv.conf",
        "HostnamePath": "/var/lib/docker/containers/82d795f14e05fa2fbc0fd25e48c7116ec9170ccb662e0e6bfcae9994c5cdb31c/hostname",
        "HostsPath": "/var/lib/docker/containers/82d795f14e05fa2fbc0fd25e48c7116ec9170ccb662e0e6bfcae9994c5cdb31c/hosts",
        "LogPath": "/var/lib/docker/containers/82d795f14e05fa2fbc0fd25e48c7116ec9170ccb662e0e6bfcae9994c5cdb31c/82d795f14e05fa2fbc0fd25e48c7116ec9170ccb662e0e6bfcae9994c5cdb31c-json.log",
        "Name": "/priceless_satoshi",
        "RestartCount": 0,
        "Driver": "overlay2",
        "Platform": "linux",
        "MountLabel": "",
        "ProcessLabel": "",
        "AppArmorProfile": "",
        "ExecIDs": null,
        "HostConfig": {
            "Binds": null,
            "ContainerIDFile": "",
            "LogConfig": {
                "Type": "json-file",
                "Config": {}
            },
            "NetworkMode": "bridge",
            "PortBindings": {
                "80/tcp": [
                    {
                        "HostIp": "",
                        "HostPort": "9999"
                    }
                ]
            },
            "RestartPolicy": {
                "Name": "no",
                "MaximumRetryCount": 0
            },
            "AutoRemove": false,
            "VolumeDriver": "",
            "VolumesFrom": null,
            "ConsoleSize": [
                41,
                156
            ],
            "CapAdd": null,
            "CapDrop": null,
            "CgroupnsMode": "private",
            "Dns": [],
            "DnsOptions": [],
            "DnsSearch": [],
            "ExtraHosts": null,
            "GroupAdd": null,
            "IpcMode": "private",
            "Cgroup": "",
            "Links": null,
            "OomScoreAdj": 0,
            "PidMode": "",
            "Privileged": false,
            "PublishAllPorts": false,
            "ReadonlyRootfs": false,
            "SecurityOpt": null,
            "UTSMode": "",
            "UsernsMode": "",
            "ShmSize": 67108864,
            "Runtime": "runc",
            "Isolation": "",
            "CpuShares": 0,
            "Memory": 0,
            "NanoCpus": 0,
            "CgroupParent": "",
            "BlkioWeight": 0,
            "BlkioWeightDevice": [],
            "BlkioDeviceReadBps": [],
            "BlkioDeviceWriteBps": [],
            "BlkioDeviceReadIOps": [],
            "BlkioDeviceWriteIOps": [],
            "CpuPeriod": 0,
            "CpuQuota": 0,
            "CpuRealtimePeriod": 0,
            "CpuRealtimeRuntime": 0,
            "CpusetCpus": "",
            "CpusetMems": "",
            "Devices": [],
            "DeviceCgroupRules": null,
            "DeviceRequests": null,
            "MemoryReservation": 0,
            "MemorySwap": 0,
            "MemorySwappiness": null,
            "OomKillDisable": null,
            "PidsLimit": null,
            "Ulimits": [],
            "CpuCount": 0,
            "CpuPercent": 0,
            "IOMaximumIOps": 0,
            "IOMaximumBandwidth": 0,
            "MaskedPaths": [
                "/proc/asound",
                "/proc/acpi",
                "/proc/kcore",
                "/proc/keys",
                "/proc/latency_stats",
                "/proc/timer_list",
                "/proc/timer_stats",
                "/proc/sched_debug",
                "/proc/scsi",
                "/sys/firmware",
                "/sys/devices/virtual/powercap"
            ],
            "ReadonlyPaths": [
                "/proc/bus",
                "/proc/fs",
                "/proc/irq",
                "/proc/sys",
                "/proc/sysrq-trigger"
            ]
        },
        "GraphDriver": {
            "Data": {
                "LowerDir": "/var/lib/docker/overlay2/d22ae4c291cb7f9beaeb80950f634b3c15a32c29bc1ff3da21ad3994a386a8b5-init/diff:/var/lib/docker/overlay2/589a1806e6ecf6b50d020d393819470ad49179b98421f0a4ffd9eff61be4d3d2/diff:/var/lib/docker/overlay2/44f0eb83a5ef1a33484067570a0ff22472709ff852fe229e4ceab7002d1a336b/diff:/var/lib/docker/overlay2/a6ea36d74a6738f39fbd106cc55482daed52febb40354460f09ddb7953b59b5d/diff:/var/lib/docker/overlay2/8e76e970520d9a1a3e43f1f21030e7410691759589e6861ada12dc18cf96219c/diff:/var/lib/docker/overlay2/0ca0299ca3b5a333130d435bb4551eab9663f744429b1cc01e3576dfcca21999/diff:/var/lib/docker/overlay2/36b5b06be2496b1385fb4b662c61d8423524d48d42836d3592b5ce1f23e7c3e5/diff:/var/lib/docker/overlay2/8b404634bf89c9b4aadc8d4e0c7da39eb2d457e5a15c0717a3685bca48652b34/diff",
                "MergedDir": "/var/lib/docker/overlay2/d22ae4c291cb7f9beaeb80950f634b3c15a32c29bc1ff3da21ad3994a386a8b5/merged",
                "UpperDir": "/var/lib/docker/overlay2/d22ae4c291cb7f9beaeb80950f634b3c15a32c29bc1ff3da21ad3994a386a8b5/diff",
                "WorkDir": "/var/lib/docker/overlay2/d22ae4c291cb7f9beaeb80950f634b3c15a32c29bc1ff3da21ad3994a386a8b5/work"
            },
            "Name": "overlay2"
        },
        "SizeRw": 1095,
        "SizeRootFs": 191759507,
        "Mounts": [],
        "Config": {
            "Hostname": "82d795f14e05",
            "Domainname": "",
            "User": "",
            "AttachStdin": false,
            "AttachStdout": false,
            "AttachStderr": false,
            "ExposedPorts": {
                "80/tcp": {}
            },
            "Tty": false,
            "OpenStdin": false,
            "StdinOnce": false,
            "Env": [
                "PATH=/usr/local/sbin:/usr/local/bin:/usr/sbin:/usr/bin:/sbin:/bin",
                "NGINX_VERSION=1.27.3",
                "NJS_VERSION=0.8.7",
                "NJS_RELEASE=1~bookworm",
                "PKG_RELEASE=1~bookworm",
                "DYNPKG_RELEASE=1~bookworm"
            ],
            "Cmd": [
                "nginx",
                "-g",
                "daemon off;"
            ],
            "Image": "nginx",
            "Volumes": null,
            "WorkingDir": "",
            "Entrypoint": [
                "/docker-entrypoint.sh"
            ],
            "OnBuild": null,
            "Labels": {
                "maintainer": "NGINX Docker Maintainers <docker-maint@nginx.com>"
            },
            "StopSignal": "SIGQUIT"
        },
        "NetworkSettings": {
            "Bridge": "",
            "SandboxID": "bd769b560d44e7d361f6fd975084d6ea653c378a84c1e64520d9799e8b89a2be",
            "SandboxKey": "/var/run/docker/netns/bd769b560d44",
            "Ports": {
                "80/tcp": [
                    {
                        "HostIp": "0.0.0.0",
                        "HostPort": "9999"
                    },
                    {
                        "HostIp": "::",
                        "HostPort": "9999"
                    }
                ]
            },
            "HairpinMode": false,
            "LinkLocalIPv6Address": "",
            "LinkLocalIPv6PrefixLen": 0,
            "SecondaryIPAddresses": null,
            "SecondaryIPv6Addresses": null,
            "EndpointID": "4132a610739cd1f3e15444ccddc3e4d4e226fe37a24d2dd2f11bf68b77b6d88b",
            "Gateway": "172.17.0.1",
            "GlobalIPv6Address": "",
            "GlobalIPv6PrefixLen": 0,
            "IPAddress": "172.17.0.2",
            "IPPrefixLen": 16,
            "IPv6Gateway": "",
            "MacAddress": "02:42:ac:11:00:02",
            "Networks": {
                "bridge": {
                    "IPAMConfig": null,
                    "Links": null,
                    "Aliases": null,
                    "MacAddress": "02:42:ac:11:00:02",
                    "DriverOpts": null,
                    "NetworkID": "4d860dd0c1c4b2db6af174a6074b09397644a64bd06bcaf266d7c4103043c0e9",
                    "EndpointID": "4132a610739cd1f3e15444ccddc3e4d4e226fe37a24d2dd2f11bf68b77b6d88b",
                    "Gateway": "172.17.0.1",
                    "IPAddress": "172.17.0.2",
                    "IPPrefixLen": 16,
                    "IPv6Gateway": "",
                    "GlobalIPv6Address": "",
                    "GlobalIPv6PrefixLen": 0,
                    "DNSNames": null
                }
            }
        }
    }
]



[quentin@TP1 ~]$ sudo ss -lnpt
[sudo] password for quentin:
State       Recv-Q       Send-Q             Local Address:Port             Peer Address:Port      Process
LISTEN      0            128                      0.0.0.0:22                    0.0.0.0:*          users:(("sshd",pid=716,fd=3))
LISTEN      0            4096                     🌞0.0.0.0:9999🌞                  0.0.0.0:*          users:(("docker-proxy",pid=13898,fd=4))
LISTEN      0            128                         [::]:22                       [::]:*          users:(("sshd",pid=716,fd=4))
LISTEN      0            4096                        [::]:9999                     [::]:*          users:(("docker-proxy",pid=13905,fd=4))



[quentin@TP1 ~]$ sudo firewall-cmd --permanent --add-port=9999/tcp🌞
success
[quentin@TP1 ~]$ sudo firewall-cmd --reload
success
```
🌞 On va ajouter un site Web au conteneur NGINX
```powershell
[quentin@TP1 ~]$ sudo cat nginx/index.html🌞
[sudo] password for quentin:
<h1>MEOWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWW<h1>



[quentin@TP1 ~]$ sudo cat nginx/site_nul.conf🌞
[sudo] password for quentin:
server {
    listen        8080;

    location / {
        root /var/www/html;
    }
}
```
🌞 Visitons
```powershell
[quentin@TP1 ~]$ docker ps
CONTAINER ID   IMAGE     COMMAND                  CREATED          STATUS          PORTS                                                 NAMES
68d8428419e0   nginx     "/docker-entrypoint.…"   14 seconds ago   Up 13 seconds   80/tcp, 0.0.0.0:9999->8080/tcp, [::]:9999->8080/tcp   nervous_sammet
```
🌞 Lance un conteneur Python, avec un shell
```powershell
[quentin@TP1 ~]$ docker run -it python bash
Unable to find image 'python:latest' locally
latest: Pulling from library/python
fdf894e782a2: Pull complete
5bd71677db44: Pull complete
551df7f94f9c: Pull complete
ce82e98d553d: Pull complete
5f0e19c475d6: Pull complete
abab87fa45d0: Pull complete
2ac2596c631f: Pull complete
Digest: sha256:220d07595f288567bbf07883576f6591dad77d824dce74f0c73850e129fa1f46
Status: Downloaded newer image for python:latest
root@8042c48ebb6c:/#
```
🌞 Installe des libs Python
```powershell
root@8042c48ebb6c:/# pip install aiohttp🌞
Collecting aiohttp
  Downloading aiohttp-3.11.10-cp313-cp313-manylinux_2_17_x86_64.manylinux2014_x86_64.whl.metadata (7.7 kB)
Collecting aiohappyeyeballs>=2.3.0 (from aiohttp)
  Downloading aiohappyeyeballs-2.4.4-py3-none-any.whl.metadata (6.1 kB)
Collecting aiosignal>=1.1.2 (from aiohttp)
  Downloading aiosignal-1.3.1-py3-none-any.whl.metadata (4.0 kB)
Collecting attrs>=17.3.0 (from aiohttp)
  Downloading attrs-24.2.0-py3-none-any.whl.metadata (11 kB)
Collecting frozenlist>=1.1.1 (from aiohttp)
  Downloading frozenlist-1.5.0-cp313-cp313-manylinux_2_5_x86_64.manylinux1_x86_64.manylinux_2_17_x86_64.manylinux2014_x86_64.whl.metadata (13 kB)
Collecting multidict<7.0,>=4.5 (from aiohttp)
  Downloading multidict-6.1.0-cp313-cp313-manylinux_2_17_x86_64.manylinux2014_x86_64.whl.metadata (5.0 kB)
Collecting propcache>=0.2.0 (from aiohttp)
  Downloading propcache-0.2.1-cp313-cp313-manylinux_2_17_x86_64.manylinux2014_x86_64.whl.metadata (9.2 kB)
Collecting yarl<2.0,>=1.17.0 (from aiohttp)
  Downloading yarl-1.18.3-cp313-cp313-manylinux_2_17_x86_64.manylinux2014_x86_64.whl.metadata (69 kB)
Collecting idna>=2.0 (from yarl<2.0,>=1.17.0->aiohttp)
  Downloading idna-3.10-py3-none-any.whl.metadata (10 kB)
Downloading aiohttp-3.11.10-cp313-cp313-manylinux_2_17_x86_64.manylinux2014_x86_64.whl (1.7 MB)
   ━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━ 1.7/1.7 MB 41.5 MB/s eta 0:00:00
Downloading aiohappyeyeballs-2.4.4-py3-none-any.whl (14 kB)
Downloading aiosignal-1.3.1-py3-none-any.whl (7.6 kB)
Downloading attrs-24.2.0-py3-none-any.whl (63 kB)
Downloading frozenlist-1.5.0-cp313-cp313-manylinux_2_5_x86_64.manylinux1_x86_64.manylinux_2_17_x86_64.manylinux2014_x86_64.whl (267 kB)
Downloading multidict-6.1.0-cp313-cp313-manylinux_2_17_x86_64.manylinux2014_x86_64.whl (131 kB)
Downloading propcache-0.2.1-cp313-cp313-manylinux_2_17_x86_64.manylinux2014_x86_64.whl (227 kB)
Downloading yarl-1.18.3-cp313-cp313-manylinux_2_17_x86_64.manylinux2014_x86_64.whl (339 kB)
Downloading idna-3.10-py3-none-any.whl (70 kB)
Installing collected packages: propcache, multidict, idna, frozenlist, attrs, aiohappyeyeballs, yarl, aiosignal, aiohttp
Successfully installed aiohappyeyeballs-2.4.4 aiohttp-3.11.10 aiosignal-1.3.1 attrs-24.2.0 frozenlist-1.5.0 idna-3.10 multidict-6.1.0 propcache-0.2.1 yarl-1.18.3



root@8042c48ebb6c:/# pip install aioconsole🌞
Collecting aioconsole
  Downloading aioconsole-0.8.1-py3-none-any.whl.metadata (46 kB)
Downloading aioconsole-0.8.1-py3-none-any.whl (43 kB)
Installing collected packages: aioconsole
Successfully installed aioconsole-0.8.1



root@8042c48ebb6c:/# python🌞
Python 3.13.1 (main, Dec  4 2024, 20:40:27) [GCC 12.2.0] on linux
Type "help", "copyright", "credits" or "license" for more information.
>>>



root@8042c48ebb6c:/# import aiohttp🌞
import-im6.q16: unable to open X server `' @ error/import.c/ImportImageCommand/346.
```
# II. Images

🌞 Récupérez des images
```powershell
[quentin@TP1 ~]$ docker images
REPOSITORY           TAG       IMAGE ID       CREATED       SIZE
linuxserver/wikijs   latest    863e49d2e56c   5 days ago    465MB
python               latest    3ca4060004b1   7 days ago    1.02GB
nginx                latest    66f8bdd3810c   2 weeks ago   192MB
wordpress            latest    c89b40a25cd1   2 weeks ago   700MB
mysql                latest    56a8c14e1404   8 weeks ago   603MB
```
🌞 Lancez un conteneur à partir de l'image Python
```powershell
[quentin@TP1 ~]$ docker run -it python bash
root@b867297c40a8:/#
```
🌞 Ecrire un Dockerfile pour une image qui héberge une application Python
```powershell
[quentin@TP1 python_app_build]$ sudo cat Dockerfile
FROM debian

RUN apt update -y && apt install -y python3

RUN apt install -y python3-emoji

COPY app.py /tmp/

ENTRYPOINT ["python3", "/tmp/app.py"]
```
🌞 Build l'image
```powershell
[quentin@TP1 python_app_build]$ docker build . -t python_app:version_de_ouf
[+] Building 0.1s (9/9) FINISHED                                                                                                 docker:default
 => [internal] load build definition from Dockerfile                                                                                       0.0s
 => => transferring dockerfile: 247B                                                                                                       0.0s
 => [internal] load metadata for docker.io/library/debian:latest                                                                           0.0s
 => [internal] load .dockerignore                                                                                                          0.0s
 => => transferring context: 2B                                                                                                            0.0s
 => [1/4] FROM docker.io/library/debian:latest                                                                                             0.0s
 => [internal] load build context                                                                                                          0.0s
 => => transferring context: 86B                                                                                                           0.0s
 => CACHED [2/4] RUN apt update -y && apt install -y python3                                                                               0.0s
 => CACHED [3/4] RUN apt install -y python3-emoji                                                                                          0.0s
 => [4/4] COPY app.py /tmp/                                                                                                                0.0s
 => exporting to image                                                                                                                     0.0s
 => => exporting layers                                                                                                                    0.0s
 => => writing image sha256:42152f5818fe6f269bcde82ba4fa976434b413ce130b769f2be21cbe079c2268                                               0.0s
 => => naming to docker.io/library/python_app:version_de_ouf
```
🌞 Lancer l'image
```powershell
[quentin@TP1 python_app_build]$ docker run python_app:version_de_ouf
Cet exemple d'application est vraiment naze 👎
```
# III. Docker compose
🌞 Créez un fichier docker-compose.yml
```powershell
[quentin@TP1 ~]$ sudo cat compose_test/docker-compose.yml
version: "3"

services:
  conteneur_nul:
    image: debian
    entrypoint: sleep 9999
  conteneur_flopesque:
    image: debian
    entrypoint: sleep 9999
```
🌞 Lancez les deux conteneurs avec docker compose
```powershell
[quentin@TP1 compose_test]$ docker compose up -d
WARN[0000] /home/quentin/compose_test/docker-compose.yml: the attribute `version` is obsolete, it will be ignored, please remove it to avoid potential confusion
[+] Running 3/3
 ✔ Network compose_test_default                  Created                                                           0.3s
 ✔ Container compose_test-conteneur_nul-1        Started                                                           0.8s
 ✔ Container compose_test-conteneur_flopesque-1  Started                                                           0.8s
```
🌞 Vérifier que les deux conteneurs tournent
```powershell
[quentin@TP1 compose_test]$ docker compose ps
WARN[0000] /home/quentin/compose_test/docker-compose.yml: the attribute `version` is obsolete, it will be ignored, please remove it to avoid potential confusion
NAME                                 IMAGE     COMMAND        SERVICE               CREATED          STATUS          PORTS
compose_test-conteneur_flopesque-1   debian    "sleep 9999"   conteneur_flopesque   14 minutes ago   Up 14 minutes
compose_test-conteneur_nul-1         debian    "sleep 9999"   conteneur_nul         14 minutes ago   Up 14 minutes
```
🌞 Pop un shell dans le conteneur conteneur_nul
```powershell
root@df00fe1c5f41:/# ping conteneur_flopesque
PING conteneur_flopesque (172.18.0.2) 56(84) bytes of data.
64 bytes from compose_test-conteneur_flopesque-1.compose_test_default (172.18.0.2): icmp_seq=1 ttl=64 time=0.034 ms
64 bytes from compose_test-conteneur_flopesque-1.compose_test_default (172.18.0.2): icmp_seq=2 ttl=64 time=0.051 ms
64 bytes from compose_test-conteneur_flopesque-1.compose_test_default (172.18.0.2): icmp_seq=3 ttl=64 time=0.040 ms
64 bytes from compose_test-conteneur_flopesque-1.compose_test_default (172.18.0.2): icmp_seq=4 ttl=64 time=0.040 ms
^C
--- conteneur_flopesque ping statistics ---
4 packets transmitted, 4 received, 0% packet loss, time 3094ms
rtt min/avg/max/mdev = 0.034/0.041/0.051/0.006 ms
```