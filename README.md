# Digital Font Tools

Tools for converting digital FPV fonts from one format to another and simplify editing with intermidiate "template" format.

_Some scripts copied with minor modifications from [Knifa's templates branch](https://github.com/Knifa/mcm2img/tree/templates)_

## Usage

Different digital FPV systems use different font formats. This repository contains simple tools to convert between such formats.  

Conversion happens via intermidiate format, a "template".

Template is a PNG image of `576x1728` pixels in size. The image contains `512`(=16x16x2) characters, each character is `36x54` pixels.  

Template is usually a result of conversion from one of digital fonts, but can be created manaully in some image editor.  
Before conversion to final format, a template image can be edited, but not necessary so.

Typical flow: `font-in-format-X -> template -> (optional editing) -> font-in-format-Y`

There are also handly little tools for templates manipulation:
  - `generate_overlay.py` -- generates an image to help with editing templates
    _put it into a separate 20% opacity layer on top of everything in your image editor_
  - `template_merge.py` -- takes two template images and outputs one templte, a merge result
    _second template replaces characters of first template for all non-empty second template characters_
  - `template_extract.py` -- takes a template and generates a new template with all characters empty except some copied from the given template
    _see examples folder for inspiration_

## HDZero

Low latency digital FPV system

- [HDZero OSD Font Library](https://github.com/hd-zero/hdzero-osd-font-library)


## Walksnail

Custom fonts must be placed in "userfont" directory on SD card!

- [Custom Walksnail OSD Fonts](https://github.com/jduerr/Custom-Walksnail-OSD-Fonts)
- [Walksnail OSD Tool](https://github.com/avsaase/walksnail-osd-tool/)


## WTFOS

Jailbreak for DJI V1 and V2 goggles and some air units that enables MSP DigitalPort among other things.

- https://github.com/fpv-wtf/msp-osd
  - [PNG previews (one-page templates)](https://github.com/fpv-wtf/msp-osd/tree/main/docs/fonts)
  - [Actual fonts that can be used, extracted from MCM files, I suppose](https://github.com/fpv-wtf/msp-osd/tree/main/fonts)
- https://github.com/Knifa/material-osd
- https://github.com/EVilm1/EVilm1-OSD-Font
