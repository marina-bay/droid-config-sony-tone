# These and other macros are documented in ../droid-configs-device/droid-configs.inc
# Feel free to cleanup this file by removing comments, once you have memorised them ;)

%define rpm_device f8331
%define rpm_vendor qualcomm

%define vendor_pretty Sony
%define device_pretty Xperia XZ

# Define this to pull in https://github.com/mer-hybris/community-adaptation.git
# for build_packages.sh
%define community_adaptation 1

# Sailfish OS is considered to-scale, if in app grid you get 4-in-a-row icons
# and 2x2 or 3x3 covers when up-to-4 or 5-or-more apps are open respectively.
# For 4-5.5" device screen sizes of 16:9 ratio, use this formula (hold portrait):
# pixel_ratio = 4.5/DiagonalDisplaySizeInches * HorizontalDisplayResolution/540
# Other screen sizes and ratios will require more trial-and-error.
%define pixel_ratio 1.75

%define provides_own_board_mapping 1
%define out_of_image_files 1

# Device-specific usb-moded configuration
Provides: usb-moded-configs

# Device-specific ofono configuration
Provides: ofono-configs
Obsoletes: ofono-configs-mer

Obsoletes: qt5-qpa-surfaceflinger-plugin

Conflicts: apkd < 8.1.0

# Community builds may use the system partition
# TODO: Define this for community builds as well!
# Explanation: vendor is not the physical parition, but rather just another
# folder in the root.img lvm. So require system-vendor-<device> as well!
# if 0%{?_obs_build_project:1}
Requires: droid-system-kagura-%{rpm_device}
Requires: droid-system-vendor-kagura-%{rpm_device}
# endif

%define ofono_enable_plugins bluez5,hfp_ag_bluez5
%define ofono_disable_plugins bluez4,dun_gw_bluez4,hfp_ag_bluez4,hfp_bluez4,dun_gw_bluez5,hfp_bluez5

%include droid-configs-device/droid-configs.inc

# IMPORTANT if you want to comment out any macros in your .spec, delete the %
# sign, otherwise they will remain defined! E.g.:
#define some_macro "I'll not be defined because I don't have % in front"

