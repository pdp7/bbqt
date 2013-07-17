bbqt
====
- Originally created by Ed B on his laptop for the BBB challenge to control Pick N Place 
- 2013-07-07: updated for Qt4 since Qt3 not available for BeagleBone Black on Debian 7.0, Ubuntu 13 or Angstrom [Drew (pdp7) & Bonnie (misterbonnie)

Installation:
=============
<pre>
sudo apt-get update && sudo apt-get install lxde 
sudo apt-get install git
sudo apt-get install python-sip python-qt4 
sudo apt-get install python-setuptools
sudo apt-get install python-pip 
sudo apt-get install python-serial
sudo apt-get install minicom
 
Generate SSH key:
 
debian@debian-armhf:~/.ssh$ ssh-keygen -t rsa
Generating public/private rsa key pair.
Enter file in which to save the key (/home/debian/.ssh/id_rsa): 
Enter passphrase (empty for no passphrase): 
Enter same passphrase again: 
Your identification has been saved in /home/debian/.ssh/id_rsa.
Your public key has been saved in /home/debian/.ssh/id_rsa.pub.
The key fingerprint is:
<snip>
 
debian@debian-armhf:~/.ssh$ cat ~/.ssh/id_rsa.pub 
ssh-rsa AAAAB3NzaC1yc2EAAAADAQABAAABAQC3JgUGY4jrc+As2v0DqphBFuoLpobK0ZmasYcuVme4okdqZ069hxIPdEvhMln/7XKIzOo/hRUN/HmaznKgzxpZCDVO8fjSsozqdzDWOBzsTfquOx5Te3Ft4QM+K+33v3ejlk6D3zUgr6xTZ2ZDQ3iLOoKVz4tmKTkveiP83eAbVDZgDiciuLzoS02xx52Zxd6rQ+o3cARDlFvF7B4Dt+aJGaCsPjLNhlWC1Os+Q/OeTkIrVBITpIum5AAok5OQtLhG+0N5HF+GfzIBRMkqWytoJu5DuKrchAl4nVICN/cm/W37RtG1/hASgev1v0VAjAcnOeZmF1vC2PPsVioGFdS/ debian@debian-armhf
 
Copy public key to authorized SSH keys in your GitHub settings:
 
debian@debian-armhf:~$ git clone git@github.com:pdp7/bbqt.git
Cloning into 'bbqt'...
remote: Counting objects: 31, done.
remote: Compressing objects: 100% (19/19), done.
remote: Total 31 (delta 12), reused 30 (delta 11)
Receiving objects: 100% (31/31), 10.01 KiB, done.
Resolving deltas: 100% (12/12), done.
 
Download Debian 7.0 image from armhf.com and burn to microSD:
 
http://www.armhf.com/index.php/boards/beaglebone-black/#wheezy
 
Next, boot off of Debian SD card by holding down the boot button and copy the image file to the BBB: debian-wheezy-7.0.0-armhf-3.8.13-bone20.img.xz.  Then flash the eMMC with Debian using this following command:
 
install: xz -cd debian-wheezy-7.0.0-armhf-3.8.13-bone20.img.xz > /dev/sdX
Note: This .img.xz can be directly applied to the Bone’s internal eMMC while booted from the external microSD card.
xz -cd debian-wheezy-7.0.0-armhf-3.8.13-bone20.img.xz > /dev/mmcblk1
power down and remove the microSD card
</pre>
