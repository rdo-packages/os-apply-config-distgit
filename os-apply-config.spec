%{!?upstream_version: %global upstream_version %{version}%{?milestone}}

%if 0%{?fedora} >= 28
%global with_python3 1
%endif

Name:		os-apply-config
Version:	XXX
Release:	XXX
Summary:	Configure files from cloud metadata

License:	ASL 2.0
URL:		http://pypi.python.org/pypi/%{name}
Source0:	https://tarballs.openstack.org/%{name}/%{name}-%{upstream_version}.tar.gz

BuildArch:	noarch

%if 0%{?with_python3} == 0
# begin python2 requirements
BuildRequires:	python2-devel
BuildRequires:	python2-setuptools
BuildRequires:	python2-pbr

Requires:	python2-pbr
Requires:	python-anyjson
Requires:	pystache
Requires:       PyYAML
Requires:	python2-six >= 1.10.0
# end python2 requirements
%else
# end python3 requirements
BuildRequires:	python3-devel
BuildRequires:	python3-setuptools
BuildRequires:	python3-pbr

Requires:	python3-pbr
Requires:	python3-anyjson
Requires:	python3-pystache
Requires:       python3-PyYAML
Requires:	python3-six >= 1.10.0
# end python3 requirements
%endif

%description
Tool to apply openstack heat metadata to files on the system.

%prep
%setup -q -n %{name}-%{upstream_version}


%build
%if 0%{?with_python3} == 0
%{py2_build}
%else
%{py3_build}
%endif

%install
%if 0%{?with_python3} == 0
%{py2_install}
%else
%{py3_install}
%endif
install -d -m 755 %{buildroot}%{_libexecdir}/%{name}/templates

%files
%doc README.rst
%doc LICENSE
%{_bindir}/os-apply-config
%{_bindir}/os-config-applier
%{_libexecdir}/%{name}/templates
%if 0%{?with_python3} == 0
%{python2_sitelib}/os_apply_config*
%else
%{python3_sitelib}/os_apply_config*
%endif


%changelog
