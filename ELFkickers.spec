Summary:	Tools to manipulate ELF files
Summary(pl):	Narzêdzia do obróbki plików ELF
Name:		ELFkickers
Version:	2.0
Release:	2
License:	GPL
Group:		Development/Tools
Source0:	ftp://ftp.muppetlabs.com/pub/software/%{name}-%{version}.tar.gz
URL:		http://www.muppetlabs.com/~breadbox/software/elfkickers.html
##BuildArch:	noarch
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%description
Collection of programs to manipulate ELF files: sstrip, rebind, elfls,
elftoc, ebfc.

%description -l pl
Zestaw programów do obróbki plików ELF: sstrip, rebind, elfls, elftoc,
ebfc.

%prep
%setup -q -n ELFkickers

%build
%{__make} CFLAGS="%{rpmcflags}" -C ebfc
%{__make} CFLAGS="%{rpmcflags}" -C sstrip
%{__make} CFLAGS="%{rpmcflags}" -C elfls
%{__make} CFLAGS="%{rpmcflags}" -C elftoc
%{__make} CFLAGS="%{rpmcflags}" -C rebind

%install
rm -rf $RPM_BUILD_ROOT
install -d $RPM_BUILD_ROOT{%{_bindir},%{_mandir}/man1}
install ebfc/ebfc sstrip/sstrip elfls/elfls elftoc/elftoc rebind/rebind $RPM_BUILD_ROOT%{_bindir}
install */*.1 $RPM_BUILD_ROOT%{_mandir}/man1

mv -f ebfc/README README.ebfc
mv -f elfls/README README.elfls
mv -f elftoc/README README.elftoc
mv -f rebind/README README.rebind
mv -f sstrip/README README.sstrip
gzip -9nf README* Changelog ebfc/elfparts.txt tiny/README

%clean
rm -rf $RPM_BUILD_ROOT

%files
%defattr(644,root,root,755)
%doc README* Changelog* tiny ebfc/bf ebfc/elfparts.txt*
%attr(755,root,root) %{_bindir}/*
%{_mandir}/man1/*
