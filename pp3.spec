Summary:	Celestial charts generation
Name:		pp3
Version:	1.3.3
Release:	0.1
License:	See %{_docdir}/%{name}-%{version}/COPYING for details
Group:		Applications/Science
Patch0:		%{name}-makefile.patch
Requires:	tetex-dvips
Requires:	tetex-fonts-jknappen
Requires:	tetex-format-latex
Requires:	tetex-latex-ams
Requires:	tetex-latex-psnfss
Requires:	tetex-metafont
Requires:	tetex-tex-pstricks
Source0:	http://dl.sourceforge.net/pp3/%{name}-%{version}.tar.bz2
# Source0-md5:	dbea2818657c3a26587d72ff5ddb9545
URL:		http://pp3.sourceforge.net/
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%description
Celestial charts generation

%prep
%setup -q -n %{name}-%{version}
%patch0 -p0

%build
%{__make}

%install
rm -rf $RPM_BUILD_ROOT
install -d $RPM_BUILD_ROOT%{_bindir}
install -d $RPM_BUILD_ROOT%{_datadir}/pp3

install pp3 $RPM_BUILD_ROOT%{_bindir}
install *.dat $RPM_BUILD_ROOT%{_datadir}/pp3

%clean
rm -rf $RPM_BUILD_ROOT

%files
%defattr(644,root,root,755)
%doc COPYING README WHATSNEW examples
%attr(755,root,root) %{_bindir}/*
%dir %{_datadir}/pp3
%{_datadir}/pp3/*.dat
