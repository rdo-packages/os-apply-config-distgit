%{!?sources_gpg: %{!?dlrn:%global sources_gpg 1} }
%global sources_gpg_sign 0x2426b928085a020d8a90d0d879ab7008d0896c8a

%{!?upstream_version: %global upstream_version %{version}%{?milestone}}
# we are excluding some BRs from automatic generator
%global excluded_brs doc8 bandit pre-commit hacking flake8-import-order bashate sphinx openstackdocstheme

Name:		os-apply-config
Version:	XXX
Release:	XXX
Summary:	Configure files from cloud metadata

License:	Apache-2.0
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
BuildRequires:	pyproject-rpm-macros

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

sed -i /^[[:space:]]*-c{env:.*_CONSTRAINTS_FILE.*/d tox.ini
sed -i "s/^deps = -c{env:.*_CONSTRAINTS_FILE.*/deps =/" tox.ini
sed -i /^minversion.*/d tox.ini
sed -i /^requires.*virtualenv.*/d tox.ini

# Exclude some bad-known BRs
for pkg in %{excluded_brs}; do
  for reqfile in doc/requirements.txt test-requirements.txt; do
    if [ -f $reqfile ]; then
      sed -i /^${pkg}.*/d $reqfile
    fi
  done
done

%generate_buildrequires
%pyproject_buildrequires -t -e %{default_toxenv}

%build
%pyproject_wheel

%install
%pyproject_install
install -d -m 755 %{buildroot}%{_libexecdir}/%{name}/templates

%check
%tox -e %{default_toxenv}

%files
%doc README.rst
%doc LICENSE
%{_bindir}/os-apply-config
%{_bindir}/os-config-applier
%{_libexecdir}/%{name}/templates
%{python3_sitelib}/os_apply_config*

%changelog
