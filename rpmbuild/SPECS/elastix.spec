Summary: Elastix is a Web based software to administrate a PBX based in open source programs
Name: elastix
Vendor: Palosanto Solutions S.A.
Version: 3.0.0
Release: 2
License: GPL
Group: Applications/System
#BuildRoot: %{_tmppath}/%{name}-%{version}-root
BuildArch: noarch
#Prereq: elastix-addons >= 3.0.0-1
Prereq: elastix-agenda >= 3.0.0-1
Prereq: elastix-email_admin >= 3.0.0-1
Prereq: elastix-fax >= 3.0.0-1
Prereq: elastix-pbx >= 3.0.0-1
Prereq: elastix-reports >= 3.0.0-1
Prereq: elastix-security >= 3.0.0-1
Prereq: elastix-system >= 3.0.0-1
Prereq: elastix-framework >= 3.0.0-1
Prereq: elastix-firstboot >= 3.0.0-1

%description
Elastix is a Web based software to administrate a PBX based in open source programs

%prep

%install

%pre

%post

%clean

%preun

%files

%changelog
* Fri Apr 12 2013 Luis Abarca <labarca@palosanto.com> 3.0.0-2
- DELETED: The IM package for now its not longer needed.

* Thu Sep 20 2012 Luis Abarca <labarca@palosanto.com> 3.0.0-1
- CHANGED: In spec file, changed prereq elastix-system >= 3.0.0-1
- CHANGED: In spec file, changed prereq elastix-security >= 3.0.0-1
- CHANGED: In spec file, changed prereq elastix-pbx >= 3.0.0-1
- CHANGED: In spec file, changed prereq elastix-email_admin >= 3.0.0-1
- CHANGED: In spec file, changed prereq elastix-framework >= 3.0.0-1
- CHANGED: In spec file, changed prereq elastix-agenda >= 3.0.0-1
- CHANGED: In spec file, changed prereq elastix-addons >= 3.0.0-1
- CHANGED: In spec file, changed prereq elastix-reports >= 3.0.0-1
- CHANGED: In spec file, changed prereq elastix-fax >= 3.0.0-1
- CHANGED: In spec file, changed prereq elastix-im >= 3.0.0-1
- CHANGED: In spec file, changed prereq elastix-firstboot >= 3.0.0-1

* Mon Sep 03 2012 Luis Abarca <labarca@palosanto.com> 2.3.0-10
- CHANGED: In spec file, changed prereq elastix-pbx >= 2.3.0-15
- CHANGED: In spec file, changed prereq elastix-framework >= 2.3.0-14
- CHANGED: In spec file, changed prereq elastix-reports >= 2.3.0-6
- CHANGED: In spec file, changed prereq elastix-firstboot >= 2.3.0-9

* Fri Aug 24 2012 Luis Abarca <labarca@palosanto.com> 2.3.0-9
- CHANGED: In spec file, changed prereq elastix-system >= 2.3.0-12
- CHANGED: In spec file, changed prereq elastix-security >= 2.3.0-7
- CHANGED: In spec file, changed prereq elastix-pbx >= 2.3.0-13
- CHANGED: In spec file, changed prereq elastix-email_admin >= 2.3.0-8
- CHANGED: In spec file, changed prereq elastix-framework >= 2.3.0-13
- CHANGED: In spec file, changed prereq elastix-agenda >= 2.3.0-7
- CHANGED: In spec file, changed prereq elastix-addons >= 2.3.0-6
- CHANGED: In spec file, changed prereq elastix-reports >= 2.3.0-4
- CHANGED: In spec file, changed prereq elastix-fax >= 2.3.0-4
- CHANGED: In spec file, changed prereq elastix-im >= 2.2.0-3
- CHANGED: In spec file, changed prereq elastix-my_extension >= 2.2.0-6

* Fri Jun 29 2012 Luis Abarca <labarca@palosanto.com> 2.3.0-8
- CHANGED: In spec file, changed prereq elastix-system >= 2.3.0-11
- CHANGED: In spec file, changed prereq elastix-security >= 2.3.0-6
- CHANGED: In spec file, changed prereq elastix-pbx >= 2.3.0-12
- CHANGED: In spec file, changed prereq elastix-email_admin >= 2.3.0-7
- CHANGED: In spec file, changed prereq elastix-framework >= 2.3.0-12
- CHANGED: In spec file, changed prereq elastix-agenda >= 2.3.0-7
- CHANGED: In spec file, changed prereq elastix-addons >= 2.3.0-5
- CHANGED: In spec file, changed prereq elastix-reports >= 2.3.0-4
- CHANGED: In spec file, changed prereq elastix-fax >= 2.3.0-4
- CHANGED: In spec file, changed prereq elastix-im >= 2.2.0-3
- CHANGED: In spec file, changed prereq elastix-my_extension >= 2.2.0-6

