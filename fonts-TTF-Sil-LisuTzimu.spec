Summary:	Free TrueType fonts for Lisu script
Summary(pl.UTF-8):	Wolnodostępne fonty TrueType dla pisma lisu
Name:		fonts-TTF-Sil-LisuTzimu
Version:	1.0
Release:	1
License:	SIL OFL, distributable
Group:		Fonts
# 4 files extracted from windows installer:
# http://www.mediafire.com/?nng3ontzxrt
Source0:	lisutzimu.ttf
# Source0-md5:	9a41e818ebafe41b200632f4874623d3
Source1:	lisutzimu-italic.ttf
# Source1-md5:	b2f0f19ed905d92f7eb6817252217592
Source2:	lisutzimu-bold.ttf
# Source2-md5:	aee579089338b66cf0b40dfe24d5408a
Source3:	lisutzimu-bolditalic.ttf
# Source3-md5:	4215f138effa1f2bbbea26ba5004b6b6
Requires(post,postun):	fontpostinst
BuildArch:	noarch
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%define		ttffontsdir	%{_fontsdir}/TTF

%description
This package contains free Unicode TrueType fonts for the Lisu script.

%prep

%install
rm -rf $RPM_BUILD_ROOT
install -d $RPM_BUILD_ROOT%{ttffontsdir}
cp -a %{SOURCE0} %{SOURCE1} %{SOURCE2} %{SOURCE3} $RPM_BUILD_ROOT%{ttffontsdir}

%clean
rm -rf $RPM_BUILD_ROOT

%post
fontpostinst TTF

%postun
fontpostinst TTF

%files
%defattr(644,root,root,755)
%{ttffontsdir}/lisutzimu*.ttf
