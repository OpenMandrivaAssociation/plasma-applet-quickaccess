%define oname plasma-widget-quickaccess

Summary:	Quick access the most used folders
Name:		plasma-applet-quickaccess
Version:	0.8.2
Release:	1
License: 	GPLv2+
Group: 		Graphical desktop/KDE
Url:		http://kde-look.org/content/show.php?content=134442
Source0:	http://kde-look.org/CONTENT/content-files/134442-%{oname}-%{version}-2.zip
BuildRequires:	kdebase4-devel
BuildRequires:	kdebase4-workspace-devel
Requires:	kdebase4-runtime

%description
This is a small applet designed for the panel to have quick access
to the most used folders.

%files -f plasma_applet_quickaccess.lang
%{_kde_libdir}/kde4/plasma_applet_*.so
%{_kde_services}/plasma-applet-*.desktop

#--------------------------------------------------------------------

%prep
%setup -q -n %{oname}-%{version}-2

%build
%cmake_kde4
%make

%install
%makeinstall_std -C build

%find_lang plasma_applet_quickaccess

%changelog
* Thu Sep 09 2010 John Balcaen <mikala@mandriva.org> 0.7.1-5mdv2011.0
+ Revision: 576991
- Rebuild

* Tue Sep 15 2009 Thierry Vignaud <tv@mandriva.org> 0.7.1-4mdv2010.0
+ Revision: 441856
- rebuild

* Thu Feb 19 2009 Nicolas Lécureuil <nlecureuil@mandriva.com> 0.7.1-3mdv2009.1
+ Revision: 343044
- Adapt for kde 4.2

* Thu Jan 01 2009 Nicolas Lécureuil <nlecureuil@mandriva.com> 0.7.1-2mdv2009.1
+ Revision: 323179
- Rebuild against kde 4.2 beta2

  + Funda Wang <fwang@mandriva.org>
    - prepareing for upcoming plasma-devel

* Mon Aug 25 2008 Funda Wang <fwang@mandriva.org> 0.7.1-1mdv2009.0
+ Revision: 275610
- import plasma-applet-quickaccess


