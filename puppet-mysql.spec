%{!?upstream_version: %global upstream_version %{commit}}
%define upstream_name puppetlabs-mysql
%global commit fff2c82628cb6aca421906cc11baf1f60e65ab04
%global shortcommit %(c=%{commit}; echo ${c:0:7})
# DO NOT REMOVE ALPHATAG
%global alphatag .%{shortcommit}git


Name:           puppet-mysql
Version:        10.4.0
Release:        1%{?alphatag}%{?dist}
Summary:        Installs, configures, and manages the MySQL service.
License:        ASL 2.0

URL:            http://github.com/puppetlabs/puppetlabs-mysql

Source0:        https://github.com/puppetlabs/%{upstream_name}/archive/%{commit}.tar.gz#/%{upstream_name}-%{shortcommit}.tar.gz
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
* Mon May 04 2020 RDO <dev@lists.rdoproject.org> 10.4.0-1.fff2c82git
- Update to post 10.4.0 (fff2c82628cb6aca421906cc11baf1f60e65ab04)



