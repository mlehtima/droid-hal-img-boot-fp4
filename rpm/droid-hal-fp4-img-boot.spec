%define device fp4

%define mkbootimg_cmd mkbootimg --header_version 2 --os_version 14.0.0 --os_patch_level 2024-11 --pagesize 0x00001000 --base 0x00000000 --kernel_offset 0x00008000 --ramdisk_offset 0x01000000 --second_offset 0x00000000 --tags_offset 0x00000100 --dtb_offset 0x0000000001f00000 --cmdline 'androidboot.selinux=permissive audit=0 androidboot.console=ttyMSM0 androidboot.hardware=qcom androidboot.memcg=1 androidboot.usbcontroller=a600000.dwc3 cgroup.memory=nokmem,nosocket loop.max_part=7 lpm_levels.sleep_disabled=1 msm_rtb.filter=0x237 service_locator.enable=1 swiotlb=2048' --board '' --kernel %{kernel} --ramdisk %{initrd} --dtb /boot/dtb.img --output

%define root_part_label userdata

%define display_brightness_path /sys/class/backlight/backlight/brightness
%define display_brightness 1024

%define lvm_root_size 10000

BuildRequires: python3-base

%include initrd/droid-hal-device-img-boot.inc
