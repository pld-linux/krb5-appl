#
# Conditional build:
%bcond_with	selinux		# build with selinux support
%bcond_without	tests		# don't perform make check
#
%define	krb5_ver	1.10
Summary:	Kerberos V5 Applications
Summary(pl.UTF-8):	Aplikacje systemu Kerberos V5
Name:		krb5-appl
Version:	1.0.3
Release:	0.1
License:	MIT
Group:		Networking
Source0:	http://web.mit.edu/kerberos/dist/krb5-appl/1.0/%{name}-%{version}-signed.tar
# Source0-md5:	802ae5dbd783689f50ea85ccb9693cac
Source1:	klogind.inetd
Source2:	kftpd.inetd
Source3:	ktelnetd.inetd
Source4:	kshell.inetd
Source5:	kftpd.pamd
Source6:	klogin.pamd
Source7:	kshell.pamd
Patch0:		krb5-manpages.patch
Patch1:		krb5-netkit-rsh.patch
Patch2:		krb5-rlogind-environ.patch
Patch3:		krb5-passive.patch
Patch4:		krb5-size.patch
Patch5:		krb5-ftp-glob.patch
Patch6:		krb5-paths.patch
Patch7:		krb5-io.patch
Patch8:		krb5-login-lpass.patch
Patch9:		krb5-rcp-markus.patch
Patch10:	krb5-rcp-sendlarge.patch
Patch11:	krb5-telnet-environ.patch
Patch12:	krb5-tests.patch
Patch13:	krb5-ftp_fdleak.patch
Patch14:	krb5-ftp_glob_runique.patch
Patch15:	krb5-pam.patch
Patch16:	krb5-selinux-label.patch
Patch17:	krb5-trunk-ftp_mget_case.patch
URL:		http://web.mit.edu/kerberos/www/
BuildRequires:	autoconf
BuildRequires:	bison
BuildRequires:	krb5-devel >= %{krb5_ver}
BuildRequires:	ncurses-devel
BuildRequires:	pam-devel
%{?with_selinux:BuildRequires:	libselinux-devel}
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%define		_localstatedir	/var/lib/kerberos
# doesn't handle %{__cc} with spaces properly
%undefine	with_ccache
# mungles cflags
%undefine	configure_cache

%description
This package contains Kerberized versions of telnet, rlogin, rsh, rcp,
and ftp clients and daemons, as well as a terminal login program which
can obtain Kerberos credentials when presented with the user's
password.

These programs are no longer in wide use, having been supplanted in
many environments by OpenSSH, but there is still some interest in
their continued maintenance. These programs were included in the main
Kerberos 5 distribution through release 1.7, but are now packaged
separately.

%description -l pl.UTF-8
Ten pakiet zawiera skerberyzowane wersje klientów i demonów usług
telnet, rlogin, rsh, rcp i ftp, a także terminalowy program login,
wszystkie potrafiące uzyskać dane uwierzytelniające Kerberosa w
przypadku przekazania wraz z hasłem użytkownika.

Programy te nie są już w szerokim użyciu, w większości środowisk
zostały zastąpione przez OpenSSH, ale jest jeszcze trochę
zainteresowanych ich utrzymywaniem. Były dołączone do dystrybucji
głównej części Kerberosa 5 do wersji 1.7, ale obecnie są rozprowadzane
osobno.

%package -n krb5-login
Summary:	Kerberized version of login program
Summary(pl.UTF-8):	Skerberyzowana wersja programu login
Group:		Networking
Obsoletes:	heimdal-login
Conflicts:	krb5-common < 1.8

%description -n krb5-login
login is used when signing onto a system. It can also be used to
switch from one user to another at any time (most modern shells have
support for this feature built into them, however). This package
contains login.krb5 - a kerberized version of login program.

%description -n krb5-login -l pl.UTF-8
login jest używany przy logowaniu do systemu. Może być także użyty do
przełączenia z jednego użytkownika na innego w dowolnej chwili
(większość współczesnych powłok ma wbudowaną obsługę tego). Ten pakiet
zawiera program login.krb5 - skerberyzowaną wersję programu login.

