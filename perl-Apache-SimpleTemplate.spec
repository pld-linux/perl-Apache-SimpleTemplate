#
# Conditional build:
# _without_tests - do not perform "make test"
#
%include	/usr/lib/rpm/macros.perl
%define	pdir	Apache
%define	pnam	SimpleTemplate
Summary:	Apache::SimpleTemplate - a very simple mod_perl template parser
Summary(pl):	Apache::SimpleTemplate - bardzo prosty parser szablonów mod_perla
Name:		perl-Apache-SimpleTemplate
Version:	0.05
Release:	1
License:	GPL/Artistic
Group:		Development/Languages/Perl
Source0:	http://www.cpan.org/modules/by-module/%{pdir}/%{pdir}-%{pnam}-%{version}.tar.gz
BuildRequires:	perl >= 5.6
BuildRequires:	rpm-perlprov >= 4.0.2-104
Requires:	apache-mod_perl
BuildArch:	noarch
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%description
Apache::SimpleTemplate is *another* Template-with-embedded-Perl
package for mod_perl. It allows you to embed blocks of Perl code into
text documents, such as HTML files, and have this code executed upon
HTTP request. It should take moments to set-up and learn; very little
knowledge of mod_perl is necessary.

%description -l pl
Apache::SimpleTemplate to jeszcze jeden pakiet szablonów z wbudowanym
Perlem dla mod_perla. Pozwala na osadzanie bloków kodu Perla w
dokumentach tekstowych, takich jak pliki HTML, oraz uruchamianie tego
kodu przy ¿±daniach HTTP. Powinna wystarczyæ chwila na uruchomienie i
naukê; wymagana jest bardzo ma³a znajomo¶æ mod_perla.

%prep
%setup -q -n %{pdir}-%{pnam}-%{version}

%build
%{__perl} Makefile.PL
%{__make}
%{!?_without_tests:%{__make} test}

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
