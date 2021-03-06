%define module	pyface
%define name	python-%{module}
%define version	4.2.0
%define	rel		1
%if %mdkversion < 201100
%define release %mkrel %{rel}
%else
%define release	%{rel}
%endif

Summary:	Enthought Tool Suite - traits-capable windowing framework
Name:		%{name}
Version:	4.3.0
Release:	2
Source0:	https://www.enthought.com/repo/ets/pyface-%{version}.tar.gz
License:	BSD
Group:		Development/Python
Url:		https://github.com/enthought/pyface/
BuildRoot:	%{_tmppath}/%{name}-%{version}-%{release}-buildroot
BuildArch:	noarch
Obsoletes:	python-enthought-traitsbackendwx
Obsoletes:	python-enthought-traitsbackendqt
Requires:	python-traits >= 4.2.0
Requires:	wxPython >= 2.8
Requires:	python-qt4
Requires:	pyside
BuildRequires:	python-setuptools >= 0.6c8
BuildRequires:	wxPython >= 2.8
BuildRequires:	x11-server-xvfb, procps
BuildRequires:	python-setupdocs >= 1.0.5
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
Xvfb :100 -ac &
XPID=$!
export DISPLAY=:100.0
%__python setup.py build_docs
kill -9 $XPID

%install
%__rm -rf %{buildroot}
PYTHONDONTWRITEBYTECODE= %__python setup.py install --root=%{buildroot}

%clean
%__rm -rf %{buildroot}

%files 
%defattr(-,root,root)
%doc *.txt *.rst examples/ build/docs/html
%py_sitedir/%{module}*


%changelog
* Mon Aug 13 2012 Lev Givon <lev@mandriva.org> 4.2.0-1
+ Revision: 814695
- Update to 4.2.0.

* Tue Dec 27 2011 Lev Givon <lev@mandriva.org> 4.1.0-1
+ Revision: 745692
- Update to 4.1.0.

* Thu Jul 07 2011 Lev Givon <lev@mandriva.org> 4.0.0-1
+ Revision: 689178
- import python-pyface



