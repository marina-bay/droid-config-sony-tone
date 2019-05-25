%define device kagura
%define rpm_device f8331

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

%include rpm/droid-config-tone-common.inc
%include droid-configs-device/droid-configs.inc
