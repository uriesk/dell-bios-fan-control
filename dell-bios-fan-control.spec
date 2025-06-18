%define debug_package %{nil}

Summary: Disable/Enable BIOS fan control on  Dell laptops
Name: {{{ git_dir_name }}}
Version: {{{ git_dir_version lead=0 follow=02 }}}
Release: 2%{?dist}
License: GPLv2+
Source: {{{ git_dir_pack }}}
URL: https://github.com/TomFreudenberg/dell-bios-fan-control
BuildRequires: gcc
Provides: %{name}-%{version}-%{release}

%description
A tool that enables/disables the BIOS fan control on some Dell Laptops. This is required on some Notebooks to be able to control fanspeed with i8kmon, without the BIOS immediately overruling it again.

%prep
{{{ git_dir_setup_macro }}}

%build
make

%install
mkdir -p %{buildroot}/%{_bindir}
cp dell-bios-fan-control %{buildroot}/%{_bindir}/

%clean
rm -rf %{buildroot}/%{_bindir}
make clean

%files
%defattr(-, root, root)
%{_bindir}/dell-bios-fan-control

%changelog
* Sun Jun 3 2018 uriesk <uriesk@posteo.de> 1.43
- created spec file
