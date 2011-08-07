%define byaccdate 20070509

Summary: Berkeley Yacc, a parser generator
Name: byacc
Version: 1.9.%{byaccdate}
Release: 6.1%{?dist}
License: Public Domain
Group: Development/Tools
URL: http://invisible-island.net/byacc/byacc.html
Source: ftp://invisible-island.net/byacc/byacc-%{byaccdate}.tgz
Patch1: skeleton.c.diff
BuildRoot: %{_tmppath}/%{name}-%{version}-%{release}-root-%(%{__id_u} -n)

%description
Byacc (Berkeley Yacc) is a public domain LALR parser generator which
is used by many programs during their build process.

If you are going to do development on your system, you will want to install
this package.

%prep
%setup -q -n byacc-%{byaccdate}
%patch1 -p1

%build
%configure --disable-dependency-tracking
make %{?_smp_mflags}

%install
rm -rf $RPM_BUILD_ROOT
make DESTDIR=$RPM_BUILD_ROOT install
ln -s yacc $RPM_BUILD_ROOT/%{_bindir}/byacc
ln -s yacc.1 $RPM_BUILD_ROOT/%{_mandir}/man1/byacc.1

%check
echo ====================TESTING=========================
make check
echo ====================TESTING END=====================

%clean
rm -rf $RPM_BUILD_ROOT

%files
%doc ACKNOWLEDGEMENTS CHANGES NEW_FEATURES NOTES NO_WARRANTY README
%defattr(-,root,root,-)
%{_bindir}/yacc
%{_bindir}/byacc
%{_mandir}/man1/yacc.1*
%{_mandir}/man1/byacc.1*

%changelog
* Mon Nov 30 2009 Dennis Gregorovic <dgregor@redhat.com> - 1.9.20070509-6.1
- Rebuilt for RHEL 6

* Fri Jul 24 2009 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 1.9.20070509-6
- Rebuilt for https://fedoraproject.org/wiki/Fedora_12_Mass_Rebuild

* Mon Feb 23 2009 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 1.9.20070509-5
- Rebuilt for https://fedoraproject.org/wiki/Fedora_11_Mass_Rebuild

* Mon Jul 14 2008 Petr Machata <pmachata@redhat.com> - 1.9.20070509-4
- Add a patch that fixes ancient buffer overflow
- Resolves: #454583

* Tue Feb 19 2008 Fedora Release Engineering <rel-eng@fedoraproject.org> - 1.9.20070509-2
- Autorebuild for GCC 4.3

* Tue Nov 13 2007 Petr Machata <pmachata@redhat.com> - 1.9.20070509-1
- Update to the 20070509 release.
- Related: #225632

* Fri Sep 12 2007 Matthias Saou <http://freshrpms.net/> 1.9.20050813-2
- Update summary.
- Remove useless doc copying in install section.
- Add NOTES and NO_WARRANTY docs.

* Thu Feb  2 2007 Petr Machata <pmachata@redhat.com> - 1.9.20050813-1
- Thomas Dickey's 20050813 version of byacc:
  - own build system (linux patch reverted)
  - use tmpfile (security patch reverted)
- Tidy up the specfile per rpmlint comments

* Wed Jul 12 2006 Jesse Keating <jkeating@redhat.com> - 1.9-29.2.2
- rebuild

* Fri Feb 10 2006 Jesse Keating <jkeating@redhat.com> - 1.9-29.2.1
- bump again for double-long bug on ppc(64)

* Tue Feb 07 2006 Jesse Keating <jkeating@redhat.com> - 1.9-29.2
- rebuilt for new gcc4.1 snapshot and glibc changes

* Fri Dec 09 2005 Jesse Keating <jkeating@redhat.com>
- rebuilt

* Sun Feb 27 2005 Florian La Roche <laroche@redhat.com>
- Copyright: -> License:

* Tue Jun 15 2004 Elliot Lee <sopwith@redhat.com>
- rebuilt

* Fri Feb 13 2004 Elliot Lee <sopwith@redhat.com>
- rebuilt

* Wed Jun 04 2003 Elliot Lee <sopwith@redhat.com>
- rebuilt

* Wed Jan 22 2003 Tim Powers <timp@redhat.com>
- rebuilt

* Thu Dec 05 2002 Elliot Lee <sopwith@redhat.com> 1.9-23
- Rebuild

* Fri Jun 21 2002 Tim Powers <timp@redhat.com>
- automated rebuild

* Thu May 23 2002 Tim Powers <timp@redhat.com>
- automated rebuild

* Wed Jan 09 2002 Tim Powers <timp@redhat.com>
- automated rebuild

* Sun Jun 24 2001 Elliot Lee <sopwith@redhat.com>
- Bump release + rebuild.

* Fri Jan 05 2001 Preston Brown <pbrown@redhat.com>
- security patch for tmpfile creation from Olaf Kirch <okir@lst.de>

* Fri Sep 29 2000 Bernhard Rosenkraenzer <bero@redhat.com>
- Update to the version in FreeBSD CVS - it's actively maintained, unlike
  the 1993 4BSD version we used to have

* Wed Jul 12 2000 Prospector <bugzilla@redhat.com>
- automatic rebuild

* Wed Jun 28 2000 Bill Nottingham <notting@redhat.com>
- fix perms in tarball

* Mon Jun 19 2000 Bernhard Rosenkraenzer <bero@redhat.com>
- FHSify
- handle RPM_OPT_FLAGS

* Sat May  6 2000 Bill Nottingham <notting@redhat.com>
- fix yacc for ia64

* Fri Feb  4 2000 Bernhard Rosenkraenzer <bero@redhat.com>
- rebuild to compress man pages
- fix up manpage symlink

* Wed Apr 07 1999 Preston Brown <pbrown@redhat.com>
- man page fixed.

* Sun Mar 21 1999 Cristian Gafton <gafton@redhat.com> 
- auto rebuild in the new build environment (release 10)

* Thu Dec 17 1998 Cristian Gafton <gafton@redhat.com>
- build for glibc 2.1

* Tue Aug 11 1998 Jeff Johnson <jbj@redhat.com>
- build root

* Tue May 05 1998 Prospector System <bugs@redhat.com>
- translations modified for de, fr, tr

* Thu Oct 23 1997 Donnie Barnes <djb@redhat.com>
- various spec file cleanups

* Mon Jun 02 1997 Erik Troan <ewt@redhat.com>
- built against glibc
