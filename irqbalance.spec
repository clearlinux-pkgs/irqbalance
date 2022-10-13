#
# This file is auto-generated. DO NOT EDIT
# Generated by: autospec.py
#
Name     : irqbalance
Version  : 1.9.1
Release  : 24
URL      : https://github.com/Irqbalance/irqbalance/archive/v1.9.1/irqbalance-1.9.1.tar.gz
Source0  : https://github.com/Irqbalance/irqbalance/archive/v1.9.1/irqbalance-1.9.1.tar.gz
Source1  : irqbalance.tmpfiles
Summary  : No detailed summary available
Group    : Development/Tools
License  : GPL-2.0
Requires: irqbalance-autostart = %{version}-%{release}
Requires: irqbalance-bin = %{version}-%{release}
Requires: irqbalance-config = %{version}-%{release}
Requires: irqbalance-license = %{version}-%{release}
Requires: irqbalance-man = %{version}-%{release}
Requires: irqbalance-services = %{version}-%{release}
BuildRequires : buildreq-meson
BuildRequires : numactl-dev
BuildRequires : pkgconfig(glib-2.0)
BuildRequires : pkgconfig(libcap-ng)
BuildRequires : pkgconfig(libnl-3.0)
BuildRequires : pkgconfig(libnl-genl-3.0)
BuildRequires : pkgconfig(libsystemd)
BuildRequires : pkgconfig(ncursesw)
BuildRequires : pkgconfig(numa)

%description
This directory contains meson build instructions for irqbalance. This is here to see if there is any interest from
the general community.

%package autostart
Summary: autostart components for the irqbalance package.
Group: Default

%description autostart
autostart components for the irqbalance package.


%package bin
Summary: bin components for the irqbalance package.
Group: Binaries
Requires: irqbalance-config = %{version}-%{release}
Requires: irqbalance-license = %{version}-%{release}
Requires: irqbalance-services = %{version}-%{release}

%description bin
bin components for the irqbalance package.


%package config
Summary: config components for the irqbalance package.
Group: Default

%description config
config components for the irqbalance package.


%package license
Summary: license components for the irqbalance package.
Group: Default

%description license
license components for the irqbalance package.


%package man
Summary: man components for the irqbalance package.
Group: Default

%description man
man components for the irqbalance package.


%package services
Summary: services components for the irqbalance package.
Group: Systemd services

%description services
services components for the irqbalance package.


%prep
%setup -q -n irqbalance-1.9.1
cd %{_builddir}/irqbalance-1.9.1

%build
export http_proxy=http://127.0.0.1:9/
export https_proxy=http://127.0.0.1:9/
export no_proxy=localhost,127.0.0.1,0.0.0.0
export LANG=C.UTF-8
export SOURCE_DATE_EPOCH=1665689146
export GCC_IGNORE_WERROR=1
export CFLAGS="$CFLAGS -fno-lto "
export FCFLAGS="$FFLAGS -fno-lto "
export FFLAGS="$FFLAGS -fno-lto "
export CXXFLAGS="$CXXFLAGS -fno-lto "
%autogen --disable-static
make  %{?_smp_mflags}

%install
export SOURCE_DATE_EPOCH=1665689146
rm -rf %{buildroot}
mkdir -p %{buildroot}/usr/share/package-licenses/irqbalance
cp %{_builddir}/irqbalance-%{version}/COPYING %{buildroot}/usr/share/package-licenses/irqbalance/dfac199a7539a404407098a2541b9482279f690d || :
%make_install
mkdir -p %{buildroot}/usr/lib/tmpfiles.d
install -m 0644 %{SOURCE1} %{buildroot}/usr/lib/tmpfiles.d/irqbalance.conf
## install_append content
mkdir -p %{buildroot}/usr/lib/systemd/system/multi-user.target.wants
install -m0644 misc/irqbalance.service %{buildroot}/usr/lib/systemd/system/
ln -s ../irqbalance.service %{buildroot}/usr/lib/systemd/system/multi-user.target.wants/irqbalance.service
## install_append end

%files
%defattr(-,root,root,-)

%files autostart
%defattr(-,root,root,-)
/usr/lib/systemd/system/multi-user.target.wants/irqbalance.service

%files bin
%defattr(-,root,root,-)
/usr/bin/irqbalance
/usr/bin/irqbalance-ui

%files config
%defattr(-,root,root,-)
/usr/lib/tmpfiles.d/irqbalance.conf

%files license
%defattr(0644,root,root,0755)
/usr/share/package-licenses/irqbalance/dfac199a7539a404407098a2541b9482279f690d

%files man
%defattr(0644,root,root,0755)
/usr/share/man/man1/irqbalance-ui.1
/usr/share/man/man1/irqbalance.1

%files services
%defattr(-,root,root,-)
%exclude /usr/lib/systemd/system/multi-user.target.wants/irqbalance.service
/usr/lib/systemd/system/irqbalance.service
