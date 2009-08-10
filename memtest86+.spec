Summary:	A stand alone memory test for i386 architecture systems
Name:		memtest86+
Version:	2.11
Release:	%mkrel 1
License:	GPL
Source0:	http://www.memtest.org/download/%{version}/%{name}-%{version}.tar.bz2
URL:		http://www.memtest.org
Group:		System/Kernel and hardware
# Note! We need to build with gcc3.3 as gcc-4.* breaks the memtest patterns.
# It will build without errors, but when used, it will report faulty memory,
# even if it actually is ok! / tmb 10.8.2009
BuildRequires:	dev86 gcc3.3
Requires:	initscripts, drakxtools-backend >= 10-53mdk
BuildRoot:	%{_tmppath}/%{name}-%{version}-%{release}-buildroot
ExclusiveArch:	%{ix86} x86_64
Obsoletes:	memtest86
Provides:	memtest86
Patch0:		memtest86+-gcc3.patch

%description
Memtest86 is thorough, stand alone memory test for i386 architecture
systems.  BIOS based memory tests are only a quick check and often
missfailures that are detected by Memtest86.    

%prep
%setup -q 
%patch0 -p1

%build
%make

%install
rm -rf $RPM_BUILD_ROOT
install -m644 memtest.bin -D $RPM_BUILD_ROOT/boot/memtest.bin

%clean
rm -rf $RPM_BUILD_ROOT

%post
if [ -x /usr/sbin/bootloader-config ]; then
    /usr/sbin/bootloader-config --action add-entry --label memtest --image /boot/memtest.bin
fi

%preun
if [ -x /usr/sbin/bootloader-config ]; then
    /usr/sbin/bootloader-config --action remove-entry --label memtest
fi

%files
%defattr(-,root,root)
%doc FAQ
/boot/memtest.bin


