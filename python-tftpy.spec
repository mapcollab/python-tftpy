Name: python-tftpy
Version: 0.6.3
Release: 0.2%{?dist}
Packager: Michael P. Soulier <michael_soulier@mitel.com>
Summary: A pure python TFTP library.
License: BSD
Group: Libraries/Net
URL: http://tftpy.sf.net/
Source0: %{name}-%{version}.tar.gz
BuildRequires: python-devel
Requires: python
BuildRoot: %{_tmppath}/%{name}-%{version}-root
BuildArch: noarch

AutoReqProv: no
%define debug_package %{nil}
%define __os_install_post %{nil}

%description
This module is a pure Python implementation of the TFTP protocol, RFCs 1350,
2347, 2348 and the tsize option from 2349.

%package examples
Summary: A pure python TFTP library - example client/server
Group: Libraries/Net
Requires:%{name} = %{version}
%description examples
Example scripts using python-tftpy.

%prep
%setup -q -n %{name}-%{version}

%build
%{__python} setup.py build

%install
rm -rf $RPM_BUILD_ROOT
%{__python} setup.py install \
    --prefix=$RPM_BUILD_ROOT/usr \
    --record=filelist-%{name}-%{version}-%{release}-temp

cat filelist-%{name}-%{version}-%{release}-temp | \
    sed -e "s;^$RPM_BUILD_ROOT;;" | \
    grep -v "doc/" | \
    grep -v "bin/" \
    > filelist-%{name}-%{version}-%{release}

%clean
rm -rf $RPM_BUILD_ROOT

%files -f filelist-%{name}-%{version}-%{release}
%defattr(-,root,root)

%files examples
%defattr(0755,root,root)
/usr/bin/*


%changelog
* Fri Dec 23 2016 Tomasz Rostanski <tomasz.rostanski@thalesgroup.com> 0.6.3-0.2
- python-tftpy.spec: fix %%setup (tomasz.rostanski@thalesgroup.com.pl)

* Fri Dec 23 2016 Michal Gawlik <michal.gawlik@thalesgroup.com> 0.6.3-0.1
- new package built with tito

* Tue Feb 15 2011 Michael P. Soulier <michael_soulier@mitel.com>
- [0.5.1-01]
- Initial rpm build.
