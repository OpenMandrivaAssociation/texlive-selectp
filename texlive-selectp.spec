Name:		texlive-selectp
Version:	20185
Release:	1
Summary:	Select pages to be output
Group:		Publishing
URL:		http://www.ctan.org/tex-archive/macros/latex/contrib/selectp
License:	PD
Source0:	http://mirrors.ctan.org/systems/texlive/tlnet/archive/selectp.r%{version}.tar.xz
Source1:	http://mirrors.ctan.org/systems/texlive/tlnet/archive/selectp.doc.r%{version}.tar.xz
BuildArch:	noarch
BuildRequires:	texlive-tlpkg
Requires(pre):	texlive-tlpkg
Requires(post):	texlive-kpathsea

%description
Defines a command \outputonly, whose argument is a list of
pages to be output. With the command present (before
\begin{document}), only those pages are output. This package
was inspired by code published by Knuth in TUGboat 8(2) (July
1987).

%post
%{_sbindir}/texlive.post

%postun
if [ $1 -eq 0 ]; then
	%{_sbindir}/texlive.post
fi

#-----------------------------------------------------------------------
%files
%{_texmfdistdir}/tex/latex/selectp/selectp.sty
%doc %{_texmfdistdir}/doc/latex/selectp/selectp-doc.pdf
%doc %{_texmfdistdir}/doc/latex/selectp/selectp-doc.tex

#-----------------------------------------------------------------------
%prep
%autosetup -p1 -c -a1

%build

%install
mkdir -p %{buildroot}%{_texmfdistdir}
cp -fpar tex doc %{buildroot}%{_texmfdistdir}
