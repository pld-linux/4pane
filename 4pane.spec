Summary:	A multi-pane, detailed-list file manager
Summary(hu.UTF-8):	Többpaneles, részletes-listás fájlkezelő
Name:		4pane
Version:	0.8.0
Release:	0.2
License:	GPL v3
Group:		X11/Applications
Source0:	http://downloads.sourceforge.net/project/fourpane/%{version}/%{name}-%{version}.tar.gz
# Source0-md5:	5152105f7c148b8a465cf85534227fb7
URL:		http://www.4pane.co.uk/index.html
BuildRequires:	gettext-devel
BuildRequires:	wxGTK2-unicode-devel
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%description
4Pane is a multi-pane, detailed-list file manager for Linux. It is
designed to be fully-featured without bloat, and aims for speed rather
than visual effects. In addition to standard file manager things, it
offers multiple undo and redo of most operations (including
deletions), archive management including 'virtual browsing' inside
archives, multiple renaming/duplication of files, a terminal emulator
and user-defined tools.

%prep
%setup -q

%build
%configure \
	--enable-unicode \
	--with-wx-config=%{_bindir}/wx-gtk2-unicode-config
%{__make}

%install
rm -rf $RPM_BUILD_ROOT

%{__make} install \
	DESTDIR=$RPM_BUILD_ROOT
install -d $RPM_BUILD_ROOT%{_desktopdir}
mv $RPM_BUILD_ROOT{%{_datadir}/4Pane/rc/4Pane.desktop,%{_desktopdir}}
%{find_lang} 4Pane

%clean
rm -rf $RPM_BUILD_ROOT

%files -f 4Pane.lang
%defattr(644,root,root,755)
%attr(755,root,root) %{_bindir}/*
%doc %{_docdir}/4Pane
%{_desktopdir}/4Pane.desktop
%{_datadir}/4Pane
