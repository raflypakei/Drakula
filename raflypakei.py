!/data/data/com.termux/files/usr/bin/bash
# Auto Install Tools Hack Facebook V3
# coded By Raflypakei

clear

blue='\e[0;34'
cyan='\e[0;36m'
green='\e[0;34m'
okegreen='\033[92m'
lightgreen='\e[1;32m'
white='\e[1;37m'
red='\e[1;31m'
yellow='\e[1;33m'

###################################################
# CTRL C
###################################################
trap ctrl_c INT
ctrl_c() {
clear
echo -e $red" GOOD BYE "
sleep 1
echo ""
echo -e $green" SILAHKAN SUBSCRIBE CHANEL SAYA DULU Rafly Pake i"
sleep 1
echo ""
echo -e $yellow" yang gak subscribe semoga cepat mati "
read enter
exit
}
os.system('xdg-open http://www.youtube.com/c/raflypakei2002')
				menu()

echo -e $red" >>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>"
echo -e $red" ??" $yellow" Code"        ? ?$red":" $lightgreen"Raflypakei"$red">>>>>>>>>>>>"
echo -e $red" >>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>"
echo -e $red" ??" $yellow" YT"     ?   ??$red":" $lightgreen"Rafly Pake i"$red">>"
echo -e $red" >>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>"
echo -e $red" ??" $yellow" WA 082290232340"        ?? ?$red":" $lightgreen"Banyak di Google"$red">>>>"
echo -e $red" >>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>"
echo -e $red" ??" $yellow" GitHun"         ? $red":" $lightgreen"Rafly pake i chanel"$red">>"
echo -e $red" >>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>"
echo -e $red" ??" $yellow" Versi"? ?$red":" $lightgreen"V3"$red">>>>>>>>>>>>>>>>>>"
echo -e $red" >>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>"

echo ""
echo -e $cyan" Kumpulan Tools Hack Facebook"
echo -e $red" >>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>"
echo -e $red" ??" $green" ["$lightgreen"01"$green"]"  "$yellow" INSTALL DULU BAHAN       $red"   ??"
echo -e $red" ??" $green" ["$lightgreen"02"$green"]"  "$yellow" Raflytobaga     $red"                 ??"
echo -e $red" ??" $green" ["$lightgreen"03"$green"]"  "$yellow" EXIT    $red"                 ??"
echo -e $red" >>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>"
echo -e $white""
echo -e "?>Dipilih Harga Murah"
read -p "?-»" act;

if [ $act = 01 ] || [ $act = 01 ]
then
clear
echo -e $cyan" Install Dulu Bahan BOS!! "
sleep 1
apt update -y
apt upgrade -y
pkg install python -y
pkg install python2 -y
pip2 install requests -y
pip2 install mechanize -y
pkg install php -y
echo -e $cyan" Done Install Cuk "
fi

if [ $act = 02 ] || [ $act = 02 ]
then
clear
echo -e $cyan" Langsung Ke Git Clone "
git clone https://github.com/raflypakei/raflytobaga
cd raflytobaga
python2 dkfb.raflytobaga
echo -e $cyan" Done Install Cuk "
fi

if [ $act = 03 ] || [ $act = 03 ]
then
echo -e $red" Pesan Terakhir "
sleep 1
echo -e $cyan" Kalian kagum dan bertanya – tanya. Siapa Aku Sebenarnya. Inilah Aku RAFLY PAKE I. Orang yang pernah kalian hina dimasa lalu. "
sleep 1
echo -e $green" Ketakutan memberi kecerdasan bahkan pada orang bodoh. "
sleep 1
echo -e $lightgreen" Dalam setiap bisnis selalu ada seseorang yang tahu persis apa yang sedang terjadi. Dan orang itu harus dipecat. "
sleep 1
echo -e $okegreen" Kamu Hagai Saya. Saya Hagai Kamu."
sleep 1
echo -e $yellow" Selamat Baca :) "
sleep 1
exit
fi
