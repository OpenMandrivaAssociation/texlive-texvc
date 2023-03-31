Name:		texlive-texvc
Version:	46844
Release:	2
Summary:	Use MediaWiki LaTeX commands
Group:		Publishing
URL:		http://www.ctan.org/tex-archive/macros/latex/contrib/texvc
License:	lppl1.3
Source0:	http://mirrors.ctan.org/systems/texlive/tlnet/archive/texvc.r%{version}.tar.xz
Source1:	http://mirrors.ctan.org/systems/texlive/tlnet/archive/texvc.doc.r%{version}.tar.xz
Source2:	http://mirrors.ctan.org/systems/texlive/tlnet/archive/texvc.source.r%{version}.tar.xz
BuildArch:	noarch
BuildRequires:	texlive-tlpkg
Requires(pre):	texlive-tlpkg
Requires(post):	texlive-kpathsea

%description
User MediaWiki LaTeX commands to copy and past formulae from
MediaWiki to LaTeX documents.

%prep
%setup -c -a1 -a2
%autopatch -p1

%build

%install
rm -rf tlpkg
mkdir -p %{buildroot}%{_texmfdistdir}
cp -a * %{buildroot}%{_texmfdistdir}

%files
%doc %{_texmfdistdir}/source/latex/texvc
%{_texmfdistdir}/tex/latex/texvc
%doc %{_texmfdistdir}/doc/latex/texvc

%post -p %{_sbindir}/texlive.post

%postun
[ "$1" -eq 0 ] && %{_sbindir}/texlive.post
