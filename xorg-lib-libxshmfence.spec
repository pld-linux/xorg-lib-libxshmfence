Summary:	X Shared Memory Fence library
Summary(pl.UTF-8):	Biblioteka X Shared Memory Fence
Name:		xorg-lib-libxshmfence
Version:	1.0
Release:	1
License:	MIT
Group:		X11/Libraries
Source0:	http://xorg.freedesktop.org/releases/individual/lib/libxshmfence-%{version}.tar.bz2
# Source0-md5:	b4437ce302bd6c3f4abda3d9330ddcf9
URL:		http://xorg.freedesktop.org/
BuildRequires:	autoconf >= 2.57
BuildRequires:	automake
BuildRequires:	libtool
BuildRequires:	pkgconfig >= 1:0.19
BuildRequires:	xorg-util-util-macros >= 1.2
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%description
X Shared Memory Fence library.

%description -l pl.UTF-8
Biblioteka X Shared Memory Fence.

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
%doc ChangeLog
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
