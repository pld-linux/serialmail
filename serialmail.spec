Summary:	serialmail
Summary(pl):	erialmail
Name:		serialmail
Version:	0.75
Release:	1
Group:		Networking/Daemons
Group(pl):	Seciowe/Serwery
Copyright:	GPL
URL:		http://www.qmail.org
Source:		%{name}-%{version}.tar.gz
BuildRoot:	/tmp/%{name}-%{version}-root
Requires:	ucspi-tcp

%description
Qmail Mail Transfer Agent - Serial Mail Delivery Utilities

%description -l pl
Qmail Mail Transfer Agent - Narzêdzie do dostarczenia poczty

%prep
%setup -q
echo gcc $RPM_OPT_FLAGS >conf-cc
echo /usr >conf-home

%build
make 

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

gzip -9nf {AUTOTURN,BLURB,CHANGES,README,THANKS,TODO,TOISP,$RPM_BUILD_ROOT%{_mandir}/man1/*.1}

%clean
rm -rf $RPM_BUILD_ROOT

%files
%defattr(644,root,root,755)
%doc {AUTOTURN,BLURB,CHANGES,README,THANKS,TODO,TOISP}.gz
%{_mandir}/man1/*
%attr(755,root,root) %{_bindir}/*
