# revision 27331
# category Collection
# catalog-ctan undef
# catalog-date undef
# catalog-license undef
# catalog-version undef
Name:		texlive-collection-publishers
Epoch:		1
Version:	20120810
Release:	4
Summary:	Support for publishers, theses, standards, conferences, etc
Group:		Publishing
URL:		http://tug.org/texlive
License:	http://www.tug.org/texlive/LICENSE.TL
Source0:	http://mirrors.ctan.org/systems/texlive/tlnet/archive/collection-publishers.tar.xz
BuildArch:	noarch
BuildRequires:	texlive-tlpkg
Requires(pre):	texlive-tlpkg
Requires:	texlive-IEEEconf
Requires:	texlive-IEEEtran
Requires:	texlive-aastex
Requires:	texlive-acmconf
Requires:	texlive-active-conf
Requires:	texlive-adfathesis
Requires:	texlive-afthesis
Requires:	texlive-aguplus
Requires:	texlive-aiaa
Requires:	texlive-ametsoc
Requires:	texlive-ANUfinalexam
Requires:	texlive-aomart
Requires:	texlive-apa
Requires:	texlive-apa6
Requires:	texlive-apa6e
Requires:	texlive-arsclassica
Requires:	texlive-articleingud
Requires:	texlive-asaetr
Requires:	texlive-ascelike
Requires:	texlive-beamer-FUBerlin
Requires:	texlive-bgteubner
Requires:	texlive-cascadilla
Requires:	texlive-chem-journal
Requires:	texlive-classicthesis
Requires:	texlive-cmpj
Requires:	texlive-confproc
Requires:	texlive-ebsthesis
Requires:	texlive-economic
Requires:	texlive-ejpecp
Requires:	texlive-elbioimp
Requires:	texlive-elsarticle
Requires:	texlive-elteikthesis
Requires:	texlive-erdc
Requires:	texlive-estcpmm
Requires:	texlive-fbithesis
Requires:	texlive-fcltxdoc
Requires:	texlive-gaceta
Requires:	texlive-gatech-thesis
Requires:	texlive-har2nat
Requires:	texlive-hobete
Requires:	texlive-icsv
Requires:	texlive-ieeepes
Requires:	texlive-ijmart
Requires:	texlive-imac
Requires:	texlive-imsproc
Requires:	texlive-imtekda
Requires:	texlive-jmlr
Requires:	texlive-jpsj
Requires:	texlive-kdgdocs
Requires:	texlive-kluwer
Requires:	texlive-lps
Requires:	texlive-macqassign
Requires:	texlive-mentis
Requires:	texlive-msu-thesis
Requires:	texlive-musuos
Requires:	texlive-muthesis
Requires:	texlive-nature
Requires:	texlive-nddiss
Requires:	texlive-nih
Requires:	texlive-nostarch
Requires:	texlive-nrc
Requires:	texlive-onrannual
Requires:	texlive-opteng
Requires:	texlive-philosophersimprint
Requires:	texlive-powerdot-FUBerlin
Requires:	texlive-pracjourn
Requires:	texlive-procIAGssymp
Requires:	texlive-ptptex
Requires:	texlive-psu-thesis
Requires:	texlive-revtex
Requires:	texlive-revtex4
Requires:	texlive-ryethesis
Requires:	texlive-sageep
Requires:	texlive-sapthesis
Requires:	texlive-seuthesis
Requires:	texlive-soton
Requires:	texlive-spie
Requires:	texlive-stellenbosch
Requires:	texlive-suftesi
Requires:	texlive-sugconf
Requires:	texlive-texilikechaps
Requires:	texlive-texilikecover
Requires:	texlive-thesis-titlepage-fhac
Requires:	texlive-thuthesis
Requires:	texlive-toptesi
Requires:	texlive-tugboat
Requires:	texlive-tugboat-plain
Requires:	texlive-tui
Requires:	texlive-uaclasses
Requires:	texlive-uafthesis
Requires:	texlive-ucdavisthesis
Requires:	texlive-ucthesis
Requires:	texlive-uiucthesis
Requires:	texlive-umthesis
Requires:	texlive-umich-thesis
Requires:	texlive-unamthesis
Requires:	texlive-ut-thesis
Requires:	texlive-uothesis
Requires:	texlive-uowthesis
Requires:	texlive-uwthesis
Requires:	texlive-vancouver
Requires:	texlive-york-thesis
Requires:	texlive-collection-latex

%description
TeXLive collection-publishers package.

#-----------------------------------------------------------------------
%files

#-----------------------------------------------------------------------
%prep
%setup -c -a0

%build

%install


%changelog
* Fri Aug 10 2012 Paulo Andrade <pcpa@mandriva.com.br> 1:20120810-1
+ Revision: 813982
- Update to latest release.

* Sat Apr 14 2012 Paulo Andrade <pcpa@mandriva.com.br> 1:20120413-1
+ Revision: 790894
- Update to latest release.

* Tue Mar 27 2012 Paulo Andrade <pcpa@mandriva.com.br> 1:20120327-1
+ Revision: 787866
- Update to latest release.

* Fri Feb 24 2012 Paulo Andrade <pcpa@mandriva.com.br> 1:20120224-1
+ Revision: 780509
- Update to latest release.
- Import texlive-collection-publishers
- Import texlive-collection-publishers

