#
# This file is auto-generated. DO NOT EDIT
# Generated by: autospec.py
#
Name     : perl-File-Sync
Version  : 0.11
Release  : 3
URL      : https://cpan.metacpan.org/authors/id/B/BR/BRIANSKI/File-Sync-0.11.tar.gz
Source0  : https://cpan.metacpan.org/authors/id/B/BR/BRIANSKI/File-Sync-0.11.tar.gz
Source1  : http://http.debian.net/debian/pool/main/libf/libfile-sync-perl/libfile-sync-perl_0.11-2.debian.tar.xz
Summary  : ~
Group    : Development/Tools
License  : Artistic-1.0 GPL-1.0
Requires: perl-File-Sync-lib = %{version}-%{release}
Requires: perl-File-Sync-license = %{version}-%{release}
BuildRequires : buildreq-cpan

%description
This is version 0.07 of the Perl 5 File::Sync module.
It provides Perl interfaces to the Unix sync(2) and POSIX.1b fsync(2)
system calls. The fsync() call is needed for putting messages into
qmail maildirs, and sync() is included for completeness.

%package dev
Summary: dev components for the perl-File-Sync package.
Group: Development
Requires: perl-File-Sync-lib = %{version}-%{release}
Provides: perl-File-Sync-devel = %{version}-%{release}

%description dev
dev components for the perl-File-Sync package.


%package lib
Summary: lib components for the perl-File-Sync package.
Group: Libraries
Requires: perl-File-Sync-license = %{version}-%{release}

%description lib
lib components for the perl-File-Sync package.


%package license
Summary: license components for the perl-File-Sync package.
Group: Default

%description license
license components for the perl-File-Sync package.


%prep
%setup -q -n File-Sync-0.11
cd ..
%setup -q -T -D -n File-Sync-0.11 -b 1
mkdir -p deblicense/
mv %{_topdir}/BUILD/debian/* %{_topdir}/BUILD/File-Sync-0.11/deblicense/

%build
export http_proxy=http://127.0.0.1:9/
export https_proxy=http://127.0.0.1:9/
export no_proxy=localhost,127.0.0.1,0.0.0.0
export LANG=C
if test -f Makefile.PL; then
%{__perl} Makefile.PL
make  %{?_smp_mflags}
else
%{__perl} Build.PL
./Build
fi

%check
export LANG=C
export http_proxy=http://127.0.0.1:9/
export https_proxy=http://127.0.0.1:9/
export no_proxy=localhost,127.0.0.1,0.0.0.0
make TEST_VERBOSE=1 test

%install
rm -rf %{buildroot}
mkdir -p %{buildroot}/usr/share/package-licenses/perl-File-Sync
cp deblicense/copyright %{buildroot}/usr/share/package-licenses/perl-File-Sync/deblicense_copyright
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
/usr/lib/perl5/vendor_perl/5.28.0/x86_64-linux-thread-multi/File/Sync.pm
/usr/lib/perl5/vendor_perl/5.28.0/x86_64-linux-thread-multi/auto/File/Sync/autosplit.ix

%files dev
%defattr(-,root,root,-)
/usr/share/man/man3/File::Sync.3

%files lib
%defattr(-,root,root,-)
/usr/lib/perl5/vendor_perl/5.28.0/x86_64-linux-thread-multi/auto/File/Sync/Sync.so

%files license
%defattr(0644,root,root,0755)
/usr/share/package-licenses/perl-File-Sync/deblicense_copyright
