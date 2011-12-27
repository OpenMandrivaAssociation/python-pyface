%define module	pyface
%define name	python-%{module}
%define version	4.1.0
%define release %mkrel 1

Summary:	Enthought Tool Suite - pyface project
Name:		%{name}
Version:	%{version}
Release:	%{release}
Source0:	http://www.enthought.com/repo/ets/%{module}-%{version}.tar.gz
License:	BSD
Group:		Development/Python
Url:		https://github.com/enthought/pyface/
BuildRoot:	%{_tmppath}/%{name}-%{version}-%{release}-buildroot
BuildArch:	noarch
Obsoletes:	python-enthought-traitsbackendwx
Obsoletes:	python-enthought-traitsbackendqt
Requires:	python-traits >= 4.1.0
Requires:	wxPython >= 2.8
Requires:	python-qt4
Requires:	pyside
BuildRequires:	python-setuptools >= 0.6c8
BuildRequires:	wxPython >= 2.8
BuildRequires:	python-sphinx

%description
The pyface project contains a toolkit-independent GUI abstraction layer,
which is used to support the "visualization" features of the Traits package.
Thus, you can write code in terms of the Traits API (views, items, editors,
etc.), and let pyface and your selected toolkit and back-end take care of
the details of displaying them.

The following GUI backends are supported:

- wxPython
- PyQt
- PySide

%prep
%setup -q -n %{module}-%{version}

%build

%__python setup.py build
pushd docs
make html
popd

%install
%__rm -rf %{buildroot}
PYTHONDONTWRITEBYTECODE= %__python setup.py install --root=%{buildroot} --record=FILE_LIST

%clean
%__rm -rf %{buildroot}

%files -f FILE_LIST
%defattr(-,root,root)
%doc *.txt *.rst examples/ docs/build/html

