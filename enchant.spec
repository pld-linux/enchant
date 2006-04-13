Summary:	libenchant - generic spell checking library
Summary(pl):	libenchant - ogólna biblioteka sprawdzania pisowni
Name:		enchant
Version:	1.2.5
Release:	1
License:	LGPL
Group:		Libraries
Source0:	http://www.abisource.com/downloads/enchant/1.2.5/%{name}-%{version}.tar.gz
# Source0-md5:	e64ec808ed2cb687c242ebb835faeb61
URL:		http://www.abisource.com/enchant/
BuildRequires:	aspell-devel >= 2:0.50.0
BuildRequires:	autoconf
BuildRequires:	automake
BuildRequires:	glib2-devel >= 2.0
BuildRequires:	hspell-devel
BuildRequires:	libtool
BuildRequires:	pkgconfig
BuildRequires:	uspell-devel >= 1.1.0
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%description
This project aims to provide an efficient, extensible abstraction for
dealing with different spell checking libraries. Enchant is meant to
provide a generic interface into various existing spell checking
libraries. These include, but are not limited to: Aspell/Pspell,
Ispell, Hspell, Uspell.

Enchant is also meant to be used in a cross-platform environment. Part
of this means that Enchant wants to limit its number of external
dependencies to 0, or as close is as humanly possible. Also, any
enchant consumer (i.e. a Word Processor) should not need to know about
what backend providers Enchant knows about. In fact, Enchant shouldn't
even need to know this information itself. To accomplish this, all of
Enchant's providers are dynamically loaded modules.

Enchant is also meant to be used in a multi-user environment, such as
Unix. It is preferable to have both a $USER and a $GLOBAL location for
both provider modules and for dictionaries themselves, when possible.
Enchant's module location algorithm takes this into account, and gives
preference to the $USER resources, when found.

%description -l pl
Celem projektu jest dostarczenie wydajnej i rozszerzalnej abstrakcji
do obs³ugi ró¿nych bibliotek kontroli pisowni. Enchant ma dostarczaæ
ogólny interfejs do ró¿nych istniej±cych bibliotek. Obejmuj± one (ale
nie s± ograniczone do): Aspella/Pspella, Ispella, Hspella, Uspella.

Enchant ma byæ tak¿e u¿ywany w ¶rodowisku wieloplatformowym. Oznacza
to miêdzy innymi, ¿e Enchant ma mieæ ograniczon± liczbê zewnêtrznych
zale¿no¶ci do zera lub najbli¿ej jak to mo¿liwe. Tak¿e dowolny klient
enchanta (czyli procesor tekstu) nie powinien potrzebowaæ wiedzy,
jakie backendy s± dostêpne dla Enchanta. W rzeczywisto¶ci nawet
Enchant nie powinien potrzebowaæ takiej informacji. Aby to osi±gn±æ,
wszystkie backendy Enchanta s± dynamicznie ³adowanymi modu³ami.

Enchant ma byæ tak¿e u¿ywany w ¶rodowisku wielou¿ytkownikowym, takim
jak Unix. Preferuje siê, ¿eby istnia³y zarówno specyficzne dla
u¿ytkownika jak i globalne lokalizacje zarówno dla modu³ów jak i
samych s³owników, je¶li to mo¿liwe. Algorytm poszukiwania modu³ów
Enchanta bierze to pod uwagê i preferuje zasoby u¿ytkownika, je¶li
takie znajdzie.

%package devel
Summary:	Header files for enchant library
Summary(pl):	Pliki nag³ówkowe biblioteki enchant
Group:		Development/Libraries
Requires:	%{name} = %{version}-%{release}
Requires:	glib2-devel >= 2.0

%description devel
Header files for enchant library.

%description devel -l pl
Pliki nag³ówkowe biblioteki enchant.

%package static
Summary:	Static enchant library
Summary(pl):	Statyczna biblioteka enchant
Group:		Development/Libraries
Requires:	%{name}-devel = %{version}-%{release}

%description static
Static enchant library.

%description static -l pl
Statyczna biblioteka enchant.