%package -n krb5-rsh
Summary:	Clients for remote access commands (rsh, rcp)
Summary(pl.UTF-8):	Klienci zdalnego dostępu (rsh, rcp)
Group:		Applications/Networking
Requires:	krb5-common >= %{krb5_ver}
Obsoletes:	rcp
Obsoletes:	rsh
Obsoletes:	heimdal-rsh

%description -n krb5-rsh
The rsh package contains a set of programs which allow users to run
commands on remote machines and copy files between machines (rsh and
rcp). Both of these commands use rhosts style authentication. This
package contains the clients needed for all of these services.

%description -n krb5-rsh -l pl.UTF-8
Ten pakiet zawiera zestaw narzędzi pozwalających na wykonywanie
poleceń na zdalnych maszynach oraz kopiowanie plików pomiędzy
maszynami (rsh, rcp).

%package -n krb5-rlogin
Summary:	Kerberized remote login program
Summary(pl.UTF-8):	Skerberyzowany program do zdalnego logowania
Group:		Networking
Requires:	krb5-common >= %{krb5_ver}
Provides:	rlogin

%description -n krb5-rlogin
rlogin is a program that connects your terminal on the current local
host system to the remote host system. This package contains
kerberized version of rlogin.

%description -n krb5-rlogin -l pl.UTF-8
rlogin to program dołączający terminal systemu lokalnego do systemu na
zdalnym hoście. Ten pakiet zawiera skerberyzowaną wersję programu
rlogin.

%package -n krb5-kshd
Summary:	Kerberized remote shell server
Summary(pl.UTF-8):	Skerberyzowany serwer zdalnego dostępu
Group:		Networking/Daemons
Requires:	krb5-common >= %{krb5_ver}
Requires:	rc-inetd >= 0.8.1
Obsoletes:	rshd
Obsoletes:	heimdal-rshd

%description -n krb5-kshd
The kshd package contains kerberized remote shell server which
provides remote execution facilities with authentication based on the
Kerberos authentication system.

%description -n krb5-kshd -l pl.UTF-8
Ten pakiet zawiera skerberyzowaną wersję serwer zdalnego dostępu,
który umożliwia zdalne wykonywanie poleceń w oparciu o system
uwierzytelniania Kerberos.

%package -n krb5-klogind
Summary:	Kerberized remote login server
Summary(pl.UTF-8):	Skerberyzowany serwer zdalnego logowania
Group:		Networking/Daemons
Requires:	krb5-common >= %{krb5_ver}
Requires:	rc-inetd >= 0.8.1
Obsoletes:	rlogind

%description -n krb5-klogind
Klogind is the server for the rlogin program. The server is based on
rlogind but uses Kerberos authentication.

%description -n krb5-klogind -l pl.UTF-8
Klogind jest serwerem dla programu rlogin. Oparty jest na rlogind ale
wykorzystuje system uwierzytelniania Kerberos.

%package -n krb5-ftp
Summary:	Kerberized UNIX FTP (file transfer protocol) client
Summary(pl.UTF-8):	Skerberyzowany klient protokołu FTP
Group:		Networking
Requires:	krb5-common >= %{krb5_ver}
Obsoletes:	heimdal-ftp

%description -n krb5-ftp
The ftp package provides the standard UNIX command-line FTP client
with kerberos authentication support. FTP is the file transfer
protocol, which is a widely used Internet protocol for transferring
files and for archiving files.

This package contains Kerberized version of FTP client.

%description -n krb5-ftp -l pl.UTF-8
Ten pakiet dostarcza standardowego klienta FTP z wbudowaną obsługą
kerberosa. FTP jest protokołem do przesyłania plików szeroko
rozpowszechnionym w Internecie.

Ten pakiet zawiera skerberyzowaną wersję klienta FTP.

