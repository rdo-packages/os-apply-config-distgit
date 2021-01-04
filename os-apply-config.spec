%{!?sources_gpg: %{!?dlrn:%global sources_gpg 1} }
%global sources_gpg_sign 0x5d2d1e4fb8d38e6af76c50d53d4fec30cf5ce3da

%{!?upstream_version: %global upstream_version %{version}%{?milestone}}

Name:		os-apply-config
Version:	12.0.0
Release:	1%{?dist}
Summary:	Configure files from cloud metadata

License:	ASL 2.0
URL:		http://pypi.python.org/pypi/%{name}
Source0:	https://tarballs.openstack.org/%{name}/%{name}-%{upstream_version}.tar.gz
# Required for tarball sources verification
%if 0%{?sources_gpg} == 1
Source101:        https://tarballs.openstack.org/%{name}/%{name}-%{upstream_version}.tar.gz.asc
Source102:        https://releases.openstack.org/_static/%{sources_gpg_sign}.txt
%endif

BuildArch:	noarch

# Required for tarball sources verification
%if 0%{?sources_gpg} == 1
BuildRequires:  /usr/bin/gpgv2
BuildRequires:  openstack-macros
%endif

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
# Required for tarball sources verification
%if 0%{?sources_gpg} == 1
%{gpgverify}  --keyring=%{SOURCE102} --signature=%{SOURCE101} --data=%{SOURCE0}
%endif
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
* Mon Jan 04 2021 RDO <dev@lists.rdoproject.org> 12.0.0-1
- Update to 12.0.0

* Tue Oct 20 2020 Joel Capitao <jcapitao@redhat.com> 11.3.0-2
- Enable sources tarball validation using GPG signature.

* Tue Sep 29 2020 RDO <dev@lists.rdoproject.org> 11.3.0-1
- Update to 11.3.0