%package aspell
Summary:	aspell provider module for Enchant
Summary(pl):	Modu³ obs³uguj±cy aspella dla Enchanta
Group:		Libraries
Requires:	%{name} = %{version}-%{release}
Requires:	aspell >= 2:0.50.0

%description aspell
aspell provider module for Enchant.

%description aspell -l pl
Modu³ obs³uguj±cy aspella dla Enchanta.

%package hspell
Summary:	hspell provider module for Enchant
Summary(pl):	Modu³ obs³uguj±cy hspella dla Enchanta
Group:		Libraries
Requires:	%{name} = %{version}-%{release}

%description hspell
hspell provider module for Enchant.

%description hspell -l pl
Modu³ obs³uguj±cy hspella dla Enchanta.

%package ispell
Summary:	ispell provider module for Enchant
Summary(pl):	Modu³ obs³uguj±cy ispella dla Enchanta
Group:		Libraries
Requires:	%{name} = %{version}-%{release}

%description ispell
ispell provider module for Enchant.

%description ispell -l pl
Modu³ obs³uguj±cy ispella dla Enchanta.

%package myspell
Summary:	myspell provider module for Enchant
Summary(pl):	Modu³ obs³uguj±cy myspella dla Enchanta
Group:		Libraries
Requires:	%{name} = %{version}-%{release}

%description myspell
myspell provider module for Enchant.

%description myspell -l pl
Modu³ obs³uguj±cy myspella dla Enchanta.

%package uspell
Summary:	uspell provider module for Enchant
Summary(pl):	Modu³ obs³uguj±cy uspella dla Enchanta
Group:		Libraries
Requires:	%{name} = %{version}-%{release}

%description uspell
uspell provider module for Enchant.

%description uspell -l pl
Modu³ obs³uguj±cy uspella dla Enchanta.

%prep
%setup -q

%build
%{__libtoolize}
%{__aclocal} -I ac-helpers
%{__autoconf}
%{__automake}
%configure \
	--disable-binreloc \
	--with-ispell-dir=/usr/lib/ispell \
	--with-uspell-dir=/usr/share/uspell
# --with-myspell-dir=/some/where

%{__make}

%install
rm -rf $RPM_BUILD_ROOT

%{__make} install \
	DESTDIR=$RPM_BUILD_ROOT

# useless - modules loaded through libgmodule
rm -f $RPM_BUILD_ROOT%{_libdir}/enchant/*.{la,a}

%clean
rm -rf $RPM_BUILD_ROOT

%post
/sbin/ldconfig
%banner %{name} -e << EOF
you should install one of the backends for enchant:
- enchant-aspell
- enchant-hspell
- enchant-ispell
- enchant-myspell
- enchant-uspell
and appropriate dictionaries
EOF
%postun	-p /sbin/ldconfig

%files
%defattr(644,root,root,755)
%doc AUTHORS MAINTAINERS NEWS README TODO
%attr(755,root,root) %{_bindir}/enchant
%attr(755,root,root) %{_bindir}/enchant-lsmod
%attr(755,root,root) %{_libdir}/lib*.so.*.*.*
%dir %{_libdir}/enchant
%{_datadir}/enchant
%{_mandir}/man1/enchant.1*

%files devel
%defattr(644,root,root,755)
%attr(755,root,root) %{_libdir}/lib*.so
%{_libdir}/lib*.la
%{_includedir}/enchant
%{_pkgconfigdir}/*.pc

%files static
%defattr(644,root,root,755)
%{_libdir}/lib*.a

%files aspell
%defattr(644,root,root,755)
%attr(755,root,root) %{_libdir}/enchant/libenchant_aspell.so*

%files hspell
%defattr(644,root,root,755)
%attr(755,root,root) %{_libdir}/enchant/libenchant_hspell.so*

%files ispell
%defattr(644,root,root,755)
%attr(755,root,root) %{_libdir}/enchant/libenchant_ispell.so*

%files myspell
%defattr(644,root,root,755)
%attr(755,root,root) %{_libdir}/enchant/libenchant_myspell.so*

%files uspell
%defattr(644,root,root,755)
%attr(755,root,root) %{_libdir}/enchant/libenchant_uspell.so*
