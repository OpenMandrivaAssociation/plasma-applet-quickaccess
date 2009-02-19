Summary:	Quick access the most used folders
Name:		plasma-applet-quickaccess
Version: 	0.7.1
Release: 	%mkrel 3
Source0: 	http://www.kde-look.org/CONTENT/content-files/84128-quickaccess-%{version}.tar.gz
Patch0:     quickaccess-0.7.1-fix-kde42-api.patch
License: 	GPLv2+
Group: 		Graphical desktop/KDE
Url: 		http://www.kde-look.org/content/show.php/QuickAccess?content=84128
BuildRoot: 	%{_tmppath}/%{name}-%{version}-%{release}-buildroot
BuildRequires: 	kdebase4-devel >= 4.0.70
BuildRequires:	plasma-devel >= 4.0.70
Requires:	konqueror >= 4.0.70

%description 
This is a small applet designed for the panel to have quick access to the most used folders.

%files
%defattr(-,root,root)
%{_kde_libdir}/kde4/plasma_applet_*.so
%{_kde_services}/plasma-applet-*.desktop

#--------------------------------------------------------------------

%prep
%setup -q -n quickaccess-%version
%patch0 -p1

%build
%cmake_kde4
%make

%install
rm -rf %{buildroot}
%{makeinstall_std} -C build

%clean
rm -rf %{buildroot}
