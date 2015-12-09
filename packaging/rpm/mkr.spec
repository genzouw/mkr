# sudo yum -y install rpmdevtools go && rpmdev-setuptree
# rpmbuild -ba ~/rpmbuild/SPECS/mkr.spec

%define _binaries_in_noarch_packages_terminate_build   0
%define _localbindir /usr/local/bin

Name:      mkr
Version:   0.7.1
Release:   1
License:   Apache-2.0
Summary:   macekrel.io api client tool
URL:       https://mackerel.io
Group:     Hatena
Packager:  Hatena
BuildArch: noarch
BuildRoot: %{_tmppath}/%{name}-%{version}-%{release}-root

%description
macekrel.io api client tool

%prep

%build

%install
rm -rf %{buildroot}
install -d -m 755 %{buildroot}/%{_localbindir}
install    -m 655 %{_builddir}/%{name}  %{buildroot}/%{_localbindir}
install -d -m 755 %{buildroot}/%{_localstatedir}/log/

%clean
rm -f %{buildroot}%{_bindir}/${name}

%pre

%post

%preun

%files
%defattr(-,root,root)
%{_localbindir}/%{name}

%changelog
* Thu Nov 12 2015 <y.songmu@gmail.com> - 0.7.1-1
- support `notificationIntervai` field in monitors (stanaka)
- [bug] fix json parameter s/hostID/hostId/g (Songmu)

* Mon Oct 26 2015 <daiksy@hatena.ne.jp> - 0.7.0-1
- append newline to the end of monitors.json (by Songmu)
- fix printMonitor (by Songmu)
- fix diff output between slices (by Songmu)

* Thu Oct 15 2015 <itchyny@hatena.ne.jp> - 0.6.0-1
- Fix update command bug about overwriting hostname (by y_uuki)
- Stop the parallel request sending temporarily (by y_uuki)
- Suppress to display empty fields when mkr monitors diff (by stanaka)

* Mon Sep 14 2015 <itchyny@hatena.ne.jp> - 0.5.0-1
- add fields for external URL monitors (by stanaka)

* Fri Aug 28 2015 <tomohiro68@gmail.com> - 0.4.1-1
- Create deb/rpm package for Linux release (by Sixeight)

* Fri Aug 14 2015 <sixeight@hatena.ne.jp> - 0.4.0-1
- first release for rpm