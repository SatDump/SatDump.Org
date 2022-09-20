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

# CLI

