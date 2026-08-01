%define upstream_name    Graph
%define upstream_version 0.9735
Name:		perl-%{upstream_name}
Version:	0.9735
Release:	49
Epoch:		1

Summary:	Graph data structures and algorithms in perl
License:	GPL+ or Artistic
Group:		Development/Perl
Url:		https://github.com/graphviz-perl/Graph
Source0:	https://cpan.metacpan.org/authors/id/E/ET/ETJ/Graph-0.9735.tar.gz

BuildRequires:	make
BuildRequires:	perl-devel
BuildRequires:	perl(Heap)
BuildArch:	noarch

%description
This module is not for drawing any sort of graphics, but instead it is for
creating abstract data structures called graphs, and for doing various
operations on those.

%prep
%setup -q -n Graph-0.9735

%build
perl Makefile.PL INSTALLDIRS=vendor
%make_build

%check
make test || :

%install
%make_install

%files
%doc Changes README
%{perl_vendorlib}/Graph
%{perl_vendorlib}/Graph.*
%{_mandir}/*/*

