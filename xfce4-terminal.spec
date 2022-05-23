#
# This file is auto-generated. DO NOT EDIT
# Generated by: autospec.py
#
Name     : xfce4-terminal
Version  : 1.0.4
Release  : 29
URL      : https://archive.xfce.org/src/apps/xfce4-terminal/1.0/xfce4-terminal-1.0.4.tar.bz2
Source0  : https://archive.xfce.org/src/apps/xfce4-terminal/1.0/xfce4-terminal-1.0.4.tar.bz2
Summary  : No detailed summary available
Group    : Development/Tools
License  : GPL-2.0
Requires: xfce4-terminal-bin = %{version}-%{release}
Requires: xfce4-terminal-data = %{version}-%{release}
Requires: xfce4-terminal-license = %{version}-%{release}
Requires: xfce4-terminal-locales = %{version}-%{release}
Requires: xfce4-terminal-man = %{version}-%{release}
BuildRequires : docbook-xml
BuildRequires : gtk-doc
BuildRequires : gtk-doc-dev
BuildRequires : intltool
BuildRequires : libxslt-bin
BuildRequires : pcre2-dev
BuildRequires : pkgconfig(gio-2.0)
BuildRequires : pkgconfig(gtk+-3.0)
BuildRequires : pkgconfig(libxfce4kbd-private-3)
BuildRequires : pkgconfig(libxfce4ui-2)
BuildRequires : pkgconfig(libxfconf-0)
BuildRequires : pkgconfig(vte-2.91)
BuildRequires : vte-dev

%description
[![License](https://img.shields.io/badge/License-GPL%20v2-blue.svg)](https://gitlab.xfce.org/apps/xfce4-terminal/-/blob/master/COPYING)

%package bin
Summary: bin components for the xfce4-terminal package.
Group: Binaries
Requires: xfce4-terminal-data = %{version}-%{release}
Requires: xfce4-terminal-license = %{version}-%{release}

%description bin
bin components for the xfce4-terminal package.


%package data
Summary: data components for the xfce4-terminal package.
Group: Data

%description data
data components for the xfce4-terminal package.


%package license
Summary: license components for the xfce4-terminal package.
Group: Default

%description license
license components for the xfce4-terminal package.


%package locales
Summary: locales components for the xfce4-terminal package.
Group: Default

%description locales
locales components for the xfce4-terminal package.


%package man
Summary: man components for the xfce4-terminal package.
Group: Default

%description man
man components for the xfce4-terminal package.


%prep
%setup -q -n xfce4-terminal-1.0.4
cd %{_builddir}/xfce4-terminal-1.0.4

%build
export http_proxy=http://127.0.0.1:9/
export https_proxy=http://127.0.0.1:9/
export no_proxy=localhost,127.0.0.1,0.0.0.0
export LANG=C.UTF-8
export SOURCE_DATE_EPOCH=1653277508
export GCC_IGNORE_WERROR=1
export AR=gcc-ar
export RANLIB=gcc-ranlib
export NM=gcc-nm
export CFLAGS="$CFLAGS -O3 -ffat-lto-objects -flto=auto "
export FCFLAGS="$FFLAGS -O3 -ffat-lto-objects -flto=auto "
export FFLAGS="$FFLAGS -O3 -ffat-lto-objects -flto=auto "
export CXXFLAGS="$CXXFLAGS -O3 -ffat-lto-objects -flto=auto "
%configure --disable-static
make  %{?_smp_mflags}

%check
export LANG=C.UTF-8
export http_proxy=http://127.0.0.1:9/
export https_proxy=http://127.0.0.1:9/
export no_proxy=localhost,127.0.0.1,0.0.0.0
make %{?_smp_mflags} check

%install
export SOURCE_DATE_EPOCH=1653277508
rm -rf %{buildroot}
mkdir -p %{buildroot}/usr/share/package-licenses/xfce4-terminal
cp %{_builddir}/xfce4-terminal-1.0.4/COPYING %{buildroot}/usr/share/package-licenses/xfce4-terminal/4cc77b90af91e615a64ae04893fdffa7939db84c
%make_install
%find_lang xfce4-terminal

%files
%defattr(-,root,root,-)

%files bin
%defattr(-,root,root,-)
/usr/bin/xfce4-terminal

%files data
%defattr(-,root,root,-)
/usr/share/applications/xfce4-terminal-settings.desktop
/usr/share/applications/xfce4-terminal.desktop
/usr/share/gnome-control-center/default-apps/xfce4-terminal-default-apps.xml
/usr/share/icons/hicolor/128x128/apps/org.xfce.terminal-settings.png
/usr/share/icons/hicolor/128x128/apps/org.xfce.terminal.png
/usr/share/icons/hicolor/16x16/apps/org.xfce.terminal-settings.png
/usr/share/icons/hicolor/16x16/apps/org.xfce.terminal.png
/usr/share/icons/hicolor/24x24/apps/org.xfce.terminal-settings.png
/usr/share/icons/hicolor/24x24/apps/org.xfce.terminal.png
/usr/share/icons/hicolor/32x32/apps/org.xfce.terminal-settings.png
/usr/share/icons/hicolor/32x32/apps/org.xfce.terminal.png
/usr/share/icons/hicolor/48x48/apps/org.xfce.terminal-settings.png
/usr/share/icons/hicolor/48x48/apps/org.xfce.terminal.png
/usr/share/icons/hicolor/scalable/apps/org.xfce.terminal-settings.svg
/usr/share/icons/hicolor/scalable/apps/org.xfce.terminal.svg
/usr/share/xfce4/terminal/colorschemes/black-on-white.theme
/usr/share/xfce4/terminal/colorschemes/dark-pastels.theme
/usr/share/xfce4/terminal/colorschemes/green-on-black.theme
/usr/share/xfce4/terminal/colorschemes/solarized-dark.theme
/usr/share/xfce4/terminal/colorschemes/solarized-light.theme
/usr/share/xfce4/terminal/colorschemes/tango.theme
/usr/share/xfce4/terminal/colorschemes/white-on-black.theme
/usr/share/xfce4/terminal/colorschemes/xterm.theme

%files license
%defattr(0644,root,root,0755)
/usr/share/package-licenses/xfce4-terminal/4cc77b90af91e615a64ae04893fdffa7939db84c

%files man
%defattr(0644,root,root,0755)
/usr/share/man/man1/xfce4-terminal.1

%files locales -f xfce4-terminal.lang
%defattr(-,root,root,-)

