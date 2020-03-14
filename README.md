# Update the operating system
```shell
osmc@osmc:~$ sudo apt-get update
```

# Before connecting the hard disk:
## Enable the high current on USB:
```shell
Add "max_usb_current=1" in /boot/config.txt
```
## Format the hard disk to EXT4

# Connect the hard disk on a USB port
# Get the UUID of the disk
```shell
osmc@osmc:~$ sudo blkid /dev/sda1
/dev/sda1: LABEL="HDD" UUID="7d59e0e6-f886-458f-83ed-0841885af0a2" TYPE="ext4" PARTUUID="809d1d5b-01"
```

# Automount the HDD. Edit the /etc/fstab and add the following line:
```shell
UUID=7d59e0e6-f886-458f-83ed-0841885af0a2 /media/HDD ext4 defaults,noatime 0 2
```

# Reboot to test the automount

#######################################################
# Shell In A Box
```shell
osmc@osmc:~$ sudo apt-get install shellinabox
```
# Edit the file 
```shell
osmc@osmc:~$ sudo vi /etc/default/shellinabox
```
# Add a "-t" at the end of the last line:
```shell
SHELLINABOX_ARGS="--no-beep -t"
```
# Reboot to test that the service a started and listen on port 4200
# Open a web navigator on port 4200

#######################################################
# OnwCloud
```shell
osmc@osmc:~$ sudo apt-get install owncloud
osmc@osmc:~$ sudo apt-get install mysql-server
```
And set mysql root password: osmc
# Edit file /etc/php5/apache2/php.ini
```shell
osmc@osmc:~$ sudo vi /etc/php5/apache2/php.ini
post_max_size = 100000M
upload_max_filesize = 100000M
osmc@osmc:~$ sudo vi /etc/owncloud/htaccess
php_value upload_max_filesize 100000M
php_value post_max_size 100000M
```
# Change listen port to 8081 in the file 
```shell
osmc@osmc:~$ sudo vi /etc/apache2/ports.conf
Listen 8081
```
# Reboot
```shell
osmc@osmc:~$ sudo reboot
```
# Open a web navigator ant go to :
http://192.168.10.237:8081/owncloud/
## Create the admin user: myusername/mypassword
## Data folder should be set to: /media/HDD/owncloud
## Database user: root
## Database password: osmc
## Database name: owncloud

#######################################################
# Create links to shared folder: Movies, Music...
osmc@osmc:~$ cd
osmc@osmc:~$ mv Movies Movies.old
osmc@osmc:~$ mv Music Music.old
osmc@osmc:~$ mv Pictures Pictures.old
osmc@osmc:~$ mv TV\ Shows TV\ Shows.old
osmc@osmc:~$ cd /media/HDD/
osmc@osmc:/media/HDD$ mkdir Movies
osmc@osmc:/media/HDD$ mkdir Music
osmc@osmc:/media/HDD$ mkdir Pictures
osmc@osmc:/media/HDD$ mkdir TV\ Shows
osmc@osmc:/media/HDD$ cd -
/home/osmc
osmc@osmc:~$ ln -s /media/HDD/Movies Movies
osmc@osmc:~$ ln -s /media/HDD/Music Music
osmc@osmc:~$ ln -s /media/HDD/Pictures Pictures
osmc@osmc:~$ ln -s /media/HDD/TV\ Shows TV\ Shows
# Change rights on HDD
osmc@osmc:~$ cd /media/HDD
osmc@osmc:/media/HDD$ sudo chmod 777 Movies Music Pictures TV\ Shows
# Goes into user account and create links to osmc and HDD area:
osmc@osmc:/media/HDD$ cd owncloud/guilhem/files
osmc@osmc:/media/HDD/owncloud/guilhem/files$ sudo ln -s /home/osmc osmc
osmc@osmc:/media/HDD/owncloud/guilhem/files$ sudo ln -s /media/HDD HDD

#######################################################
# Create torrent user account
osmc@osmc:~$ sudo useradd -m torrent
# Change password to "torrent"
osmc@osmc:~$ sudo passwd torrent

