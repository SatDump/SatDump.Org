---
layout: post
title:  "APT Beginner tutorial"
date:   2023-1-1 17:10:00 +0200
tags: tutorial
author: feuerwerko
---

This post is there to help you get started with retreiving APT Imagery from NOAA satellites and give you
a general introduction to SatDump.

First off, there are generally two ways of processing APT data. Either recording the satellite signal and processing it after, or live processing it. In this guide we will be focusing on the first option, as it is the less resource intensive and generally better way for APT.

# Obtaining an APT recording

## Getting an Antenna and SDR

You will need a bit of hardware to be able to receive and record satellites. The first of which being a laptop or android phone to run SatDump. 
The next thing you need is of course an SDR. If youre just beginning your SDR journey, the best SDR for you is an RTLSDR, as they are rellatively cheap yet enough to receive APT Data. The best RTLSDRs are the RTLSDR Blog or the NooElec smart.
Lastly, you will of course need an antenna. Essentially any antenna for the 2m band will do, but ideally youre gonna want a V-Dipole that is centerd around 137 MHz (The satellite band). There are many tutorials on how to build one, and making one is also extreamly easy.

## Predicting satellite passes

To record APT Data, you will of course need to know when a NOAA satellite is passing over you. I wont go into much detail in this post, However predicting satellite passes is very simple.
To predict satellite passes you will need a software to do so, the most common of which is called [GPredict](http://gpredict.oz9aec.net/). There are many different pieces of software to do this out there tho.
The satellites that carry an APT payload are called NOAA 15, NOAA 18 and NOAA 19

## Recording the APT data

Once you know when a satellite is going to pass over your location, You will need to head into an ideally open area, where you can have line of sight to the satellite throughout most of its pass.
Line of sight means that there are not any obstructions in the path between you and the satellite.

To record APT data you can either use the built in SatDump recorder or any other SDR software. In this guide I will explain how to record with the SatDump built in recorder.

First, start satdump and navigate to the "Recorder" tab.

Before we record anything, we need to configure a few things. Note that the settings in the recorder should be saved, so you dont have to do all this everytime you open satdump
![](/assets/apt_beginner_tutorial/Recorder-Devices.png)


First, open the Device section, and select your SDR from the drop down menu at the top. If your device doesnt show up, try pressing the button next to the drop down to refresh the device list. Also make sure to input your SDRs PPM correction into the field called "Decimation", however this is not important for most modern SDRs at such low frequencies. Also set the sample rate to 250000 for APT. You can leave the other fields as standard for now. We will need to edit the gain and frequency before we begin recording tho.

![](/assets/apt_beginner_tutorial/Recorder-FFT.png)

Now we will edit the FFT. You will have to adjust the FFT Min and FFT Max values to your liking. For RTLSDRs I recommend -120 Min and -80 Max. You can also choose an FFT Palette. Please note that FFT settings are only for visual appearance and dont change your reception strength.

![](/assets/apt_beginner_tutorial/Recorder-Recorder.png)

Now onto the recorder. You should change the Format to s8, as its the smallest format. More detail than s8 isnt required for any satellites on the VHF band. Now we are ready for receiving! Configure the frequency under the devices section. Here is a list of the frequencies you will need to set for each satellite: 
NOAA 15: 137.62 MHz
NOAA 18: 137.9125 MHz
NOAA 19: 137.1 MHz


Under the devices section you will also have to adjust the gain. For RTLSDRs and some other SDRs you will most likely need to set this to the maximum to get a solid signal. Once you see a signal appearing on the FFT, You can hit the record button. After 10-15 minutes the signal should start to fade, you can then stop the recording.

The record should be located in the install directory of SatDump in the recordings folder on windows, and in ~/.config/satdump/recordings on linux.

# Processing the apt recording

After you have got your hands on an APT recording, you can go ahead and process it.
In SatDump, head to the tab "Offline processing"

![](/assets/apt_beginner_tutorial/pipelines-apt.png)

Now search for the NOAA APT pipeline. We will now have to set a few settings.
First, go ahead and select the recording you just took and set it as the input file.
Now set an output directory where you want satdump to store the image file. Every recording you process should have its own output directory. The input level should already be set to baseband, and the baseband format and sample rate should be auto detected by satdump. You now have to select the NOAA satellite you were recording, and if you want to project the image onto a map enter the unix timestamp at which your pass begun. You can get it at [unixtimestamp.com](https://www.unixtimestamp.com/). If you want to you can also select the "Autocrop with Wedges" option. It will automatically remove the noisy parts of your image. This may remove alot of your image tho.

Now we are finally done, press start and watch as your recording is processed. Once its done you will be able to see the image and apply various enhanchements to its in the viewer. For more info about the viewer, check out the documentation.

# Troubleshooting

## SDR is not showing up in the Recorder
Try plugging your SDR into another USB port, or on linux check if you have permission to acces the usb device. Also make sure you have the latest drivers for you SDR installed. A guide on updating the SDRs driver is usually on the manufacturers website.
## Cant see option thats mentioned in the guide
Make sure you have the latest satdump version installed. You can get the newest nightly at the top of the [releases page](https://github.com/SatDump/SatDump/releases).

Having other issues or need help? Join the SatDump [Matrix chat](https://matrix.to/#/#satdump:altillimity.com)!
