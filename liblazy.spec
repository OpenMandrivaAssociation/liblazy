%define major	1
%define libname	%mklibname lazy %{major}
%define devname	%mklibname lazy -d

%define _disable_lto 1

Summary:	Liblazy - D-Bus methods provided for convenience
Name:		liblazy
Version:	0.2
Release:	16
License:	LGPLv2
Group:		Development/C
Source0:	%{name}-%{version}.tar.bz2
BuildRequires:	pkgconfig(dbus-1)

%description
Liblazy is a simple and easy to use library that provides convenient
functions for sending messages over the D-Bus daemon, querying
information from HAL or asking PolicyKit for a privilege.

%package -n %{libname}
Summary:	%{summary}
Group:		%{group}

%description -n %{libname}
Liblazy is a simple and easy to use library that provides convenient
functions for sending messages over the D-Bus daemon, querying
information from HAL or asking PolicyKit for a privilege.

%package -n %{devname}
Summary:	%{summary}
Group:		%{group}
Provides:	%{name}-devel = %{version}-%{release}
Requires:	%{libname} = %{version}-%{release}

%description -n %{devname}
Liblazy is a simple and easy to use library that provides convenient
functions for sending messages over the D-Bus daemon, querying
information from HAL or asking PolicyKit for a privilege.

%prep
%setup -q

%build
export CFLAGS="$RPM_OPT_FLAGS"

%configure2_5x \
	--enable-static=no 

%make

%install
%makeinstall_std

%files -n %{libname}
%{_libdir}/liblazy.so.%{major}*

%files -n %{devname}
%{_includedir}/liblazy.h
%{_libdir}/liblazy.so
%{_libdir}/pkgconfig/*.pc

