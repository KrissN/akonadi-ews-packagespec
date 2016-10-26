%global framework kcoreaddons

Summary:            Microsoft Exchange resource for Akonadi using the Exchange Web Services (EWS) protocol
Name:               akonadi-ews
Version:            0.8.1
Release:            1%{?dist}
License:            GPLv2+
Group:              Applications/Productivity
Source:             %{name}-%{version}.tar.xz
URL:                https://github.com/KrissN/akonadi-ews
BuildRequires:      cmake
BuildRequires:      gcc-c++
BuildRequires:      extra-cmake-modules
BuildRequires:      kf5-kio-devel
%if 0%{?fedora} <= 23
BuildRequires:      kf5-akonadi-devel
%else
BuildRequires:      kf5-akonadi-server-devel
%endif
BuildRequires:      kf5-akonadi-mime-devel
BuildRequires:      libxslt
BuildRequires:      kf5-kmime-devel
BuildRequires:      kf5-kcalendarcore-devel
BuildRequires:      kf5-kcontacts-devel
BuildRequires:      kf5-kcodecs-devel
BuildRequires:      kf5-kdelibs4support-devel
BuildRequires:      kf5-kwallet-devel
BuildRequires:      kf5-kwidgetsaddons-devel
Requires:           kf5-kio >= 5.19


%description
The Microsoft Exchange (EWS) Akonadi resource allows to use Microsoft Exchange accounts with
the KDE PIM suite including e-mail sending and retrieval and calendar access.

%prep
%autosetup -n %{name}-%{version}

%build
mkdir -p %{_target_platform}
pushd %{_target_platform}
%{cmake_kf5} ..
popd

make %{?_smp_mflags} -C %{_target_platform}

%install
%make_install -C %{_target_platform}

#%find_lang akonadi-ews --with-qt --all-name

%files
%{_kf5_bindir}/akonadi_ews_resource
%{_kf5_bindir}/akonadi_ewsmta_resource
%{_kf5_datadir}/akonadi/agents/*.desktop
%{_kf5_datadir}/icons/*

%changelog
* Sat Apr 30 2016 Krzysztof Nowicki <krissn@op.pl> - 0.8.0-1
- Version 0.8.1

* Sat Apr 30 2016 Krzysztof Nowicki <krissn@op.pl> - 0.8.0-1
- Initial version

