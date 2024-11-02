#!/bin/bash

echo Repack by @pr0xit

pip install requests pystyle google faker qrcode whois

if [ $? -ne 0 ]; then
    echo "Failed to install some packages. Exiting."
    exit 1
fi

echo Repack by @pr0xit

python serpentine1.4.py

read -p "Press [Enter] key to continue..."
