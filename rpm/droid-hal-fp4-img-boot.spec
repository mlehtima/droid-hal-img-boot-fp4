%define device fp4

%define mkbootimg_cmd mkbootimg --cmdline 'androidboot.console=ttyMSM0 androidboot.hardware=qcom androidboot.memcg=1 androidboot.usbcontroller=a600000.dwc3 cgroup.memory=nokmem,nosocket loop.max_part=7 lpm_levels.sleep_disabled=1 msm_rtb.filter=0x237 service_locator.enable=1 swiotlb=2048 androidboot.selinux=permissive audit=0 video=vfb:640x400,bpp=32,memsize=3072000' --kernel %{kernel} --ramdisk %{initrd} --dtb /boot/dtb.img --header_version 2 --base 0 --pagesize 4096 --kernel_offset 0x00008000 --ramdisk_offset 0x01000000 --second_offset 0x00000000 --tags_offset 0x00000100 --board '' --output

%define root_part_label userdata

%define display_brightness_path /sys/class/backlight/backlight/brightness
%define display_brightness 1024

%define lvm_root_size 5000

%include initrd/droid-hal-device-img-boot.inc
