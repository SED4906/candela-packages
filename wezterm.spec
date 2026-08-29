Name: wezterm
Version: 20260828_101755_27d55bef
Release: 1%{?dist}
Packager: Wez Furlong <wez@wezfurlong.org>
License: MIT
URL: https://wezterm.org/
Summary: Wez's Terminal Emulator.

Requires: wezterm-common, wezterm-gui, wezterm-mux-server

%global debug_package %{nil}

%description
wezterm is a terminal emulator with support for modern features
such as fonts with ligatures, hyperlinks, tabs and multiple
windows.

# Subpackage: wezterm-common
%package -n wezterm-common
Summary: Wez's Terminal Emulator - Common CLI components
Requires: openssl
%description -n wezterm-common
wezterm-common provides the base CLI launcher and utilities shared by
all wezterm components.

# Subpackage: wezterm-gui
%package -n wezterm-gui
Summary: Wez's Terminal Emulator - GUI and multiplexer
Requires: wezterm-common
%if 0%{?suse_version}
Requires: dbus-1, fontconfig, libxcb1, libxkbcommon0, libxkbcommon-x11-0, libwayland-client0, libwayland-egl1, libwayland-cursor0, Mesa-libEGL1, libxcb-keysyms1, libxcb-ewmh2, libxcb-icccm4
%else
Requires: dbus, fontconfig, libxcb, libxkbcommon, libxkbcommon-x11, libwayland-client, libwayland-egl, libwayland-cursor, mesa-libEGL, xcb-util-keysyms, xcb-util-wm
%endif
%description -n wezterm-gui
wezterm-gui is a GPU-accelerated cross-platform terminal emulator with
support for modern features such as fonts with ligatures, hyperlinks,
tabs and multiple windows.

# Subpackage: wezterm-mux-server
%package -n wezterm-mux-server
Summary: Wez's Terminal Emulator - Multiplexer server (headless)
Requires: openssl
%description -n wezterm-mux-server
wezterm-mux-server is a headless terminal multiplexer that can be used
as a session manager for terminal sessions, without requiring X11,
Wayland, or other GUI libraries.

%build
echo build

%install
set -x
mkdir -p %{buildroot}/usr/bin %{buildroot}/etc/profile.d %{buildroot}/usr/share/icons/hicolor/128x128/apps %{buildroot}/usr/share/applications %{buildroot}/usr/share/metainfo %{buildroot}/usr/share/nautilus-python/extensions
install -Dm755 assets/open-wezterm-here -t %{buildroot}/usr/bin
install -Dsm755 target/release/wezterm -t %{buildroot}/usr/bin
install -Dsm755 target/release/wezterm-gui -t %{buildroot}/usr/bin
install -Dsm755 target/release/wezterm-mux-server -t %{buildroot}/usr/bin
install -Dsm755 target/release/strip-ansi-escapes -t %{buildroot}/usr/bin
install -Dm644 assets/shell-integration/* -t %{buildroot}/etc/profile.d
install -Dm644 assets/shell-completion/zsh %{buildroot}/usr/share/zsh/site-functions/_wezterm
install -Dm644 assets/shell-completion/bash %{buildroot}/etc/bash_completion.d/wezterm
install -Dm644 assets/icon/terminal.png %{buildroot}/usr/share/icons/hicolor/128x128/apps/org.wezfurlong.wezterm.png
install -Dm644 assets/wezterm.desktop %{buildroot}/usr/share/applications/org.wezfurlong.wezterm.desktop
install -Dm644 assets/wezterm.appdata.xml %{buildroot}/usr/share/metainfo/org.wezfurlong.wezterm.appdata.xml
install -Dm644 assets/wezterm-nautilus.py %{buildroot}/usr/share/nautilus-python/extensions/wezterm-nautilus.py

%files
# Main package (metapackage) has no files

%files -n wezterm-common
/usr/bin/wezterm
/usr/bin/strip-ansi-escapes
/usr/share/zsh/site-functions/_wezterm
/etc/bash_completion.d/wezterm
/etc/profile.d/*

%files -n wezterm-gui
/usr/bin/open-wezterm-here
/usr/bin/wezterm-gui
/usr/share/icons/hicolor/128x128/apps/org.wezfurlong.wezterm.png
/usr/share/applications/org.wezfurlong.wezterm.desktop
/usr/share/metainfo/org.wezfurlong.wezterm.appdata.xml
/usr/share/nautilus-python/extensions/wezterm-nautilus.py*

%files -n wezterm-mux-server
/usr/bin/wezterm-mux-server

%changelog
* Mon Oct 2 2023 Wez Furlong
- See git for full changelog
