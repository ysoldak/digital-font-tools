#!/bin/bash

# tmp dir
mkdir -p tmp

# full version
cp template_fpvc.png ./tmp/template_fpvc_full.png
python3 ../../template_merge.py template_sneakyfpv_inav.png ./tmp/template_fpvc_full.png ./tmp/template_fpvc_full_merged.png

# short version
python3 ../../template_extract.py template_fpvc.png 0x1D0 0x1FF ./tmp/template_fpvc_short.png
python3 ../../template_merge.py template_sneakyfpv_inav.png ./tmp/template_fpvc_short.png ./tmp/template_fpvc_short_merged.png

# --------------------

# generate hdzero
python3 ../../template2hdzero.py ./tmp/template_fpvc_full_merged.png
python3 ../../template2hdzero.py ./tmp/template_fpvc_short_merged.png

# generate walksnail
python3 ../../template2walksnail.py ./tmp/template_fpvc_full_merged.png
python3 ../../template2walksnail.py ./tmp/template_fpvc_short_merged.png

# generate wtfos
python3 ../../template2wtfos.py ./tmp/template_fpvc_full_merged.png
python3 ../../template2wtfos.py ./tmp/template_fpvc_short_merged.png

# --------------------

# package
mkdir -p output

# hdzero
mkdir -p output/hdzero
cp ./tmp/template_fpvc_short_merged_hdzero.bmp ./output/hdzero/FPVCombat_Short.bmp
cp ./tmp/template_fpvc_full_merged_hdzero.bmp ./output/hdzero/FPVCombat_Full.bmp

# walksnail
mkdir -p output/walksnail
cp ./walksnail/font_update.ini ./output/walksnail/
cp ./tmp/template_fpvc_short_merged_walksnail_24.png ./output/walksnail/FPVCombat_Short_24.png
cp ./tmp/template_fpvc_short_merged_walksnail_36.png ./output/walksnail/FPVCombat_Short_36.png
cp ./tmp/template_fpvc_full_merged_walksnail_24.png ./output/walksnail/FPVCombat_Full_24.png
cp ./tmp/template_fpvc_full_merged_walksnail_36.png ./output/walksnail/FPVCombat_Full_36.png

# wtfos
mkdir -p output/wtfos
mkdir -p output/wtfos/FPVCombat_Short
cp ./tmp/template_fpvc_short_merged_wtfos/font.bin ./output/wtfos/FPVCombat_Short/
cp ./tmp/template_fpvc_short_merged_wtfos/font_hd.bin ./output/wtfos/FPVCombat_Short/
cp ./tmp/template_fpvc_short_merged_wtfos/font_2.bin ./output/wtfos/FPVCombat_Short/
cp ./tmp/template_fpvc_short_merged_wtfos/font_hd_2.bin ./output/wtfos/FPVCombat_Short/
mkdir -p output/wtfos/FPVCombat_Full
cp ./tmp/template_fpvc_full_merged_wtfos/font.bin ./output/wtfos/FPVCombat_Full/
cp ./tmp/template_fpvc_full_merged_wtfos/font_hd.bin ./output/wtfos/FPVCombat_Full/
cp ./tmp/template_fpvc_full_merged_wtfos/font_2.bin ./output/wtfos/FPVCombat_Full/
cp ./tmp/template_fpvc_full_merged_wtfos/font_hd_2.bin ./output/wtfos/FPVCombat_Full/
