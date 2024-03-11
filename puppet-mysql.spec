%{!?upstream_version: %global upstream_version %{version}%{?milestone}}
%define upstream_name puppetlabs-mysql

Name:           puppet-mysql
Version:        XXX
Release:        XXX
Summary:        Installs, configures, and manages the MySQL service.
License:        ASL 2.0

URL:            http://github.com/puppetlabs/puppetlabs-mysql

Source0:        https://github.com/puppetlabs/%{upstream_name}/archive/v%{upstream_version}.tar.gz
BuildArch:      noarch

Requires:       puppet-stdlib
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

