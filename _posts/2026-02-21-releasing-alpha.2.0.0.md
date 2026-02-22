---
layout: post
title:  "First 2.0.0 Alpha Releases"
date:   2026-02-26 14:55:55 +0200
tags:   release
authors: [Aang23, lego11]
---

This article is more or less a follow up to [the previous one about 2.0.0](http://127.0.0.1:4000/posts/towards-2.0.0/).

# Summary

For the short version, as explained in the previous article v2.0.0 Alpha builds will start being rolled out until things are stable enough for an actual release. In the meantime, most users are encourage to switch over as v1.2.x is now officially being superseeded.  
However, do note that for some workflows, upgrading may be not an option yet (and if so, please report everything missing!). Please check before upgrading!

And now for the long version... :-)

# Development Status & Plans

TODO

# Changes

## New satellites support

As with many previous SatDump releases, this one also brings many more satellites to the portfolio!

### Kanopus-Vulkan (Канопус-Вулкан) (Kanopus-V-2, -3, -4, -5 and Kanopus-V-IK)

Kanopus-Vulkan satellites are dedicated to high-resolution remote sensing. They form a constellation composed of six 500km orbit satellites, of which five of those are operational, including the lone Kanopus-V-IK (where the *IK* stands for *Инфра-Краснии*, infrared) and all are now supported by SatDump thanks to a months-long process of reverse engineering by Aang (with a bit of help by Andrew and lego11).

These satellites currently provide the best imagery (in terms of resolution) available for general reception by amateurs, at 2.5 meters per pixel with the PSS instrument providing panchromatic (black and white) imagery; there is also support for MSS (a four-channel multispectral radiometer) that can output true-color imagery at 12 meters per pixel.

All of the Kanopus-V satellites do both dumps from memory (generally over Moscow, Khabrovsk or Irkutsk, similar to Meteor-M) as well as direct broadcast over most of Eastern and Central Europe (possibly elsewhere too, such as Antarctica). As with most other Russian satellites, the Kanopus series transmits on the X band at 61.44 Msym/s QPSK, on either 8128 or 8320 MHz.

![Kanopus-V PSS](/assets/release_200alpha/pss.png)
*Kanopus-V PSS*

### Metop-SG

Europe's latest weather satellite, Metop-SG-A1 has also been added to SatDump for reception. The METimage, 3MI, MWS and Sentinel 5 instruments are supported. 3MI and Sentinel 5's support is very experimental for the moment, while METimage and MWS output fully compatible products with new enhancements added by lego11 (although they are not calibrated yet). 

The imagery obtained from 3MI is quite interesting as shown by this clip created by Nate @saito720 using data from Drew @plugger_lockett:

![Metop-SG 3MI](/assets/release_200alpha/metop-sg_3mi.webp)

Unfortunately, the large bandwidth of the signal means that receptions with the BladeRF are not really possible at an acceptable quality level, if at all.
An SDR with a wider bandwidth capability, such as the RFNM or Spectran, is required for good results.

![Metop-SG METimage](/assets/release_200alpha/metimage.jpeg)
*Metop-SG-A1 METimage by @UngerKonrad*

### FengYun-3H

While surely less impressive than Kanopus or 3MI imagery, the latest addition to the Chinese weather satellite constellation has also earned its spot in the list of supported satellites in SatDump. The satellite itself is almost identical to FengYun-3F and will eventually replace FengYun-3D in the early afternoon orbit.

![FengYun-3H MERSI-3](/assets/release_200alpha/202512081211_OBJECT_A_TRUE_COLOR2.jpg)
*FengYun-3H MERSI-III by lego11*

### SeaWiFS (OrbView-2 SeaStar)

This satellite is unfortunately no longer active, however over its lifespan it collected a large quantity of true color imagery that is widely used in the scientific community, for example to track algae bloom events and land use changes over historical periods.

Thanks to excellent work and dedication by Meti, SatDump now fully supports loading and decoding data from SeaWiFS. While the satellite is no more, its legacy lives on, and even if you're not an Earth scientist, you'd probably find its imagery quite interesting nonetheless.


