Name:           uupd
Version:        1.4.0
Release:        3%{?dist}
Summary:       Centralized update service/checker made for Universal Blue
Vendor:        ublue-os
URL:           https://github.com/%{vendor}/%{name}
Source0:        %{url}/archive/fd09b47a1e56ba93cb84feffec8ceaa202462fdc.tar.gz
License:        Apache-2.0

BuildRequires:  golang
BuildRequires:  systemd-rpm-macros
Recommends:     bootc
Recommends:     distrobox
Recommends:     flatpak
Requires:       libnotify
Requires:       systemd
Provides:       %{name} = %{version}

%description
A simple updater for Universal Blue systems

%global debug_package %{nil}

%prep
%autosetup -n uupd-fd09b47a1e56ba93cb84feffec8ceaa202462fdc

%build
go build -v -o %{name}

%install
install -Dpm 0755 %{name} %{buildroot}%{_bindir}/%{name}
install -Dpm 644 %{name}.service %{buildroot}%{_unitdir}/%{name}.service
install -Dpm 644 %{name}-manual.service %{buildroot}%{_unitdir}/%{name}-manual.service
install -Dpm 644 %{name}.timer %{buildroot}%{_unitdir}/%{name}.timer
install -Dpm 644 %{name}.rules %{buildroot}%{_datadir}/polkit-1/rules.d/%{name}.rules
install -Dpm 644 config.json %{buildroot}/%{_sysconfdir}/%{name}/config.json

%check
go test -v ./...

%post
%systemd_post %{name}.timer

%preun
%systemd_preun %{name}.timer

%files
%{_bindir}/%{name}
%{_unitdir}/%{name}.service
%{_unitdir}/%{name}.timer
%{_unitdir}/%{name}-manual.service
%{_datadir}/polkit-1/rules.d/%{name}.rules
%config(noreplace) %{_sysconfdir}/%{name}/config.json
%changelog
%autochangelog
