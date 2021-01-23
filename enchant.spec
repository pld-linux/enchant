#
# Conditional build:
%bcond_without	static_libs	# don't build static library
#
Summary:	libenchant - generic spell checking library
Summary(pl.UTF-8):	libenchant - ogólna biblioteka sprawdzania pisowni
Name:		enchant
# version 2.x packaged as enchant2
Version:	1.6.1
Release:	4
License:	LGPL v2
Group:		Libraries
# versions up to 1.6.0
#Source0:	http://www.abisource.com/downloads/enchant/%{version}/%{name}-%{version}.tar.gz
# 1.6.x > 1.6.0 (for 2.x see enchant2.spec)
#Source0Download: https://github.com/AbiWord/enchant/releases
Source0:	https://github.com/AbiWord/enchant/releases/download/enchant-1-6-1/%{name}-%{version}.tar.gz
# Source0-md5:	4110afe7d7010acbb5c69dd1214fa936
Patch0:		hunspell-1.4.patch
Patch1:		%{name}-sh.patch
URL:		https://www.abisource.com/projects/enchant/
BuildRequires:	aspell-devel >= 2:0.50.0
BuildRequires:	autoconf >= 2.50
BuildRequires:	automake
BuildRequires:	dbus-glib-devel >= 0.62
BuildRequires:	glib2-devel >= 1:2.12.0
BuildRequires:	hspell-devel >= 0.9-3
BuildRequires:	hunspell-devel
BuildRequires:	libtool >= 2:2
BuildRequires:	libvoikko-devel
BuildRequires:	pkgconfig
BuildRequires:	uspell-devel >= 1.1.0
Requires:	glib2 >= 1:2.12.0
Suggests:	%{name}-backend
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

%description -l pl.UTF-8
Celem projektu jest dostarczenie wydajnej i rozszerzalnej abstrakcji
do obsługi różnych bibliotek kontroli pisowni. Enchant ma dostarczać
ogólny interfejs do różnych istniejących bibliotek. Obejmują one (ale
nie są ograniczone do): Aspella/Pspella, Ispella, Hspella, Uspella.

Enchant ma być także używany w środowisku wieloplatformowym. Oznacza
to między innymi, że Enchant ma mieć ograniczoną liczbę zewnętrznych
zależności do zera lub najbliżej jak to możliwe. Także dowolny klient
enchanta (czyli procesor tekstu) nie powinien potrzebować wiedzy,
jakie backendy są dostępne dla Enchanta. W rzeczywistości nawet
Enchant nie powinien potrzebować takiej informacji. Aby to osiągnąć,
wszystkie backendy Enchanta są dynamicznie ładowanymi modułami.

Enchant ma być także używany w środowisku wieloużytkownikowym, takim
jak Unix. Preferuje się, żeby istniały zarówno specyficzne dla
użytkownika jak i globalne lokalizacje zarówno dla modułów jak i
samych słowników, jeśli to możliwe. Algorytm poszukiwania modułów
Enchanta bierze to pod uwagę i preferuje zasoby użytkownika, jeśli
takie znajdzie.

%package devel
Summary:	Header files for enchant library
Summary(pl.UTF-8):	Pliki nagłówkowe biblioteki enchant
Group:		Development/Libraries
Requires:	%{name} = %{version}-%{release}
Requires:	glib2-devel >= 1:2.12.0

%description devel
Header files for enchant library.

%description devel -l pl.UTF-8
Pliki nagłówkowe biblioteki enchant.

%package static
Summary:	Static enchant library
Summary(pl.UTF-8):	Statyczna biblioteka enchant
Group:		Development/Libraries
Requires:	%{name}-devel = %{version}-%{release}

%description static
Static enchant library.

%description static -l pl.UTF-8
Statyczna biblioteka enchant.

%package aspell
Summary:	aspell provider module for Enchant
Summary(pl.UTF-8):	Moduł obsługujący aspella dla Enchanta
Group:		Libraries
Requires:	%{name} = %{version}-%{release}
Requires:	aspell >= 2:0.50.0
Provides:	%{name}-backend

%description aspell
aspell provider module for Enchant.

%description aspell -l pl.UTF-8
Moduł obsługujący aspella dla Enchanta.

%package hspell
Summary:	hspell provider module for Enchant
Summary(pl.UTF-8):	Moduł obsługujący hspella dla Enchanta
Group:		Libraries
Requires:	%{name} = %{version}-%{release}
Provides:	%{name}-backend

%description hspell
hspell provider module for Enchant.

%description hspell -l pl.UTF-8
Moduł obsługujący hspella dla Enchanta.

%package ispell
Summary:	ispell provider module for Enchant
Summary(pl.UTF-8):	Moduł obsługujący ispella dla Enchanta
Group:		Libraries
Requires:	%{name} = %{version}-%{release}
Provides:	%{name}-backend

