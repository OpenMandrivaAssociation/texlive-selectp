# revision 20185
# category Package
# catalog-ctan /macros/latex/contrib/selectp
# catalog-date 2010-10-24 16:23:58 +0200
# catalog-license pd
# catalog-version 1.0
Name:		texlive-selectp
Version:	1.0
Release:	1
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
Conflicts:	texlive-texmf <= 20110705-3
Conflicts:	texlive-doc <= 20110705-3

%description
Defines a command \outputonly, whose argument is a list of
pages to be output. With the command present (before
\begin{document}), only those pages are output. This package
was inspired by code published by Knuth in TUGboat 8(2) (July
1987).

%pre
    %_texmf_mktexlsr_pre

%post
    %_texmf_mktexlsr_post

%preun
    if [ $1 -eq 0 ]; then
	%_texmf_mktexlsr_pre
    fi

%postun
    if [ $1 -eq 0 ]; then
	%_texmf_mktexlsr_post
    fi

#-----------------------------------------------------------------------
%files
%{_texmfdistdir}/tex/latex/selectp/selectp.sty
%doc %{_texmfdistdir}/doc/latex/selectp/selectp-doc.pdf
%doc %{_texmfdistdir}/doc/latex/selectp/selectp-doc.tex
%doc %{_tlpkgobjdir}/*.tlpobj

#-----------------------------------------------------------------------
%prep
%setup -c -a0 -a1

%build

%install
mkdir -p %{buildroot}%{_texmfdistdir}
cp -fpar tex doc %{buildroot}%{_texmfdistdir}
mkdir -p %{buildroot}%{_tlpkgobjdir}
cp -fpa tlpkg/tlpobj/*.tlpobj %{buildroot}%{_tlpkgobjdir}
