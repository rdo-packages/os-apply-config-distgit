%{!?upstream_version: %global upstream_version %{version}%{?milestone}}

Name:		os-apply-config
Version:	9.1.2
Release:	1%{?dist}
Summary:	Configure files from cloud metadata

License:	ASL 2.0
URL:		http://pypi.python.org/pypi/%{name}
Source0:	https://tarballs.openstack.org/%{name}/%{name}-%{upstream_version}.tar.gz

BuildArch:	noarch
BuildRequires:	python2-devel
BuildRequires:	python2-setuptools
BuildRequires:	python2-pbr

Requires:	python2-pbr
Requires:	python-anyjson
Requires:	pystache
Requires:       PyYAML
Requires:	python2-six >= 1.10.0

%description
Tool to apply openstack heat metadata to files on the system.

%prep
%setup -q -n %{name}-%{upstream_version}


%build
%{__python2} setup.py build

%install
%{__python2} setup.py install -O1 --skip-build --root %{buildroot}
install -d -m 755 %{buildroot}%{_libexecdir}/%{name}/templates

%files
%doc README.rst
%doc LICENSE
%{_bindir}/os-apply-config
%{_bindir}/os-config-applier
%{python2_sitelib}/os_apply_config*
%{_libexecdir}/%{name}/templates

%changelog
* Fri Jun 21 2019 RDO <dev@lists.rdoproject.org> 9.1.2-1
- Update to 9.1.2

* Thu Mar 14 2019 RDO <dev@lists.rdoproject.org> 9.1.1-1
- Update to 9.1.1

* Mon Aug 27 2018 RDO <dev@lists.rdoproject.org> 9.1.0-1
- Update to 9.1.0

