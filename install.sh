dpkg --add-architecture i386 
apt-get -y update
apt-get -y install autoconf automake bison build-essential dfu-util genromfs flex git gperf
apt-get -y install libncurses5 lib32ncurses5-dev libc6-dev-i386 libx11-dev libx11-dev:i386 libxext-dev
apt-get -y install libxext-dev:i386 net-tools pkgconf unionfs-fuse zlib1g-dev

# Ubuntu20.04安装gcc-11需要添加源
apt-get -y install software-properties-common
add-apt-repository ppa:ubuntu-toolchain-r/test -y
apt-get update && sudo apt-get -y upgrade

# 切换国内源安装速度比较快
sed -i "s/http:\/\/ppa.launchpad.net/https:\/\/launchpad.proxy.ustclug.org/g" /etc/apt/sources.list.d/*.list
apt-get update && sudo apt-get -y upgrade
apt-get install -y gcc-11 g++-11 g++-11-multilib

apt-get -y install kconfig-frontends
apt-get -y install libpulse-dev:i386
apt-get -y install libasound2-dev:i386
apt-get -y install libasound2-plugins:i386
apt-get -y install libusb-1.0-0-dev
apt-get -y install libusb-1.0-0-dev:i386
apt-get -y install libmad0-dev:i386
apt-get -y install libv4l-dev libv4l-dev:i386
apt-get -y install libuv1-dev
apt-get -y install libmp3lame-dev:i386 libmad0-dev:i386 libv4l-dev:i386

apt-get -y install xxd
apt-get -y install qemu-system-arm qemu-efi-aarch64 qemu-utils 
apt-get -y install nasm yasm
apt-get -y install libdivsufsort-dev
apt-get -y install libc++-dev libc++abi-dev
apt-get install -y libprotobuf-dev protobuf-compiler protobuf-c-compiler
apt-get -y install gcc-multilib g++-multilib
