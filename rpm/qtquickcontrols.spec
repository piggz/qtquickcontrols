%global qt_version 5.15.9

Name:    opt-qt5-qtquickcontrols
Summary: Qt5 - module with set of QtQuick controls
Version: 5.15.9
Release: 1%{?dist}

License: LGPL-3.0-only OR GPL-3.0-only WITH Qt-GPL-exception-1.0
Url:     http://www.qt.io
Source0: %{name}-%{version}.tar.bz2

# filter qml provides
%global __provides_exclude_from ^%{_opt_qt5_archdatadir}/qml/.*\\.so$
%{?opt_qt5_default_filter}

BuildRequires: make
BuildRequires: opt-qt5-qtbase-devel >= %{qt_version}
BuildRequires: opt-qt5-qtbase-static >= %{qt_version}
BuildRequires: opt-qt5-qtbase-private-devel
%{?_opt_qt5:Requires: %{_opt_qt5}%{?_isa} = %{_opt_qt5_version}}
BuildRequires: opt-qt5-qtdeclarative-devel
Requires: opt-qt5-qtbase-gui >= %{qt_version}
Requires: opt-qt5-qtdeclarative >= %{qt_version}

%description
The Qt Quick Controls module provides a set of controls that can be used to
build complete interfaces in Qt Quick.

%package examples
Summary: Programming examples for %{name}
Requires: %{name}%{?_isa} = %{version}-%{release}
%description examples
%{summary}.


%prep
%autosetup -n %{name}-%{version}/upstream


%build
%{opt_qmake_qt5}

%make_build

# bug in sb2 leading to 000 permission in some generated plugins.qmltypes files
chmod -R ugo+r .

%install
make install INSTALL_ROOT=%{buildroot}


%files
%license LICENSE.*
%{_opt_qt5_archdatadir}/qml/QtQuick/

%if 0%{?_qt5_examplesdir:1}
%files examples
%{_opt_qt5_examplesdir}/
%endif
