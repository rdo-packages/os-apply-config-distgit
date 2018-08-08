# Macros for py2/py3 compatibility
%if 0%{?fedora} || 0%{?rhel} > 7
%global pydefault 3
%else
%global pydefault 2
%endif

%global pydefault_bin python%{pydefault}
%global pydefault_sitelib %python%{pydefault}_sitelib
%global pydefault_install %py%{pydefault}_install
%global pydefault_build %py%{pydefault}_build
# End of macros for py2/py3 compatibility

%{!?upstream_version: %global upstream_version %{version}%{?milestone}}

Name:		os-apply-config
Version:	XXX
Release:	XXX
Summary:	Configure files from cloud metadata

License:	ASL 2.0
URL:		http://pypi.python.org/pypi/%{name}
Source0:	https://tarballs.openstack.org/%{name}/%{name}-%{upstream_version}.tar.gz

BuildArch:	noarch

BuildRequires:	python%{pydefault}-devel
BuildRequires:	python%{pydefault}-setuptools
BuildRequires:	python%{pydefault}-pbr

Requires:   python%{pydefault}-pbr
Requires:   python%{pydefault}-six >= 1.10.0

%if %{pydefault} == 2
Requires:   pystache
Requires:   PyYAML
Requires:   python-anyjson
%else
Requires:   python%{pydefault}-anyjson
Requires:   python%{pydefault}-pystache
Requires:   python%{pydefault}-PyYAML
%endif

%description
Tool to apply openstack heat metadata to files on the system.

%prep
%setup -q -n %{name}-%{upstream_version}


%build
%{pydefault_build}

%install
%{pydefault_install}
install -d -m 755 %{buildroot}%{_libexecdir}/%{name}/templates

%files
%doc README.rst
%doc LICENSE
%{_bindir}/os-apply-config
%{_bindir}/os-config-applier
%{_libexecdir}/%{name}/templates
%{pydefault_sitelib}/os_apply_config*

%changelog
