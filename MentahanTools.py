clear 
#!/bin/bash
#WELCOME TO TERMUX

b="\033[1m"
u="\033[4m"
bl="\033[30m"
r="\033[31m"
g="\033[32m"
bu="\033[34m"
m="\033[35m"
c="\033[36m"
w="\033[37m"
endc="\033[0m"
enda="\033[0m"
blue="\033[1;34m"
cyan="\033[1;36m"
red="\033[1;31m"

echo  "+×××××××××××××××××××××××××××××××××××××××××××××+" |lolcat
echo  "× Team              : 606 Hack Team $white             " |lolcat
echo  "× Author            : xn_SW4llOW $white                   " |lolcat
echo  "× Channel Boss Kami : 606 Hack $white             " |lolcat
echo  "+×××××××××××××××××××××××××××××××××××××××××××××+" |lolcat

trap ctrl_c INT
ctrl_c() {
clear
echo  $red"[#]> (Ctrl + C ) Detected,
Trying To Exit ... "
sleep 1
echo ""
echo  $white"[#]> semoga bermanfaat :)"
sleep 1
exit
}

lagi=1
while [ $lagi -lt 6 ];
do
echo ""
echo  "============================================" |lolcat
echo  $r "1.        ${endc}";
echo  "÷_÷_÷_÷_÷_÷_÷_÷_÷_÷_÷_÷_÷_÷_÷_÷_÷_÷_÷_÷_÷_÷_÷_÷_÷"  |lolcat
echo  $g "2.            ${endc}";
echo  "÷_÷_÷_÷_÷_÷_÷_÷_÷_÷_÷_÷_÷_÷_÷_÷_÷_÷_÷_÷_÷_÷_÷_÷_÷"  |lolcat
echo $c "3.            ${endc}";
echo  "÷_÷_÷_÷_÷_÷_÷_÷_÷_÷_÷_÷_÷_÷_÷_÷_÷_÷_÷_÷_÷_÷_÷_÷_÷"  |lolcat
echo  $r "4.              ${endc}";
echo  "÷_÷_÷_÷_÷_÷_÷_÷_÷_÷_÷_÷_÷_÷_÷_÷_÷_÷_÷_÷_÷_÷_÷_÷_÷"  |lolcat
echo  $g "5.              ${endc}";
echo  "÷_÷_÷_÷_÷_÷_÷_÷_÷_÷_÷_÷_÷_÷_÷_÷_÷_÷_÷_÷_÷_÷_÷_÷_÷"  |lolcat
echo  $c "6.                ${endc}";
echo  "÷_÷_÷_÷_÷_÷_÷_÷_÷_÷_÷_÷_÷_÷_÷_÷_÷_÷_÷_÷_÷_÷_÷_÷_÷"  |lolcat
echo  $r "7.             ${endc}";
echo  "÷_÷_÷_÷_÷_÷_÷_÷_÷_÷_÷_÷_÷_÷_÷_÷_÷_÷_÷_÷_÷_÷_÷_÷_÷"  |lolcat
echo  $g "8.              ${endc}";
echo  "÷_÷_÷_÷_÷_÷_÷_÷_÷_÷_÷_÷_÷_÷_÷_÷_÷_÷_÷_÷_÷_÷_÷_÷_÷"  |lolcat
echo  $c "9.                ${endc}";
echo  "÷_÷_÷_÷_÷_÷_÷_÷_÷_÷_÷_÷_÷_÷_÷_÷_÷_÷_÷_÷_÷_÷_÷_÷_÷"  |lolcat
echo  $r "10.             ${endc}";
echo  "÷_÷_÷_÷_÷_÷_÷_÷_÷_÷_÷_÷_÷_÷_÷_÷_÷_÷_÷_÷_÷_÷_÷_÷_÷"  |lolcat
echo  $g "11.          ${endc}";
echo  "÷_÷_÷_÷_÷_÷_÷_÷_÷_÷_÷_÷_÷_÷_÷_÷_÷_÷_÷_÷_÷_÷_÷_÷_÷"  |lolcat
echo  $c "00. Exit                               ${endc}";
echo  "============================================" |lolcat
echo ""
echo  "╭─pilih teros!!" |lolcat
read -p "╰─#" use;

#

case $use in
1)apt update
pkg install git


;;

#

2)apt update
pkg install git


;;

#

3)apt update
pkg install git

;;

#

4)apt update
pkg install git


;;

#

5)apt update
pkg install git


;;

#

6)apt update
pkg install git


;;

#

7)apt update
pkg install git


;;

#

8)apt update
pkg install git


;;

#

9)apt update
pkg install git


;;

#

10)apt update
pkg install git


;;

#

11)apt update
pkg install git


;;

00) echo "Tq lurr | sw4llow " |lolcat
exit

;;

*) echo "WARNING!!!,
pilihan yang anda cari tidak terdeteksi,Coba yang lain!"
esac
done
done