%package -n krb5-ftpd
Summary:	Kerberized UNIX FTP (file transfer protocol) server
Summary(pl.UTF-8):	Skerberyzowana wersja serwera FTP
Group:		Networking/Daemons
Requires:	krb5-common >= %{krb5_ver}
Requires:	rc-inetd >= 0.8.1
Obsoletes:	ftpd
Obsoletes:	heimdal-ftpd

%description -n krb5-ftpd
FTP is the file transfer protocol, which is a widely used Internet
protocol for transferring files and for archiving files.

This package contains Kerberized version of FTP server.

%description -n krb5-ftpd -l pl.UTF-8
FTP jest protokołem transmisji plików szeroko rozpowszechnionym w
Internecie.

Ten pakiet zawiera skerberyzowaną wersję serwera FTP.

%package -n krb5-telnetd
Summary:	Kerberized server for the telnet remote login
Summary(pl.UTF-8):	Skerberyzowany serwer protokołu telnet
Group:		Networking/Daemons
Requires:	krb5-common >= %{krb5_ver}
Requires:	rc-inetd >= 0.8.1
Obsoletes:	telnetd
Obsoletes:	heimdal-telnetd

%description -n krb5-telnetd
Telnet is a popular protocol for remote logins across the Internet.
This package provides a kerberized telnet daemon which allows remote
logins into the machine it is running on.

%description -n krb5-telnetd -l pl.UTF-8
Telnet jest popularnym protokołem zdalnego logowania. Ten pakiet
zawiera skerberyzowany serwer pozwalający na zdalne logowanie się
klientów na maszynę na której działa.

%package -n krb5-telnet
Summary:	Kerberized client for the telnet remote login
Summary(pl.UTF-8):	Skerberyzowany klient usługi telnet
Group:		Networking
Requires:	krb5-common >= %{krb5_ver}
Obsoletes:	telnet
Obsoletes:	heimdal-telnet

%description -n krb5-telnet
Telnet is a popular protocol for remote logins across the Internet.
This package provides kerberized command line telnet client.

%description -n krb5-telnet -l pl.UTF-8
Telnet jest popularnym protokołem zdalnego logowania. Ten pakiet
zawiera skerberyzowanego klienta tej usługi.

