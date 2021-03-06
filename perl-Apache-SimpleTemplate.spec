#
# Conditional build:
%bcond_without	tests	# do not perform "make test"

%define		pdir	Apache
%define		pnam	SimpleTemplate
Summary:	Apache::SimpleTemplate - a very simple mod_perl template parser
Summary(pl.UTF-8):	Apache::SimpleTemplate - bardzo prosty parser szablonów mod_perla
Name:		perl-Apache-SimpleTemplate
Version:	0.06b
Release:	1
# same as perl
License:	GPL v1+ or Artistic
Group:		Development/Languages/Perl
Source0:	http://www.cpan.org/modules/by-module/%{pdir}/%{pdir}-%{pnam}-%{version}.tar.gz
# Source0-md5:	59d49dc085d2cb7f7af8c1fa7588d650
URL:		http://search.cpan.org/dist/Apache-SimpleTemplate/
BuildRequires:	perl-devel >= 1:5.8.0
BuildRequires:	rpm-perlprov >= 4.1-13
Requires:	apache-mod_perl
BuildArch:	noarch
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%description
Apache::SimpleTemplate is *another* Template-with-embedded-Perl
package for mod_perl. It allows you to embed blocks of Perl code into
text documents, such as HTML files, and have this code executed upon
HTTP request. It should take moments to set-up and learn; very little
knowledge of mod_perl is necessary.

%description -l pl.UTF-8
Apache::SimpleTemplate to jeszcze jeden pakiet szablonów z wbudowanym
Perlem dla mod_perla. Pozwala na osadzanie bloków kodu Perla w
dokumentach tekstowych, takich jak pliki HTML, oraz uruchamianie tego
kodu przy żądaniach HTTP. Powinna wystarczyć chwila na uruchomienie i
naukę; wymagana jest bardzo mała znajomość mod_perla.

%prep
%setup -q -n %{pdir}-%{pnam}-%{version}

%build
%{__perl} Makefile.PL \
	INSTALLDIRS=vendor
%{__make}

%{?with_tests:%{__make} test}

%install
rm -rf $RPM_BUILD_ROOT

%{__make} install \
	DESTDIR=$RPM_BUILD_ROOT

%clean
rm -rf $RPM_BUILD_ROOT

%files
%defattr(644,root,root,755)
%doc README
%{perl_vendorlib}/%{pdir}/*.pm
%{_mandir}/man3/*
