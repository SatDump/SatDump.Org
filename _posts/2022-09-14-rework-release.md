---
layout: post
title:  "SatDump ReWork Release"
date:   2022-09-14 20:28:21 +0200
tags: release
---

*First of all, why?*  

Back when I started SatDump, it started as a "simple" UI to simplify the process of using the previous command-line tools (ironically, that's why I initially went with the module system). It wasn't meant to be too complicated at the time, so I kept some things pretty basic, and it initially was mostly a 1:1 port of the old codebase. But soon after, I started adding features, rewriting a bunch of code, supporting more and more satellites. At the same time, it became a lot more widespread & popular than I was expecting, meaning I ended up focusing on community-requested features.  

All that was great, but as things grew fast (*too* fast), without rewriting some parts of the core codebase that were not up to the task anymore. Hence, things became increasingly difficult to debug, work on and maintain.  
It was hence inevitable, at some point some *major* rewrite would have to be undertaken. After some events leading to a break in development (everyone's busy sometimes!), I decided to stop doing any sensible on what was 0.0.39 at the time, in order to focus on said rewrite.  

So, I made a private fork of the codebase at the time. I decided to keep it private for a simple reason : Users. With such a long TO-DO list, it was going to be several months before the new codebase would be in any way even remotely usable. Even worse to reach feature parity and be sure things would not crap out randomly.  
As such, a private repo and staying silent about it avoided having to deal with supporting the (curious) people that would inevitably want to give it a go (as unfortunately, that can slow down development quite a lot!).  

I do apologize for the worse support there was in the meantime - Hope you understand :-)

*What is it?*

I won't go in details here as there is a (mostly) complete list below, but : It's pretty much an entire rewrite. When I started, I literally just deleted everything that I know had to be redone in some way, stripping down SatDump to *pretty much nothing*. Some code was still not modified much though (such as the Pipeline / Module system), but the rest (including *all* UI code) was either rewritten from scratch, or improved in compatbility-breaking ways.  
Older concepts were also heavily modified (such as the new products system, which supersedes the .georef format), bringing huge improvements upon the previous projection system, alongside further optimizations, small improvements like the option to skip the intermediate soft symbol level...   
The Android version was also entirely redone, to now be "officially" supported at the same level as Desktop support. Anyway, I won't elaborate too much here!  
Just as warning, while everything features-wise should be fine, it's totally possible some things were messed up / forgotten! *Please report if that's the case!*

# Introduction

Below is a list of (hopefully) all changes, with explanations. It's in no specific order, so I'd recommend reading it entirely if you wish to not miss some useful information. This is more about what "the user will see" though, than under-the-hood specifics unless it matters.  
I will also ***not*** enumerate changes specific to each satellite or so on, as there were a lot of small improvements overall and it would just be too long.

# Core Changes

## User Interface

### What's different?

"It kinda looks the same, but it also looks very different.. So what did we change? The theme stayed pretty much the same (except it is all rounded now!), so did the menus You have already seen before (well, mostly.. more on that below :). When rewriting the UI I've focused on making it more user friendly, but also making it more refined (making widgets for specific tasks, rather than trying to make it work with what we already had). You may notice, that there are a lot of small touches in the UI such as icons and symbols. I do hope you like that! The UI of new apps should be self-explanatory, so I won't go into details in this text."
 \- Zbychu

### Main Menu

Previously, the overall navigation was rather "static". You'd be greeted by several tabs, but each of them would bring you to another "entire program" taking over the whole window. That's *really* not the case anymore. Instead, everything lives below its own tab. You can start processing something, while it's in progress, check on another tab, etc!

![](/assets/rework_release/main_ui_menu.png)

### Offline Processing

As far as the `Offline Processing` menu goes, as you can see above, it's both similar, but also very different. The categories and pipelines drop-down menus are gone, instead replaced by a Search-based system. After testing for a while this ended up feeling the nicest and fastest to use.  
Something more under-the-hood is that default options you can set for all pipelines are now also defined in satdump.cfg, with the option for pipelines to expose additonal parameters if necessary.

![](/assets/rework_release/pipelines_with_extra_opts.png)

This of course is an ***extreme*** example, but it shows it well! That way, it's not needed anymore to have 2 identical pipelines for a single different parameter.

### Recorder / Live Processing

*Wait? What? Where's live-processing!?*
Well, now both baseband recording and live-processing are done in the same menu, as they all share the same basic functions (opening a device and providing a FFT).

![](/assets/rework_release/record_live_proc.png)

As you may see above, both features are in their own sub-menu, and can actually even be used at once!

![](/assets/rework_release/record_liveproc.png)

And for live-processing, running modules now live at the bottom by default (but you can still restore floating windows if you wish).  

Other changes include a *much* better waterfall / FFT, nicer SDR controls and so on... As well as a bunch of code optimizations.

### Viewer

Yes. That's new. It's an interface to let you view and quickly *manually* edit and view the output data.   
It will let you :
- Generate preset or custom RGB composites
- Apply several operations on the image, such as equalization, rotation, Earth curvature correction
- Draw a border/cities overlay
- And more!

![](/assets/rework_release/viewer_1.png)

And just to prove it's universal enough, even though it's not an usual thing to do :  
Yes, map overlay on MHS.

![](/assets/rework_release/viewer_mhs.png)

Though you might have noticed the "Projection" tab, which hides everything you need to generate fancy projections and merge several passes.

"The projection tool is very powerfull. It allows the user to project products to any of the available projections. The system features a layer system, which is designed to help merge multiple images into one. There are two layer modes available: blend and overlay. Blend (as the name suggests) blends the images together, Overlay overlays them. Layer order can be changed, so you can arrange passes in the way you want! You can save the image created by this tool."
\- Zbychu

![](/assets/rework_release/projections_1.png)

And... Thanks to Zbychu's work, you can also use an OpenStreeMap (or other tile map) as a background!

### Modules

Modules also had some changes here and there, I won't list them of all though but a few notables ones.

Before, instrument decoders would not be very indicative of their progress. Well, that's fixed.

![](/assets/rework_release/instruments_dec_ui.png)

And, demodulators now indicate PLL frequency.

![](/assets/rework_release/new_ui_demod.png)

Alongside those UI changes, that's a good example of 2 modules running at once to skip a step!

### Settings

Not a lot to say there, but they were heavily cleaned up!

![](/assets/rework_release/settingsui.png)

## Plugins

While plugins were already a thing previously, now they're *a lot* more utilized. Everything specific to a specific satellite / mission is now in a separate plugin. That makes it possible to build and load *only* what you need at compile-time. This includes SDR support, to also make it easier to manage. 

![](/assets/rework_release/plugins_logs.png)

So if you only need GOES support (for let's say, a GRB or HRIT station) :

```
cmake [OTHER FLAGS] -DPLUGINS_ALL=OFF -DPLUGIN_GOES=ON
```

Though, for many users wanting the entire support package this will pretty identical to how things worked before.

## Products

A new concept that was introduced is products. They were created to allow storing metadata alongside exported raw channel data (images) or other formats, so that it could be loaded at a later time in a viewer, which would let users manually edit and create visualizations of the data.

So now, alongside most data generated by an instrument decoder you will be getting 1 or 2 new files :
- `products.cbor` : This one will be present in an instrument's subfolder. It contains the instrument's description, projection information, timestamps... Everything that may be required to process the data further.
- `dataset.json` : A simple list of all products to load from a specific decoded pass / recording.

Those are the files you should load in the viewer if you wish to do so :  
![](/assets/rework_release/viewer_products_open.png)

It also means that now all instruments (well, that have been ported to the new system, which is most of them) are not generating hard-coded composites or projections. It's all defined in satdump_cfg.json! But those are *only* what will be shown in the viewer by default or generated when using automated processing!

**This means products such as composites are NOT automatically generated anymore by default! You will have to go in settings and enable the option if you wish for SatDump to do so.**

If this option is enabled, once it is done with processing instruments you will see the following pop up :  
![](/assets/rework_release/products_processing.png)

# Module changes

## Merge of all instrument decoders into one

Not a lot to say, but now instead of a bunch of separate modules to decode each instruments, it's all done into one. That was a side-effect of SatDump's origins... But anyway, not a huge change from an user-perspective, apart from some speed gains!

## Demodulators

Now, all demodulators share a common base. That means things "just work" on all of them! Alongside some small additions such as the option to show a FFT while demodulating. 

![](/assets/rework_release/demod_fft_mod.png)

## DVB-S2

A new module allowing for DVB-S2 demodulation was added. It is capable of demodulating any constellation and FEC rate in CCM mode. It does so using a full-fledged FEC stack (thanks Ahmet!) at symbolrate up to ~10M on a decently powerful machine.

![](/assets/rework_release/dvbs2_1.png)

The addition of DVB-S2 demodulation allowed supporting some new downlinks though!

### GOES-R GRB

For a while now, thanks to SnazzLazz's help, it's been possible to fully process GRB in software on a decent PC in real-time.  
*Credits to SnazzLazz for receiving this data from GOES-16*

![](/assets/rework_release/ABI_CONUS_RGB135_20220618T074720Z.jpg)
![](/assets/rework_release/SUVI_Fe304_20040327T032458Z.jpg)

### HimawariCast

Another DVB-S2 downlink, which is doable on a decent laptop. Lots of thanks go to Sam for helping out with the formats, recording and such!

![](/assets/rework_release/IMG_DK01IR2_202009201140.jpg)

## DVB-S

Not as big of a deal (yet?), but there's also a DVB-S demodulator now. It's not quite finished yet (but totally functional) :-)

![](/assets/rework_release/dvbs_demod.png)

# SDR Support

Some new SDR devices are now supported :
- BladeRF (1.0 and 2.0)
- SDRPlay RSPDUO (was already supported but buggy)
- PlutoSDR
- MiriSDR (for Mirics-based sticks)

# Command-Line

The CLI interface was also redone, for all 3 main usecases :

## Offline Processing

```
Usage : ./satdump [pipeline_id] [input_level] [input_file] [output_file_or_directory] [additional options as required]
Extra options (examples. Any parameter used in modules can be used here) :
 --samplerate [baseband_samplerate] --baseband_format [f32/s16/s8/u8] --dc_block --iq_swap
Sample command :
./satdump metop_ahrpt baseband /home/user/metop_baseband.s16 metop_output_directory --samplerate 6e6 --baseband_format s16
```

## Live Processing

The old ingestor system is now gone. It's been replaced by something taking everything on the command-line, complete with a timeout feature for those who like to write scripts that way!

```
Usage : ./satdump live [pipeline_id] [output_file_or_directory] [additional options as required]
Extra options (examples. Any parameter used in modules or sources can be used here) :
 --samplerate [baseband_samplerate] --baseband_format [f32/s16/s8/u8] --dc_block --iq_swap
 --source [airspy/rtlsdr/etc] --gain 20 --bias
As well as --timeout in seconds
Sample command :
./satdump live metop_ahrpt metop_output_directory --source airspy --samplerate 6e6 --frequency 1701.3e6 --general_gain 18 --bias --timeout 780
```

Of course, the http statistics system is still availbe using the `--http_server 0.0.0.0:8080` flag. It's also giving out a bit more information than before.

## Recording

```
Usage : ./satdump record [output_baseband (without extension!)] [additional options as required]
Extra options (examples. Any parameter used in sources can be used here) :
 --samplerate [baseband_samplerate] --baseband_format [f32/s16/s8/u8] --dc_block --iq_swap
 --source [airspy/rtlsdr/etc] --gain 20 --bias
As well as --timeout in seconds
Sample command :
./satdump record baseband_name --source airspy --samplerate 6e6 --frequency 1701.3e6 --general_gain 18 --bias --timeout 780
```

# Android

Let's say it. The old Android port was absolute garbage! Well, now it *should* be better. It's ironic because that was really a lot of work, but the end result is pretty much "same as on Desktop, but on Android". So honestly? I will keep it short.

Though... One major difference is that now, thanks to some fixes in Volk (a library utilized for all DSP code), it can now use SIMD instructions leading to huge performances improvements! Live-Decoding MetOp AHRPT is perfectly feasible on a decently modern phone or tablet (in this case, thanks to Volk merging my PR about their FEC kernel!).

![](/assets/rework_release/android_main.png)
![](/assets/rework_release/android_live.png)

SDRs supported :
- Airspy
- AirspyHF
- HackRF
- LimeSDR
- RTL-SDR
- MiriSDR Sticks

Otherwise, the main change with Android is that it's now considered "stable enough".

# Projections

## Old algorithm (LEO Satellites)

This is a slightly better version of the previous projection algorithm. This one "draws" points. It's not the best way to do it *by far*, but it's fast, and bad data (low SNR / cuts) will not destroy the entire image.  
It's why it was kept. It has cons, but the pros are handy to many despite the lower quality result.

## New algorithm (LEO Satellites)

This more proper. It's a Thin-Plate-Spline (TPS) interpolation algorithm. It gives very good results and should be preferred when possible. The downside is : Bad data can mess the math up easily enough! There are ways to filter it to improve things, and it's already done and will be improved in the future along the way.
Though honestly, in most cases if the image is mostly OK, this will do just fine.  

## GPU (OpenCL) Support

Most reprojection operations (including the above new algorithm) can now run on your graphics card for *much* faster processing (even a low-end card will easily be a magnitude faster). If you plan on doing projections often, I'd highly recommend doing it this way!