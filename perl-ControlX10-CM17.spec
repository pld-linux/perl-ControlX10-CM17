#
# Conditional build:
%bcond_without	tests		# do not perform "make test"
#
%include	/usr/lib/rpm/macros.perl
%define	pdir	ControlX10
%define	pnam	CM17
Summary:	ControlX10::CM17 - Perl extension for 'FireCracker' RF Transmitter
Summary(pl.UTF-8):	ControlX10::CM17 - rozszerzenie Perla dla nadajnika radiowego 'FireCracker'
Name:		perl-ControlX10-CM17
Version:	0.07
Release:	1
License:	GPL v1+ or Artistic
Group:		Development/Languages/Perl
Source0:	http://search.cpan.org/CPAN/authors/id/B/BB/BBIRTH/%{pdir}-%{pnam}-%{version}.tar.gz
# Source0-md5:  edf927ad1b5ca9a7df18ca67a7f77afd
URL:		http://search.cpan.org/dist/ControlX10-CM17/
BuildRequires:	perl-devel >= 1:5.8.0
BuildRequires:	rpm-perlprov >= 4.1-13
BuildArch:	noarch
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%description
The FireCracker (CM17A) is a send-only X10 controller that connects to
a serial port and transmits commands via RF to X10 transceivers.

The FireCracker derives its power supply from either the RTS or DTR
signals from the serial port. At least one of these signals must be
high at all times to ensure that power is not lost from the
FireCracker. The signals are pulsed to transmit a bit (DTR for '1' and
RTS for '0'). The normal rx/tx read/write lines are not used by the
device - but are passed through to allow another serial device to be
connected (as long as it does not require hardware handshaking).

%description -l pl.UTF-8
Pakiet ten jest rozszerzeniem Perla dla nadajnika radiowego
'FireCracker'

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

install -d $RPM_BUILD_ROOT%{_examplesdir}/%{name}-%{version}
cp -a eg $RPM_BUILD_ROOT%{_examplesdir}/%{name}-%{version}

%clean
rm -rf $RPM_BUILD_ROOT

%files
%defattr(644,root,root,755)
%doc Changes README README.txt
%{perl_vendorlib}/ControlX10/*.pm
%{_mandir}/man3/*
%{_examplesdir}/%{name}-%{version}