* Mon May 28 2012 Rocio Mera <rmera@palosanto.com> 2.3.0-7
- CHANGED: In spec file, changed prereq elastix-agenda >= 2.3.0-7

* Mon May 28 2012 Bruno Macias <bmacias@palosanto.com> 2.3.0-6
- CHANGED: In spec file, changed prereq elastix-addons >= 2.3.0-4
- CHANGED: In spec file, changed prereq elastix-fax >= 2.3.0-4
- CHANGED: In spec file, changed prereq elastix-pbx >= 2.3.0-9
- CHANGED: In spec file, changed prereq elastix-report >= 2.3.0-4
- CHANGED: In spec file, changed prereq elastix-framework >= 2.3.0-11  

* Mon Apr 02 2012 Rocio Mera <rmera@palosanto.com> 2.3.0-5
- CHANGED: In spec file, changed prereq elastix-system >= 2.3.0-6
- CHANGED: In spec file, changed prereq elastix-pbx >= 2.3.0-5
- CHANGED: In spec file, changed prereq elastix-email_admin >= 2.3.0-6
- CHANGED: In spec file, changed prereq elastix-addons >= 2.3.0-3
- CHANGED: In spec file, changed prereq elastix-framework >= 2.3.0-5

* Fri Mar 30 2012 Rocio Mera <rmera@palosanto.com> 2.3.0-4
- CHANGED: In spec file, changed prereq elastix-system >= 2.3.0-5
- CHANGED: In spec file, changed prereq elastix-security >= 2.3.0-4
- CHANGED: In spec file, changed prereq elastix-pbx >= 2.3.0-4
- CHANGED: In spec file, changed prereq elastix-email_admin >= 2.3.0-5
- CHANGED: In spec file, changed prereq elastix-framework >= 2.3.0-4
- CHANGED: In spec file, changed prereq elastix-agenda >= 2.3.0-3
- CHANGED: In spec file, changed prereq elastix-addons >= 2.3.0-2
- CHANGED: In spec file, changed prereq elastix-reports >= 2.3.0-3

* Mon Mar 27 2012 Rocio Mera <rmera@palosanto.com> 2.3.0-3
- CHANGED: In spec file, changed prereq elastix-system >= 2.3.0-3
- CHANGED: In spec file, changed prereq elastix-security >= 2.3.0-3
- CHANGED: In spec file, changed prereq elastix-pbx >= 2.3.0-3
- CHANGED: In spec file, changed prereq elastix-email_admin >= 2.3.0-4
- CHANGED: In spec file, changed prereq elastix-framework >= 2.3.0-4
- CHANGED: In spec file, changed prereq elastix-agenda >= 2.3.0-2
- CHANGED: In spec file, changed prereq elastix-reports >= 2.3.0-2

* Fri Mar 9 2012 Alberto Santos <asantos@palosanto.com> 2.3.0-2
- CHANGED: In spec file, changed prereq elastix-system >= 2.3.0-2
- CHANGED: In spec file, changed prereq elastix-fax >= 2.3.0-2
- CHANGED: In spec file, changed prereq elastix-pbx >= 2.3.0-2
- CHANGED: In spec file, changed prereq elastix-email_admin >= 2.3.0-2
- CHANGED: In spec file, changed prereq elastix-framework >= 2.3.0-2

* Wed Mar 7 2012 Rocio Mera <rmera@palosanto.com> 2.3.0-1
- CHANGED: In spec file, changed prereq elastix-addons >= 2.3.0-1
- CHANGED: In spec file, changed prereq elastix-agenda >= 2.3.0-1
- CHANGED: In spec file, changed prereq elastix-email_admin >= 2.3.0-1
- CHANGED: In spec file, changed prereq elastix-fax >= 2.3.0-1
- CHANGED: In spec file, changed prereq elastix-pbx >= 2.3.0-1
- CHANGED: In spec file, changed prereq elastix-reports >= 2.3.0-1
- CHANGED: In spec file, changed prereq elastix-security >= 2.3.0-1
- CHANGED: In spec file, changed prereq elastix-system >= 2.3.0-1
- CHANGED: In spec file, changed prereq elastix-framework >= 2.3.0-1

