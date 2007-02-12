# TODO
# - check license
Summary:	Qmail Mail Transfer Agent - Serial Mail Delivery Utilities
Summary(pl.UTF-8):   Qmail Mail Transfer Agent - Narzędzie do dostarczenia poczty
Name:		serialmail
Version:	0.75
Release:	1
License:	ASIS
Group:		Networking/Daemons
Source0:	http://cr.yp.to/software/%{name}-%{version}.tar.gz
# Source0-md5:	e6a3049863ae8577b1780fcd9fbc98a9
Patch0:		serialmail-errno.patch
URL:		http://cr.yp.to/serialmail.html
Requires:	ucspi-tcp
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%description
serialmail is a collection of tools for passing mail across serial
links. It works with qmail: you use qmail to deliver messages to a
maildir, and then serialmail to deliver messages out of the maildir.

serialmail supports SMTP, including ESMTP PIPELINING, and QMTP.

%description -l pl.UTF-8
serialmail to zestaw narzędzi do przekazywania poczty po łączach
szeregowych. Działa z qmailem - qmaila używa się do dostarczania
wiadomości do maildirów, a następnie serialmaila do dostarczania
wiadomości z maildirów.

%prep
%setup -q
%patch0 -p1
echo "%{__cc} %{rpmcflags}" > conf-cc
echo "%{_prefix}" > conf-home

%build
%{__make}

%install
rm -rf $RPM_BUILD_ROOT

install -d $RPM_BUILD_ROOT{%{_bindir},%{_mandir}/man1}

install maildirqmtp				$RPM_BUILD_ROOT%{_bindir}
install maildirsmtp				$RPM_BUILD_ROOT%{_bindir}
install maildirserial				$RPM_BUILD_ROOT%{_bindir}
install serialqmtp				$RPM_BUILD_ROOT%{_bindir}
install serialsmtp				$RPM_BUILD_ROOT%{_bindir}
install setlock					$RPM_BUILD_ROOT%{_bindir}
install *.1					$RPM_BUILD_ROOT%{_mandir}/man1

%clean
rm -rf $RPM_BUILD_ROOT

%files
%defattr(644,root,root,755)
%doc AUTOTURN BLURB CHANGES README THANKS TODO TOISP
%attr(755,root,root) %{_bindir}/*
%{_mandir}/man1/*
