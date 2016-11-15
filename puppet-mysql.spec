%{!?upstream_version: %global upstream_version %{commit}}
%define upstream_name puppetlabs-mysql
%global commit c840a358878fc5c51ce33b7981678f2a4229a18c
%global shortcommit %(c=%{commit}; echo ${c:0:7})
# DO NOT REMOVE ALPHATAG
%global alphatag .%{shortcommit}git


Name:           puppet-mysql
Version:        3.10.0
Release:        1%{?alphatag}%{?dist}'
Summary:        Installs, configures, and manages the MySQL service.
License:        Apache-2.0

URL:            http://github.com/puppetlabs/puppetlabs-mysql

Source0:        https://github.com/puppetlabs/%{upstream_name}/archive/%{commit}.tar.gz#/%{upstream_name}-%{shortcommit}.tar.gz

BuildArch:      noarch

Requires:       puppet-stdlib
Requires:       puppet-staging
Requires:       puppet >= 2.7.0

%description
Installs, configures, and manages the MySQL service.

%prep
%setup -q -n %{upstream_name}-%{upstream_version}

find . -type f -name ".*" -exec rm {} +
find . -size 0 -exec rm {} +
find . \( -name "*.pl" -o -name "*.sh"  \) -exec chmod +x {} +
find . \( -name "*.pp" -o -name "*.py"  \) -exec chmod -x {} +
find . \( -name "*.rb" -o -name "*.erb" \) -exec chmod -x {} +
find . \( -name spec -o -name ext \) | xargs rm -rf

%build


%install
rm -rf %{buildroot}
install -d -m 0755 %{buildroot}/%{_datadir}/openstack-puppet/modules/mysql/
cp -rp * %{buildroot}/%{_datadir}/openstack-puppet/modules/mysql/



%files
%{_datadir}/openstack-puppet/modules/mysql/


%changelog
* Tue Nov 15 2016 Alfredo Moralejo <amoralej@redhat.com> 3.10.0-1.c840a35.git
- Newton update 3.10.0 (c840a358878fc5c51ce33b7981678f2a4229a18c)

* Wed Sep 21 2016 Haikel Guemar <hguemar@fedoraproject.org> - 3.9.0-1.ad259bd.git
- Newton update 3.9.0 (ad259bd05a0190475fde02dacdc9a3d7b9621ec9)