## Improvements for other satellites

### FengYun-2 calibration

Thanks to Meti's good work and some suggestions by lego11, FengYun-2 satellites are now totally calibrated! This, together with the earlier corrector patches also by Meti that make it possible to decode acceptable images at low SNR, greatly improves the usefulness and potential of the S-VISSR broadcast from this satellite series.

![FengYun-2H S-VISSR](/assets/release_200alpha/fy2h.png)
*FengYun-2H S-VISSR calibrated imagery (Cloud Top IR) from @Meti's automated station «Vadim»*

### RDAS improvements

Other patches by Meti greatly improved RDAS (direct X band broadcast from Elektro satellites) support in SatDump. A corrector, similar to those for S-VISSR and GOES GVAR, can now be used with RDAS data. Also, channel order was fixed (previously channel 1 and 2 were swapped).

### Projection alignments

Some love by lego11 and Meti was given to FengYun-3 and MSU-MR projections so that they are aligned with the map overlay.

### STEREO decoder patch

The ICER Decompressor was not working to decode STEREO under certain circumstances, this patch from Meti fixes it.

## Other improvements

### Generic (wavelength/frequency-based) enhancements

Previously, each time a new satellite or instrument was added, a new set of enhancements would have to be copied over. This was the case even if the instrument itself was comparable (in physical characteristics) to the other ones. 

The problem with this approach was that it created a lot of repeated code, which quickly grew unmaintainable. Often, an enhancement was added for a specific instrument, but even though other instruments could have benefitted from this new enhancement with no changes required, they didn't because *someone* (yes, it's lego11's fault more likely than not!) forgot to copy the config over. Also, when a mistake was found, it was quite painful (not to mention time consuming and error prone) to track down ALL of the enhancements that needed to be fixed (and again, *someone* **cough** *lego11 again*, likely forgot to update one or two of them).

With this new system, an enhancement can be defined in physical terms, e.g. it needs an 89 GHz channel (with a tolerance of 5%), calibrated for radiance, with a bandwidth not exceeding 3 GHz, and with vertical polarization. 

Once that is done, the enhancement will be applied automatically to all instruments that respond to those criteria.

For further information  see [the documentation](https://docs.satdump.org/v2/md_docs_2pages_2ImageProductExpression.html#autotoc_md33)

### LDPC Improvements

While working with lego11 for a (somewhat) unrelated project to SatDump, Aang pushed a lot of improvements for LDPC, that also fixed a number of bugs.

### First Party Support improvements

New file types and data types were added to the First Party Support in SatDump, including rudimentary support for files sent through EUMETCast.

### New BitView

A new and improved BitView (binary file analysis tool) was added in SatDump by Aang. In addition to most of the features found in software such as Hobbits, SatDump's BitView is optimized for use with satellites and includes tools such as a deframer, dediff and deinterleaver, CCSDS VCID splitter and more. Despite this, lego11 has successfully managed to reverse engineer the proprietary file format for *a train simulator* with it, of all things!

![bitview](/assets/release_200alpha/bitview.png)
*The BitView's VCID splitter feature operating on FengYun-3D*

### RTL-SDR PLL locking fix

This fix improves the PLL locking for RTL-SDR sticks at high frequencies (L band). This makes the RTL-SDR sticks work better at L band frequencies compared to before, which greatly improves their reliability when used for (A)HRPT or LRIT/HRIT receptions.

### Geostationary satellites now work in autotrack

Thanks to work from Meti, it is now possible to add geostationary satellites to the autotrack. This makes it possible to have a station doing both LEO as well as geostationary satellites with a single dish, switching seamlessly between the two.

### Minor improvements

A few minor improvements were added to SatDump:
* The HydraSDR RFone is now supported officially
* ImGUI was updated
* MacOS no longer uses vcpkg for building

# Bugfixes

... a lot of them, with a large majority of those related to Windows...
