%global debug_package %{nil}
Name:           gram
Version:        1.2.1
Release:        1%{?dist}
Summary:        The Gram Code Editor

License:        GPLv3
URL:            https://gram.liten.app/
Source0:        https://codeberg.org/GramEditor/gram/releases/download/%{version}/%{name}-linux-x86_64-%{version}.tar.gz

Requires:       zlib-ng-compat libXau libXdmcp libxcb libxkbcommon

%description
Gram is a powerful and modern source code editor. It features solid performance and is highly configurable, yet comes with batteries included out of the box. Gram supports many popular programming languages and file formats, and can use Zed extensions to support additional languages. Other features include built-in documentation, debugger support via the DAP protocol, source control using git and more. Gram started as a fork of the Zed editor.

%prep
%setup -n gram.app

%build

%install
mkdir -p %{buildroot}/usr/{bin,libexec,share/{applications,icons/hicolor/{scalable,symbolic}/apps}}
cp bin/gram %{buildroot}%{_bindir}/gram
cp libexec/gram-editor %{buildroot}%{_libexecdir}/gram-editor
cp share/icons/hicolor/scalable/apps/app.liten.Gram.svg %{buildroot}%{_datadir}/icons/hicolor/scalable/apps/app.liten.Gram.svg
cp share/icons/hicolor/symbolic/apps/app.liten.Gram-symbolic.svg %{buildroot}%{_datadir}/icons/hicolor/symbolic/apps/app.liten.Gram-symbolic.svg
cp share/applications/gram.desktop %{buildroot}%{_datadir}/applications/gram.desktop

%files
%{_bindir}/gram
%{_libexecdir}/gram-editor
%{_datadir}/applications/gram.desktop
%{_datadir}/icons/hicolor/scalable/apps/app.liten.Gram.svg
%{_datadir}/icons/hicolor/symbolic/apps/app.liten.Gram-symbolic.svg
%license licenses.md

%changelog
* Sat May 02 2026 SED4906 <sed4906birdie@gmail.com>
- Initial packaging
