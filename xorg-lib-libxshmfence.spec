Summary:	X Shared Memory Fence library
Summary(pl.UTF-8):	Biblioteka X Shared Memory Fence
Name:		xorg-lib-libxshmfence
Version:	1.3.3
Release:	1
License:	MIT
Group:		X11/Libraries
Source0:	https://xorg.freedesktop.org/releases/individual/lib/libxshmfence-%{version}.tar.xz
# Source0-md5:	9805be7e18f858bed9938542ed2905dc
URL:		https://xorg.freedesktop.org/
BuildRequires:	autoconf >= 2.60
BuildRequires:	automake
BuildRequires:	libtool >= 2:2
BuildRequires:	pkgconfig >= 1:0.19
BuildRequires:	tar >= 1:1.22
BuildRequires:	xorg-util-util-macros >= 1.3
BuildRequires:	xz
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%description
X Shared Memory Fence library - shared memory "SyncFence"
synchronization primitive.

This library offers a CPU-based synchronization primitive compatible
with the X SyncFence objects that can be shared between processes
using file descriptor passing.

%description -l pl.UTF-8
Biblioteka X Shared Memory Fence to implementacja synchronizacji
pamięci dzielonej "SyncFence.

Biblioteka oferuje synchronizację dla procesora zgodną z obiektami X
SyncFence, które można współdzieloć między procesami przy użyciu
przekazywania deskryptorów plików.

%package devel
Summary:	Header files for libxshmfence library
Summary(pl.UTF-8):	Pliki nagłówkowe biblioteki libxshmfence
Group:		X11/Development/Libraries
Requires:	%{name} = %{version}-%{release}

%description devel
xshmfence library.

This package contains the header files needed to develop programs that
use libxshmfence.

%description devel -l pl.UTF-8
Biblioteka xshmfence.

Pakiet zawiera pliki nagłówkowe niezbędne do kompilowania programów
używających biblioteki libxshmfence.

%package static
Summary:	Static libxshmfence library
Summary(pl.UTF-8):	Biblioteka statyczna libxshmfence
Group:		X11/Development/Libraries
Requires:	%{name}-devel = %{version}-%{release}

%description static
xshmfence library.

This package contains the static libxshmfence library.

%description static -l pl.UTF-8
Biblioteka xshmfence.

Pakiet zawiera statyczną bibliotekę libxshmfence.

%prep
%setup -q -n libxshmfence-%{version}

%build
%{__libtoolize}
%{__aclocal}
%{__autoconf}
%{__autoheader}
%{__automake}
%configure

%{__make}

%install
rm -rf $RPM_BUILD_ROOT

%{__make} install \
	DESTDIR=$RPM_BUILD_ROOT

# obsoleted by pkg-config, no external dependencies
%{__rm} $RPM_BUILD_ROOT%{_libdir}/libxshmfence.la

%clean
rm -rf $RPM_BUILD_ROOT

%post	-p /sbin/ldconfig
%postun -p /sbin/ldconfig

%files
%defattr(644,root,root,755)
%doc COPYING ChangeLog README.md
%attr(755,root,root) %{_libdir}/libxshmfence.so.*.*.*
%attr(755,root,root) %ghost %{_libdir}/libxshmfence.so.1

%files devel
%defattr(644,root,root,755)
%attr(755,root,root) %{_libdir}/libxshmfence.so
%{_includedir}/X11/xshmfence.h
%{_pkgconfigdir}/xshmfence.pc

%files static
%defattr(644,root,root,755)
%{_libdir}/libxshmfence.a