%description ispell
ispell provider module for Enchant.

%description ispell -l pl.UTF-8
Moduł obsługujący ispella dla Enchanta.

%package myspell
Summary:	myspell provider module for Enchant
Summary(pl.UTF-8):	Moduł obsługujący myspella dla Enchanta
Group:		Libraries
Requires:	%{name} = %{version}-%{release}
Provides:	%{name}-backend

%description myspell
myspell provider module for Enchant.

%description myspell -l pl.UTF-8
Moduł obsługujący myspella dla Enchanta.

%package uspell
Summary:	uspell provider module for Enchant
Summary(pl.UTF-8):	Moduł obsługujący uspella dla Enchanta
Group:		Libraries
Requires:	%{name} = %{version}-%{release}
Provides:	%{name}-backend

%description uspell
uspell provider module for Enchant.

%description uspell -l pl.UTF-8
Moduł obsługujący uspella dla Enchanta.

%package voikko
Summary:	Voikko provider module for Enchant
Summary(pl.UTF-8):	Moduł obsługujący backend voikko dla Enchanta
Group:		Libraries
Requires:	%{name} = %{version}-%{release}
Provides:	%{name}-backend

%description voikko
Voikko (Finnish) provider module for Enchant.

%description voikko -l pl.UTF-8
Moduł obsługujący backend voikko (fiński) dla Enchanta.

%package zemberek
Summary:	Zemberek provider module for Enchant
Summary(pl.UTF-8):	Moduł obsługujący backend zemberek dla Enchanta
Group:		Libraries
Requires:	%{name} = %{version}-%{release}
Requires:	dbus-glib >= 0.62
Provides:	%{name}-backend

%description zemberek
Zemberek (Turkish) provider module for Enchant.

%description zemberek -l pl.UTF-8
Moduł obsługujący backend zemberek (turecki) dla Enchanta.

%prep
%setup -q
%patch0 -p1
%patch1 -p1

%build
%{__libtoolize}
%{__aclocal} -I m4
%{__autoconf}
%{__automake}
export CFLAGS="%{rpmcflags} -fpermissive"
export CXXFLAGS="%{rpmcxxflags} -fpermissive"
%configure \
	--disable-binreloc \
	%{!?with_static_libs:--disable-static} \
	--enable-zemberek \
	--with-ispell-dir=/usr/%{_lib}/ispell \
	--with-myspell-dir=/usr/share/myspell \
	--with-uspell-dir=/usr/share/uspell

%{__make}

%install
rm -rf $RPM_BUILD_ROOT

%{__make} install \
	DESTDIR=$RPM_BUILD_ROOT

# useless - modules loaded through libgmodule
%{__rm} $RPM_BUILD_ROOT%{_libdir}/enchant/*.la
%{?with_static_libs:%{__rm} $RPM_BUILD_ROOT%{_libdir}/enchant/*.a}
# obsoleted by pkg-config
%{__rm} $RPM_BUILD_ROOT%{_libdir}/libenchant.la

%clean
rm -rf $RPM_BUILD_ROOT

%post	-p /sbin/ldconfig
%postun	-p /sbin/ldconfig

%files
%defattr(644,root,root,755)
%doc AUTHORS MAINTAINERS NEWS README
%attr(755,root,root) %{_bindir}/enchant
%attr(755,root,root) %{_bindir}/enchant-lsmod
%attr(755,root,root) %{_libdir}/libenchant.so.*.*.*
%attr(755,root,root) %ghost %{_libdir}/libenchant.so.1
%dir %{_libdir}/enchant
%{_datadir}/enchant
%{_mandir}/man1/enchant.1*

%files devel
%defattr(644,root,root,755)
%attr(755,root,root) %{_libdir}/libenchant.so
%{_includedir}/enchant
%{_pkgconfigdir}/enchant.pc

%if %{with static_libs}
%files static
%defattr(644,root,root,755)
%{_libdir}/libenchant.a
%endif

%files aspell
%defattr(644,root,root,755)
%attr(755,root,root) %{_libdir}/enchant/libenchant_aspell.so

%files hspell
%defattr(644,root,root,755)
%attr(755,root,root) %{_libdir}/enchant/libenchant_hspell.so

%files ispell
%defattr(644,root,root,755)
%attr(755,root,root) %{_libdir}/enchant/libenchant_ispell.so

%files myspell
%defattr(644,root,root,755)
%attr(755,root,root) %{_libdir}/enchant/libenchant_myspell.so

%files uspell
%defattr(644,root,root,755)
%attr(755,root,root) %{_libdir}/enchant/libenchant_uspell.so

%files voikko
%defattr(644,root,root,755)
%attr(755,root,root) %{_libdir}/enchant/libenchant_voikko.so

%files zemberek
%defattr(644,root,root,755)
%attr(755,root,root) %{_libdir}/enchant/libenchant_zemberek.so
