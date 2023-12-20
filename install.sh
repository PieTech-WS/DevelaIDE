sudo dpkg --add-architecture i386 
sudo apt-get -y update
sudo apt-get -y install autoconf automake bison build-essential dfu-util genromfs flex git gperf
sudo apt-get -y install libncurses5 lib32ncurses5-dev libc6-dev-i386 libx11-dev libx11-dev:i386 libxext-dev
sudo apt-get -y install libxext-dev:i386 net-tools pkgconf unionfs-fuse zlib1g-dev

# Ubuntu20.04安装gcc-11需要添加源
sudo apt-get -y install software-properties-common
sudo add-apt-repository ppa:ubuntu-toolchain-r/test -y
sudo apt-get update && sudo apt-get -y upgrade

# 切换国内源安装速度比较快
sudo sed -i "s/http:\/\/ppa.launchpad.net/https:\/\/launchpad.proxy.ustclug.org/g" /etc/apt/sources.list.d/*.list
sudo apt-get update && sudo apt-get -y upgrade
sudo apt-get install -y gcc-11 g++-11 g++-11-multilib

sudo apt-get -y install kconfig-frontends
sudo apt-get -y install libpulse-dev:i386
sudo apt-get -y install libasound2-dev:i386
sudo apt-get -y install libasound2-plugins:i386
sudo apt-get -y install libusb-1.0-0-dev
sudo apt-get -y install libusb-1.0-0-dev:i386
sudo apt-get -y install libmad0-dev:i386
sudo apt-get -y install libv4l-dev libv4l-dev:i386
sudo apt-get -y install libuv1-dev
sudo apt-get -y install libmp3lame-dev:i386 libmad0-dev:i386 libv4l-dev:i386

sudo apt-get -y install xxd
sudo apt-get -y install qemu-system-arm qemu-efi-aarch64 qemu-utils 
sudo apt-get -y install nasm yasm
sudo apt-get -y install libdivsufsort-dev
sudo apt-get -y install libc++-dev libc++abi-dev
sudo apt-get install -y libprotobuf-dev protobuf-compiler protobuf-c-compiler
sudo apt-get -y install gcc-multilib g++-multilib
