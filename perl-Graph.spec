%define upstream_name    Graph
%define upstream_version 0.91

Name:       perl-%{upstream_name}
Version:    %perl_convert_version %{upstream_version}
Release:    %mkrel 1
Epoch:      1

Summary:    Graph data structures and algorithms in perl
License:    GPL+ or Artistic
Group:      Development/Perl
Url:        http://search.cpan.org/dist/%{upstream_name}/
Source0:    http://www.cpan.org/modules/by-module/Graph/%{upstream_name}-%{upstream_version}.tar.bz2

%if %{mdkversion} < 1010
BuildRequires:  perl-devel
%endif
BuildRequires:  perl(Heap)
BuildArch:      noarch
BuildRoot:      %{_tmppath}/%{name}-%{version}-%{release}

%description
This module is not for drawing any sort of graphics, but instead it is for
creating abstract data structures called graphs, and for doing various
operations on those.

%prep
%setup -q -n %{upstream_name}-%{upstream_version}

%build
%{__perl} Makefile.PL INSTALLDIRS=vendor
%make

%install
rm -rf %{buildroot}
%{makeinstall_std}

%check
%{__make} test

%clean 
rm -rf %{buildroot}

%files
%defattr(-,root,root)
%doc Changes README DESIGN RELEASE TODO
%{perl_vendorlib}/Graph
%{perl_vendorlib}/Graph.*
%{perl_vendorlib}/Heap071
%{perl_vendorlib}/auto/Heap071
%{_mandir}/*/*
