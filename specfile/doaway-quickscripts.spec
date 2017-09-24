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

Name:           doaway-quickscripts
License:        BSD
Group:          Productivity/
Version:        1.0.0
Release:        0
Summary:        Collection of scripts that leverage the doaway tools
URL:            http://thepenguinpriest.com/packages/doaway.html
Requires:       doaway
Source:         http://thepenguinpriest.com/packages/doaway-quickscripts-%{version}.tar.gz
BuildArch:      noarch
BuildRoot:      %{_tmppath}/%{name}-%{version}-build

%description
This contains a collection of scripts that leverage the
dooaway tools to preform specific tasks.


Authors:
--------
    Ron Terry <roncterry@gmail.com>

%prep
%setup -c

%build

%install
rm -rf $RPM_BUILD_ROOT
mkdir -p $RPM_BUILD_ROOT
mkdir -p $RPM_BUILD_ROOT/usr/lib/doaway/quickscripts

cp -R %{name}/*.sh $RPM_BUILD_ROOT/usr/lib/doaway/quickscripts


%clean
rm -rf $RPM_BUILD_ROOT

%files
%defattr(-, root, root)
/usr/lib/doaway/quickscripts
%attr(555,root,root) /usr/lib/doaway/quickscripts/*

%changelog
* Fri May 25 2012 - Ron Terry <roncterry@gmail.com>
- Initial spec file
