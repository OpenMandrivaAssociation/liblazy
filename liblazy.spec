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



%changelog
* Mon May 02 2011 Oden Eriksson <oeriksson@mandriva.com> 0.2-6mdv2011.0
+ Revision: 661480
- mass rebuild

* Sun Nov 28 2010 Oden Eriksson <oeriksson@mandriva.com> 0.2-5mdv2011.0
+ Revision: 602566
- rebuild

* Tue Mar 16 2010 Oden Eriksson <oeriksson@mandriva.com> 0.2-4mdv2010.1
+ Revision: 520877
- rebuilt for 2010.1

* Wed Sep 02 2009 Christophe Fergeau <cfergeau@mandriva.com> 0.2-3mdv2010.0
+ Revision: 425590
- rebuild

* Tue Jun 17 2008 Thierry Vignaud <tv@mandriva.org> 0.2-2mdv2009.0
+ Revision: 222919
- rebuild

  + Pixel <pixel@mandriva.com>
    - do not call ldconfig in %%post/%%postun, it is now handled by filetriggers

  + Olivier Blin <oblin@mandriva.com>
    - restore BuildRoot

* Sat Dec 22 2007 Helio Chissini de Castro <helio@mandriva.com> 0.2-1mdv2008.1
+ Revision: 136759
- Fix group
- New upstream version of liblazy. Required for new kickoff menu

  + Thierry Vignaud <tv@mandriva.org>
    - kill re-definition of %%buildroot on Pixel's request

* Fri Apr 27 2007 Helio Chissini de Castro <helio@mandriva.com> 0.1.1-3mdv2008.0
+ Revision: 18668
- Missing requires

* Thu Apr 26 2007 Helio Chissini de Castro <helio@mandriva.com> 0.1.1-2mdv2008.0
+ Revision: 18416
- import liblazy-0.1.1-2mdv2008.0


