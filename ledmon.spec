Summary: Enclosure LED Utilities
Name: ledmon
Version: 0.79
Release: 1%{?dist}
License: GPLv2+
Group: Applications/System
URL: http://sourceforge.net/projects/ledmon/
Source0: http://download.sourceforge.net/%{name}/%{name}-%{version}.tar.gz
Patch0: ledmon_cflags.patch
BuildRequires: perl
BUildRequires: sg3_utils-devel
BuildRoot: %{_tmppath}/%{name}-%{version}-%{release}-root-%(%{__id_u} -n)
Provides: ledctl = %{version}-%{release}
Requires: sg3_utils-libs

%description
The ledmon and ledctl are user space applications design to control LED
associated with each slot in an enclosure or a drive bay. There are two
types of system: 2-LED system (Activity LED, Status LED) and 3-LED system
(Activity LED, Locate LED, Fail LED). User must have root privileges to
use this application.

%prep
%setup -q
%patch0 -p1 -b .cflags

%build
# can't use smp_flags because -j4 makes the build fail
make CFLAGS="$RPM_OPT_FLAGS"

%install
rm -rf $RPM_BUILD_ROOT
make install INSTALL="%{__install} -p" DESTDIR=$RPM_BUILD_ROOT SBIN_DIR=$RPM_BUILD_ROOT/%{_sbindir} MANDIR=$RPM_BUILD_ROOT%{_mandir}

%clean
rm -rf $RPM_BUILD_ROOT

%files
%defattr(-,root,root,-)
%doc README COPYING
%{_sbindir}/ledctl
%{_sbindir}/ledmon
%{_mandir}/*/*

%changelog
* Tue Jun 10 2014 Jan Synáček <jsynacek@redhat.com> - 0.79-1
- Update to 0.79 (#1030622)

* Fri Aug 23 2013 Jan Synáček <jsynacek@redhat.com> - 0.78-1
- Update to 0.78 (#922976)

* Thu Oct 18 2012 Jan Synáček <jsynacek@redhat.com> - 0.74-1
- Update to 0.74

* Mon Mar 05 2012 Jan Synáček <jsynacek@redhat.com> - 0.32-1
- Update to 0.32

* Tue Feb 14 2012 Jan Synáček <jsynacek@redhat.com> - 0.31-2
- Remove 'Obsolete' from specfile

* Fri Feb 10 2012 Jan Synáček <jsynacek@redhat.com> - 0.31-1
- initial release
