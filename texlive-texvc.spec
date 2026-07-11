%global tl_name texvc
%global tl_revision 76874

Name:		texlive-%{tl_name}
Epoch:		1
Version:	1.3
Release:	%{tl_revision}.1
Summary:	Use MediaWiki LaTeX commands
Group:		Publishing
URL:		https://www.ctan.org/tex-archive/macros/latex/contrib/texvc
License:	lppl1.3
Source0:	https://mirrors.ctan.org/systems/texlive/tlnet/archive/texvc.r%{tl_revision}.tar.xz
Source1:	https://mirrors.ctan.org/systems/texlive/tlnet/archive/texvc.doc.r%{tl_revision}.tar.xz
Source2:	https://mirrors.ctan.org/systems/texlive/tlnet/archive/texvc.source.r%{tl_revision}.tar.xz
BuildArch:	noarch
BuildSystem:	texlive
Provides:	texlive(%{tl_name}) = %{tl_revision}

%description
User MediaWiki LaTeX commands to copy and past formulae from MediaWiki
to LaTeX documents.

