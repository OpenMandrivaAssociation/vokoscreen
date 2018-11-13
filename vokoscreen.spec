%define _enable_debug_packages %{nil}
%define  debug_package %{nil}

Name:           vokoscreen
Version:        2.5.8
Release:        1
Summary:        Screencast creator
License:        GPLv2+ and BSD
Group:          Video
Url:            https://github.com/vkohaupt/vokoscreen
# Download:       https://github.com/vkohaupt/vokoscreen/archive/%{version}.tar.gz
Source0:        %{name}-master.zip
Source1:	%{name}-master.zip
BuildRequires:  desktop-file-utils
BuildRequires:  pkgconfig(alsa)
BuildRequires:  ffmpeg-devel
BuildRequires:  libv4l-devel
BuildRequires:  opencv-devel
BuildRequires:  qt5-linguist-tools
#BuildRequires:	pkgconfig(Qt5Multimedia)
BuildRequires:	pkgconfig(Qt5Test)
BuildRequires:	pkgconfig(Qt5Widgets)
#BuildRequires:	pkgconfig(Qt5X11Extras)
BuildRequires:  qt5-qttools
Requires:       alsa-utils
Requires:       mkvtoolnix
Requires:       pulseaudio-utils
Requires:       v4l-utils
Requires:       mpv

%description
vokoscreen is an easy to use screencast creator to record educational
videos, live recordings of browser, installation, videoconferences, etc.

%prep
%setup -qn %{name}-master

pushd language
tar -xvzf %{SOURCE1}
popd

# remove bundled libqxt + QtSingleApplication libraries
rm -f libqxt/*.h
rm -f QtSingleApplication/qtsingleapplication.h

%build
%qmake_qt5 "CONFIG+=LINUX_INTEGRATED" \
          "CONFIG+=release" \
        "CONFIG+=c++14"
%make


%install
make INSTALL_ROOT=%{buildroot} install
desktop-file-validate %{buildroot}%{_datadir}/applications/%{name}.desktop


%files
%doc AUTHORS COPYING CHANGE CREDITS
%{_bindir}/%{name}
%{_datadir}/applications/%{name}.desktop
%{_mandir}/man1/%{name}.1*
%{_datadir}/pixmaps/%{name}.png

%changelog
* Mon Nov 12 2018 Luthfi Emka <panahbiru@gmail.com>
- Import project from ROSA ABF to Openmandriva ABF

