%undefine _debugsource_packages
%define oname Kooha

Name:           kooha
Version:        2.3.1
Release:        1
Summary:        Elegantly record your screen

License:        GPLv3+
URL:            https://github.com/SeaDve/%{oname}
Source0:        https://github.com/SeaDve/Kooha/archive/v%{version}/%{name}-%{version}.tar.gz


BuildSystem:  meson
BuildRequires:  appstream
BuildRequires:  cargo
BuildRequires:  rust
BuildRequires:  x264
BuildRequires:  pkgconfig(gstreamer-1.0)
BuildRequires:  pkgconfig(gstreamer-plugins-base-1.0)
BuildRequires:  pkgconfig(glib-2.0)
BuildRequires:  pkgconfig(gtk4)
BuildRequires:  libadwaita-common
BuildRequires:	pkgconfig(libadwaita-1)
BuildRequires:  gettext

Requires: pipewire
Requires: gstreamer1.0-pipewire
Requires: xdg-desktop-portal
Requires: gstreamer1.0-audiosink
Requires: gstreamer1.0-audiosrc
Requires: gstreamer1.0-pulse

%description
Kooha is a simple screen recorder with a minimal interface.

%post
%{_bindir}/touch --no-create %{_datadir}/icons/hicolor &>/dev/null || :

%postun
if [ $1 -eq 0 ]
then
    %{_bindir}/touch --no-create %{_datadir}/icons/hicolor &>/dev/null
    %{_bindir}/gtk-update-icon-cache %{_datadir}/icons/hicolor &>/dev/null || :
    %{_bindir}/glib-compile-schemas %{_datadir}/glib-2.0/schemas &> /dev/null || :
fi

%posttrans
%{_bindir}/glib-compile-schemas %{_datadir}/glib-2.0/schemas &> /dev/null || :
%{_bindir}/gtk-update-icon-cache %{_datadir}/icons/hicolor &>/dev/null || :

%files 
%{_bindir}/kooha
%{_datadir}/kooha/
%{_datadir}/locale/*/LC_MESSAGES/%{name}.mo
%{_datadir}/glib-2.0/schemas/*
%{_datadir}/applications/io.github.seadve.Kooha.desktop
%{_datadir}/icons/hicolor/*/apps/io.github.seadve.*
%{_datadir}/metainfo/*.xml
%{_datadir}/dbus-1/services/*.service
