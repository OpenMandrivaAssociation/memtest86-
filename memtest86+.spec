# Debug package is empty and rpmlint rejects build
%define _enable_debug_packages %{nil}
%define debug_package %{nil}

Summary:	A stand alone memory test for i386 architecture systems
Name:		memtest86+
Version:	5.01
Release:	4
License:	GPLv2
Group:		System/Kernel and hardware
Url:		http://www.memtest.org
Source0:	http://www.memtest.org/download/%{version}/%{name}-%{version}.tar.gz
Source1:	%{name}.rpmlintrc
Patch1:		memtest86+-5.01-makefile_clean.patch
Patch2:		memtest86+-5.01-O0.patch
Patch3:		memtest86+-5.01-io.patch
Patch4:		memtest86+-5.01-array-size-fix.patch
BuildRequires:	dev86
Requires:	initscripts
Requires:	drakxtools-backend
Requires(post,preun):	drakxtools-backend

ExclusiveArch:	%{ix86} x86_64
%rename		memtest86

%description
Memtest86 is thorough, stand alone memory test for i386 architecture
systems. BIOS based memory tests are only a quick check and often
missfailures that are detected by Memtest86.

%prep
%setup -q 
%apply_patches

%build
make LD=/usr/bin/ld.bfd

%install
install -m644 memtest.bin -D %{buildroot}/boot/memtest.bin

%files
%doc FAQ
/boot/memtest.bin


