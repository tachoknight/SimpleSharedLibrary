%global debug_package %{nil}

Name:           SimpleSharedLibrary
Version:        1.0
Release:        1%{?dist}
Summary:        Nothing package

License:        Apache-2.0        
URL:            https://github.com/tachoknight/SimpleSharedLibrary
Source0:        https://github.com/tachoknight/SimpleSharedLibrary/archive/refs/tags/v1.0.tar.gz        
Source1:        excludes.inc

BuildRequires:  make
BuildRequires:  gcc

Requires:       binutils-gold

%include %{SOURCE1}

%description
Just a nothing package to test the exclusion flags above

%prep
%setup -q


%build
make %{?_smp_mflags}


%install
mkdir -p %{buildroot}%{_libexecdir}/simplesharedlibrary
cp %{_builddir}/%{name}-%{version}/main %{buildroot}%{_libexecdir}/simplesharedlibrary
cp %{_builddir}/%{name}-%{version}/libadd.so %{buildroot}%{_libexecdir}/simplesharedlibrary


%files
%{_libexecdir}/simplesharedlibrary/main
%{_libexecdir}/simplesharedlibrary/libadd.so


%changelog
* Wed Nov 13 2024 Ron Olson <tachoknight@gmail.com> - 1.0-1
- First test version
