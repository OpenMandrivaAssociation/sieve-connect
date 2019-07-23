Name:		sieve-connect
Version:	0.90
Release:	1
Summary:	A client for the ManageSieve protocol
Group:		Networking/Mail
License:	BSD
URL:		http://people.spodhuis.org/phil.pennock/software/
Source0:	http://people.spodhuis.org/phil.pennock/software/%{name}-%{version}.tar.bz2
BuildArch:	noarch
Requires:	perl
Requires:	perl-Authen-SASL
Requires:	perl-IO-Socket-INET6
Requires:	perl-IO-Socket-SSL
Requires:	perl-Net-DNS
Requires:	perl-Term-ReadKey
Suggests:	perl-Pod-Simple
Suggests:	perl-Term-ReadLine-Gnu

%description
This is sieve-connect.  A client for the ManageSieve protocol, as
specified in RFC 5804.  Historically, this was MANAGESIEVE as implemented
by timsieved in Cyrus IMAP.

sieve-connect speaks ManageSieve and supports TLS for connection privacy
and also authentication if using client certificates.  sieve-connect
will use SASL authentication; SASL integrity layers are not supported,
use TLS instead.  GSSAPI-based authentication should generally work,
provided that client and server can use a common underlaying protocol.
If it doesn't work for you, please report the issue.

sieve-connect is designed to be both a tool which can be invoked from
scripts and also a decent interactive client.  It should also be a
drop-in replacement for "sieveshell", as supplied with Cyrus IMAP.

%prep
%setup -q

%build

%install
%__install -d -m 755 %{buildroot}%{_bindir}/
%__install -d -m 755 %{buildroot}%{_mandir}/man1/
make INSTALLROOT=%{buildroot} PREFIX=%{_prefix} MANDIR=/share/man install

%files
%{_bindir}/%{name}
%{_mandir}/man1/%{name}.1*


%changelog
* Wed Mar 28 2012 Dmitry Mikhirev <dmikhirev@mandriva.org> 0.81-2
+ Revision: 787979
- fix requires

* Wed Mar 28 2012 Dmitry Mikhirev <dmikhirev@mandriva.org> 0.81-1
+ Revision: 787964
- imported package sieve-connect

