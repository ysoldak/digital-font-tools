#!/bin/bash

# output dir
mkdir -p output

# full version
cp template_fpvc.png ./output/template_fpvc_full.png
python3 ../../template_merge.py template_sneakyfpv_inav.png ./output/template_fpvc_full.png ./output/template_fpvc_full_merged.png

# short version
python3 ../../template_extract.py template_fpvc.png 0x1D0 0x1FF ./output/template_fpvc_short.png
python3 ../../template_merge.py template_sneakyfpv_inav.png ./output/template_fpvc_short.png ./output/template_fpvc_short_merged.png

# --------------------

# generate hdzero
# TODO

# generate walksnail
python3 ../../template2walksnail.py ./output/template_fpvc_full_merged.png
python3 ../../template2walksnail.py ./output/template_fpvc_short_merged.png

# generate wtfos
python3 ../../template2wtfos.py ./output/template_fpvc_full_merged.png
python3 ../../template2wtfos.py ./output/template_fpvc_short_merged.png

# --------------------

# package
mkdir -p result

# hdzero
mkdir -p result/hdzero
# TODO

# walksnail
mkdir -p result/walksnail
cp ./walksnail/font_update.ini ./result/walksnail/
cp ./output/template_fpvc_short_merged_walksnail_24.png ./result/walksnail/FPVCombat_Short_24.png
cp ./output/template_fpvc_short_merged_walksnail_36.png ./result/walksnail/FPVCombat_Short_36.png
cp ./output/template_fpvc_full_merged_walksnail_24.png ./result/walksnail/FPVCombat_Full_24.png
cp ./output/template_fpvc_full_merged_walksnail_36.png ./result/walksnail/FPVCombat_Full_36.png

# wtfos
mkdir -p result/wtfos
mkdir -p result/wtfos/FPVCombat_Short
cp ./output/template_fpvc_short_merged_wtfos/font.bin ./result/wtfos/FPVCombat_Short/
cp ./output/template_fpvc_short_merged_wtfos/font_hd.bin ./result/wtfos/FPVCombat_Short/
cp ./output/template_fpvc_short_merged_wtfos/font_2.bin ./result/wtfos/FPVCombat_Short/
cp ./output/template_fpvc_short_merged_wtfos/font_hd_2.bin ./result/wtfos/FPVCombat_Short/
mkdir -p result/wtfos/FPVCombat_Full
cp ./output/template_fpvc_full_merged_wtfos/font.bin ./result/wtfos/FPVCombat_Full/
cp ./output/template_fpvc_full_merged_wtfos/font_hd.bin ./result/wtfos/FPVCombat_Full/
cp ./output/template_fpvc_full_merged_wtfos/font_2.bin ./result/wtfos/FPVCombat_Full/
cp ./output/template_fpvc_full_merged_wtfos/font_hd_2.bin ./result/wtfos/FPVCombat_Full/
