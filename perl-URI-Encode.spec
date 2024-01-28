%define module URI-Encode
%undefine _debugsource_packages

Name:		perl-%{module}
Version:	1.1.1
Release:	1
Summary:	Perl module for URI encoding
URL:		https://metacpan.org/pod/URI::Encode
Source:		https://cpan.org/modules/by-module/URI/%{module}-v%{version}.tar.gz
License:	Perl (Artistic or GPL)
Group:		Development/Perl
BuildRequires:	perl
BuildRequires:	perl(ExtUtils::MakeMaker)
BuildArch:	noarch

%description
This modules provides simple URI (Percent) encoding/decoding

The main purpose of this module (at least for me) was to provide an easy method
to encode strings (mainly URLs) into a format which can be pasted into a plain
text emails, and that those links are 'click-able' by the person reading that
email. This can be accomplished by NOT encoding the reserved characters.

This module can also be useful when using HTTP::Tiny to ensure the URLs are properly escaped.

%prep
%autosetup -p1 -n %{module}-v%{version}
perl Makefile.PL INSTALLDIRS=vendor

%build
%make_build

%check
make test

%install
%make_install INSTALLDIRS=vendor

%files
%doc Changes MANIFEST README
%{perl_vendorlib}/*/*
%{_mandir}/man3/*.3pm*
