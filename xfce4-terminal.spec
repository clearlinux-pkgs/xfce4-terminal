#
# This file is auto-generated. DO NOT EDIT
# Generated by: autospec.py
#
Name     : xfce4-terminal
Version  : 0.6.3
Release  : 5
URL      : http://archive.xfce.org/src/apps/xfce4-terminal/0.6/xfce4-terminal-0.6.3.tar.bz2
Source0  : http://archive.xfce.org/src/apps/xfce4-terminal/0.6/xfce4-terminal-0.6.3.tar.bz2
Summary  : No detailed summary available
Group    : Development/Tools
License  : GPL-2.0
Requires: xfce4-terminal-bin
Requires: xfce4-terminal-data
Requires: xfce4-terminal-locales
Requires: xfce4-terminal-doc
BuildRequires : gtk+-dev
BuildRequires : intltool
BuildRequires : libxml2-dev
BuildRequires : perl(XML::Parser)
BuildRequires : pkgconfig(ice)
BuildRequires : pkgconfig(libxfce4ui-1)
BuildRequires : pkgconfig(x11)
BuildRequires : vte-dev
Patch1: 0001-Set-Droid-Sans-Mono-for-Powerline-10-as-default-font.patch

%description
What is it?
===========
This is the Terminal emulator application. Terminal is a lightweight and
easy to use terminal emulator for the X windowing system, with some new
ideas and features that makes it unique among X terminal emulators.

%package bin
Summary: bin components for the xfce4-terminal package.
Group: Binaries
Requires: xfce4-terminal-data

%description bin
bin components for the xfce4-terminal package.


%package data
Summary: data components for the xfce4-terminal package.
Group: Data

%description data
data components for the xfce4-terminal package.


%package doc
Summary: doc components for the xfce4-terminal package.
Group: Documentation

%description doc
doc components for the xfce4-terminal package.


%package locales
Summary: locales components for the xfce4-terminal package.
Group: Default

%description locales
locales components for the xfce4-terminal package.


%prep
%setup -q -n xfce4-terminal-0.6.3
%patch1 -p1

%build
%configure --disable-static
make V=1  %{?_smp_mflags}

%check
export http_proxy=http://127.0.0.1:9/
export https_proxy=http://127.0.0.1:9/
export no_proxy=localhost
make VERBOSE=1 V=1 %{?_smp_mflags} check

%install
rm -rf %{buildroot}
%make_install
%find_lang xfce4-terminal

%files
%defattr(-,root,root,-)

%files bin
%defattr(-,root,root,-)
/usr/bin/xfce4-terminal

%files data
%defattr(-,root,root,-)
/usr/share/applications/xfce4-terminal.desktop
/usr/share/gnome-control-center/default-apps/xfce4-terminal-default-apps.xml
/usr/share/man/ar/man1/xfce4-terminal.1
/usr/share/man/ca/man1/xfce4-terminal.1
/usr/share/man/da/man1/xfce4-terminal.1
/usr/share/man/de/man1/xfce4-terminal.1
/usr/share/man/el/man1/xfce4-terminal.1
/usr/share/man/es/man1/xfce4-terminal.1
/usr/share/man/fr/man1/xfce4-terminal.1
/usr/share/man/gl/man1/xfce4-terminal.1
/usr/share/man/id/man1/xfce4-terminal.1
/usr/share/man/it/man1/xfce4-terminal.1
/usr/share/man/ja/man1/xfce4-terminal.1
/usr/share/man/ko/man1/xfce4-terminal.1
/usr/share/man/lt/man1/xfce4-terminal.1
/usr/share/man/pl/man1/xfce4-terminal.1
/usr/share/man/pt/man1/xfce4-terminal.1
/usr/share/man/pt_BR/man1/xfce4-terminal.1
/usr/share/man/ru/man1/xfce4-terminal.1
/usr/share/man/sr/man1/xfce4-terminal.1
/usr/share/man/sv/man1/xfce4-terminal.1
/usr/share/man/tr/man1/xfce4-terminal.1
/usr/share/man/ug/man1/xfce4-terminal.1
/usr/share/man/uk/man1/xfce4-terminal.1
/usr/share/man/zh_CN/man1/xfce4-terminal.1
/usr/share/xfce4/terminal/colorschemes/black-on-white.theme
/usr/share/xfce4/terminal/colorschemes/dark-pastels.theme
/usr/share/xfce4/terminal/colorschemes/green-on-black.theme
/usr/share/xfce4/terminal/colorschemes/solarized-dark.theme
/usr/share/xfce4/terminal/colorschemes/solarized-light.theme
/usr/share/xfce4/terminal/colorschemes/tango.theme
/usr/share/xfce4/terminal/colorschemes/white-on-black.theme
/usr/share/xfce4/terminal/colorschemes/xterm.theme
/usr/share/xfce4/terminal/terminal-preferences.ui

%files doc
%defattr(-,root,root,-)
%doc /usr/share/man/man1/*

%files locales -f xfce4-terminal.lang 
%defattr(-,root,root,-)