* Thu Jan 31 2012 Rocio Mera <rmera@palosanto.com> 2.2.0-26
- CHANGED: In spec file, changed prereq elastix-addons >= 2.2.0-12
- CHANGED: In spec file, changed prereq elastix-agenda >= 2.2.0-11
- CHANGED: In spec file, changed prereq elastix-pbx >= 2.2.0-25
- CHANGED: In spec file, changed prereq elastix-reports >= 2.2.0-13
- CHANGED: In spec file, changed prereq elastix-security >= 2.2.0-12
- CHANGED: In spec file, changed prereq elastix-system >= 2.2.0-20
- CHANGED: In spec file, changed prereq elastix-framework >= 2.2.0-29


* Sat Jan 28 2012 Rocio Mera <rmera@palosanto.com> 2.2.0-25
- CHANGED: In spec file, changed prereq elastix-addons >= 2.2.0-11
- CHANGED: In spec file, changed prereq elastix-agenda >= 2.2.0-10
- CHANGED: In spec file, changed prereq elastix-email_admin >= 2.2.0-13
- CHANGED: In spec file, changed prereq elastix-fax >= 2.2.0-7
- CHANGED: In spec file, changed prereq elastix-pbx >= 2.2.0-24
- CHANGED: In spec file, changed prereq elastix-reports >= 2.2.0-12
- CHANGED: In spec file, changed prereq elastix-security >= 2.2.0-11
- CHANGED: In spec file, changed prereq elastix-system >= 2.2.0-19
- CHANGED: In spec file, changed prereq elastix-framework >= 2.2.0-28

* Tue Jan 17 2012 Rocio Mera <rmera@palosanto.com> 2.2.0-24
- CHANGED: In spec file, changed prereq elastix-addons >= 2.2.0-10
- CHANGED: In spec file, changed prereq elastix-agenda >= 2.2.0-9
- CHANGED: In spec file, changed prereq elastix-email_admin >= 2.2.0-12
- CHANGED: In spec file, changed prereq elastix-pbx >= 2.2.0-23
- CHANGED: In spec file, changed prereq elastix-reports >= 2.2.0-11
- CHANGED: In spec file, changed prereq elastix-system >= 2.2.0-18
- CHANGED: In spec file, changed prereq elastix-framework >= 2.2.0-26

* Tue Jan 03 2012 Alberto Santos <asantos@palosanto.com> 2.2.0-23
- CHANGED: In spec file, changed prereq elastix-addons >= 2.2.0-9
- CHANGED: In spec file, changed prereq elastix-pbx >= 2.2.0-22
- CHANGED: In spec file, changed prereq elastix-reports >= 2.2.0-9
- CHANGED: In spec file, changed prereq elastix-security >= 2.2.0-10
- CHANGED: In spec file, changed prereq elastix-framework >= 2.2.0-25

* Tue Dec 20 2011 Eduardo Cueva <ecueva@palosanto.com> 2.2.0-22
- CHANGED: In spec file, changed prereq elastix-framework >= 2.2.0-23
- CHANGED: In spec file, changed prereq elastix-addons >= 2.2.0-8
- CHANGED: In spec file, changed prereq elastix-agenda >= 2.2.0-8
- CHANGED: In spec file, changed prereq elastix-pbx >= 2.2.0-19
- CHANGED: In spec file, changed prereq elastix-system >= 2.2.0-17

* Mon Dec 05 2011 Eduardo Cueva <ecueva@palosanto.com> 2.2.0-21
- CHANGED: In spec file, changed prereq elastix-framework >= 2.2.0-21

* Fri Dec 02 2011 Alberto Santos <asantos@palosanto.com> 2.2.0-20
- CHANGED: In spec file, changed prereq elastix-framework >= 2.2.0-20

* Thu Dec 01 2011 Alberto Santos <asantos@palosanto.com> 2.2.0-19
- ADDED: In spec file, added prereq elastix-framework >= 2.2.0-19

* Mon Nov 28 2011 Alberto Santos <asantos@palosanto.com> 2.2.0-18
- Initial Version
