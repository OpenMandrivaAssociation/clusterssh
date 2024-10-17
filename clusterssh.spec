%define name	clusterssh
%define version 3.28
%define release 3

Name:          %name
Version:       %version
Release:       %release
Summary:       Secure concurrent multi-server terminal control
Group:         Shells
License:       GPL
URL:           https://clusterssh.sourceforge.net
Source0:       http://download.sourceforge.net/%{name}/%{name}-%{version}.tar.gz
BuildRoot:     %{_tmppath}/%{name}-%{version}-%{release}
BuildArch:     noarch
Requires:      perl-Tk perl-X11-Protocol xterm
Buildrequires:	perl-devel

%description
Control multiple terminals open on different servers to perform administration
tasks, for example multiple hosts requiring the same config within a cluster.
Not limited to use with clusters, however.

%prep
%setup -q

%build
%configure
%make

%install
rm -rf %{buildroot}
make install DESTDIR=%{buildroot}

%clean
rm -rf %{buildroot}

%files
%defattr(-,root,root,-)
%doc COPYING AUTHORS README NEWS ChangeLog
%{_bindir}/cssh
%{_mandir}/man1/*.1*




%changelog
* Sun Dec 05 2010 Oden Eriksson <oeriksson@mandriva.com> 3.28-2mdv2011.0
+ Revision: 610143
- rebuild

* Fri Dec 25 2009 Frederik Himpe <fhimpe@mandriva.org> 3.28-1mdv2010.1
+ Revision: 482288
- update to new version 3.28

* Thu Sep 24 2009 Frederik Himpe <fhimpe@mandriva.org> 3.27-1mdv2010.0
+ Revision: 448488
- Update to new version 3.27

* Tue Jun 09 2009 Frederik Himpe <fhimpe@mandriva.org> 3.26-1mdv2010.0
+ Revision: 384474
- Update to new version 3.26

* Fri Jan 09 2009 Jérôme Soyer <saispo@mandriva.org> 3.22-1mdv2009.1
+ Revision: 327425
- New upstream version

* Wed Jul 23 2008 Thierry Vignaud <tv@mandriva.org> 3.19.1-3mdv2009.0
+ Revision: 243533
- rebuild

* Fri Dec 21 2007 Olivier Blin <oblin@mandriva.com> 3.19.1-1mdv2008.1
+ Revision: 136322
- restore BuildRoot

  + Thierry Vignaud <tv@mandriva.org>
    - kill re-definition of %%buildroot on Pixel's request


* Wed Jan 17 2007 Erwan Velu <erwan@mandriva.org> 3.19.1-1mdv2007.0
+ Revision: 109909
- 3.19.1
- Import clusterssh

* Fri Jun 23 2006 Erwan Velu <erwan@seanodes.com> 3.18.1-2
- Rebuild

* Mon Dec 19 2005 Erwan Velu <erwan@seanodes.com> 3.18.1-1mdk
- Initial release

