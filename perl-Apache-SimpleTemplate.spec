%include	/usr/lib/rpm/macros.perl
%define	pdir	Apache
%define	pnam	SimpleTemplate
Summary:	Apache::SimpleTemplate - a very simple mod_perl template parser
#Summary(pl):	
Name:		perl-Apache-SimpleTemplate
Version:	0.02
Release:	1
License:	GPL/Artistic
Group:		Development/Languages/Perl
Source0:	ftp://ftp.cpan.org/pub/CPAN/modules/by-module/%{pdir}/%{pdir}-%{pnam}-%{version}.tar.gz
BuildRequires:	perl >= 5.6
BuildRequires:	rpm-perlprov >= 3.0.3-26
Requires:	apache-mod_perl
BuildArch:	noarch
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%description
Apache::SimpleTemplate is *another* Template-with-embedded-Perl package
for mod_perl. It allows you to embed blocks of Perl code into text
documents, such as HTML files, and have this code executed upon HTTP
request. It should take moments to set-up and learn; very little knowledge
of mod_perl is necessary.

# %description -l pl
# TODO

%prep
%setup -q -n %{pdir}-%{pnam}-%{version}

%build
perl Makefile.PL
%{__make}

%install
rm -rf $RPM_BUILD_ROOT

%{__make} install DESTDIR=$RPM_BUILD_ROOT

%clean
rm -rf $RPM_BUILD_ROOT

%files
%defattr(644,root,root,755)
%doc README
%{perl_sitelib}/%{pdir}/*.pm
%{_mandir}/man3/*
