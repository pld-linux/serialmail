Summary:	serialmail
Summary(pl):	serialmail
Name:		serialmail
Version:	0.75
Release:	1
License:	GPL
Group:		Networking/Daemons
Source0:	http://cr.yp.to/software/%{name}-%{version}.tar.gz
# Source0-md5:	e6a3049863ae8577b1780fcd9fbc98a9
URL:		http://www.qmail.org/
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)
Requires:	ucspi-tcp

%description
Qmail Mail Transfer Agent - Serial Mail Delivery Utilities.

%description -l pl
Qmail Mail Transfer Agent - Narzêdzie do dostarczenia poczty.

%prep
%setup -q
echo %{__cc} %{rpmcflags} >conf-cc
echo /usr >conf-home

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
%{_mandir}/man1/*
%attr(755,root,root) %{_bindir}/*
