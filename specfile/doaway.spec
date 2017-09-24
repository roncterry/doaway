#
# spec file for package doaway
#
# Copyright (c) 2007 Ron Terry.
# This file and all modifications and additions to the pristine
# package are under the same license as the package itself.
#
#

# norootforbuild

%define _binary_payload w9.bzdio


Name:           doaway
License:        BSD
Group:          Productivity/
Version:        1.5.2
Release:        0
Summary:        Toolset for deploying files via multicast and unicast and remotly executing commands in serial or parallel
URL:            http://thepenguinpriest.com/packages/doaway.html
Requires:       udpcast openssh wol screen
Obsoletes:	deployit
Source:         http://thepenguinpriest.com/packages/doaway-%{version}.tar.gz
BuildArch:      noarch
BuildRoot:      %{_tmppath}/%{name}-%{version}-build

%description
This toolset contains a group of tools that enable you 
to copy files to and execute commands on remote systems.
You can unicast or multicast files to remote machines 
and execute commands in serial or in parallel on remote
machines.

Included are the following tools:
  castaway
  putaway
  runaway
  walkaway
  getaway
  syncaway
  pullaway
  lookaway
  awayke
  mkhostlist
  mkmaclist
  mkmaclist-from-hosts
  mkiplist
  mklablist
  isalive
  populate-known_hosts
  distribute-keys
  build-dhcp-config

"castaway" is a tool that uses udpcast to deploy files
or disk images to multiple computers via multicast.  
It allows you to launch a receiving session on a list
of machines (using ssh and screen) an then a sending 
session on the server (the machine castaway is running 
on) with one command.

"putaway" is a tool that uses screen and scp to copy
files to remote hosts in parallel unicast sessions.

"lookaway" is a tool that uses screen and vncviewer to
view the desktop of a list of remote hosts.

"runaway" allows you to run one or more commands on one
or more remote hosts in parallel via ssh.  The list of
commands are provided as a semi-colon delimited list 
wrapped in double-quotes as an opperand to this command.

"walkaway" places you at a walkaway> prompt.  Any command(s) 
entered will be executed on the remote hosts via ssh.
When remote execution is complete you are returned to a
walkaway> prompt.  WalkAway essentially gets a list of 
commands and walks through a list of hosts executing
the commands

"getaway" uses rsync to retrieve a file or directory from
a list of machines in parallel.  The files retrieved from 
each machine are placed into their own directory

"syncaway" uses rsync to copy a file or directory to a 
list of machines in parallel by either pushing the file
with rsync via ssh or by causing the client to pull
the file or directroy from a server with rsync via ssh
or from an rsync server. 

"awayke" uses the wol utility to send magic packets to
a list of MAC addresses to wake them up (wake on lan)

"mkhostlist" creates a list of hosts that are powered on 
and their ssh daemons listening on a network.

"mkmaclist" outputs a list of mac addresses parsed from
a dhcpd leases file.

"mkmaclist-from-hosts" outputs a list of mac addresses retrieved
the hosts listed in a provided host list file.

"mkiplist" outputs a list of IP addresses parsed from a dhcpd
configuration file.

"mklablist" calls the mkhostlist, populate-known_hosts and 
mkmaclist-from-hosts commands and accepts the same options as
the mkhostlist command.

"isalive" tests wheter a list of hosts are alive and accessable
via the network

"populate-known_hosts" uses ssh-keygen to add the host keys 
for all of the machines listed in the supplied host list 
or host list file to the user's .ssh/known_hosts file.

"distribute-keys" uses ssh-copy-id to copy the specified
ssh ket to the authorized_kays file of the specified user
on the specified machines

"build-dhcp-config" takes a list of MAC addresses and 
outputs to stdout a dhcpd.conf file with address 
reservations for each MAC address.


Authors:
--------
    Ron Terry <roncterry@gmail.com>

%prep
%setup -c

%build

%install
rm -rf $RPM_BUILD_ROOT
mkdir -p $RPM_BUILD_ROOT/etc
mkdir -p $RPM_BUILD_ROOT/usr/lib/doaway/templates
mkdir -p $RPM_BUILD_ROOT/usr/bin/
mkdir -p $RPM_BUILD_ROOT/var/lib/doaway/

cp -R %{name}/config/doaway.conf $RPM_BUILD_ROOT/etc/

cp -R %{name}/templates $RPM_BUILD_ROOT/usr/lib/doaway/
cp -R %{name}/doaway_aliases.sh $RPM_BUILD_ROOT/usr/lib/doaway/

cp -R %{name}/bin/castaway $RPM_BUILD_ROOT/usr/bin/castaway
cp -R %{name}/bin/putaway $RPM_BUILD_ROOT/usr/bin/putaway
cp -R %{name}/bin/lookaway $RPM_BUILD_ROOT/usr/bin/lookaway
cp -R %{name}/bin/runaway $RPM_BUILD_ROOT/usr/bin/runaway
cp -R %{name}/bin/walkaway $RPM_BUILD_ROOT/usr/bin/walkaway
cp -R %{name}/bin/getaway $RPM_BUILD_ROOT/usr/bin/getaway
cp -R %{name}/bin/syncaway $RPM_BUILD_ROOT/usr/bin/syncaway
cp -R %{name}/bin/awayke $RPM_BUILD_ROOT/usr/bin/awayke
cp -R %{name}/bin/mkhostlist $RPM_BUILD_ROOT/usr/bin/mkhostlist
cp -R %{name}/bin/mkmaclist $RPM_BUILD_ROOT/usr/bin/mkmaclist
cp -R %{name}/bin/mkmaclist-from-hosts $RPM_BUILD_ROOT/usr/bin/mkmaclist-from-hosts
cp -R %{name}/bin/mkiplist $RPM_BUILD_ROOT/usr/bin/mkiplist
cp -R %{name}/bin/mklablist $RPM_BUILD_ROOT/usr/bin/mklablist
cp -R %{name}/bin/isalive $RPM_BUILD_ROOT/usr/bin/isalive
cp -R %{name}/bin/populate-known_hosts $RPM_BUILD_ROOT/usr/bin/populate-known_hosts
cp -R %{name}/bin/distribute-keys $RPM_BUILD_ROOT/usr/bin/distribute-keys
cp -R %{name}/bin/build-dhcp-config $RPM_BUILD_ROOT/usr/bin/build-dhcp-config


