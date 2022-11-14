---
layout: post
title:  "Decoding BW-3"
date:   2022-10-27 12:20:00 +0200
tags: release
---

# Introduction

For a while now, the BlueWalker-3 has been continuously monitored by amateurs worldwide including myself due to it's very controversial nature (won't go in details about it here. See [Scott Tilley](https://twitter.com/coastal8049)'s posts of the topic), both optically and on UHF/S-Band.   

Daniel Estévez published a [first analysis of the UHF downlink back in September](https://twitter.com/ea4gpz/status/1572681924421865472), and later of the [S-Band downlink](https://destevez.net/2022/10/decoding-the-bluewalker-3-s-band-downlink/).   

Both downlinks were quite quite stange. But about a week ago, likely due to the incoming deployment at the time S-Band began being a lot more active, containing what clearly was mainly house-keeping and other telemetry that's not easy to make sense of blindly.

CADU Frames :

![](/assets/decoding_bluewalker3_downlink/FhUYQCsWYAAeFhK.png)

One frame type :

![](/assets/decoding_bluewalker3_downlink/FhFcN-VWYAAZeL4.png)

At some unknown point between Daniel's analysis and me updating the pipelines in SatDump, the CADU length for the narrow (128k GFSK, 1/2) downlink changed from 355 bytes to 331. You may note this is odd number is not common for CCSDS CADUs... And that's not the only thing making it quite non-compliant. Thankfully though, as of today the frame period has remained the same.  

Here we are going to be going through my findings decoding [CrossWalkerSam's](https://twitter.com/Crosswalkersam) reception on the 14th of November 2022, around 2:40 UTC which resulted in decoding imagery from the onboard camera, apparently before deployment took place.

# "CADU" Analysis

I say "CADU" because this is definitely not CCSDS compliant.   

![](/assets/decoding_bluewalker3_downlink/bw3_cadu.png)

As you may see above, things start with the usual 0x1acffc1d CCSDS sync. Then, after one unused byte there is some sort of header before some payload data. This data area ends with a 32-bits CRC, which I have not yet attempted to reverse-engineer. The frame is then finished with what seems like Reed-Solomon parity check symbols, but they do not match CCSDS configurations (68 bytes of parity check? CCSDS only allows either 16 or 32 per block. None of them allows getting 68 bytes) and finally a single, static byte. No clue why that one is there.  

It's definitely a bit weird their (potential) RS is not compliant, and having so much filler in the downlink feels a bit wasteful.

# Header/Format analysis

So, first of all back when I got my hands on some initial data, I found out the second byte after the header was a frame type ID. This is how the frames shown int the introduction were isolated.  

In the imagery data, after finding out the frames contained valid JPEG signatures (0xFFD8FFE0) I isolated them the same way. The marker for those ended up being 217 decimal.

![](/assets/decoding_bluewalker3_downlink/header.png)

So first, to confirm this was indeed imagery I dumped some data from the payload area starting from one of the JPEG headers... And was able to see a bit of the imagery.

![](/assets/decoding_bluewalker3_downlink/first_img.png)

Hence... I started reverse-engineering the header. This was mostly isolating the various counters to identify what they were doing.

Therefore, I initially started reading the 16-bits counter that starts on byte 17 (little-endian format). This revealed it was always increasing by 198, which happens to be the number of bytes in the payload area. It was also resetting every so often to near-0, which lead me to believe some bigger payloads needed to be reconstructed.  

So, I then proceeded to analyze the 8-bits right after this counter in correlation with the previous counter. Everytime the previous counter would go to 0, those 8-bits would indicate something different than 198, otherwise always 198. That once again indicated there was some further packetization, hence I wrote something to extract those packets.

![](/assets/decoding_bluewalker3_downlink/internal_pkts.png)

And... Bingo! :-). There was a 64-bits header visible, directly followed by JPEG signatures once in a while (highlighted in blue). Dumping those provided nearly-proper JPEG imagery... But unfortunately relying on their header proved unreliable with the signal-level, so I am searching for signatures manually in order to extract the data.

![](/assets/decoding_bluewalker3_downlink/BlueWaker3_Cam_2.png)
![](/assets/decoding_bluewalker3_downlink/BlueWaker3_Cam_3.png)
![](/assets/decoding_bluewalker3_downlink/BlueWaker3_Cam_4.png)

# Final findings

| 0-3     | ASM                     | 0x1acffc1d                                                      |
|---------|-------------------------|-----------------------------------------------------------------|
| 5       | Frame Type              | uint8_t                                                         |
| 17-18   | Current Payload Pointer | uint16_t, LE                                                    |
| 19      | First Header Pointer    | uint16_t, LE. Equal to payload area size if no header is present|
| 21-218  | Payload Area            | Varies                                                          |
| 219-222 | CRC                     | Unknown, not attempted                                          |
| 262-331 | RS? + Static value?     | Unknown                                                         |

Other packets type also appear to use the same format, but using them this way did not reveal anything useful either.  
Also keep in mind the payload area size is likely to change if the CADU size changes.  

The image data is just standard 1280x720p JPEG files.

# Conclusion

As this imagery was received ~10 hours before AST confirmed a full deployment, this confirms it was not fully deployed on previous observations, which was an unknown at the time. Though, this does at least confirm their downlink is definitely not CCSDS-compliant!

An implementation of everything detailled here was added to SatDump, if further image dumps are ever captured again.

