%define module	pyface

Summary:	Enthought Tool Suite - traits-capable windowing framework
Name:		python-%{module}
Version:	8.0.0
Release:	2
Source0:	https://pypi.python.org/packages/source/p/pyface/pyface-%{version}.tar.gz
License:	BSD
Group:		Development/Python
Url:		https://github.com/enthought/pyface/
BuildRoot:	%{_tmppath}/%{name}-%{version}-%{release}-buildroot
BuildArch:	noarch
Obsoletes:	python-enthought-traitsbackendwx
Obsoletes:	python-enthought-traitsbackendqt
Requires:	python-traits >= 4.2.0
BuildRequires:	python-setuptools >= 0.6c8
BuildRequires:	x11-server-xvfb, procps
BuildRequires:	python-setupdocs >= 1.0.5
BuildRequires:	python-sphinx
BuildSystem:	python

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

%files 
%defattr(-,root,root)
%doc *.txt *.rst examples/
%py_sitedir/%{module}*
