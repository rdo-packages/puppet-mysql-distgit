%{!?upstream_version: %global upstream_version %{version}%{?milestone}}
%define upstream_name puppetlabs-mysql


Name:           puppet-mysql
Version:        6.2.0
Release:        1%{?dist}
Summary:        Installs, configures, and manages the MySQL service.
License:        ASL 2.0

URL:            http://github.com/puppetlabs/puppetlabs-mysql

Source0:        https://github.com/puppetlabs/%{upstream_name}/archive/%{version}.tar.gz
BuildArch:      noarch

Requires:       puppet-stdlib
Requires:       puppet-staging
Requires:       puppet >= 2.7.0

%description
Installs, configures, and manages the MySQL service.

%prep
%autosetup -p1 -n %{upstream_name}-%{upstream_version}

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
* Thu Feb 15 2018 RDO <dev@lists.rdoproject.org> 6.2.0-1.6.2.0git
- Update to 6.2.0



