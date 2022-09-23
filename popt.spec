#
# This file is auto-generated. DO NOT EDIT
# Generated by: autospec.py
#
%define keepstatic 1
Name     : popt
Version  : 1.18
Release  : 25
URL      : https://github.com/rpm-software-management/popt/archive/popt-1.18-release/popt-1.18.tar.gz
Source0  : https://github.com/rpm-software-management/popt/archive/popt-1.18-release/popt-1.18.tar.gz
Summary  : popt library.
Group    : Development/Tools
License  : MIT X11
Requires: popt-lib = %{version}-%{release}
Requires: popt-license = %{version}-%{release}
Requires: popt-locales = %{version}-%{release}
BuildRequires : gettext
Patch1: backport-Work-around-test-failures.patch

%description
This is the popt(3) command line option parsing library. While it is similiar
to getopt(3), it contains a number of enhancements, including:

%package dev
Summary: dev components for the popt package.
Group: Development
Requires: popt-lib = %{version}-%{release}
Provides: popt-devel = %{version}-%{release}
Requires: popt = %{version}-%{release}

%description dev
dev components for the popt package.


%package lib
Summary: lib components for the popt package.
Group: Libraries
Requires: popt-license = %{version}-%{release}

%description lib
lib components for the popt package.


%package license
Summary: license components for the popt package.
Group: Default

%description license
license components for the popt package.


%package locales
Summary: locales components for the popt package.
Group: Default

%description locales
locales components for the popt package.


%package staticdev
Summary: staticdev components for the popt package.
Group: Default
Requires: popt-dev = %{version}-%{release}

%description staticdev
staticdev components for the popt package.


%prep
%setup -q -n popt-popt-1.18-release
cd %{_builddir}/popt-popt-1.18-release
%patch1 -p1

%build
export http_proxy=http://127.0.0.1:9/
export https_proxy=http://127.0.0.1:9/
export no_proxy=localhost,127.0.0.1,0.0.0.0
export LANG=C.UTF-8
export SOURCE_DATE_EPOCH=1663958175
export GCC_IGNORE_WERROR=1
export CFLAGS="$CFLAGS -Os -fdata-sections -ffunction-sections -fno-lto -fno-semantic-interposition "
export FCFLAGS="$FFLAGS -Os -fdata-sections -ffunction-sections -fno-lto -fno-semantic-interposition "
export FFLAGS="$FFLAGS -Os -fdata-sections -ffunction-sections -fno-lto -fno-semantic-interposition "
export CXXFLAGS="$CXXFLAGS -Os -fdata-sections -ffunction-sections -fno-lto -fno-semantic-interposition "
%autogen
make  %{?_smp_mflags}

%check
export LANG=C.UTF-8
export http_proxy=http://127.0.0.1:9/
export https_proxy=http://127.0.0.1:9/
export no_proxy=localhost,127.0.0.1,0.0.0.0
make %{?_smp_mflags} check || :

%install
export SOURCE_DATE_EPOCH=1663958175
rm -rf %{buildroot}
mkdir -p %{buildroot}/usr/share/package-licenses/popt
cp %{_builddir}/popt-popt-%{version}-release/COPYING %{buildroot}/usr/share/package-licenses/popt/61bb7a8ea669080cfc9e7dbf37079eae70b535fb
%make_install
%find_lang popt

%files
%defattr(-,root,root,-)

%files dev
%defattr(-,root,root,-)
/usr/include/popt.h
/usr/lib64/libpopt.so
/usr/lib64/pkgconfig/popt.pc
/usr/share/man/man3/popt.3

%files lib
%defattr(-,root,root,-)
/usr/lib64/libpopt.so.0
/usr/lib64/libpopt.so.0.0.1

%files license
%defattr(0644,root,root,0755)
/usr/share/package-licenses/popt/61bb7a8ea669080cfc9e7dbf37079eae70b535fb

%files staticdev
%defattr(-,root,root,-)
/usr/lib64/libpopt.a

%files locales -f popt.lang
%defattr(-,root,root,-)