%prep
%setup -q -c
tar xf %{name}-%{version}.tar.gz
mv %{name}-%{version}/* .
%patch -P0 -p1
%patch -P1 -p1
%patch -P2 -p1
%patch -P3 -p1
%patch -P4 -p1
%patch -P5 -p1
%patch -P6 -p1
%patch -P7 -p1
%patch -P8 -p1
%patch -P9 -p1
%patch -P10 -p1
%patch -P11 -p1
%patch -P12 -p1
%patch -P13 -p1
%patch -P14 -p1
%patch -P15 -p1
%{?with_selinux:%patch16 -p1}
%patch -P17 -p1

%build
# Get LFS support on systems that need additional flags.
LFS_CFLAGS="$(getconf LFS_CFLAGS)"
CFLAGS="%{rpmcflags} $LFS_CFLAGS -I%{_includedir}/ncurses"
CPPFLAGS="$LFS_CFLAGS -I%{_includedir}/ncurses"

%{__autoconf}
%{__autoheader}
%configure \
	%{?with_selinux:--with-selinux}

%{__make}

%{?with_tests:%{__make} -j1 check SKIP_NET_TESTS=1}

%install
rm -rf $RPM_BUILD_ROOT
install -d $RPM_BUILD_ROOT{%{_sysconfdir},%{_localstatedir},/var/log/kerberos} \
	$RPM_BUILD_ROOT{%{_infodir},%{_mandir}} \
	$RPM_BUILD_ROOT/etc/{pam.d,rc.d/init.d,sysconfig/rc-inetd,shrc.d,logrotate.d}

%{__make} install \
	DESTDIR=$RPM_BUILD_ROOT

install %{SOURCE1} $RPM_BUILD_ROOT/etc/sysconfig/rc-inetd/klogind
install %{SOURCE2} $RPM_BUILD_ROOT/etc/sysconfig/rc-inetd/ftpd
install %{SOURCE3} $RPM_BUILD_ROOT/etc/sysconfig/rc-inetd/telnetd
install %{SOURCE4} $RPM_BUILD_ROOT/etc/sysconfig/rc-inetd/kshd

install %{SOURCE5} $RPM_BUILD_ROOT/etc/pam.d/kftpd
install %{SOURCE6} $RPM_BUILD_ROOT/etc/pam.d/klogin
install %{SOURCE7} $RPM_BUILD_ROOT/etc/pam.d/kshell

%clean
rm -rf $RPM_BUILD_ROOT

%post -n krb5-kshd
%service -q rc-inetd reload

%postun -n krb5-kshd
if [ "$1" = 0 ]; then
	%service -q rc-inetd reload
fi

%post -n krb5-klogind
%service -q rc-inetd reload

%postun -n krb5-klogind
if [ "$1" = 0 ]; then
	%service -q rc-inetd reload
fi

%post -n krb5-ftpd
%service -q rc-inetd reload

%postun -n krb5-ftpd
if [ "$1" = 0 ]; then
	%service -q rc-inetd reload
fi

%post -n krb5-telnetd
%service -q rc-inetd reload

%postun -n krb5-telnetd
if [ "$1" = 0 ]; then
	%service -q rc-inetd reload
fi

%files -n krb5-login
%defattr(644,root,root,755)
%doc NOTICE README
%attr(755,root,root) %{_sbindir}/login.krb5
%{_mandir}/man8/login.krb5.8*

%files -n krb5-rsh
%defattr(644,root,root,755)
%doc NOTICE README
%attr(755,root,root) %{_bindir}/rcp
%attr(755,root,root) %{_bindir}/rsh
%{_mandir}/man1/rsh.1*
%{_mandir}/man1/rcp.1*

%files -n krb5-rlogin
%defattr(644,root,root,755)
%doc NOTICE README
%attr(755,root,root) %{_bindir}/rlogin
%{_mandir}/man1/rlogin.1*

%files -n krb5-kshd
%defattr(644,root,root,755)
%doc NOTICE README
%attr(755,root,root) %{_sbindir}/kshd
%attr(640,root,root) %config(noreplace) %verify(not md5 mtime size) /etc/sysconfig/rc-inetd/kshd
%attr(640,root,root) %config(noreplace) %verify(not md5 mtime size) /etc/pam.d/kshell
%{_mandir}/man8/kshd.8*

%files -n krb5-klogind
%defattr(644,root,root,755)
%doc NOTICE README
%attr(755,root,root) %{_sbindir}/klogind
%attr(640,root,root) %config(noreplace) %verify(not md5 mtime size) /etc/sysconfig/rc-inetd/klogind
%attr(640,root,root) %config(noreplace) %verify(not md5 mtime size) /etc/pam.d/klogin
%{_mandir}/man8/klogind.8*

%files -n krb5-ftp
%defattr(644,root,root,755)
%doc NOTICE README gssftp/README.gssftp
%attr(755,root,root) %{_bindir}/ftp
%{_mandir}/man1/ftp.1*

%files -n krb5-ftpd
%defattr(644,root,root,755)
%doc NOTICE README gssftp/README.gssftp
%attr(755,root,root) %{_sbindir}/ftpd
%attr(640,root,root) %config(noreplace) %verify(not md5 mtime size) /etc/sysconfig/rc-inetd/ftpd
%attr(640,root,root) %config(noreplace) %verify(not md5 mtime size) /etc/pam.d/kftpd
%{_mandir}/man8/ftpd.8*

%files -n krb5-telnet
%defattr(644,root,root,755)
%doc NOTICE README
%attr(755,root,root) %{_bindir}/telnet
%{_mandir}/man1/telnet.1*

%files -n krb5-telnetd
%defattr(644,root,root,755)
%doc NOTICE README
%attr(755,root,root) %{_sbindir}/telnetd
%attr(640,root,root) %config(noreplace) %verify(not md5 mtime size) /etc/sysconfig/rc-inetd/telnetd
%{_mandir}/man8/telnetd.8*
