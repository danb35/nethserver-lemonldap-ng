Summary: NethServer configuration for LemonLDAP::NG
%define name nethserver-lemonldap-ng
%define version 0.1.0
%define release 4
Name: %{name}
Version: %{version}
Release: %{release}%{?dist}
License: GPL
Source: %{name}-%{version}.tar.gz
BuildArch: noarch
URL: https://github.com/danb35/nethserver-lemonldap-ng

BuildRequires: nethserver-devtools
Requires: lemonldap-ng lasso lasso-perl
Requires: nethserver-release = 7
#AutoReq: no

%description
NethServer configuration for LemonLDAP::NG
(https://lemonldap-ng.org/welcome/)

%prep
%setup

%post
%preun

%build
%{makedocs}
perl createlinks

%install
rm -rf $RPM_BUILD_ROOT
(cd root; find . -depth -print | cpio -dump $RPM_BUILD_ROOT)

%{genfilelist} %{buildroot} $RPM_BUILD_ROOT > default.lst

%clean
rm -rf $RPM_BUILD_ROOT

%files -f default.lst
%dir %{_nseventsdir}/%{name}-update

%changelog
* Sun Apr  4 2021 Dan Brown <dan@familybrown.org> 0.1.0-4.ns7
- Correct template expansion
- Reload httpd on completion of lemon_config.sh

* Tue Mar 23 2021 Dan Brown <dan@familybrown.org> 0.1.0-3.ns7
- Correct TLS certificate path when no config property present

* Thu Mar 18 2021 Dan Brown <dan@familybrown.org> 0.1.0-2.ns7
- Fixed error in createlinks

* Thu Mar 18 2021 Dan Brown <dan@familybrown.org> 0.1.0-1.ns7
- Initial Release
