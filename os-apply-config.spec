%{!?upstream_version: %global upstream_version %{version}%{?milestone}}

Name:		os-apply-config
Version:	7.2.0
Release:	1%{?dist}
Summary:	Configure files from cloud metadata

License:	ASL 2.0
URL:		http://pypi.python.org/pypi/%{name}
Source0:	https://tarballs.openstack.org/%{name}/%{name}-%{upstream_version}.tar.gz

BuildArch:	noarch
BuildRequires:	python2-devel
BuildRequires:	python-setuptools
BuildRequires:	python-pbr

Requires:	python-pbr
Requires:	python-anyjson
Requires:	pystache
Requires:       PyYAML
Requires:	python-six >= 1.9.0

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
* Sun Sep 10 2017 rdo-trunk <javier.pena@redhat.com> 7.2.0-1
- Update to 7.2.0

* Thu Aug 24 2017 Alfredo Moralejo <amoralej@redhat.com> 7.1.0-1
- Update to 7.1.0

