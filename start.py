import os

os.system("apt update && apt upgrade -y") 
os.system("apt install python3-pip -y") 
os.system("apt install ffmpeg -y")
os.system("curl -sL https://deb.nodesource.com/setup_18.x | bash -")
os.system("apt-get install -y nodejs")
os.system("npm i -g npm")
os.system("git clone https://github.com/Elric-xD/DeadlyVC")
os.system("cd DeadlyVC")
os.system("python3 -m Deadly")
