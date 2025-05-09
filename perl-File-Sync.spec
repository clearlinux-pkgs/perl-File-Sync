#
# This file is auto-generated. DO NOT EDIT
# Generated by: autospec.py
# Using build pattern: cpan
# autospec version: v21
# autospec commit: 94c6be0
#
Name     : perl-File-Sync
Version  : 0.11
Release  : 31
URL      : https://cpan.metacpan.org/authors/id/B/BR/BRIANSKI/File-Sync-0.11.tar.gz
Source0  : https://cpan.metacpan.org/authors/id/B/BR/BRIANSKI/File-Sync-0.11.tar.gz
Source1  : http://http.debian.net/debian/pool/main/libf/libfile-sync-perl/libfile-sync-perl_0.11-2.debian.tar.xz
Summary  : ~
Group    : Development/Tools
License  : Artistic-1.0 GPL-1.0
Requires: perl-File-Sync-license = %{version}-%{release}
Requires: perl-File-Sync-perl = %{version}-%{release}
BuildRequires : buildreq-cpan
# Suppress stripping binaries
%define __strip /bin/true
%define debug_package %{nil}

%description
This is version 0.07 of the Perl 5 File::Sync module.
It provides Perl interfaces to the Unix sync(2) and POSIX.1b fsync(2)
system calls. The fsync() call is needed for putting messages into
qmail maildirs, and sync() is included for completeness.

%package dev
Summary: dev components for the perl-File-Sync package.
Group: Development
Provides: perl-File-Sync-devel = %{version}-%{release}
Requires: perl-File-Sync = %{version}-%{release}

%description dev
dev components for the perl-File-Sync package.


%package license
Summary: license components for the perl-File-Sync package.
Group: Default

%description license
license components for the perl-File-Sync package.


%package perl
Summary: perl components for the perl-File-Sync package.
Group: Default
Requires: perl-File-Sync = %{version}-%{release}

%description perl
perl components for the perl-File-Sync package.


%prep
%setup -q -n File-Sync-0.11
cd %{_builddir}
tar xf %{_sourcedir}/libfile-sync-perl_0.11-2.debian.tar.xz
cd %{_builddir}/File-Sync-0.11
mkdir -p deblicense/
cp -r %{_builddir}/debian/* %{_builddir}/File-Sync-0.11/deblicense/

%build
export http_proxy=http://127.0.0.1:9/
export https_proxy=http://127.0.0.1:9/
export no_proxy=localhost,127.0.0.1,0.0.0.0
export LANG=C.UTF-8
if test -f Makefile.PL; then
%{__perl} -I. Makefile.PL
make  %{?_smp_mflags}
else
%{__perl} Build.PL
./Build
fi

%check
export LANG=C.UTF-8
export http_proxy=http://127.0.0.1:9/
export https_proxy=http://127.0.0.1:9/
export no_proxy=localhost,127.0.0.1,0.0.0.0
make TEST_VERBOSE=1 test

%install
rm -rf %{buildroot}
mkdir -p %{buildroot}/usr/share/package-licenses/perl-File-Sync
cp %{_builddir}/debian/copyright %{buildroot}/usr/share/package-licenses/perl-File-Sync/f23efe57ff9597e10055a4f0815c42cef121bedc || :
if test -f Makefile.PL; then
make pure_install PERL_INSTALL_ROOT=%{buildroot} INSTALLDIRS=vendor
else
./Build install --installdirs=vendor --destdir=%{buildroot}
fi
find %{buildroot} -type f -name .packlist -exec rm -f {} ';'
find %{buildroot} -depth -type d -exec rmdir {} 2>/dev/null ';'
find %{buildroot} -type f -name '*.bs' -empty -exec rm -f {} ';'
%{_fixperms} %{buildroot}/*

%files
%defattr(-,root,root,-)

%files dev
%defattr(-,root,root,-)
/usr/share/man/man3/File::Sync.3

%files license
%defattr(0644,root,root,0755)
/usr/share/package-licenses/perl-File-Sync/f23efe57ff9597e10055a4f0815c42cef121bedc

%files perl
%defattr(-,root,root,-)
/usr/lib/perl5/*
