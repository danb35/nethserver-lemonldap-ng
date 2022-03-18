#!/bin/bash

# Script to install LemonLDAP::NG on a Nethserver 7 system and perform basic configuration
# See https://github.com/danb35/nethserver-lemonldap-ng

yum install -y https://repo.familybrown.org/nethserver/7/noarch/nethserver-danb35-1.1.0-1.ns7.noarch.rpm

cat <<-'__EOF__' >/etc/yum.repos.d/lemonldap-ng.repo
	[lemonldap-ng]
	name=LemonLDAP::NG packages
	baseurl=https://lemonldap-ng.org/redhat/stable/$releasever/noarch
	enabled=1
	gpgcheck=1
	gpgkey=file:///etc/pki/rpm-gpg/RPM-GPG-KEY-OW2

	[lemonldap-ng-extras]
	name=LemonLDAP::NG extra packages
	baseurl=https://lemonldap-ng.org/redhat/extras/$releasever
	enabled=1
	gpgcheck=1
	gpgkey=file:///etc/pki/rpm-gpg/RPM-GPG-KEY-OW2
__EOF__

curl https://lemonldap-ng.org/_media/rpm-gpg-key-ow2 > /etc/pki/rpm-gpg/RPM-GPG-KEY-OW2
yum install -y nethserver-lemonldap-ng --enablerepo=lemonldap-ng,lemonldap-ng-extras
/root/lemon_config.sh
