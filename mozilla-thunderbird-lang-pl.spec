# TODO:
#  - do something with *.rdf file, there is file conflict with other lang packages
#
Summary:	Polish resources for Mozilla-thunderbird
Summary(pl):	Polskie pliki j�zykowe dla Mozilli-thunderbird
Name:		mozilla-thunderbird-lang-pl
Version:	1.5.0.4
Release:	0.1
License:	GPL
Group:		X11/Applications/Networking
Source0:	http://ftp.mozilla.org/pub/mozilla.org/thunderbird/releases/%{version}/linux-i686/xpi/pl.xpi
# Source0-md5:	201453edde0adbdda1bed3bbcb25f5f4
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
Polskie pliki j�zykowe dla Mozilli-thunderbird.

%prep

%install
rm -rf $RPM_BUILD_ROOT
install -d $RPM_BUILD_ROOT{%{_bindir},%{_chromedir},%{_thunderbirddir}/{defaults/profile,searchplugins}}

unzip %{SOURCE0} -d $RPM_BUILD_ROOT%{_libdir}
mv -f $RPM_BUILD_ROOT%{_libdir}/chrome/pl.jar $RPM_BUILD_ROOT%{_chromedir}/pl-PL.jar
mv -f $RPM_BUILD_ROOT%{_libdir}/*.rdf $RPM_BUILD_ROOT%{_thunderbirddir}/defaults/profile
mv -f $RPM_BUILD_ROOT%{_libdir}/chrome/* $RPM_BUILD_ROOT%{_chromedir}
mv -f $RPM_BUILD_ROOT%{_libdir}/chrome.manifest $RPM_BUILD_ROOT%{_chromedir}/pl-PL.manifest

%clean
rm -rf $RPM_BUILD_ROOT

%files
%defattr(644,root,root,755)
%{_chromedir}/pl-PL.jar
%{_chromedir}/pl-PL.manifest
%{_chromedir}/chromelist.txt
%{_thunderbirddir}/defaults/profile/*.rdf

#   /usr/lib/#   /usr/lib/chrome/
