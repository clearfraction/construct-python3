%global         abi_package %{nil}

Summary:        A powerful declarative parser/builder for binary data
Name:           construct-python3
Version:        2.9.45
Release:        1%{?dist}
License:        MIT
URL:            http://construct.readthedocs.org
Source0:        https://pypi.python.org/packages/source/c/construct/construct-%{version}.tar.gz
BuildArch:      noarch

BuildRequires:  python3-dev

%global _description\
Construct is a powerful declarative parser (and builder) for binary\
data.\
\
Instead of writing imperative code to parse a piece of data, you\
declaratively define a data structure that describes your data. As\
this data structure is not code, you can use it in one direction to\
parse data into Pythonic objects, and in the other direction, convert\
(build) objects into binary data.

%description %_description

%package     -n python3-construct
Summary:        %summary
Requires:       six-python3
%description -n python3-construct %_description

%prep
%setup -q -n construct-%{version}

%build
export http_proxy=http://127.0.0.1:9/
export https_proxy=http://127.0.0.1:9/
export no_proxy=localhost,127.0.0.1,0.0.0.0
export LANG=C.UTF-8
export SOURCE_DATE_EPOCH=1572997294
export GCC_IGNORE_WERROR=1
export CFLAGS="$CFLAGS -fno-lto "
export FCFLAGS="$CFLAGS -fno-lto "
export FFLAGS="$CFLAGS -fno-lto "
export CXXFLAGS="$CXXFLAGS -fno-lto "
export MAKEFLAGS=%{?_smp_mflags}
python3 setup.py build


%install
export http_proxy=http://127.0.0.1:9/
export https_proxy=http://127.0.0.1:9/
export no_proxy=localhost,127.0.0.1,0.0.0.0
python3 -tt setup.py build  install --root=%{buildroot}



%files
%license LICENSE
%doc README.rst
/usr/lib/python3*/*


%changelog
# based on https://koji.fedoraproject.org/koji/packageinfo?packageID=16364
