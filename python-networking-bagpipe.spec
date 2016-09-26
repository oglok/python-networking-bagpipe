%global pypi_name networking-bagpipe
%global sname networking_bagpipe
%{!?upstream_version: %global upstream_version %{version}%{?milestone}}

Name:           python-%{pypi_name}
Version:        4.0.0
Release:        1%{?dist}
Summary:        Mechanism driver for Neutron ML2 plugin using BGP E-VPNs/IP VPNs as a backend

License:        ASL 2.0
URL:            https://github.com/Orange-OpenSource/bagpipe-bgp
Source0:        https://files.pythonhosted.org/packages/source/n/%{pypi_name}/%{pypi_name}-%{upstream_version}.tar.gz
BuildArch:      noarch

BuildConflicts: python-oslosphinx = 3.4.0
BuildConflicts: python-sphinx = 1.2.0
BuildConflicts: python-sphinx = 1.3b1
BuildRequires:  python-coverage >= 3.6
BuildRequires:  python-hacking >= 0.10.0
BuildRequires:  python-oslo-sphinx >= 2.5.0
BuildRequires:  python-oslotest >= 1.10.0
BuildRequires:  python-pbr >= 1.8
BuildRequires:  python-setuptools
BuildRequires:  python-sphinx >= 1.1.2
BuildRequires:  python-subunit >= 0.0.18
BuildRequires:  python-testrepository >= 0.0.18
BuildRequires:  python-testscenarios >= 0.4
BuildRequires:  python-testtools >= 1.4.0
BuildRequires:  python2-devel
BuildRequires:  python-sphinx

%description
 BaGPipe BGP is a lightweight implementation of BGP VPNs (IP VPNs and E-VPNs),
targeting deployments on servers hosting VMs, in particular for Openstack/KVM
platforms.

%package -n     python2-%{pypi_name}
Summary:        Mechanism driver for Neutron ML2 plugin using BGP E-VPNs/IP VPNs as a backend
%{?python_provide:%python_provide python2-%{pypi_name}}

Requires:       python-pbr >= 1.6
Requires:       python-Babel >= 2.3.4
Requires:       python-neutron-lib >= 0.1.0
Requires:       python-oslo-db >= 4.1.0
Requires:       python-oslo-config >= 3.9.0
Requires:       python-oslo-concurrency >= 3.5.0
Requires:       python-oslo-log >= 1.14.0
Requires:       python-oslo-messaging >= 4.5.0
Requires:       python-oslo-service >= 1.0.0
Requires:       python-setuptools

%description -n python2-%{pypi_name}
 BaGPipe BGP is a lightweight implementation of BGP VPNs (IP VPNs and E-VPNs),
targeting deployments on servers hosting VMs, in particular for Openstack/KVM
platforms.

%package -n python-%{pypi_name}-doc
Summary:        networking-bagpipe documentation
%description -n python-%{pypi_name}-doc
Documentation for networking-bagpipe

%prep
%autosetup -n %{pypi_name}-%{upstream_version}
# Remove bundled egg-info
rm -rf %{pypi_name}.egg-info

%build
%py2_build
# generate html docs
sphinx-build doc/source html
# remove the sphinx-build leftovers
rm -rf html/.{doctrees,buildinfo}

%install
%py2_install


%files -n python2-%{pypi_name}
%license LICENSE
%doc README.rst doc/source/readme.rst
%{python2_sitelib}/%{sname}
%{python2_sitelib}/%{sname}-*.egg-info
%{_bindir}/neutron-bagpipe-linuxbridge-agent

%files -n python-%{pypi_name}-doc
%doc html

%changelog
* Fri Sep 23 2016 Luke Hinds <lhinds@redhat.com> - 4.0.0-1
- Initial package.
