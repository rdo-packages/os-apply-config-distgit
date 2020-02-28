# Macros for py2/py3 compatibility
%if 0%{?fedora} || 0%{?rhel} > 7
%global pyver 3
%else
%global pyver 2
%endif

%global pyver_bin python%{pyver}
%global pyver_sitelib %{expand:%{python%{pyver}_sitelib}}
%global pyver_install %{expand:%{py%{pyver}_install}}
%global pyver_build %{expand:%{py%{pyver}_build}}
# End of macros for py2/py3 compatibility

%{!?upstream_version: %global upstream_version %{version}%{?milestone}}

Name:		os-apply-config
Version:	10.5.1
Release:	1%{?dist}
Summary:	Configure files from cloud metadata

License:	ASL 2.0
URL:		http://pypi.python.org/pypi/%{name}
Source0:	https://tarballs.openstack.org/%{name}/%{name}-%{upstream_version}.tar.gz

BuildArch:	noarch

BuildRequires:	python%{pyver}-devel
BuildRequires:	python%{pyver}-setuptools
BuildRequires:	python%{pyver}-pbr

Requires:   python%{pyver}-pbr
Requires:   python%{pyver}-six >= 1.10.0

%if %{pyver} == 2
Requires:   pystache
Requires:   PyYAML
Requires:   python-anyjson
%else
Requires:   python%{pyver}-anyjson
Requires:   python%{pyver}-pystache
Requires:   python%{pyver}-PyYAML
%endif

%description
Tool to apply openstack heat metadata to files on the system.

%prep
%setup -q -n %{name}-%{upstream_version}

# Remove unnecessary shebang
sed -i '1{/^#!/d}' os_apply_config/tests/templates/etc/glance/script.conf
chmod -x os_apply_config/tests/templates/etc/glance/script.conf

%build
%{pyver_build}

%install
%{pyver_install}
install -d -m 755 %{buildroot}%{_libexecdir}/%{name}/templates

%files
%doc README.rst
%doc LICENSE
%{_bindir}/os-apply-config
%{_bindir}/os-config-applier
%{_libexecdir}/%{name}/templates
%{pyver_sitelib}/os_apply_config*

%changelog
* Mon Jan 06 2020 RDO <dev@lists.rdoproject.org> 10.5.1-1
- Update to 10.5.1

* Mon Oct 21 2019 RDO <dev@lists.rdoproject.org> 10.5.0-1
- Update to 10.5.0

