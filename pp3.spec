Summary:	Program for drawing celestial maps
Summary(pl):	Program do rysowania map nieba
Name:		pp3
Version:	1.3.3
Release:	1
License:	distributable (see COPYING for details)
Group:		Applications/Science
Source0:	http://dl.sourceforge.net/pp3/%{name}-%{version}.tar.bz2
# Source0-md5:	dbea2818657c3a26587d72ff5ddb9545
Source1:	http://dl.sourceforge.net/pp3/%{name}.pdf
# Source1-md5:	2656f4e125afb487bf13af429751458e
Patch0:		%{name}-makefile.patch
URL:		http://pp3.sourceforge.net/
Requires:	tetex-dvips
Requires:	tetex-fonts-jknappen
Requires:	tetex-format-latex
Requires:	tetex-latex-ams
Requires:	tetex-latex-psnfss
Requires:	tetex-metafont
Requires:	tetex-tex-pstricks
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%description
There are many programs that can create stellar maps. But none of them
reaches PP3's typographic and graphical quality. In contrast to other
programs PP3 produces vector images (e.g. PDFs) rather than mere
bitmaps. Therefore it is perfectly suited for creating illustrations
for books or other print media. But even converted to bitmaps for web
pages, it exceeds usual quality.

%description -l pl
Istnieje wiele program�w, kt�re potrafi� tworzy� mapy nieba. Ale �aden
z nich nie dor�wnuje PP3 jako�ci� generowanych obraz�w. W
przeciwie�stwie do innych tego typu program�w PP3 tworzy zamiast
zwyk�ych bitmap obrazy wektorowe (na przyk�ad w formacie PDF). Dlatego
�wietnie nadaje si� do tworzenia ilustracji do ksi��ek oraz innych
publikacji przeznaczonych do druku. Jednak�e nawet po konwersji do
bitmapy do wykorzystania przyk�adowo na stronie WWW uzyskuje
zadowalaj�c� jako��.

%package doc
Summary:        PP3 documentation in PDF and examples
Summary(pl):    Dokumentacja PP3 w formacie PDF i przyk�ady
Group:          Applications/Science

%description doc
There are many programs that can create stellar maps. But none of them
reaches PP3's typographic and graphical quality. In contrast to other
programs PP3 produces vector images (e.g. PDFs) rather than mere
bitmaps. Therefore it is perfectly suited for creating illustrations
for books or other print media. But even converted to bitmaps for web
pages, it exceeds usual quality.

This package contains PP3 documentation in PDF and examples.

%description doc -l pl
Istnieje wiele program�w, kt�re potrafi� tworzy� mapy nieba. Ale �aden
z nich nie dor�wnuje PP3 jako�ci� generowanych obraz�w. W
przeciwie�stwie do innych tego typu program�w PP3 tworzy zamiast
zwyk�ych bitmap obrazy wektorowe (na przyk�ad w formacie PDF). Dlatego
�wietnie nadaje si� do tworzenia ilustracji do ksi��ek oraz innych
publikacji przeznaczonych do druku. Jednak�e nawet po konwersji do
bitmapy do wykorzystania przyk�adowo na stronie WWW uzyskuje
zadowalaj�c� jako��.

Pakiet ten zawiera dokumentacj� PP3 w formacie PDF oraz przyk�ady.

%prep
%setup -q
%patch0 -p0

%build
%{__make}

%install
rm -rf $RPM_BUILD_ROOT
install -d $RPM_BUILD_ROOT%{_bindir}
install -d $RPM_BUILD_ROOT%{_datadir}/pp3

install pp3 $RPM_BUILD_ROOT%{_bindir}
install *.dat $RPM_BUILD_ROOT%{_datadir}/pp3

cp %{SOURCE1} .

%clean
rm -rf $RPM_BUILD_ROOT

%files
%defattr(644,root,root,755)
%doc COPYING README WHATSNEW
%attr(755,root,root) %{_bindir}/*
%dir %{_datadir}/pp3
%{_datadir}/pp3/*.dat

%files doc
%defattr(644,root,root,755)
%doc pp3.pdf examples
