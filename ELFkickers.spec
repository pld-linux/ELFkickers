Summary:	Tools to manipulate ELF files
Summary(pl.UTF-8):	Narzędzia do obróbki plików ELF
Name:		ELFkickers
Version:	2.0a
Release:	2
License:	GPL
Group:		Development/Tools
Source0:	ftp://ftp.muppetlabs.com/pub/software/%{name}-%{version}.tar.gz
# Source0-md5:	3bf4d8d285591a5b7f31170f9b87aba0
URL:		http://www.muppetlabs.com/~breadbox/software/elfkickers.html
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%description
Collection of programs to manipulate ELF files: sstrip, rebind, elfls,
elftoc, ebfc.

%description -l pl.UTF-8
Zestaw programów do obróbki plików ELF: sstrip, rebind, elfls, elftoc,
ebfc.

%prep
%setup -q -n ELFkickers

mv -f ebfc/README README.ebfc
mv -f elfls/README README.elfls
mv -f elftoc/README README.elftoc
mv -f rebind/README README.rebind
mv -f sstrip/README README.sstrip

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

%clean
rm -rf $RPM_BUILD_ROOT

%files
%defattr(644,root,root,755)
%doc README* Changelog tiny ebfc/bf ebfc/elfparts.txt
%attr(755,root,root) %{_bindir}/*
%{_mandir}/man1/*
