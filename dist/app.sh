#!/bin/bash
if [ -d "/usr/share/doc/xdotool" ]
then
    xdotool key ctrl+alt+t
    sleep 1
    xdotool type "cd Desktop/Select_Jeu/dist/ && python3 ../app.py"
    xdotool key Return
else
    kdialog --error "Veuillez installer le paquet xdotool via la commande 'sudo apt intstall xdotool' et relancez le programme"
fi
