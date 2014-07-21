#
# Conditional build:
%bcond_with	tests		# build without tests

Summary:	Pimp your CHANGELOG.md
Name:		pimpmychangelog
Version:	0.1.2
Release:	2
License:	GPL v2+ or Ruby
Group:		Applications/Text
Source0:	http://rubygems.org/downloads/%{name}-%{version}.gem
# Source0-md5:	0359fcd357bc127fe58a5762e07b70c4
Patch0:		require.patch
URL:		https://github.com/pcreux/pimpmychangelog
BuildRequires:	rpm-rubyprov
BuildRequires:	rpmbuild(macros) >= 1.656
BuildRequires:	sed >= 4.0
%if %{with tests}
BuildRequires:	ruby-guard-rspec
BuildRequires:	ruby-rake
BuildRequires:	ruby-rspec
%endif
BuildArch:	noarch
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%description
Linkify issue numbers (#123) and github users (@gregbell) in markdown
changelogs.

%prep
%setup -q
%{__sed} -i -e '1 s,#!.*ruby,#!%{__ruby},' bin/*
%patch0 -p1

%install
rm -rf $RPM_BUILD_ROOT
install -d $RPM_BUILD_ROOT{%{ruby_vendorlibdir},%{_bindir}}
cp -a lib/* $RPM_BUILD_ROOT%{ruby_vendorlibdir}
cp -a bin/* $RPM_BUILD_ROOT%{_bindir}

%clean
rm -rf $RPM_BUILD_ROOT

%files
%defattr(644,root,root,755)
%attr(755,root,root) %{_bindir}/pimpmychangelog
%{ruby_vendorlibdir}/%{name}.rb
%{ruby_vendorlibdir}/%{name}