%clean
rm -rf $RPM_BUILD_ROOT

%post
grep -q ". /usr/lib/doaway/doaway_aliases.sh" /etc/bash.bashrc.local || echo ". /usr/lib/doaway/doaway_aliases.sh" >> /etc/bash.bashrc.local

%postun
sed -i '/\. \/usr\/lib\/doaway\/doaway_aliases.sh/d' /etc/bash.bashrc.local

%files
%defattr(-, root, root)
%config /etc/doaway.conf
/usr/lib/doaway/templates
/usr/lib/doaway/doaway_aliases.sh
%attr(1775,root,root)/var/lib/doaway
%attr(555,root,root) /usr/bin/castaway
%attr(555,root,root) /usr/bin/putaway
%attr(555,root,root) /usr/bin/lookaway
%attr(555,root,root) /usr/bin/runaway
%attr(555,root,root) /usr/bin/walkaway
%attr(555,root,root) /usr/bin/getaway
%attr(555,root,root) /usr/bin/syncaway
%attr(555,root,root) /usr/bin/awayke
%attr(555,root,root) /usr/bin/mkhostlist
%attr(555,root,root) /usr/bin/mkmaclist
%attr(555,root,root) /usr/bin/mkmaclist-from-hosts
%attr(555,root,root) /usr/bin/mkiplist
%attr(555,root,root) /usr/bin/mklablist
%attr(555,root,root) /usr/bin/isalive
%attr(555,root,root) /usr/bin/populate-known_hosts
%attr(555,root,root) /usr/bin/distribute-keys
%attr(555,root,root) /usr/bin/build-dhcp-config

%changelog
* Tue Nov 1 2015 - Ron Terry <roncterry@gmail.com>
- Released 1.5.2
- Fixed bug in distribute-keys
* Tue Sep 1 2015 - Ron Terry <roncterry@gmail.com>
- Released 1.5.0
- Updated all scripts to use a common config file
* Wed Aug 19 2015 - Ron Terry <roncterry@gmail.com>
- Released 1.4.1
- updated functions names in preparation for pulling all functions into a common library
* Mon Apr 15 2013 - Ron Terry <roncterry@gmail.com>
- Released 1.4.0
- Added mkmaclist-from-hosts and mklablist commands
- Updated the build-dhcp-config command and added a template for it
* Thu May 25 2012 - Ron Terry <roncterry@gmail.com>
- Released 1.3.1
- Added templates for quickscripts
- Fixed bug in getaway script
- Fixed bug in populate-known_hosts script
- Updated lookaway to support both parallel and serial modes
* Sat Mar 31 2012 - Ron Terry <roncterry@gmail.com>
- Released 1.3.0
- Added lookaway
- Move library directory from /opt/doaway to /usr/lib/doaway
* Wed Sep 29 2010 - Ron Terry <roncterry@gmail.com>
- Released 1.2.2
- Now under the New and Simplified BSD lcense
* Fri Apr 09 2010 - Ron Terry <roncterry@gmail.com>
- Released 1.2.1
- Removed the alises file from the profile.d directory and appended it to the /etc/bash.bashrc.local file
- Fixed bugs in chech_ssh_agent functions in the *away scripts that caused them to always try to add your ssh keys to the ssh agent
- Added an option to castaway (-b) to set the max bitrate for the udp-sender
* Tue Feb 17 2010 - Ron Terry <roncterry@gmail.com>
- Released 1.2.0
- Added new scripts: isalive
- Added a file to /etc/profile.d/ to set some aliases for the doaway tools
- Fixed bugs in scripts: putaway, syncaway
- Added the ability in the syncaway script to cause the files to be pulled from a server in addition to being pushed
* Tue Jul 14 2009 - Ron Terry <roncterry@gmail.com>
- Released 1.1.0
- Added new script: mkiplist
- Fixed buges in scripts: putaway, syncaway, getaway
* Mon Jun 01 2009 - Ron Terry <roncterry@gmail.com>
- Released 1.0.1
- Added new scripts: syncaway, getaway, mkmaclist
- Updated walkaway to use a for loop instead of xargs to increment through the list of hosts
- Updated mkhostlist to be smarter at guessing the interface to use.  You can also specify and interface for scaning
* Mon Mar 11 2009 - Ron Terry <roncterry@gmail.com>
- Fixed bugs in scripts
* Sat Feb 27 2009 - Ron Terry <roncterry@gmail.com>
- Fixed a bug in putaway where the path on the remote machine was incorrect
* Sat Feb 24 2009 - Ron Terry <roncterry@gmail.com>
- Initial release of the doaway tools (forked from deployit)
