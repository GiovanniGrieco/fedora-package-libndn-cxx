%define commit d776a93c9ca8940553e601bb7000d15c26ac02a8
%define commit_short d776a93
%define __version 0.7.0
%define date 20200325

Name:       libndn-cxx
Version:    %{__version}.%{date}+%{commit_short}
Release:    1%{?dist}
Summary:    C++ library implementing Named Data Networking primitives
License:    LGPLv3+ and (BSD or LGPLv3+) and (GPLv3+ or LGPLv3+)
URL:        http://named-data.net
Source0:    https://github.com/named-data/ndn-cxx/archive/%{commit}.tar.gz

BuildRequires:  sqlite-devel 
BuildRequires:  cryptopp-devel 
BuildRequires:  boost-devel 
BuildRequires:  pkgconfig 
BuildRequires:  openssl-devel
BuildRequires:  boost-python3-devel 
BuildRequires:  python3-devel 
BuildRequires:  gcc-c++

%description
libndn-cxx is a C++ library that implements NDN primitives.

%package  devel
Summary:  Development files for %{name}
Requires: %{name}%{?_isa} = %{version}-%{release}

%description    devel
The %{name}-devel package contains libraries and header files for
developing applications that use %{name}.

%prep
%setup -qn ndn-cxx-%{commit}


%build
CXXFLAGS="%{optflags}" \
LINKFLAGS="-Wl,--as-needed" \
./waf \
	--enable-shared \
	--disable-static \
	--prefix=%{_prefix} \
	--bindir=%{_bindir} \
	--libdir=%{_libdir} \
	--datadir=%{_datadir} \
	--sysconfdir=%{_sysconfdir} \
	--with-examples \
	configure

./waf -v %{?_smp_mflags}

%install
./waf install \
	--destdir=%{buildroot} \
	--prefix=%{_prefix} \
	--bindir=%{_bindir} \
	--libdir=%{_libdir}

%check
export LD_LIBRARY_PATH=$PWD/build
#build/unit-tests

%ldconfig_scriptlets

%files
%{_libdir}/libndn-cxx.so.%{__version}
%doc AUTHORS.md  README-dev.md  README.md
%dir %{_sysconfdir}/ndn
%license COPYING.md
%{_bindir}/*
%config(noreplace) %{_sysconfdir}/ndn/client.conf.sample

%files devel
%{_includedir}/ndn-cxx/
%{_libdir}/libndn-cxx.so
%{_libdir}/pkgconfig/libndn-cxx.pc

