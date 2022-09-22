---
layout: post
title:  "SatDump Basic Usage"
date:   2022-09-17 19:48:00 +0200
tags: tutorial
author: zbychu
---

We've noticed that the UI after the rework (even though we think is pretty clean) can be quite confusing to many people. That's why I've have decided to write this post in which I explain some basic features of SatDump and how to use them efficiently!

# UI

## First Start

When you launch `satdump-ui` you are greeted with a GUI window. The main way of navigating in it is the Tab Bar on the top [1]. Using that you can switch between the different tools SatDump has to offer. The UI of each tool is loaded into the main screen [2].

![](/assets/basic_usage/window1.png)

## Offline Decoding

This tool (as the name suggests) lets you process data from a file. It can be any level (meaning you can process a baseband as well as a cadu file). the UI can be divided into 3 main sections:
+ Pipeline Selection [1]
+ File Selection [2]
+ Pipeline Options [3]

![](/assets/basic_usage/offline.png)
### Pipeline Selection
This widgets lets you select which pipeline to use. Each pipeline is specific to one downlink, so for NOAA you have several: DSB, HRPT and GAC.

### File Selection
Here you select the input file, output directory as well as input level. While the last may sound complex, it's really simple. It just specifies what the input file is. Usually `baseband` is selected when you want to process a recorded signal and `cadu` or `frames` (depending on the downlink) is used when processing data coming from live decoding.

### Pipeline Options
This table has all the options specific to a pipeline, such as samplerate and baseband format (only valid when you are using baseband as input, otherwise irrelevant).

Once everything is set to the correct values you can start the decoding using the 'Start' button [4].

## Recorder (Live Processing)

*This is new!*
In this menu, you can find everything that's related to using an SDR in SatDump. Here you can view, record as well as process data from a radio. Here is the breakdown of the UI:
+ Source Controls [1]
+ FFT Options [2]
+ Processing [3]
+ Recording [4]
+ FFT and Waterfall [5]
  
![](/assets/basic_usage/recorder.png)

### Source Controls
This menu lets you select what source to use (SDR or a file) and has all the options regarding the selected source. Here you set the frequency, samplerate, gain, etc. The menu changes depending on the source. **You can refresh the source list by pressing the 'arrow' button on the right of the combobox.**

### FFT Options
Here you can control the FFT and waterfall displays. Using the sliders you can change the displayed range. The sliders change the lower and upper cutoff (so the difference between these is the displayed range). You may also notice the 'Avg Rate' slider. This controls the level of averaging applied to the FFT. Lower values give a smoother FFT.

### Processing
**In this menu you can initiate live decoding.** It is simmilar in a way to the Offline Decoding section. You can find a pipeline selector and pipeline options in both of them. You may start the processing with the 'Start' button. Some new widgets will appear. *The output will be saved in a directory specified in the Settings!*

  ![](/assets/basic_usage/processing.png)

### Recording
This is a menu where you can Record a baseband file. You have to select a baseband format. available formats are s8 (8 bit), s16 (16 bit), f32 (32bit float) and wav16 (wav compatible with other software like SDR++). Status of the recording is indicated by the colored text.

### FFT and Waterfall
This is self explanatory, it's the FFT and waterfall of the current signal. However it is worth nothing that the waterfall can be disabled to improve performance.

## The Viewer
This is probably the biggest new feature in SatDump after the rewrite. This menu lets you view, tune and project your data. There are two main tools you can change between using the tabs: Products and Projections. There is too many options to fit into one screenshot so I will have to divide them into several.

![](/assets/basic_usage/viewer.png)

## Products (Viewer)
Here you can edit and view your decoded images. There are a few menus that house different settings:
+ General
+ Image
+ RGB Composites
+ Products
+ Map Overlay
+ Projection
  
### General
  ![](/assets/basic_usage/viewer/products/general.png)

In this menu are the most basic functions. There is a tree view of opened datasets and products and options for laoding new datasets and products. (products are automatically loaded after decoding) **When you open the viewer with no products loaded you will be greeted with only this tab and loading options.** Note: the product and dataset names are highlighted yellow when they are added to the projection list, more on that later.

### Image
![](/assets/basic_usage/viewer/products/image.png)

Here you can choose what channel (or composite) to use. You can also apply options such as equalization, white balance, etc. The 'Save' button saves the displayed image.

### RGB Composites
![](/assets/basic_usage/viewer/products/rgb.png)

This section gives you controll over the RGB composites. You can select from available presets, but also manually create composites of your liking. To do that, simply enter the formula into the textbox. Satdump will understand basic mathematical and logic (ternary) operators, so you can create more elaborate composites, such as the VIS/IR blend: 

`ch1 < 0.065 ? (ch4 - 0.7) * 2.66 : ch2 * 2.2 - 0.15, ch1 < 0.065 ? (ch4 - 0.7) * 2.66 : ch2 * 2.2 - 0.15, ch1 < 0.065 ? (ch4 - 0.7) * 2.66 : ch1 * 2.2 - 0.15`

### Products
This Tab will contain information about calibration and other higher level products we introduce. So far very few instruments are calibrated.


# CLI

