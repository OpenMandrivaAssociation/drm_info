Summary:	Small utility to dump info about DRM devices
Name:		drm_info
Version:	2.7.0
Release:	1
License:	MIT
Group:		Graphics
URL:		https://gitlab.freedesktop.org/emersion/drm_info
Source0:	%{url}/-/releases/v%{version}/downloads/%{name}-v%{version}.tar.gz
BuildRequires:	meson >= 0.49.0
BuildRequires:	pkgconfig(json-c)
BuildRequires:	pkgconfig(libdrm) >= 2.4.113
BuildRequires:	pkgconfig(libpci)
BuildRequires:	pkgconfig(scdoc)

%description
%{summary}.

%prep
%autosetup -p1

%build
%meson
%meson_build

%install
%meson_install

%files
%license LICENSE
%doc README.md
%{_bindir}/%{name}
%doc %{_mandir}/man1/%{name}.1*
