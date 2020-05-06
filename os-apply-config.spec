
%{!?upstream_version: %global upstream_version %{version}%{?milestone}}

Name:		os-apply-config
Version:	XXX
Release:	XXX
Summary:	Configure files from cloud metadata

License:	ASL 2.0
URL:		http://pypi.python.org/pypi/%{name}
Source0:	https://tarballs.openstack.org/%{name}/%{name}-%{upstream_version}.tar.gz

BuildArch:	noarch

BuildRequires:	python3-devel
BuildRequires:	python3-setuptools
BuildRequires:	python3-pbr

Requires:   python3-pbr
Requires:   python3-six >= 1.10.0

Requires:   python3-anyjson
Requires:   python3-pystache
Requires:   python3-PyYAML

%description
Tool to apply openstack heat metadata to files on the system.

%prep
%setup -q -n %{name}-%{upstream_version}

# Remove unnecessary shebang
sed -i '1{/^#!/d}' os_apply_config/tests/templates/etc/glance/script.conf
chmod -x os_apply_config/tests/templates/etc/glance/script.conf

%build
%{py3_build}

%install
%{py3_install}
install -d -m 755 %{buildroot}%{_libexecdir}/%{name}/templates

%files
%doc README.rst
%doc LICENSE
%{_bindir}/os-apply-config
%{_bindir}/os-config-applier
%{_libexecdir}/%{name}/templates
%{python3_sitelib}/os_apply_config*

%changelog
