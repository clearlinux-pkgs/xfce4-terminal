#
# This file is auto-generated. DO NOT EDIT
# Generated by: autospec.py
#
Name     : xfce4-terminal
Version  : 0.8.9.1
Release  : 22
URL      : http://archive.xfce.org/src/apps/xfce4-terminal/0.8/xfce4-terminal-0.8.9.1.tar.bz2
Source0  : http://archive.xfce.org/src/apps/xfce4-terminal/0.8/xfce4-terminal-0.8.9.1.tar.bz2
Summary  : No detailed summary available
Group    : Development/Tools
License  : GPL-2.0
Requires: xfce4-terminal-bin = %{version}-%{release}
Requires: xfce4-terminal-data = %{version}-%{release}
Requires: xfce4-terminal-license = %{version}-%{release}
Requires: xfce4-terminal-locales = %{version}-%{release}
Requires: xfce4-terminal-man = %{version}-%{release}
BuildRequires : gtk+-dev
BuildRequires : intltool
BuildRequires : libxml2-dev
BuildRequires : pcre2-dev
BuildRequires : pkgconfig(gio-2.0)
BuildRequires : pkgconfig(gtk+-3.0)
BuildRequires : pkgconfig(libxfce4ui-1)
BuildRequires : pkgconfig(libxfce4ui-2)
BuildRequires : pkgconfig(libxfconf-0)
BuildRequires : pkgconfig(vte-2.91)
BuildRequires : vte-dev

%description
What is it?
===========
Xfce Terminal is a lightweight and easy to use terminal emulator application
with many advanced features including drop down, tabs, unlimited scrolling,
full colors, fonts, transparent backgrounds, and more.

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
%setup -q -n xfce4-terminal-0.8.9.1
cd %{_builddir}/xfce4-terminal-0.8.9.1

%build
export http_proxy=http://127.0.0.1:9/
export https_proxy=http://127.0.0.1:9/
export no_proxy=localhost,127.0.0.1,0.0.0.0
export LANG=C.UTF-8
export SOURCE_DATE_EPOCH=1579908419
export GCC_IGNORE_WERROR=1
export AR=gcc-ar
export RANLIB=gcc-ranlib
export NM=gcc-nm
export CFLAGS="$CFLAGS -O3 -ffat-lto-objects -flto=4 "
export FCFLAGS="$CFLAGS -O3 -ffat-lto-objects -flto=4 "
export FFLAGS="$CFLAGS -O3 -ffat-lto-objects -flto=4 "
export CXXFLAGS="$CXXFLAGS -O3 -ffat-lto-objects -flto=4 "
%configure --disable-static
make  %{?_smp_mflags}

%check
export LANG=C.UTF-8
export http_proxy=http://127.0.0.1:9/
export https_proxy=http://127.0.0.1:9/
export no_proxy=localhost,127.0.0.1,0.0.0.0
make VERBOSE=1 V=1 %{?_smp_mflags} check

%install
export SOURCE_DATE_EPOCH=1579908419
rm -rf %{buildroot}
mkdir -p %{buildroot}/usr/share/package-licenses/xfce4-terminal
cp %{_builddir}/xfce4-terminal-0.8.9.1/COPYING %{buildroot}/usr/share/package-licenses/xfce4-terminal/4cc77b90af91e615a64ae04893fdffa7939db84c
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
/usr/share/xfce4/terminal/colorschemes/black-on-white.theme
/usr/share/xfce4/terminal/colorschemes/dark-pastels.theme
/usr/share/xfce4/terminal/colorschemes/green-on-black.theme
/usr/share/xfce4/terminal/colorschemes/solarized-dark.theme
/usr/share/xfce4/terminal/colorschemes/solarized-light.theme
/usr/share/xfce4/terminal/colorschemes/tango.theme
/usr/share/xfce4/terminal/colorschemes/white-on-black.theme
/usr/share/xfce4/terminal/colorschemes/xterm.theme
/usr/share/xfce4/terminal/terminal-preferences.ui

%files license
%defattr(0644,root,root,0755)
/usr/share/package-licenses/xfce4-terminal/4cc77b90af91e615a64ae04893fdffa7939db84c

%files man
%defattr(0644,root,root,0755)
/usr/share/man/man1/xfce4-terminal.1

%files locales -f xfce4-terminal.lang
%defattr(-,root,root,-)

