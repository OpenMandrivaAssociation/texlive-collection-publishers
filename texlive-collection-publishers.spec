# revision 34295
# category Collection
# catalog-ctan undef
# catalog-date undef
# catalog-license undef
# catalog-version undef
Name:		texlive-collection-publishers
Epoch:		1
Version:	20140621
Release:	3
Summary:	Publisher styles, theses, etc
Group:		Publishing
URL:		http://tug.org/texlive
License:	http://www.tug.org/texlive/LICENSE.TL
Source0:	http://mirrors.ctan.org/systems/texlive/tlnet/archive/collection-publishers.tar.xz
BuildArch:	noarch
BuildRequires:	texlive-tlpkg
Requires(pre):	texlive-tlpkg
Requires:	texlive-collection-latex
Requires:	texlive-IEEEconf
Requires:	texlive-IEEEtran
Requires:	texlive-aastex
Requires:	texlive-abntex2
Requires:	texlive-acmconf
Requires:	texlive-active-conf
Requires:	texlive-adfathesis
Requires:	texlive-afthesis
Requires:	texlive-aguplus
Requires:	texlive-aiaa
Requires:	texlive-ametsoc
Requires:	texlive-anufinalexam
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
Requires:	texlive-brandeis-dissertation
Requires:	texlive-cascadilla
Requires:	texlive-chem-journal
Requires:	texlive-classicthesis
Requires:	texlive-cmpj
Requires:	texlive-confproc
Requires:	texlive-dccpaper
Requires:	texlive-dithesis
Requires:	texlive-ebook
Requires:	texlive-ebsthesis
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
Requires:	texlive-imtekda
Requires:	texlive-jmlr
Requires:	texlive-jpsj
Requires:	texlive-kdgdocs
Requires:	texlive-kluwer
Requires:	texlive-lps
Requires:	texlive-matc3
Requires:	texlive-matc3mem
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
Requires:	texlive-pittetd
Requires:	texlive-pkuthss
Requires:	texlive-powerdot-FUBerlin
Requires:	texlive-pracjourn
Requires:	texlive-procIAGssymp
Requires:	texlive-proposal
Requires:	texlive-ptptex
Requires:	texlive-psu-thesis
Requires:	texlive-resphilosophica
Requires:	texlive-resumecls
Requires:	texlive-revtex
Requires:	texlive-revtex4
Requires:	texlive-ryethesis
Requires:	texlive-sageep
Requires:	texlive-sapthesis
Requires:	texlive-scrjrnl
Requires:	texlive-schule
Requires:	texlive-seuthesis
Requires:	texlive-soton
Requires:	texlive-spie
Requires:	texlive-sr-vorl
Requires:	texlive-stellenbosch
Requires:	texlive-suftesi
Requires:	texlive-sugconf
Requires:	texlive-tabriz-thesis
Requires:	texlive-texilikechaps
Requires:	texlive-texilikecover
Requires:	texlive-thesis-ekf
Requires:	texlive-thesis-titlepage-fhac
Requires:	texlive-thuthesis
Requires:	texlive-toptesi
Requires:	texlive-tudscr
Requires:	texlive-tugboat
Requires:	texlive-tugboat-plain
Requires:	texlive-tui
Requires:	texlive-uaclasses
Requires:	texlive-uadocs
Requires:	texlive-uafthesis
Requires:	texlive-ucbthesis
Requires:	texlive-ucdavisthesis
Requires:	texlive-ucthesis
Requires:	texlive-uestcthesis
Requires:	texlive-uiucredborder
Requires:	texlive-uiucthesis
Requires:	texlive-ulthese
Requires:	texlive-umthesis
Requires:	texlive-umich-thesis
Requires:	texlive-unamth-template
Requires:	texlive-unamthesis
Requires:	texlive-unswcover
Requires:	texlive-ut-thesis
Requires:	texlive-uothesis
Requires:	texlive-uowthesis
Requires:	texlive-uowthesistitlepage
Requires:	texlive-uspatent
Requires:	texlive-uwthesis
Requires:	texlive-vancouver
Requires:	texlive-wsemclassic
Requires:	texlive-xcookybooky
Requires:	texlive-york-thesis

%description
TeXLive collection-publishers package.

#-----------------------------------------------------------------------
%files

#-----------------------------------------------------------------------
%prep
%setup -c -a0

%build

%install
