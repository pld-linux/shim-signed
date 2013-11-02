Summary:	EFI loader to chain-load signed boot loaders under Secure Boot
Summary(pl.UTF-8):	Bootloader EFI do wczytywania podpisanych bootloaderów w ramach Secure Boot
Name:		shim-signed
Version:	0.4
Release:	1
License:	BSD
Group:		Applications/System
# Extracted from Fedora package
Source0:	%{name}-%{version}.efi
# Source0-md5:	abf18595e08e1be3458e5e18c87dfe3c
URL:		http://mjg59.dreamwidth.org/20303.html
# noarch or %{x8664}? build doesn't depend on arch, but package is usable on %{x8664} only
BuildArch:	noarch
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%description
EFI boot loader to chain-load signed boot loaders under Secure Boot.

%description -l pl.UTF-8
Bootloader EFI do wczytywania podpisanych bootloaderów kolejnego
poziomu w ramach Secure Boot.

%prep
%setup -q -c -T

%install
rm -rf $RPM_BUILD_ROOT

install -d $RPM_BUILD_ROOT/lib/efi/x64
install %{SOURCE0} $RPM_BUILD_ROOT/lib/efi/x64/shim-signed.efi

%clean
rm -rf $RPM_BUILD_ROOT

%files
%defattr(644,root,root,755)
/lib/efi/x64/shim-signed.efi
