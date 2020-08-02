%define upstream_name    Graph
%define upstream_version 0.9704

Name:		perl-%{upstream_name}
Version:	%perl_convert_version %{upstream_version}
Release:	1
Epoch:		1

Summary:	Graph data structures and algorithms in perl
License:	GPL+ or Artistic
Group:		Development/Perl
Url:		http://search.cpan.org/dist/%{upstream_name}/
Source0:	http://www.cpan.org/modules/by-module/Graph/%{upstream_name}-%{upstream_version}.tar.gz

BuildRequires:	perl-devel
BuildRequires:	perl(Heap)
BuildArch:	noarch

%description
This module is not for drawing any sort of graphics, but instead it is for
creating abstract data structures called graphs, and for doing various
operations on those.

%prep
%setup -q -n %{upstream_name}-%{upstream_version}

%build
perl Makefile.PL INSTALLDIRS=vendor
%make_build

%install
%make_nstall

%files
%doc Changes README DESIGN RELEASE TODO
%{perl_vendorlib}/Graph
%{perl_vendorlib}/Graph.*
%{perl_vendorlib}/Heap071
%{perl_vendorlib}/auto/Heap071
%{_mandir}/*/*

%changelog
* Mon Mar 15 2010 JÃ©rÃ´me Quelin <jquelin@mandriva.org> 1:0.940.0-1mdv2010.1
+ Revision: 519954
- update to 0.94

* Sun Mar 07 2010 JÃ©rÃ´me Quelin <jquelin@mandriva.org> 1:0.930.0-1mdv2010.1
+ Revision: 515498
- update to 0.93

* Thu Mar 04 2010 JÃ©rÃ´me Quelin <jquelin@mandriva.org> 1:0.920.0-1mdv2010.1
+ Revision: 514097
- update to 0.92

* Wed Jul 29 2009 JÃ©rÃ´me Quelin <jquelin@mandriva.org> 1:0.910.0-1mdv2010.0
+ Revision: 403227
- rebuild using %%perl_convert_version

* Sun Jan 18 2009 Guillaume Rousse <guillomovitch@mandriva.org> 1:0.91-1mdv2009.1
+ Revision: 330909
- update to new version 0.91

* Tue Dec 30 2008 Guillaume Rousse <guillomovitch@mandriva.org> 1:0.90-1mdv2009.1
+ Revision: 321298
- update to new version 0.90

* Sun Dec 28 2008 Guillaume Rousse <guillomovitch@mandriva.org> 1:0.89-1mdv2009.1
+ Revision: 320432
- update to new version 0.89

* Tue Dec 02 2008 Guillaume Rousse <guillomovitch@mandriva.org> 1:0.86-1mdv2009.1
+ Revision: 309305
- update to new version 0.86

* Thu Jul 31 2008 Thierry Vignaud <tv@mandriva.org> 1:0.84-3mdv2009.0
+ Revision: 257131
- rebuild

* Thu Dec 20 2007 Olivier Blin <oblin@mandriva.com> 1:0.84-1mdv2008.1
+ Revision: 135846
- restore BuildRoot

  + Thierry Vignaud <tv@mandriva.org>
    - kill re-definition of %%buildroot on Pixel's request

* Thu Aug 30 2007 Guillaume Rousse <guillomovitch@mandriva.org> 1:0.84-1mdv2008.0
+ Revision: 75226
- update to new version 0.84

* Fri Aug 17 2007 Funda Wang <fwang@mandriva.org> 1:0.83-1mdv2008.0
+ Revision: 65371
- fix file list
- New version 0.83


* Tue Mar 06 2007 Guillaume Rousse <guillomovitch@mandriva.org> 0.81-1mdv2007.0
+ Revision: 133721
- new version
- Import perl-Graph

* Tue Sep 12 2006 Guillaume Rousse <guillomovitch@mandriva.org> 1:0.80-1mdv2007.0
- New version 0.80

* Sat Aug 26 2006 Guillaume Rousse <guillomovitch@mandriva.org> 1:0.79-1mdv2007.0
- New version 0.79

* Tue Aug 01 2006 Guillaume Rousse <guillomovitch@mandriva.org> 10.78-1mdv2007.0
- New version 0.78

* Sat Jul 01 2006 Guillaume Rousse <guillomovitch@mandriva.org> 10.76-1mdv2007.0
- New version 0.76

* Tue Jun 13 2006 Guillaume Rousse <guillomovitch@mandriva.org> 1:0.75-1mdv2007.0
- New release 0.75

* Fri Jun 02 2006 Guillaume Rousse <guillomovitch@mandriva.org> 1:0.74-1
- New release 0.74

* Wed May 31 2006 Guillaume Rousse <guillomovitch@mandriva.org> 1:0.73-1mdv2007.0
- New release 0.73

* Tue May 23 2006 Guillaume Rousse <guillomovitch@mandriva.org> 1:0.70-1mdk
- New release 0.70
- better source URL
- better buildrequires syntax

* Wed Dec 07 2005 Rafael Garcia-Suarez <rgarciasuarez@mandriva.com> 1:0.69-1mdk
- 0.69

* Thu Nov 24 2005 Rafael Garcia-Suarez <rgarciasuarez@mandriva.com> 1:0.68-1mdk
- 0.68

* Wed Aug 17 2005 Guillaume Rousse <guillomovitch@mandriva.org> 0.67-1mdk
- New release 0.67

* Thu Jul 21 2005 Rafael Garcia-Suarez <rgarciasuarez@mandriva.com> 1:0.66-1mdk
- 0.66

* Sun Jun 12 2005 Guillaume Rousse <guillomovitch@mandriva.org> 1:0.65-2mdk 
- don't ship empty directories
- spec cleanup
- make test in %%check

* Sat May 28 2005 Rafael Garcia-Suarez <rgarciasuarez@mandriva.com> 0.65-1mdk
- 0.65

* Sun Apr 17 2005 Oden Eriksson <oeriksson@mandriva.com> 1:0.63-1mdk
- 0.63

* Mon Feb 21 2005 Rafael Garcia-Suarez <rgarciasuarez@mandrakesoft.com> 0.58-1mdk
- 0.58

* Sat Feb 12 2005 Rafael Garcia-Suarez <rgarciasuarez@mandrakesoft.com> 0.57-1mdk
- 0.57
- New docs
- API not compatible with the 0.2xxxx series

* Mon Dec 20 2004 Guillaume Rousse <guillomovitch@mandrake.org> 0.20105-2mdk
- fix buildrequires in a backward compatible way

* Sat Jun 05 2004 Per Øyvind Karlsen <peroyvind@linux-mandrake.com> 0.20105-1mdk
- 0.20105

* Wed May 12 2004 Michael Scherer <misc@mandrake.org> 0.20104-1mdk
- New release 0.20104

* Thu Apr 22 2004 Guillaume Rousse <guillomovitch@mandrake.org> 0.20102-1mdk
- new version
- rpmbuildupdate aware
- make test
- buildrequires

