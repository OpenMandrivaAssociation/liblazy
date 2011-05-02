%define lib_major 1
%define lib_name %mklibname lazy %{lib_major}
%define lib_name_devel %mklibname lazy -d

Name: liblazy
Summary: Liblazy - D-Bus methods provided for convenience
Version: 0.2
Release: %mkrel 6
License: LGPL
Group: Development/C
Source: %{name}-%{version}.tar.bz2
BuildRequires: dbus-devel 
BuildRequires: pkgconfig
BuildRoot:      %{_tmppath}/%{name}-%{version}-build

%description
Liblazy is a simple and easy to use library that provides convenient
functions for sending messages over the D-Bus daemon, querying
information from HAL or asking PolicyKit for a privilege.

Authors:
--------
    Holger Macht <holger@homac.de>

#--------------------------------------------------------------------

%package -n %{lib_name}
Summary:  %{summary}
Group: %{group}

%description -n %{lib_name}
Liblazy is a simple and easy to use library that provides convenient
functions for sending messages over the D-Bus daemon, querying
information from HAL or asking PolicyKit for a privilege.

%if %mdkversion < 200900
%post -p /sbin/ldconfig
%endif
%if %mdkversion < 200900
%postun -p /sbin/ldconfig
%endif

%files -n %{lib_name}
%defattr(-,root,root)
%_libdir/liblazy.so.*

#--------------------------------------------------------------------

%package -n %{lib_name_devel}
Summary:  %{summary}
Group: %{group}
Provides: %name-devel
Requires: %{lib_name} = %{version}
Obsoletes: %{_lib}lazy0-devel

%description -n %{lib_name_devel}
Liblazy is a simple and easy to use library that provides convenient
functions for sending messages over the D-Bus daemon, querying
information from HAL or asking PolicyKit for a privilege.

%files -n %{lib_name_devel}
%defattr(-,root,root)
%_libdir/liblazy.so
%_libdir/liblazy.la
%_includedir/liblazy.h
%_libdir/pkgconfig/*.pc

#--------------------------------------------------------------------

%prep
%setup -q

%build
export CFLAGS="$RPM_OPT_FLAGS"

%configure2_5x \
    --enable-static=no 

%make

%install
make DESTDIR=%buildroot install

%clean
rm -rf %buildroot 

