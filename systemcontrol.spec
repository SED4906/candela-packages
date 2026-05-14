Name:           systemcontrol
Version:        0.1.0
Release:        1%{?dist}
Summary:        A simple GUI for managing systemd units.

License:        MIT
URL:            https://4906.org/
Source0:        hhttps://github.com/SED4906/%{name}/archive/refs/tags/%{version}.tar.gz#/systemcontrol-0.1.0.tar.gz

Requires:       cargo-rpm-macros

%description
A simple GUI for managing systemd units.

%prep
%setup
%cargo_prep
sed -i '22,32d' .cargo/config.toml

%build
%cargo_build

%install
mkdir -p %{buildroot}/usr/{bin,share/{applications,icons/hicolor/scalable/apps}}
cp target/rpm/systemcontrol %{buildroot}%{_bindir}/systemcontrol
cp res/systemcontrol.svg %{buildroot}%{_datadir}/icons/hicolor/scalable/apps/systemcontrol.svg
cp res/systemcontrol.desktop %{buildroot}%{_datadir}/applications/systemcontrol.desktop

%files
%{_bindir}/systemcontrol
%{_datadir}/applications/systemcontrol.desktop
%{_datadir}/icons/hicolor/scalable/apps/systemcontrol.svg

%changelog
* Thu May 14 2026 SED4906 <sed4906birdie@gmail.com>
- Initial packaging
