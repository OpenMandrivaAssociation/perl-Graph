%define module  Graph
%define name    perl-%{module}
%define version 0.84
%define release %mkrel 1

Name:           %{name}
Epoch:          1
Version:        %{version}
Release:        %{release}
Summary:        Graph data structures and algorithms in perl
License:        GPL or Artistic
Group:          Development/Perl
Url:            http://search.cpan.org/dist/%{module}/
Source:         http://www.cpan.org/modules/by-module/Graph/%{module}-%{version}.tar.bz2
%if %{mdkversion} < 1010
BuildRequires:  perl-devel
%endif
BuildRequires:  perl(Heap)
BuildArch:      noarch
BuildRoot:      %{_tmppath}/%{name}-%{version}

%description
This module is not for drawing any sort of graphics, but instead it is for
creating abstract data structures called graphs, and for doing various
operations on those.

%prep
%setup -q -n %{module}-%{version}

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
