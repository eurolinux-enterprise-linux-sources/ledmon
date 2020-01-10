Summary: Enclosure LED Utilities
Name: ledmon
Version: 0.90
Release: 1%{?dist}
License: GPLv2+
Group: Applications/System
URL: http://sourceforge.net/projects/ledmon/
Source0: http://download.sourceforge.net/%{name}/%{name}-%{version}.tar.gz
Patch0: ledmon_cflags.patch
BuildRequires: perl
BuildRequires: sg3_utils-devel
BuildRequires: systemd-devel
Obsoletes: ledctl = 0.1-1
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
make CFLAGS="$RPM_OPT_FLAGS --std=c99"

%install
make install INSTALL="%{__install} -p" DESTDIR=$RPM_BUILD_ROOT SBIN_DIR=$RPM_BUILD_ROOT/%{_sbindir} MANDIR=$RPM_BUILD_ROOT%{_mandir}

%files
%doc README COPYING
%{_sbindir}/ledctl
%{_sbindir}/ledmon
%{_mandir}/*/*

%changelog
* Wed Jun 13 2018 Jan Synáček <jsynacek@redhat.com> - 0.90-1
- Update to 0.90 (#1494473)

* Fri May 12 2017 Jan Synáček <jsynacek@redhat.com> - 0.80-2
- LEDs don't blink during resync/recovery operations on the NVMe RAID volume (#1449990)

* Mon Feb  6 2017 Jan Synáček <jsynacek@redhat.com> - 0.80-1
- Update to 0.80 (#1380018)

* Wed Sep 16 2015 Jan Synáček <jsynacek@redhat.com> - 0.79-4
- Fix: Ledmon does not work with AHCI (#1262799)

* Fri Jan 24 2014 Daniel Mach <dmach@redhat.com> - 0.79-3
- Mass rebuild 2014-01-24

* Fri Dec 27 2013 Daniel Mach <dmach@redhat.com> - 0.79-2
- Mass rebuild 2013-12-27

* Thu Nov 28 2013 Jan Synáček <jsynacek@redhat.com> - 0.79-1
- Update to 0.79
- Resolves: #887206

* Fri Apr 19 2013 Jan Synáček <jsynacek@redhat.com> - 0.77-1
- Update to 0.77
- Documentation enhancements

* Thu Feb 14 2013 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 0.75-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_19_Mass_Rebuild

* Mon Jan 07 2013 Jan Synáček <jsynacek@redhat.com> - 0.75-1
- Update to 0.75 and drop upstreamed patch

* Thu Nov 15 2012 Jan Synáček <jsynacek@redhat.com> - 0.74-3
- Some coverity fixes

* Fri Oct 19 2012 Jan Synáček <jsynacek@redhat.com> - 0.74-2
- Require sg3_utils-libs

* Mon Aug 13 2012 Jan Synáček <jsynacek@redhat.com> - 0.74-1
- Update to 0.74
- Resolves: #847072

* Tue Aug 07 2012 Jan Synáček <jsynacek@redhat.com> - 0.72-1
- Update to 0.72 and update patch
- Resolves: #846018

* Wed Jul 25 2012 Jan Synáček <jsynacek@redhat.com> - 0.40-1
- Update to 0.40
- Resolves: #838086
- Make spec fedora-review friendly

* Thu Jul 19 2012 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 0.32-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_18_Mass_Rebuild

* Mon Mar 05 2012 Jan Synáček <jsynacek@redhat.com> - 0.32-1
- Update to 0.32

* Fri Feb 10 2012 Jan Synáček <jsynacek@redhat.com> - 0.31-1
- Update to 0.31

* Fri Jan 13 2012 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 0.1-4
- Rebuilt for https://fedoraproject.org/wiki/Fedora_17_Mass_Rebuild

* Mon Feb 07 2011 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 0.1-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_15_Mass_Rebuild

* Fri Jan 14 2011 Jiri Moskovcak <jmoskovc@redhat.com> 0.1-2
- renamed to ledmon, because ledctl is taken

* Fri Jan 07 2011 Jiri Moskovcak <jmoskovc@redhat.com> 0.1-1
- initial release
