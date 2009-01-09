%define name	clusterssh
%define version 3.22
%define release %mkrel 1

Name:          %name
Version:       %version
Release:       %release
Summary:       Secure concurrent multi-server terminal control
Group:         Shells
License:       GPL
URL:           http://clusterssh.sourceforge.net
Source0:       http://download.sourceforge.net/%{name}/%{name}-%{version}.tar.bz2
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