#######################################################
# Deluge
# Install deluge
osmc@osmc:~$ sudo apt-get install deluged
osmc@osmc:~$ sudo apt-get install deluge-console
# Create folders for deluge software
osmc@osmc:~$ sudo su -l deluge
$ pwd
/home/deluge
$ mkdir log
$ mkdir config
$ mkdir run
$ exit
# Create deluge configuration file
osmc@osmc:~$ deluged
osmc@osmc:~$ sudo pkill deluged
osmc@osmc:~$ ls .config/deluge/
auth           core.conf      deluged.log    dht.state      plugins/       session.state  ssl/           state/      
# Add new user to deluge authorization file
osmc@osmc:~$ vi .config/deluge/auth
remoteDelugeUser:remoteDelugePassword:10
(user:password:level)
# Reboot
osmc@osmc:~$ sudo reboot
# Launch deluge server
osmc@osmc:~$ deluged
# Allow remote access
osmc@osmc:~$ deluge-console
config -s allow_remote True
config allow_remote
exit
osmc@osmc:~$ sudo pkill deluged
# Install web UI
osmc@osmc:~$ sudo apt-get install python-mako
osmc@osmc:~$ sudo apt-get install deluge-web
# Create web UI configuration file
osmc@osmc:~$ deluge-web
# Wait 1 minute
CTRL+C
osmc@osmc:~$ ls -als .config/deluge/web.conf
# Copy configuration files to deluge home folder
osmc@osmc:~$ sudo cp -R .config/deluge/* /home/deluge/config/.
osmc@osmc:~$ sudo chown -R deluge:deluge /home/deluge/config
# Run deluge at startup
osmc@osmc:~$ sudo wget -O /etc/default/deluge-daemon http://www.howtogeek.com/wp-content/uploads/gg/up/sshot5151a8c86fb85.txt
# Edit file /etc/default/deluge-daemon and change user to "deluge"
osmc@osmc:~$ sudo vi /etc/default/deluge-daemon
DELUGED_USER="deluge"             # !!!CHANGE THIS!!!!
### Deprecated ### # Get the startup script
### Deprecated ### osmc@osmc:~$ sudo wget -O /etc/init.d/deluge-daemon http://www.howtogeek.com/wp-content/uploads/gg/up/sshot5151aa042ad11.txt
### Deprecated ### # Configure it
### Deprecated ### osmc@osmc:~$ sudo chmod 755 /etc/init.d/deluge-daemon
### Deprecated ### osmc@osmc:~$ sudo update-rc.d deluge-daemon defaults
### Deprecated ### # Edit startup script and change the following:
### Deprecated ### osmc@osmc:~$ sudo vi /etc/init.d/deluge-daemon
### Deprecated ### DAEMON1_ARGS="-d -c /home/deluge/config -l /home/deluge/log/deluged.log -L info"             # Consult `man deluged` for more options
### Deprecated ### DAEMON2_ARGS="-c /home/deluge/config -l /home/deluge/log/deluge-web.log -L info"               # Consult `man deluge-web` for more options
### Deprecated ### PIDFILE1=/home/deluge/run/$NAME1.pid
### Deprecated ### PIDFILE2=/home/deluge/run/$NAME2.pid
### Deprecated ### UMASK=000                     # Change this to 0 if running deluged as its own user  
# Remove auto installed script
osmc@osmc:~$ sudo update-rc.d deluged remove
osmc@osmc:~$ sudo rm /etc/init.d/deluged
osmc@osmc:~$ sudo rm /etc/default/deluged
# Reboot
osmc@osmc:~$ sudo reboot
# Open a web navigator on port 8112
http://192.168.10.237:8112/
# Default password is "deluge"
# After the connection, go to "Preferences" and change the following:
## Downloads:
### Download to: /media/HDD/Movies
### Only check "Use Full"
## Network:
Incoming Ports: From 6881 To: 6891
Outgoing Ports: From 6870 To: 6880
### Only check "Peer Exchange", "LSD", "DHT"
## Encryption:
### Inbound: Forced
### Outbound: Forced
### Level: Full Stream
### Check: Encrypt entire stream
## Interface:
### Check Show session speed in titlebar
## Proxy:
### Peer: Socksv5 / 82.75.161.197 / 48111
### Web Seed: Socksv5 / 82.75.161.197 / 48111
### Tracker: Socksv5 / 82.75.161.197 / 48111
### DHT: Socksv5 / 82.75.161.197 / 48111
## Download plugins fom deluge repository:
https://github.com/ratanakvlun/deluge-ltconfig/releases/download/v0.2.5.0/ltConfig-0.2.5.0-py2.7.egg
## Plugins: ItConfig
## ItConfig:
### Check "user_agent" and change to "none"

osmc@osmc:/$ sudo update-rc.d deluge-daemon disable
insserv: warning: current start runlevel(s) (empty) of script `deluge-daemon' overrides LSB defaults (2 3 4 5).
insserv: warning: current stop runlevel(s) (0 1 2 3 4 5 6) of script `deluge-daemon' overrides LSB defaults (0 1 6).
osmc@osmc:/$ sudo update-rc.d deluge-daemon remove

#######################################################
# Transmission
osmc@osmc:~$ sudo apt-get install transmission-daemon
osmc@osmc:~$ sudo rm /etc/init.d/transmission-daemon
osmc@osmc:/$ sudo systemctl disable transmission-daemon
Removed symlink /etc/systemd/system/multi-user.target.wants/transmission-daemon.service.
osmc@osmc:/$ sudo systemctl stop transmission-daemon

#######################################################
# Nginx
osmc@osmc:~$ sudo apt-get install nginx-extras
# Copy the file "default" in this folder
osmc@osmc:~$ cd /etc/nginx/sites-available/
# Create html folder
# Copy the file "default" in this folder
osmc@osmc:/etc/nginx/html$ cd /etc/nginx/
osmc@osmc:/etc/nginx$ sudo mkdir html
# Go to HTML folder
osmc@osmc:/etc/nginx$ cd html
# Copy "index.html", "favicon.png" and folder "css"
# Create authentification file
osmc@osmc:/etc/nginx/html$ cd /etc/nginx/
osmc@osmc:/etc/nginx$ sudo htpasswd -c .htpasswd user1
osmc@osmc:/etc/nginx$ sudo htpasswd .htpasswd user2
# Edit NGINX configuration file to allow big file upload
osmc@osmc:~$ sudo vi /etc/nginx/nginx.conf
# Add the following line:
        client_max_body_size 100000M;
        server_tokens off;
# Reboot
osmc@osmc:/etc/nginx$ sudo reboot

#######################################################
# Kodi
# In Kodi Extensions / Programs / My OSMC / App Store enable :
- FTP Server
- SSH Server
- Samba (SMB) Server
- Cron Task Scheduler
# In extension programs install:
- XBMX Library auto update

#######################################################
# Install OpenVPN and file from your VPN provider
osmc@osmc:~$ sudo apt-get install openvpn
osmc@osmc:~$ cd /etc/openvpn
osmc@osmc:/etc/openvpn$ ls
ca.rsa.4096.crt  crl.rsa.4096.pem  nl.conf  pass.txt  update-resolv-conf

#######################################################
# Namspaces
osmc@osmc:~$ sudo vi /etc/openvpn/up.sh
#!/bin/bash

echo "#################################"
echo "### Remove old process if any ###"
/usr/bin/sudo /usr/bin/pkill deluged
echo "#############################################"
echo "### Remove all default routes in VPN namespace if any ###"
/usr/bin/sudo /bin/ip netns exec vpn /bin/ip route flush 0/0

echo "##############################"
echo "### Creating VPN namespace ###"
/usr/bin/sudo /bin/ip netns add vpn
/usr/bin/sudo /bin/ip netns 
/usr/bin/sudo /bin/ip netns exec vpn /bin/ip link list
/usr/bin/sudo /bin/ip netns exec vpn /bin/ip link set dev lo up

echo "###########################"
echo "### Creating inter link ###"
/usr/bin/sudo /bin/ip link add vpn0 type veth peer name vpn1
/usr/bin/sudo /bin/ip link set vpn1 netns vpn
/usr/bin/sudo /bin/ip netns exec vpn /bin/ip link list

echo "##############################"
echo "### Setting inter link IPs ###"
/usr/bin/sudo /bin/ip netns exec vpn /sbin/ifconfig vpn1 192.168.100.2/24 up
/usr/bin/sudo /bin/ip netns exec vpn /sbin/ifconfig vpn1
/usr/bin/sudo /sbin/ifconfig vpn0 192.168.100.1/24 up
/usr/bin/sudo /bin/ip netns exec vpn /sbin/route -n

echo "####################################"
echo "### Get data from tun0 interface ###"
TUN0_ADDR=`/usr/bin/sudo /sbin/ifconfig tun0 | grep -oP 'inet addr:\K\S+'`
TUN0_PTP=`/usr/bin/sudo /sbin/ifconfig tun0 | grep -oP 'P-t-P:\K\S+'`
TUN0_MASK=`/usr/bin/sudo /sbin/ifconfig tun0 | grep -oP 'Mask:\K\S+'`
echo "TUN0 ADDR = $TUN0_ADDR"
echo "TUN0 PTP = $TUN0_PTP"
echo "TUN0 MASK = $TUN0_MASK"

echo "#########################################"
echo "### Trasnfering TUN0 to VPN namespace ###"
/usr/bin/sudo /bin/ip link set tun0 netns vpn
echo "#################################"
echo "###Configuring TUN0 interface ###"
/usr/bin/sudo /bin/ip netns exec vpn /sbin/ifconfig tun0 inet $TUN0_ADDR netmask $TUN0_MASK dstaddr $TUN0_PTP up
echo "###############################################"
echo "### Adding default gateway in VPN namespace ###"
/usr/bin/sudo /bin/ip netns exec vpn /sbin/route add default gw $TUN0_PTP
echo "############################################"
echo "### Show the result of the configuration ###"
/usr/bin/sudo /bin/ip netns exec vpn /sbin/ifconfig
/usr/bin/sudo /bin/ip netns exec vpn /sbin/route -n

echo "############################"
echo "### Launch Deluge server ###"
/usr/bin/sudo /bin/ip netns exec vpn /usr/bin/sudo /bin/su deluge -c "/usr/bin/python /usr/bin/deluged -d -c /home/deluge/config -l /home/deluge/deluged.log -L info &"
/usr/bin/sudo /bin/ip netns exec vpn /usr/bin/sudo /bin/su deluge -c "/usr/bin/python /usr/bin/deluge-web -c /home/deluge/config -l /home/deluge/deluge-web.log -L info &"
/usr/bin/sudo /bin/ip netns exec vpn /usr/bin/sudo /bin/su deluge -c "/usr/bin/transmission-daemon -f --log-error &"

###################################################################
# Edit nl.conf file to call up.sh script when vpn link is establish
osmc@osmc:~$ sudo vi /etc/openvpn/nl.conf
route-noexec
route-nopull
keepalive 10 60
script-security 2
up /etc/openvpn/up.sh


#######################################################
# Set capabilities to openvpn
sudo vi /lib/systemd/system/openvpn@.service
CapabilityBoundingSet=CAP_IPC_LOCK CAP_NET_ADMIN CAP_NET_BIND_SERVICE CAP_NET_RAW CAP_SETGID CAP_SETUID CAP_SYS_CHROOT CAP_DAC_READ_SEARCH CAP_AUDIT_WRITE CAP_SYS_ADMIN

#######################################################
# Set DNS in VPN namespace
osmc@osmc:~$ sudo mkdir /etc/netns
osmc@osmc:~$ sudo mkdir /etc/netns/vpn
osmc@osmc:~$ sudo vi /etc/netns/vpn/resolv.conf
nameserver 208.67.222.222
nameserver 208.67.220.220-

##########################################################################################
# Install firewall to forbit VPN namespace access to default namespace (increase security)
osmc@osmc:~$ sudo apt-get install ufw
osmc@osmc:~$ sudo ufw default allow outgoing
Default outgoing policy changed to 'allow'
(be sure to update your rules accordingly)
osmc@osmc:~$ sudo ufw default allow incoming
Default incoming policy changed to 'allow'
(be sure to update your rules accordingly)
osmc@osmc:~$ sudo ufw reset
Resetting all rules to installed defaults. This may disrupt existing ssh
connections. Proceed with operation (y|n)? y
osmc@osmc:~$ sudo ufw deny in on vpn0
Rules updated
Rules updated (v6)
osmc@osmc:~$ sudo ufw enable
Command may disrupt existing ssh connections. Proceed with operation (y|n)? y
Firewall is active and enabled on system startup
osmc@osmc:~$ sudo ufw status verbose
Status: active
Logging: on (low)
Default: allow (incoming), allow (outgoing)
New profiles: skip

To                         Action      From
--                         ------      ----
Anywhere on vpn0           DENY IN     Anywhere
Anywhere (v6) on vpn0      DENY IN     Anywhere (v6)

# Test the firewall protection. The following command must be blocked
/usr/bin/sudo /bin/ip netns exec vpn ssh osmc@192.168.100.1

##########################################################################################
# Camera
osmc@osmc:~$ sudo apt-get install git
osmc@osmc:~$ git clone https://github.com/silvanmelchior/RPi_Cam_Web_Interface.git

##########################################################################################
# NFS
osmc@osmc:~$ sudo apt-get install nfs-kernel-server
osmc@osmc:~$ sudo vi /etc/exports
/media/HDD *(rw,all_squash,no_subtree_check,sync)
osmc@osmc:~$ sudo /etc/init.d/nfs-kernel-server restart
