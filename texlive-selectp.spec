# revision 20185
# category Package
# catalog-ctan /macros/latex/contrib/selectp
# catalog-date 2010-10-24 16:23:58 +0200
# catalog-license pd
# catalog-version 1.0
Name:		texlive-selectp
Version:	1.0
Release:	4
Summary:	Select pages to be output
Group:		Publishing
URL:		http://www.ctan.org/tex-archive/macros/latex/contrib/selectp
License:	PD
Source0:	http://mirrors.ctan.org/systems/texlive/tlnet/archive/selectp.tar.xz
Source1:	http://mirrors.ctan.org/systems/texlive/tlnet/archive/selectp.doc.tar.xz
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
%setup -c -a0 -a1

%build

%install
mkdir -p %{buildroot}%{_texmfdistdir}
cp -fpar tex doc %{buildroot}%{_texmfdistdir}


%changelog
* Wed Jan 04 2012 Paulo Andrade <pcpa@mandriva.com.br> 1.0-2
+ Revision: 755903
- Rebuild to reduce used resources

* Sat Nov 05 2011 Paulo Andrade <pcpa@mandriva.com.br> 1.0-1
+ Revision: 719501
- texlive-selectp
- texlive-selectp
- texlive-selectp
- texlive-selectp

