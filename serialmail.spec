Summary:     serialmail
Summary(pl): serialmail
Name:        serialmail
Version:     0.75
Release:     1
Group:       Networking/Daemons
Group(pl):   Sieciowe/Serwery
Copyright:   GPL
URL:         http://www.qmail.org
Source:      %{name}-%{version}.tar.gz
BuildRoot:   /tmp/%{name}-%{version}-root
Requires:    ucspi-tcp

%description
Qmail Mail Transfer Agent - Serial Mail Delivery Utilities

%description -l pl
Qmail Mail Transfer Agent - Narzêdzie do dostarczenia poczty

%prep
%setup -q
echo gcc $RPM_OPT_FLAGS >conf-cc
echo /var/qmail >conf-home
%build
make 

%install
rm -rf $RPM_BUILD_ROOT

install -d $RPM_BUILD_ROOT{/var/qmail/bin,%{_mandir}/man1}

install maildirqmtp				$RPM_BUILD_ROOT/var/qmail/bin
install maildirsmtp				$RPM_BUILD_ROOT/var/qmail/bin
install maildirserial				$RPM_BUILD_ROOT/var/qmail/bin
install serialqmtp				$RPM_BUILD_ROOT/var/qmail/bin
install serialsmtp				$RPM_BUILD_ROOT/var/qmail/bin
install setlock					$RPM_BUILD_ROOT/var/qmail/bin
install *.1					$RPM_BUILD_ROOT%{_mandir}/man1

gzip -9nf {AUTOTURN,BLURB,CHANGES,README,THANKS,TODO,TOISP,$RPM_BUILD_ROOT%{_mandir}/man1/*.1}

%post
%preun
%postun
%clean
rm -rf $RPM_BUILD_ROOT
%files
%defattr(644,root,root,755)
%attr(644,root,root) %{_mandir}/man1/*
%attr(755,root,root) /var/qmail/bin/*

%doc {AUTOTURN,BLURB,CHANGES,README,THANKS,TODO,TOISP}.gz
