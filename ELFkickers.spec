Summary:	Tools to manipulate elf files
Name:		ELFkickers
Version:	2.0
Release:	1
License:	GPL
Group:		Development/Tools
Group(de):	Entwicklung/Werkzeuge
Group(fr):	Development/Outils
Group(pl):	Programowanie/Narzêdzia
Source0:	ftp://ftp.muppetlabs.com/pub/software/%{name}-%{version}.tar.gz
URL:		http://www.muppetlabs.com/~breadbox/software/elfkickers.html
##BuildArch:	noarch
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%description

%prep
%setup -q -n ELFkickers

%build
%{__make} -C ebfc
%{__make} -C sstrip
%{__make} -C elfls
%{__make} -C elftoc
%{__make} -C rebind

%install
rm -rf $RPM_BUILD_ROOT
install -d $RPM_BUILD_ROOT%{_bindir}
install -d $RPM_BUILD_ROOT%{_mandir}/man1
install ebfc/ebfc sstrip/sstrip elfls/elfls elftoc/elftoc rebind/rebind $RPM_BUILD_ROOT%{_bindir}
install */*.1 $RPM_BUILD_ROOT%{_mandir}/man1


%clean
rm -rf $RPM_BUILD_ROOT

%files
%defattr(644,root,root,755)
%doc README tiny ebfc/bf
%attr(755,root,root) %{_bindir}/*
%{_mandir}/man1/*
