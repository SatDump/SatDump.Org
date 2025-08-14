---
layout: post
title:  "Beyond POES: what to do with amateur weather satellite reception?"
date:   2025-08-14 14:00:00 +0200
tags:   release
authors: [lego11, aang23]
---

*This article was written by lego11 and originally published on his website, [www.a-centauri.com](https://www.a-centauri.com/). We decided to publish it here to give it the widest circulation possible, for the best interests of the satellite community.*

After the eventual decommissioning of the last POES satellite (NOAA-15, known as The King), many satellite amateurs are worried about the end of the hobby, given the apparent lack of satellites to receive imagery from. However, this is far from the truth! Here are a few misconceptions and how the future might look like after even the King needs to pass on its throne and reign to some other satellite.

## Meteor-M (Метеор-М) satellites

Contrary to popular belief, the LRPT transmission is not much harder to receive than APT and only needs the same hardware and software (SatDump). No other adjustments are needed, other than perhaps the purchase of an inexpensive SAW-filtered LNA from Aliexpress to improve the reception in interference-prone areas (APT was a bit more resilient to that, as for example VDL2 bursts caused thin lines on APT that were barely visible).

![Schema del Meteor-M2](/assets/beyond-poes/meteor-m2en.jpg) 

Roscosmos has recently announced that Meteor-M satellites are here to stay, with the launch of at least four more spacecrafts (numbers 5 through 8), with the option of two more (9 and 10).

These are expected to be launched as far as 2033, pushing the availability of the easily receivable LRPT transmissions on 137 MHz well into the 2040s. At that point, I will be over 42 years old, so who knows what happens by then!

Modern Meteor satellites have proven more reliable than Meteor-M N°2 and N°1, which both were experimental models that were different from the series productions ones (2-2 through 2-8). For example, the failure modes on Meteor-M N°2 and N°1 were corrected on more modern satellites, so it is very likely these can have a six-year or more life span.

![Immagine decodificata](/assets/beyond-poes/MeteorFrance.png)  <br />
*Meteor-M LRPT imagery, RGB321*

The Russian constellation will always consist of at least two satellites, with an option for a third in early morning orbit, similar to Meteor-M N°2.

These satellites also transmit a very strong signal on HRPT in the 1.7 GHz band, that is stronger than the POES HRPT signal and easily receivable on a portable helicone antenna, excellent for high quality data reception on the go.

Further refinements to the helicone antenna concept, including the design of a foldable version by OE1RCI (Richi) who has done an excellent job in turning my idea into reality, are expected in the future and this will make portable receptions even easier, especially for those that have limited LoS at home.

![Helicone](/assets/beyond-poes/helicone.jpg)  <br />
*A helicone from OE1RCI in use to receive Meteor-M N°2-3*

If you still haven't tried received Meteor-M, here is [a guide](https://www.a-centauri.com/articoli/meteor-satellite-reception) to do it on the 137 MHz band (LRPT), and here is [another guide](https://www.a-centauri.com/articoli/easy-hrpt-guide) for HRPT. It is easy to receive and it will delight you with beautiful calibrated imagery that is ready even for scientific use.

## Meteor-MP (Метеор-МП) 

These improved Meteor-M satellites will sport new, improved instruments. They will be transmitting their data on 137 MHz LRPT, L-band AHRPT (same as current Metop) and X band, and will be launched in the late 2030s, lasting well into the 2050s.

![Helicone](/assets/beyond-poes/meteor-mp.jpg)  <br />
*Meteor-MP satellite render. Note the 137 MHz QFH antenna for LRPT, and the usual conical antenna for L-band AHRPT.*

## Metop satellites

The Metop-B and Metop-C satellites are expected to stay according to EUMETSAT at least until 2027 and 2030 respectively, and their downlink on the L Band is also quite easy to receive with a small 80 to 100cm dish. 

They can also be done easily on a helicone, although naturally there will be some minor compromise to be found. For best results they require a wider SDR than the normal RTL-SDR, although nowadays this is easy to find. SDRs such as the HydraSDR are perfect for this task.

![Metop](/assets/beyond-poes/metop.jpg) 

If you still haven't tried Metop, here is [a guide](https://www.a-centauri.com/articoli/easy-hrpt-guide) to help you.

## Arctic Weather Satellite and STERNA series

These satellite series transmit microwave radiometric data on the L band at 1707 MHz with parameters similar to Metop.

While less "shiny" and "sexy" than visual imagery, this data is nevertheless quite important and can be used to complement Meteor data for weather forecasting. 

AWS is already transmitting and almost calibrated in SatDump (will be in a matter of days). This means that radiometric data will then be available for forecasting use, including measuring geopotential height, cloud top temperature, total precipitable water and much more. With a little bit of practice, you'll be able to make better forecasts than your weather application, even just by using AWS.

![EPS Sterna](/assets/beyond-poes/eps-sterna.jpg)  <br />
*Arctic Weather Satellite imaging the boundary between hot, wet air (black) and cool, dry air (white) as a front is passing over Italy*

AWS is also notable for dumping on the same easily receivable L-band frequency when in view of its ground station in Kiruna (Sweden) with exactly the same parameters of the direct broadcast. This means that whole orbits can be projected easily.

![EPS Sterna](/assets/beyond-poes/eps-sterna-dump.jpg)  <br />
*Arctic Weather Satellite dump from [@Aang23](https://twitter.com/aang254/) © Aang23*

Three more satellites (STERNA 1 through 3) are planned and they will be identical to AWS, except the instrument will be improved. The last will be launched in 2030 and is expected to run at least until 2042.

If you still haven't tried AWS, here is [a guide](https://www.a-centauri.com/articoli/easy-hrpt-guide) to help you. The parameters and difficulty are very similar to Metop.

## Elektro-L (Электро-Л)

These Russian geostationary satellites transmit easily receivable signals on the L band, on 1691 MHz (HRIT and LRIT). The system employs three satellites, covering most of the globe except the Americas.

![Electro](/assets/beyond-poes/electro.jpg)  <br />
*Elektro-L constellaton as of August 2025*

Currently, only Elektro-L N°3 and N°4 transmit on 1691 MHz because of a failure on the power supply of N°2 (affecting the L band transmitter), which is currently stationed over Europe.

This will change on October 22, 2025: the Elektro-L N°5 satellite will be launched, and it will be stationed over the Indian Ocean at the current position of Elektro-L N°3 (76°E).

After a brief testing period of a few months, Elektro-L N°3 will then be moved to the position of Elektro-L N°2 (14.5°W): this means, that **Europe will once again have LRIT/HRIT access**, which it hasn't had since 2018 when EUMETSAT decided to turn off HRIT on its Meteosat satellites.

The new Elektro-L N°5 will do HRIT/LRIT at 30 minutes interval, compared to 3 hours for older satellites. It is likely the 30 minute interval will be applied on N°3 as well.

![Elektro-L MSU-GS](/assets/beyond-poes/msugs.jpg)  <br />
*MSU-GS reception from Elektro-L N°3 with HRIT, by Slawek*

More Elektros are planned for launch, including N°6 (2030), N°7 (2032) and improved models, Elektro-M N°1 (2035) and N°2 (2036). These improved models will feature a new imager (MSU-GSM) with better resolution and more spectral bands, and will keep the LRIT/HRIT transmitter as it is needed for remote Siberian weather centers and villages.

Each time a new Elektro launches, the constellation gets "turned" counterclockwise, so Europe will then get N°4, N°5, N°6 and so on.

I will be installing shortly an X band station dedicated to Elektro-L N°2 (and in the future N°3), which will allow me to design many new calibrated L2 products for weather forecasting. These will include cloud type, wind vectors and all the other good stuff you can obtain from your usual weather website, except from your antenna (HRIT included)!

![ELEKTRO HRIT](/assets/beyond-poes/hrit.png)  <br />
*Elektro-L N°3 HRIT from the latest SatDump, entirely calibrated and ready for scientific use*

### GOES

Although this article was primarily written from the Eurasian perspective, people in the Americas will be pleased to know that GOES-U (GOES-18 and GOES-19) satellites will continue to operate and transmit HRIT and GRB well into the 2030s.

### EWS-G

Following the success of EWS-G1 (ex GOES-13), the USSF has opted to replace it with GOES-15. If and when it breaks, it will be replaced by either GOES-14, -16 or -17 and the EWS missions are expected to continue for years to come. The GVAR broadcast on L band is more challenging to receive than HRIT from Elektro-L satellites, but it is doable on a low budget.

![GVAR](/assets/beyond-poes/ewsg.jpg)  <br />
*A GVAR reception from EWS-G2 by @bosslike5*

Because GVAR is not cropped (like HRIT is), if the Moon is in the correct position EWS-G satellites will image it.

![GVAR](/assets/beyond-poes/ewsg_moon.jpg)  <br />
*The Moon on EWS-G2 by @bosslike5*


## S band

This band is not strictly related to weather satellites, but it is nonetheless interesting, especially for those that like new challenges or SWLing. The barrier for entry is very low, with inexpensive MMDS hardware that can be found for 50 euros or less.

A guide on how to begin with S band [is available](https://www.a-centauri.com/articoli/the-definitive-s-band-satellite-guide)

### Jason-3

This is a very interesting satellite because it does a world-wide dump in direct broadcast, so by receiving enough passes you can build a world map of radiation, altimetry and humidity. SatDump recently improved support for it. Hams can build radiation maps of the globe, helping them with shortwave DX activity.

![JASON](/assets/beyond-poes/jason.png)  <br />
*Jason-3 radiometric data showing the South Atlantic Anomaly*

### UVSQSat-NG

This French satellite dumps high resolution imagery on S band when in view of the ground station in Paris. 

![JASON](/assets/beyond-poes/uvsqsat.png)  <br />
*UVSQSat-NG camera*

### DMSP

These two satellites (DMSP 5D-3 F17 and DMSP 5D-3 F18) transmit unencrypted data containing medium resolution imagery, including night-time imagery (artificial lights) when over the contiguous US (CONUS, no Hawaii or Alaska). It can also be received from neighboring countries such as Canada or Mexico.

These satellites also go unencryped when over the poles (Antarctica and the Arctic Ocean), which means that people in Northern Europe, Russia and Southern Australia and Argentina can get it unencrypted.

![DMSP](/assets/beyond-poes/dmsp.jpg)  <br />
*DMSP 5D-3 F18 received by [Scott Tilley](https://twitter.com/coastal8049) (VE7TIL). © Scott Tilley.*

### Other S band satellites worth mentioning

* HINODE: sun imagery
* ISS: the ISS does DATV DVB-S on S band.
* Proba-2: sun imagery

![Immagine decodificata](/assets/beyond-poes/SWAP_2024_Eclipse.gif)  <br />
*Proba-2 SWAP imagery of the 2014 Solar Eclipse over the USA*

## X band

It is widely known that modern weather satellite constellations only transmit on the X band, and many people think this band is unobtanium.

However, this was also true for L band back in the day!

For example, a L band station in 2010 would cost around 2000 euros, not including the dish and rotator and not adjusted for inflation.

When I got into X band, the price was already inferior to that - it was 1000 euros. With recent improvements to the SDR panorama and new downconverters, the price can go below 500 euros easily. 

Many people are developing X band LNAs that will be cost competitive, but a good solution can already be bought now for 150 euros from Down East Microwave Inc.

Computers also got more powerful, so much so that a ~400€ refurbished laptop is capable of recording 245 MHz of bandwidth, which is enough to do LandSat receptions.

A new software-defined radio that is capable of at least 100 MHz of bandwidth for a competitive price could also be available in the near future.

All in all, X band is looking great for the future and it is likely it will reach price parity with a current good quality HRPT setup (i.e. with G4DDK and Sysmocom filter, so around 200 euros) in the next 3 to 4 years.

Investing in an X band station is a good idea right now, especially gathering the components besides the SDR and settling temporarily with a lesser SDR (even just a HackRF can obtain FengYun-3G and Aqua).
It is not true that you need a rotator for X band. It is also not true that it is impossible to track: in fact yours truly does it on a daily basis and finds it quite fun!

If you still haven't looked into doing X band, there is [a guide to help you](https://www.a-centauri.com/articoli/an-x-band-primer), of course!

### Meteor-M KMSS (Метеор-М КМСС)

All the Meteor satellites except N°2-3 do, or will do KMSS imagery in direct broadcast over the X band. This is 60 meters per pixel imagery in the classic "CIR" (Color Infrared) three channels, similar to the old LandSat TM and IR film cameras for aerophotogrammetry.

![EPS Sterna](/assets/beyond-poes/kmss.jpg)  <br />
*A view of the Vesuvius wildfire from KMSS direct broadcast*

This broadcast is quite strong and can be received with a BladeRF, as it is 61.44 MSym/s (same as all the other broadcasts transmitted with the «Soviet modulator»). With the upcoming wideband SDRs, it will be easily receivable.

### Meteor-M dumps

Meteor-M dumps imagery and other data over three ground stations: Moscow, Novosibirsk and Ekaterinburg. 

![EPS Sterna](/assets/beyond-poes/meteor_gs.png) 

There are both narrow (15.75 Msym/s) and wide (61.44 Msym/s) dumps. Wide dumps contain KMSS recordings from other parts of the world, entire MSU-MR orbits, MeteoSAR (radar) acquisitions. Narrow dumps carry 12-orbit MTVZA dumps, and IKFS hyperspectral soundings.

![MTVZA dump](/assets/beyond-poes/mtvza_dump.jpg)  <br />
*Entire-Earth MTVZA dump from Meteor-M N°2-4*

Currently SatDump supports KMSS and MTVZA dumps, but others will be supported once we have some samples. 

The narrow band dumps are very interesting, because they can be received with an inexpensive SDR such as an HackRF or PlutoPlus.

### FengYun-3

These satellites are very strong in the X band and receivable even with cheap X band SDRs such as the PlutoPlus. They are very varied and the series is expected to go on for many years, and have frequent launches. Future launches include FengYun-3H (like FengYun-3D), FengYun-3I (like FengYun-3G) and FengYun-3J (like FengYun-3E), which will complement the existent ones for many years to come, at least until 2035. MERSI instruments will also be calibrated shortly within SatDump, providing gorgeous true color images, high resolution 250 m/px infrared and much more.

![FY3D](/assets/beyond-poes/fy3d.jpg)  <br />
*FengYun-3D MERSI-II showing wildfires in Greece aumnd Turkey*

### GEO-KOMPSAT-2A (GK-2A) UHRIT

Support for GK-2A UHRIT (on the X band) was added recently into SatDump. It provides very high quality images of Asia, Oceania and the Pacific. The images are completely calibrated and delightful for amateurs in those regions. GK-2A also transmits LRIT and HRIT on the L band, naturally.

![GK2A UHRIT](/assets/beyond-poes/uhrit.jpg)  <br />
*GEO-KOMPSAT-2A UHRIT True Color received by [@eswnl](https://twitter.com/eswnl) © John Bell*

### Elektro-L RDAS (Электро-Л РДАС)

Elektro satellits transmit raw data from MSU-GS at 15 minute intervals (30 on Elektro-L N°2). This signal is fairly strong for what it is (it is beamed at two ground stations: Moscow for N°2 and N°3, and Vladivostok for N°4) and can be received from most places in Europe, although the signal does vary a bit throughout the year.

Since the signal is raw, the Moon can sometimes be spotted too on Elektro RDAS.

![MSUGS RDAS Moon](/assets/beyond-poes/msugs_rdas.jpg)  <br />
*MSU-GS imaging the Moon, received with RDAS.*

### Metop-SG

The new Metop Second Generation satellite series is the upcoming European satellite series complementing and then replacing Metop B and C. The first, Metop-SG-A1, has just been launched and will be in service for about a decade, or more. Three doublets (one imager satellite, one sounder satellite) are planned in the constellation.
The BladeRF is adequate for this transmission, even though it is quite wide at 80 Msym/s. Future wideband SDRs will be easily able to receive these transmissions, and the satellites include several interesting instruments.

### SatDump DSP improvements

As already witnessed by the community with FengYun-2H SVISSR and GOES-15 GVAR, SatDump has already improved considerably with respect to digital signal processing. SNRs that would have resulted in a blurry image a few years ago now yield much better quality images. But that doesn't stop there!

The DSP improvements will carry on to the X band, with the goal being to make it possible to do **LIVE** X band on a mid-range computer.

For example, initial testing on my Fujitsu LIFEBOOK E5412 laptop, with i5-1235U CPU, allowed a good quality **live** reception of Elektro-L N°2 RDAS and this was only an initial test. This means that future X band decoding will be faster and will use up less energy, which is important for laptops.

### SatDump v2.0.0

It is not a secret anymore: SatDump will be updated to version 2.0.0, bringing many new features and improving a lot on many fronts. [Here](https://www.satdump.org/posts/towards-2.0.0/) is a more in depth discussion on the upcoming update.

## Challenges

There will undoubtedly be some challenges in the future. The current political situation on Earth in the Western world is very unfavourable for space exploration and (especially) Earth observation, and the push for commercialization has resulted in some missions, such as PREFIRE, being encrypted for no good reason: sometimes, even the mission specialists themselves have no idea their downlinks are encrypted! However, the bulk of the weather satellites will remain unencrypted, given it is a requirement stated in the CGMS (part of the World Meteorological Organization).

## Conclusion

The satellite panorama is changing, but the hobby is not going away. 
In the railfanning community, many people predicted the hobby would fade away into nothing during the 60s and 70s when railway companies were scrapping steam engines in favour of diesel and electric locomotives. What happened instead was the reverse: new technology enabled new possibilities, the lowering cost of film, cameras and railway tickets made it possible for younger people to enjoy the hobby more. It will be the same for the satellite hobby: improvements in the computers, the lower cost for SDRs, and new developments in software and hardware will open up countless possibilities for the future. 

There will be many surprises, and I will be the author of some of these surprises, as will be the SatDump team. Questions? Head on over [the SatDump Discord server](https://discord.gg/ctt3M8pRYG) (or [Matrix](https://github.com/SatDump/SatDump), if you prefer - both are connected)
Will you be part of the future? I hope so!

## Acknowledgements

I thank Aang23 (F4LAU), Aweeri, bosslike5, ElMarko (2M0IIG), Meti, Richi OE1RCI, seler1500, for their help in writing and proofreading this article. 
I thank also Scott Tilley (VE7TIL) for his excellent DMSP image, John Bell for his true color GK-2A UHRIT image, bosslike5 for his GVAR images, Aang23 for his AWS dumps (and the work on SatDump naturally!)