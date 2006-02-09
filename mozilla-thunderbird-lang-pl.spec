# TODO:
#  - do something with *.rdf file, there if file conflict with other lang packages
#
Summary:	Polish resources for Mozilla-thunderbird
Summary(pl):	Polskie pliki jêzykowe dla Mozilli-thunderbird
Name:		mozilla-thunderbird-lang-pl
Version:	1.5
Release:	0.1
License:	GPL
Group:		X11/Applications/Networking
Source0:	http://ftp.mozilla.org/pub/mozilla.org/thunderbird/releases/%{version}/linux-i686/xpi/pl.xpi
# Source0-md5:	ddffac7d447d7b917eee4fd61f20ff8a
Source1:	%{name}-installed-chrome.txt
URL:		http://www.thunderbird.pl/
BuildRequires:	unzip
Requires(post,postun):	mozilla-thunderbird >= %{version}
Requires(post,postun):	textutils
Requires:	mozilla-thunderbird >= %{version}
Provides:	mozilla-thunderbird-lang-resources = %{version}
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%define		_thunderbirddir	%{_libdir}/mozilla-thunderbird
%define		_chromedir	%{_thunderbirddir}/chrome

%description
Polish resources for Mozilla-thunderbird.

%description -l pl
Polskie pliki jêzykowe dla Mozilli-thunderbird.

%prep

%install
rm -rf $RPM_BUILD_ROOT
install -d $RPM_BUILD_ROOT{%{_bindir},%{_chromedir},%{_thunderbirddir}/{defaults/profile,searchplugins}}

unzip %{SOURCE0} -d $RPM_BUILD_ROOT%{_libdir}
mv -f $RPM_BUILD_ROOT%{_libdir}/chrome/pl*.jar $RPM_BUILD_ROOT%{_chromedir}
mv -f $RPM_BUILD_ROOT%{_libdir}/*.rdf $RPM_BUILD_ROOT%{_thunderbirddir}/defaults/profile

install %{SOURCE1} $RPM_BUILD_ROOT%{_chromedir}

%clean
rm -rf $RPM_BUILD_ROOT

%post
umask 022
cat %{_thunderbirddir}/chrome/*-installed-chrome.txt >%{_thunderbirddir}/chrome/installed-chrome.txt

%postun
umask 022
cat %{_thunderbirddir}/chrome/*-installed-chrome.txt >%{_thunderbirddir}/chrome/installed-chrome.txt

%files
%defattr(644,root,root,755)
%{_chromedir}/pl.jar
#%{_chromedir}/pl-PL-mail.jar
%{_chromedir}/%{name}-installed-chrome.txt
%{_thunderbirddir}/defaults/profile/*.rdf
#   /usr/lib/chrome.manifest
#   /usr/lib/chrome/chromelist.txt
