---
title: Satellite List
icon: fas fa-book
order: 4
---

When looking for the operational status of some satellites & their instruments, I noticed there doesn't appear to be a combined list for all.
Thats why I compiled this list and wrote together information on (almost) all satellites that are featured in satDump.
Maybe its useful to someone - if you spot any mistakes or want to add to it, please let me know! 
I made this list with the best of my knowledge, but mistakes can always happen - Crosswalkersam

Thanks to Zbychu, Aang23, SnazzLazz and Carl Reinemann for double checking this list! 


## Orbiting satellites

### NOAA-15 [[Norad 25338](https://celestrak.org/NORAD/elements/gp.php?CATNR=25338)]

| Frequency  | Status | Downlink type | Location |
| ------------- | ------------- | ------------- | ------------- |
| DSB (137.35MHz) | Active  | DB | Global |
| APT (137.62MHz) | Active  | DB | Global |
| HRPT (1702.5MHz) | Active | DB | Global |
| GAC (2247.5MHz) | Active | Dump | Wallops [US] |

| Instrument  | Status |
| ------------- | ------------- |
| AVHRR 3 | Working (degraded) |
| HIRS | Working (degraded) |
| AMSU A | Working |
| AMSU B | Defective |
| SEM | Working |

### NOAA-18 [[Norad 28654](https://celestrak.org/NORAD/elements/gp.php?CATNR=28654)]

| Frequency  | Status | Downlink type | Location |
| ------------- | ------------- | ------------- | ------------- |
| DSB (137.35MHz) | Active  | DB | Global |
| APT (137.9125MHz) | Active  | DB | Global |
| HRPT (1707MHz) | Active | DB | Global |
| HRPT (2247.5MHz) | Active | DB | Global |
| GAC (1698MHz) | Active | Dump | Wallops [US] |

| Instrument  | Status |
| ------------- | ------------- |
| AVHRR 3 | Working |
| MHS | Defective |
| HIRS  | Defective |
| AMSU A | Working |
| SEM  | Working |
| SBUV  | Defective |

### NOAA-19 [[Norad 33591](https://celestrak.org/NORAD/elements/gp.php?CATNR=33591)]

| Frequency  | Status | Downlink type | Location |
| ------------- | ------------- | ------------- | ------------- |
| DSB (137.77MHz) | Active | DB | Global |
| APT (137.1MHz) | Active | DB | Global |
| HRPT (1698MHz) | Active | DB | Global |
| GAC (1702.5 MHz) | Active | Dump | Wallops [US] and Svalbard [NOR]|

| Instrument  | Status |
| ------------- | ------------- |
| AVHRR 3 | Working |
| MHS | Working (degraded) |
| HIRS  | Defective (?) |
| AMSU A | Working |
| SEM  | Working |
| SBUV  | Defective |

### METEOR-M N1 [[Norad 35865](https://celestrak.org/NORAD/elements/gp.php?CATNR=35865)]

| Frequency  | Status | Downlink type | Location |
| ------------- | ------------- | ------------- | ------------- |
| LRPT (137.1/.9MHz) | Inactive | DB | Global |
| HRPT (1700MHz) | Inactive | DB | Global |
| C-Band (3405MHz) | Inactive | DB | Global |
| X-Band 1 (8120MHz) | Inactive | Dump | Moscow [RUS] |
| X-Band 2 (8320MHz) | Inactive | Dump | Moscow [RUS] |

| Instrument  | Status |
| ------------- | ------------- |
| MSU-MR | Deactivated |

Annotation: METEOR-M N1 suffered a loss of attitude. It was completely deactivated, some rare activity on 1700Mhz.

### METEOR-M N2 [[Norad 40069](https://celestrak.org/NORAD/elements/gp.php?CATNR=40069)]

| Frequency  | Status | Downlink type | Location |
| ------------- | ------------- | ------------- | ------------- |
| LRPT (137.1/.9MHz) | Inactive | DB | Global |
| HRPT (1700MHz) | Inactive | DB | Global |
| C-Band (3405MHz) | Unknown | DB | Global |
| X-Band 1 (8120MHz) | Unknown | Dump | Moscow [RUS] |
| X-Band 2 (8320MHz) | Unknown | Dump | Moscow [RUS] |

| Instrument  | Status |
| ------------- | ------------- |
| MSU-MR | Deactivated |
| KMSS | Deactivated |
| Severjanin-M | Deactivated |
| IKFS-2 | Deactivated |
| GGAK | Working (?) |

Annotation: METEOR-M N2 suffered a loss of attitude on 24/12/2022. Because of that, most instruments have been deactivated and recovery is unlikely.
Only instruments that do not require NADIR continue to work.

### METEOR-M N2-2 [[Norad 44387](https://celestrak.org/NORAD/elements/gp.php?CATNR=44387)]

| Frequency  | Status | Downlink type | Location |
| ------------- | ------------- | ------------- | ------------- |
| LRPT (137.1/.9MHz) | Inactive | DB | Global |
| HRPT (1700MHz)  | Active | DB | Global |
| C-Band (3405MHz)  | Active | DB | Global |
| X-Band 1 (8120MHz)  | Active | Dump | Moscow [RUS] |
| X-Band 2 (8320MHz)  | Active | Dump | Moscow [RUS] |

| Instrument  | Status |
| ------------- | ------------- |
| MSU-MR | Working |
| KMSS | Working |
| Severjanin-M | Defective |
| MTVZA | Deactivated |
| GGAK | Working |

Annotation: A depressurization accured and N2-2 leaked coolant, causing some parts of the sat to overheat. Due to this,  LRPT is unavailable.
MTVZA may be switched on and off randomly (Deactivated as of 21/05/2023).

Update 28/01/2023: HRPT is now also active at night, and not limited by daylight. 

### METEOR-M N2-3 [[Norad 57166](https://celestrak.org/NORAD/elements/gp.php?CATNR=57166)]

| Frequency  | Status | Downlink type | Location |
| ------------- | ------------- | ------------- | ------------- |
| LRPT (137.1/.9MHz) | Inactive | DB | Global |
| HRPT (1700MHz)  | Active | DB | Global |
| C-Band (3405MHz)  | Active | DB | Global |
| X-Band 1 (8120MHz)  | Active | Dump | Moscow [RUS] |
| X-Band 2 (8320MHz)  | Active | Dump | Moscow [RUS] |

| Instrument  | Status |
| ------------- | ------------- |
| MSU-MR | Working |
| KMSS | Working |
| Severjanin-M | Unknown |
| MTVZA | Deactivated |
| GGAK | Working |

### METOP-A [[Norad 29499](https://celestrak.org/NORAD/elements/gp.php?CATNR=29499)]

| Frequency  | Status | Downlink type | Location |
| ------------- | ------------- | ------------- | ------------- |
| LRPT (137.1/.9MHz) | Inactive | DB | Global |
| AHRPT (1701.3MHz) | Inactive | DB | Global |
| S-Band (2230MHz) | Inactive | DB | Global |
| X-Band (7800MHz)  | Inactive | Dump | Svalbard [NOR] |

Annotation: METOP-A was decomissioned.

### METOP-B [[Norad 38771](https://celestrak.org/NORAD/elements/gp.php?CATNR=38771)]

| Frequency  | Status | Downlink type | Location |
| ------------- | ------------- | ------------- | ------------- |
| AHRPT (1701.3MHz)  | Active | DB | Global |
| S-Band (2230MHz) | Active | DB | Global |
| X-Band (7800MHz)  | Active | Dump | Svalbard [NOR] |

| Instrument  | Status |
| ------------- | ------------- |
| AVHRR 3 | Working |
| MHS | Working |
| HIRS | Working |
| AMSU A1 | Working |
| AMSU A2 | Working |
| SEM  | Working |
| ASCAT  | Working |
| IASI  | Working |
| GOME  | Working |

### METOP-C [[Norad 43689](https://celestrak.org/NORAD/elements/gp.php?CATNR=43689)]

| Frequency  | Status | Downlink type | Location |
| ------------- | ------------- | ------------- | ------------- |
| AHRPT (1701.3MHz)  | Active | DB | Global |
| S-Band (2230MHz) | Active | DB | Global |
| X-Band (7800MHz)  | Active | Dump | Svalbard [NOR] |

| Instrument  | Status |
| ------------- | ------------- |
| AVHRR 3 | Working |
| MHS | Working (degraded) |
| AMSU A1 | Working |
| AMSU A2 | Working |
| SEM  | Working |
| ASCAT  | Working |
| IASI  | Working |
| GOME  | Working |

### YUNHAI 1 / 3 [Norad 41856 / 54235]

| Frequency  | Status | Downlink type | Location |
| ------------- | ------------- | ------------- | ------------- |
| L-band (1704MHz) | Active | DB | Global |

Annotation: Encrypted.

### ANGELS [[Norad 44876](https://celestrak.org/NORAD/elements/gp.php?CATNR=44876)]

| Frequency  | Status | Downlink type | Location |
| ------------- | ------------- | ------------- | ------------- |
| L-band (1703MHz) | Active | DB | Global |

### SARAL [[Norad 39086](https://celestrak.org/NORAD/elements/gp.php?CATNR=39086)]

| Frequency  | Status | Downlink type | Location |
| ------------- | ------------- | ------------- | ------------- |
| L-band ARGOS (1698.4MHz) | Active | DB | Global |
| S-band (2245MHz) | Active | Dumps | Unknown |
| X-band (8212.5MHz) | Active | Dumps | Svalbard [NOR] |

### OCEANSAT-2 [[Norad 35931](https://celestrak.org/NORAD/elements/gp.php?CATNR=35931)]

| Frequency  | Status | Downlink type | Location |
| ------------- | ------------- | ------------- | ------------- |
| S-band (2245MHz) | Active | DB | Global |
| X-band (8212.5MHz) | Inactive | Dumps | Svalbard [NOR] and Unknown [IND] |

| Instrument  | Status |
| ------------- | ------------- |
| OCM-2 | Deactivated |
| SCAT | Defective |
| ROSA | Defective |

### OCEANSAT-3 [[Norad 54361](https://celestrak.org/NORAD/elements/gp.php?CATNR=54361)]

| Frequency  | Status | Downlink type | Location |
| ------------- | ------------- | ------------- | ------------- |
| L-band ARGOS (1703MHz) | Active | DB | Global |
| S-band (2250MHz) | Active | Dumps | Svalbard [NOR] and Unknown [IND] |
| X-band (8275MHz) | Active | Dumps | Svalbard [NOR] and Unknown [IND] |

| Instrument  | Status |
| ------------- | ------------- |
| OCM-3 | Working |
| OSCAT-3 | Working |
| SSTM | Working |

### OTB-3 (GAZELLE) [[Norad 54023](https://celestrak.org/NORAD/elements/gp.php?CATNR=54023)]

| Frequency  | Status | Downlink type | Location |
| ------------- | ------------- | ------------- | ------------- |
| L-band (1703MHz) | Active | DB | Global |

### FENGYUN 3-A [[Norad 32958](https://celestrak.org/NORAD/elements/gp.php?CATNR=32958)]

| Frequency  | Status | Downlink type | Location |
| ------------- | ------------- | ------------- | ------------- |
| AHRPT (1704.5MHz) | Inactive | DB | Global |
| S-Band (22XXMHz) | Active | DB | Global |
| MPT (7775MHz) | Inactive | DB | Global |
| DPT (8145.95MHz)  | Inactive | Dump | Unknown [CHN] and Kiruna [SWE] |

| Instrument  | Status |
| ------------- | ------------- |
| MERSI-I | Deactivated |
| ERM-I | Deactivated |
| IRAS | Deactivated |
| MWHS-I | Deactivated |
| MWRI-I | Deactivated |
| MWTS-I | Deactivated |
| SBUS | Deactivated |
| SIM-I | Deactivated |
| TOU | Deactivated |
| VIRR | Deactivated |

Annotation: FENGYUN 3-A has been decomissioned.

### FENGYUN 3-B [[Norad 37214](https://celestrak.org/NORAD/elements/gp.php?CATNR=37214)]

| Frequency  | Status | Downlink type | Location |
| ------------- | ------------- | ------------- | ------------- |
| AHRPT (1704.5MHz) | Inactive | DB | Global |
| S-Band (22XXMHz) | Active | DB | Global |
| MPT (7775MHz) | Inactive | DB | Global |
| DPT (8145.95MHz) | Inactive | Dump | Unknown [CHN] and Kiruna [SWE] |

| Instrument  | Status |
| ------------- | ------------- |
| MERSI-I | Deactivated |
| ERM-I | Deactivated |
| IRAS | Deactivated |
| MWHS-I | Deactivated |
| MWRI-I | Deactivated |
| MWTS-I | Deactivated |
| SBUS | Deactivated |
| SIM-I | Deactivated |
| TOU | Deactivated |
| VIRR | Deactivated |

Annotation: FENGYUN 3-B has been decomissioned.

### FENGYUN 3-C [[Norad 39260](https://celestrak.org/NORAD/elements/gp.php?CATNR=39260)]

| Frequency  | Status | Downlink type | Location |
| ------------- | ------------- | ------------- | ------------- |
| AHRPT (1701.3MHz) | Active | DB | China |
| MPT (7780MHz) | Inactive | DB | China |
| DPT (UnknownMHz) | Active | Dump | Unknown [CHN] |

| Instrument  | Status |
| ------------- | ------------- |
| MERSI-I | Deactivated |
| ERM-I | Working |
| GNOS-I | Working |
| IRAS | Working |
| MWHS-II | Working |
| MWRI-I | Deactivated |
| MWTS-II | Working |
| SBUS | Working |
| SIM-II | Working |
| TOU | Working |
| VASS | Working |
| VIRR | Working |

### FENGYUN 3-D [[Norad 43010](https://celestrak.org/NORAD/elements/gp.php?CATNR=43010)]

| Frequency  | Status | Downlink type | Location |
| ------------- | ------------- | ------------- | ------------- |
| AHRPT (7820MHz) | Active | DB | Global |
| DPT (8250MHz) | Active | Dump | Unknown [CHN] and Kiruna [SWE] |

| Instrument  | Status |
| ------------- | ------------- |
| MERSI-II | Working |
| GAS | Working |
| GNOS-I | Working |
| HIRAS-I | Working |
| IPM | Working |
| MWHS-II | Working |
| MWRI-I | Working |
| MWTS-II | Working |
| SEM | Working |
| WAI | Working |

### FENGYUN 3-E [[Norad 49008](https://celestrak.org/NORAD/elements/gp.php?CATNR=49008)]

| Frequency  | Status | Downlink type | Location |
| ------------- | ------------- | ------------- | ------------- |
| AHRPT (7860MHz)  | Active | DB | Global |
| DPT (8212.5MHz)  | Active | Dump | Unknown [CHN] and Kiruna [SWE] |

| Instrument  | Status |
| ------------- | ------------- |
| MERSI-LL | Working |
| GNOS-II | Working |
| HIRAS-II | Working |
| MWHS-II | Working |
| MWTS-III | Working |
| SEM | Working |
| SIM-II | Working |
| SSIM | Working |
| Tri-IPM | Working |
| WindRAD | Working |
| X-EUVI | Partially working |

Annotation: X-EUVI is fully functional, but the X-Ray channel is inactive, only EUV is being transmitted.

### FENGYUN 3-G [[Norad 56232](https://celestrak.org/NORAD/elements/gp.php?CATNR=56232)]

| Frequency  | Status | Downlink type | Location |
| ------------- | ------------- | ------------- | ------------- |
| AHRPT (7790MHz)  | Active | DB | Global |
| S-Band (2243MHz)  | Active | DB | Global |

| Instrument  | Status |
| ------------- | ------------- |
| MERSI-RM | Working |
| PMR-Radar | Working |
| MWRI-RM | Working |
| SIPMAI | Deactivated |
| HAOC | Deactivated |

Annotation: While the S-Band transmitter is active, it appears to be unmodulated as of 23/04/23.

Update: 19/05/2023, the satellite has been rotated 180 degrees, as visible on all instruments.

### PROBA-1 [[Norad 26958](https://celestrak.org/NORAD/elements/gp.php?CATNR=26958)]

| Frequency  | Status | Downlink type | Location |
| ------------- | ------------- | ------------- | ------------- |
| S-Band (2235MHz) | Active | Dump | Redu [BEL] |

| Instrument  | Status |
| ------------- | ------------- |
| CHRIS | Deactivated |
| HRC | Working (Degraded) |
| DEBIE | Working |
| SEM | Working |

Annotation: On 19/01/2023, ESA officially declared the "CHRIS" instrument's mission as completed. SEM, DEBIE and HRC data will still be acquired.

### PROBA-2 [[Norad 36037](https://celestrak.org/NORAD/elements/gp.php?CATNR=36037)]

| Frequency  | Status | Downlink type | Location |
| ------------- | ------------- | ------------- | ------------- |
| S-Band (2235MHz) | Active | Dump | Redu [BEL] |

| Instrument  | Status |
| ------------- | ------------- |
| SWAP | Working |
| LYRA | Working |
| TPMU | Working |
| DSLP | Working |
| X-CAM | Deactivated |

### PROBA-V [[Norad 39159](https://celestrak.org/NORAD/elements/gp.php?CATNR=39159)]

| Frequency  | Status | Downlink type | Location |
| ------------- | ------------- | ------------- | ------------- |
| S-Band (2235MHz) | Active | Dump | Redu [BEL] |
| X-Band (8090MHz) | Inactive | Dump | Kiruna [NOR] |

| Instrument  | Status |
| ------------- | ------------- |
| Vegetation Imager | Working |
| EPS | Working |

Annotation: Although PROBA-V's mission has been declared completed, it sometimes transmits preview-data from its vegetation instrument on S-band. It is yet unclear if it will fully resume its duty and start dumping on X-Band aswell. PROBA-V was also seen transmitting GPS data.

### CORIOLIS [[Norad 27640](https://celestrak.org/NORAD/elements/gp.php?CATNR=27640)]

| Frequency  | Status | Downlink type | Location |
| ------------- | ------------- | ------------- | ------------- |
| S-Band (2221.5MHz) | Active | DB | Global |
| X-Band (Unknown MHz) | Active | Dump | SafetyNet? |

| Instrument  | Status |
| ------------- | ------------- |
| WINDSAT | Working |
| SMEI | Deactivated |

Annotation : SMEI is functional as far as it is known. Shutdown due to program funding issues.

### CLOUDSAT [[Norad 29107](https://celestrak.org/NORAD/elements/gp.php?CATNR=29107)]

| Frequency  | Status | Downlink type | Location |
| ------------- | ------------- | ------------- | ------------- |
| S-Band (2217.5MHz) | Active | Dump | Redu [BEL] / Wallops [US] |

| Instrument  | Status |
| ------------- | ------------- |
| CPR | Working |

### SCISAT-1 [[Norad 27858](https://celestrak.org/NORAD/elements/gp.php?CATNR=27858)]

| Frequency  | Status | Downlink type | Location |
| ------------- | ------------- | ------------- | ------------- |
| S-Band (2232MHz) | Active | Dump | Kiruna [SWE], Quebec [CAN], etc |

| Instrument  | Status |
| ------------- | ------------- |
| MAESTRO | Working |
| FTS | Working |

Annotation : Dumps are done to various Canadian groundstation. No exhaustive list available.

### CHEOPS [[Norad 44874](https://celestrak.org/NORAD/elements/gp.php?CATNR=44874)]

| Frequency  | Status | Downlink type | Location |
| ------------- | ------------- | ------------- | ------------- |
| S-Band (2208.5) | Active | Dump | Torrejon de Ardoz [SPA] |

| Instrument  | Status |
| ------------- | ------------- |
| CIS | Working |

### SMAP [[Norad 40376](https://celestrak.org/NORAD/elements/gp.php?CATNR=40376)]

| Frequency  | Status | Downlink type | Location |
| ------------- | ------------- | ------------- | ------------- |
| S-Band (2274.3MHz) | Active | Dump | Svalbard [NOR], NEN |
| X-Band (8180MHz) | Active | Dump | Svalbard [NOR], NEN |

| Instrument  | Status |
| ------------- | ------------- |
| SAR | Working |
| Radiometer | Working |

Annotation: While S-Band is active, it only seems to transmit filler.

### GRACE-FO 1 [[Norad 43476](https://celestrak.org/NORAD/elements/gp.php?CATNR=43476)]

| Frequency  | Status | Downlink type | Location |
| ------------- | ------------- | ------------- | ------------- |
| S-Band (2211MHz) | Active | Dump | Svalbard [NOR] |

| Instrument  | Status |
| ------------- | ------------- |
| MWI | Working |
| LRI | Working |

### GRACE-FO 2 [[Norad 43477](https://celestrak.org/NORAD/elements/gp.php?CATNR=43477)]

| Frequency  | Status | Downlink type | Location |
| ------------- | ------------- | ------------- | ------------- |
| S-Band (2260.5MHz) | Active | Dump | Svalbard [NOR] |

| Instrument  | Status |
| ------------- | ------------- |
| MWI | Working |
| LRI | Working |

### JASON-3 [[Norad 41240](https://celestrak.org/NORAD/elements/gp.php?CATNR=41240)]

| Frequency  | Status | Downlink type | Location |
| ------------- | ------------- | ------------- | ------------- |
| S-Band (2215.92MHz) | Active | Dump | Kiruna [SWE], Wallops [US]? |

| Instrument  | Status |
| ------------- | ------------- |
| POSEIDON | Working |
| AMR-2 | Working |
| LPT | Working |

### MATS [[Norad 54227](https://celestrak.org/NORAD/elements/gp.php?CATNR=54227)]

| Frequency  | Status | Downlink type | Location |
| ------------- | ------------- | ------------- | ------------- |
| S-Band (2214MHz) | Active | Dump | Kiruna [SWE] |

| Instrument  | Status |
| ------------- | ------------- |
| NADIR | Working |
| UV | Working |
| IR A | Working |
| IR BG | Working |

### TUBIN [[Norad 48900](https://celestrak.org/NORAD/elements/gp.php?CATNR=48900)]

| Frequency  | Status | Downlink type | Location |
| ------------- | ------------- | ------------- | ------------- |
| S-Band 1 (2263MHz) | Active | Dump | Berlin [GER] |
| S-Band 2 (2266MHz) | Active | Dump | Berlin [GER] |
| X-Band (8392.5MHz) | Active | Dump | Berlin [GER] and Svalbard [NOR] |

| Instrument  | Status |
| ------------- | ------------- |
| Imager | Working |
| SOLID | Working |


### AIM [[Norad 31304](https://celestrak.org/NORAD/elements/gp.php?CATNR=31304)]

| Frequency  | Status | Downlink type | Location |
| ------------- | ------------- | ------------- | ------------- |
| S-Band (2282.5MHz) | Inactive | Dump | Svalbard [NOR] and Wallops [US] |

| Instrument  | Status |
| ------------- | ------------- |
| CDE | Working |
| CIPS | Working |
| SOFIE | Working |

Annotation: On 16/03/2023, NASA declared AIM's mission finished due to a battery failure. It still transmits in the daylight.

### IRIS [[Norad 39197](https://celestrak.org/NORAD/elements/gp.php?CATNR=39197)]

| Frequency  | Status | Downlink type | Location |
| ------------- | ------------- | ------------- | ------------- |
| S-Band (2220.8MHz) | Active | Dump | Svalbard [NOR] |
| X-Band (8483MHz) | Active | Dump | Svalbard [NOR] |

| Instrument  | Status |
| ------------- | ------------- |
| UV telescope & Spectrograph | Working |

### OPS-SAT [[Norad 44878](https://celestrak.org/NORAD/elements/gp.php?CATNR=44878)]

| Frequency  | Status | Downlink type | Location |
| ------------- | ------------- | ------------- | ------------- |
| S-Band (2229.5MHz) | Active | Dump | SMILE [Darmstadt, GER] |
| X-Band (8176MHz) | Active | Dump | SMILE [Darmstadt, GER] |

| Instrument  | Status |
| ------------- | ------------- |
| Camera | Working |

### DMSP 17 [[Norad 29522](https://celestrak.org/NORAD/elements/gp.php?CATNR=29522)]

| Frequency  | Status | Downlink type | Location |
| ------------- | ------------- | ------------- | ------------- |
| RTD (2252.5MHz) | Active | DB | Global (Encrypted, but clear over the US and the Poles) |

| Instrument  | Status |
| ------------- | ------------- |
| OLS | Working |
| SSMIS | Working |

Annotation: Is encrypted, but transmits in the clear when over the US or the poles.

### DMSP 18 [[Norad 35951](https://celestrak.org/NORAD/elements/gp.php?CATNR=35951)]

| Frequency  | Status | Downlink type | Location |
| ------------- | ------------- | ------------- | ------------- |
| RTD (2252.5MHz) | Active | DB | Global (Encrypted, but clear over the US and the Poles) |

| Instrument  | Status |
| ------------- | ------------- |
| OLS | Working |
| SSMIS | Working |

Annotation: Is encrypted, but transmits in the clear when over the US or the poles.

### SWARM A [[Norad 39452](https://celestrak.org/NORAD/elements/gp.php?CATNR=39452)]

| Frequency  | Status | Downlink type | Location |
| ------------- | ------------- | ------------- | ------------- |
| S-Band (2249MHz) | Active | Dump | Kiruna [SWE] |

| Instrument  | Status |
| ------------- | ------------- |
| ASM | Working |
| VFM | Working |
| EFI | Working |

### SWARM B [[Norad 39451](https://celestrak.org/NORAD/elements/gp.php?CATNR=39451)]

| Frequency  | Status | Downlink type | Location |
| ------------- | ------------- | ------------- | ------------- |
| S-Band (2270MHz) | Active | Dump | Kiruna [SWE] |

| Instrument  | Status |
| ------------- | ------------- |
| ASM | Working |
| VFM | Working |
| EFI | Working |

### SWARM C [[Norad 39453](https://celestrak.org/NORAD/elements/gp.php?CATNR=39453)]

| Frequency  | Status | Downlink type | Location |
| ------------- | ------------- | ------------- | ------------- |
| S-Band (2277MHz) | Active | Dump | Kiruna [SWE] |

| Instrument  | Status |
| ------------- | ------------- |
| ASM | Working |
| VFM | Working |
| EFI | Working |

### HINODE [[Norad 29479](https://celestrak.org/NORAD/elements/gp.php?CATNR=29479)]

| Frequency  | Status | Downlink type | Location |
| ------------- | ------------- | ------------- | ------------- |
| S-Band (2256.22MHz) | Active | Dump | Svalbard [NOR] |
| X-Band (8460.81MHz) | Unknown | Dump | Svalbard [NOR]? |

| Instrument  | Status |
| ------------- | ------------- |
| SOT | Unknown |
| EIS | Unknown |
| XRT | Unknown |

Annotation : Data is being produced, but no detection of the X-Band link was ever possible...

### INTEGRAL [[Norad 27540](https://celestrak.org/NORAD/elements/gp.php?CATNR=27540)]

| Frequency  | Status | Downlink type | Location |
| ------------- | ------------- | ------------- | ------------- |
| S-Band (2215MHz) | Active | Dump | ? |

| Instrument  | Status |
| ------------- | ------------- |
| SPI | Working |
| IBIS | Working |
| JEM-X | Working |
| OMC | Working |

### SWOT [[Norad 54754](https://celestrak.org/NORAD/elements/gp.php?CATNR=54754)]

| Frequency  | Status | Downlink type | Location |
| ------------- | ------------- | ------------- | ------------- |
| S-Band (2282.4MHz) | Active | Dump | Svalbard [NOR], Inuvik [CAN], Hartebeesthoek [ZA], Kourou [FRG] and Kerguelen [FRA] |
| X-Band (8205MHz) | Active | Dump | Svalbard [NOR] |

| Instrument  | Status |
| ------------- | ------------- |
| LRA | Working |
| POSEIDON-3C | Working |
| KaRIN | Working |
| AMR-S | Working |
| DORIS-NG | Working |

### BLUEWALKER-3 [[Norad 53807](https://celestrak.org/NORAD/elements/gp.php?CATNR=53807)]

| Frequency  | Status | Downlink type | Location |
| ------------- | ------------- | ------------- | ------------- |
| VHF (437.5MHz) | Active | Dump | SSC Network |
| GSM (Unknown) | Unknown | DB | Global |
| S-Band (2245MHz) | Active | Dump | SSC Network |

| Instrument  | Status |
| ------------- | ------------- |
| Engineering camera | Working |

Annotation: BLUEWALKER-3 is now encrypted.

### FORMOSAT-5 [[Norad 42920](https://celestrak.org/NORAD/elements/gp.php?CATNR=42920)]

| Frequency  | Status | Downlink type | Location |
| ------------- | ------------- | ------------- | ------------- |
| S-Band (2215MHz) | Active | Dump | Kiruna [SWE] |
| X-Band (Unknown) | Unknown | Dump | Kiruna [SWE] |

| Instrument  | Status |
| ------------- | ------------- |
| AIP | Working |
| RSI | Working |

Annotation : X-Band is likely encrypted.

### BRITE-PL2 [[Norad 40119](https://celestrak.org/NORAD/elements/gp.php?CATNR=40119)]

| Frequency  | Status | Downlink type | Location |
| ------------- | ------------- | ------------- | ------------- |
| S-Band (2234.4MHz) | Active | Dump | Unknown [POL] |

| Instrument  | Status |
| ------------- | ------------- |
| BSP | Unknown |

### NOAA-20 (JPSS-1) [[Norad 43013](https://celestrak.org/NORAD/elements/gp.php?CATNR=43013)]

| Frequency  | Status | Downlink type | Location |
| ------------- | ------------- | ------------- | ------------- |
| S-Band (2247.5MHz) | Active | DB | Global |
| HRD (7812MHz) | Active | DB | Global |
| Ka-Band (26703.4MHz) | Active | Dump | Svalbard [NOR] |

| Instrument  | Status |
| ------------- | ------------- |
| ATMS | Working |
| CERES | Working |
| CrIS | Working |
| OMPS | Working |
| VIIRS | Working |

### NOAA-21 (JPSS-2) [[Norad 54234](https://celestrak.org/NORAD/elements/gp.php?CATNR=54234)]

| Frequency  | Status | Downlink type | Location |
| ------------- | ------------- | ------------- | ------------- |
| S-Band (2247.5MHz) | Active | DB | Global |
| HRD (7812MHz) | Active | DB | Global |
| Ka-Band (26703.4MHz) | Active | Dump | Svalbard [NOR] |

| Instrument  | Status |
| ------------- | ------------- |
| ATMS | Working |
| CrIS | Working |
| OMPS | Working |
| VIIRS | Working |

### SUOMI-NPP [[Norad 37849](https://celestrak.org/NORAD/elements/gp.php?CATNR=37849)]

| Frequency  | Status | Downlink type | Location |
| ------------- | ------------- | ------------- | ------------- |
| X-Band (7812MHz) | Active | DB | Global |
| X-Band (8212.5Mhz) | Active | Dumps | Svalbard [NOR] |
| Ku-Band (15003.4Mhz) | Active | Dumps | TDRS |

| Instrument  | Status |
| ------------- | ------------- |
| ATMS | Working |
| CERES | Working |
| CrlS | Working |
| OMPS | Working |
| VIIRS | Working |

### SMOS [[Norad 36036](https://celestrak.org/NORAD/elements/gp.php?CATNR=36036)]

| Frequency  | Status |
| ------------- | ------------- |
| S-Band (Unknown MHz) | Active |
| X-Band (8150MHz) | Active |

| Instrument  | Status |
| ------------- | ------------- |
| MIRAS | Working |

### AQUA [[Norad 27424](https://celestrak.org/NORAD/elements/gp.php?CATNR=27424)]

| Frequency  | Status | Downlink type | Location |
| ------------- | ------------- | ------------- | ------------- |
| S-Band (2287.5 MHz) | Active | DB and Dump | Global, dumps to NEN or TDRS|
| X-Band (8160MHz) | Active | DB and Dump | Global, dumps to Svalbard [NOR] |

| Instrument  | Status |
| ------------- | ------------- |
| MODIS | Working |
| AMSU A1 | Working |
| AMSU A2 | Defective |
| AMSR-E | Defective |
| HSB | Defective |
| CERES 1 | Working |
| CERES 2 | Working (degraded) |
| AIRS | Working |

### TERRA [[Norad 25994](https://celestrak.org/NORAD/elements/gp.php?CATNR=25994)]

| Frequency  | Status | Downlink type | Location |
| ------------- | ------------- | ------------- | ------------- |
| S-Band (2287.5 MHz) | Active | DB | Global, TDRS |
| X-Band (8212.5MHz) | Active | DB | Global |
| Ku-Band (~15000MHz) | Active | Dumps | TDRS |

| Instrument  | Status |
| ------------- | ------------- |
| ASTER | Working |
| CERES | Working |
| MISR | Working |
| MODIS | Working |
| MOPITT | Working |

Annotation: On X-Band, only MODIS data.

### AURA [[Norad 28376](https://celestrak.org/NORAD/elements/gp.php?CATNR=28376)]

| Frequency  | Status | Downlink type | Location |
| ------------- | ------------- | ------------- | ------------- |
| S-Band (2287.5 MHz) | Active | DB & Dump | Global, dumps to Svalbard [NOR] or TDRS|
| X-Band (8160MHz) | Active | DB & Dump | Global, dumps to Svalbard [NOR] |

| Instrument  | Status |
| ------------- | ------------- |
| HIRDLS | Working |
| MLS | Working |
| OMI | Working |
| TES | Working |

Annotation: OMI is the sole X-Band instrument.

### CRYOSAT-2 [[Norad 36508](https://celestrak.org/NORAD/elements/gp.php?CATNR=36508)]

| Frequency  | Status | Downlink type | Location |
| ------------- | ------------- | ------------- | ------------- |
| S-Band (2201MHz) | Active | Dump | Kiruna [SWE] |
| X-Band (8100MHz) | Active | Dump | Kiruna [SWE] |

| Instrument  | Status |
| ------------- | ------------- |
| SIRAL | Working |

### ARKTIKA-M 1 [[Norad 47719](https://celestrak.org/NORAD/elements/gp.php?CATNR=47719)]

| Frequency  | Status | Downlink type | Location |
| ------------- | ------------- | ------------- | ------------- |
| L-Band DCP (1703MHz) | Active | Transponder | Global |
| L-Band CGAK (1701MHz) | Inactive | DB | Global |
| RDAS (7865MHz) | Active | Dump | Moscow [RUS] and Unknown |

| Instrument  | Status |
| ------------- | ------------- |
| GGAK-VE | Unknown |
| MSU-GS/VE | Working |

Annotation : The CGAK downlink was active in the first few weeks, and has remained off since.

### GCOM-W1 [[Norad 38337](https://celestrak.org/NORAD/elements/gp.php?CATNR=38337)]

| Frequency  | Status | Downlink type | Location |
| ------------- | ------------- | ------------- | ------------- |
| S-Band (2220MHz) | Active | Dump | Kiruna [SWE] |
| X-Band (8245MHz) | Active | Dump | Svalbard [NOR] |

| Instrument  | Status |
| ------------- | ------------- |
| AMSR-2 | Working |

### GCOM-C1 [[Norad 43065](https://celestrak.org/NORAD/elements/gp.php?CATNR=43065)]

| Frequency  | Status | Downlink type | Location |
| ------------- | ------------- | ------------- | ------------- |
| S-Band (2220MHz) | Active | Dump | Kiruna [SWE] |
| X-Band (8105MHz) | Active | Dump | Svalbard [NOR] |

| Instrument  | Status |
| ------------- | ------------- |
| SGLI | Working |

### CALIPSO [[Norad 29108](https://celestrak.org/NORAD/elements/gp.php?CATNR=29108)]

| Frequency  | Status | Downlink type | Location |
| ------------- | ------------- | ------------- | ------------- |
| S-Band (2268.5MHz) | Active | Dump | Wallops [US] |
| X-Band (8330MHz) | Unknown | Dump | Wallops [US] |

| Instrument  | Status |
| ------------- | ------------- |
| IIR | Unknown |
| ILT | Unknown |
| WFC | Unknown |

### PAZ [[Norad 43215](https://celestrak.org/NORAD/elements/gp.php?CATNR=43215)]

| Frequency  | Status | Downlink type | Location |
| ------------- | ------------- | ------------- | ------------- |
| S-Band (2285MHz) | Active | Dump | Kiruna [SWE] |
| X-Band (8150MHz) | Active | Dump | Spain |

| Instrument  | Status |
| ------------- | ------------- |
| SAR | Working |

### CFOSAT [[Norad 43662](https://celestrak.org/NORAD/elements/gp.php?CATNR=43662)]

| Frequency  | Status | Downlink type | Location |
| ------------- | ------------- | ------------- | ------------- |
| S-Band (2262.5MHz) | Active | DB | Global |
| X-Band (8304MHz) | Active | Dump | Kiruna [KIR], Unknown [CHN] |

| Instrument  | Status |
| ------------- | ------------- |
| SCAT | Working |
| SWIM | Working |

### PRISMA [[Norad 44072](https://celestrak.org/NORAD/elements/gp.php?CATNR=44072)]

| Frequency  | Status | Downlink type | Location |
| ------------- | ------------- | ------------- | ------------- |
| S-Band (2283.5MHz) | Active | Dump | Italy |
| X-Band 1 (8120MHz) | Active | Dump | Italy |
| X-Band 2 (8250MHz) | Active | Dump | Italy |

| Instrument  | Status |
| ------------- | ------------- |
| HYC | Working |
| Pan camera | Working |

Annotation: PRISMA is encrypted.

### AEOLUS [[Norad 43600](https://celestrak.org/NORAD/elements/gp.php?CATNR=43600)]

| Frequency  | Status | Downlink type | Location |
| ------------- | ------------- | ------------- | ------------- |
| S-Band (2205MHz) | Inactive | Dump | Kiruna [SWE] |
| X-Band (8040MHz) | Inactive | Dump | Svalbard [NOR] |

| Instrument  | Status |
| ------------- | ------------- |
| ALADIN | Deactivated |

Annotation : AEOLUS has now been decomissioned.

### STEREO A/B [Norad 29510/29511]

| Frequency  | Status | Downlink type | Location |
| ------------- | ------------- | ------------- | ------------- |
| X-Band (8443.52MHz) | Active | DB and Dump | Global and dumps to DSN |

| Instrument  | Status |
| ------------- | ------------- |
| SECCHI | Working |
| IMPACT | Working |
| PLASTIC | Unknown |
| SWAVES | Unknown |

### LANDSAT 8/9 [Norad 39084/49260]

| Frequency  | Status | Downlink type | Location |
| ------------- | ------------- | ------------- | ------------- |
| S-Band (2282.3MHz) | Active | Dump | Kiruna [SWE], NEN |
| X-Band (8200.5MHz) | Active | DB and Dump | Global and dumps to a few stations, Svalbard [NOR] |

| Instrument  | Status |
| ------------- | ------------- |
| OLI| Working |
| TIRS | Working |

### SENTINEL 6 [[Norad 46984](https://celestrak.org/NORAD/elements/gp.php?CATNR=46984)]

| Frequency  | Status | Downlink type | Location |
| ------------- | ------------- | ------------- | ------------- |
| S-Band (2256.75MHz) | Active | Dump | Kiruna [SWE] |
| X-Band (8090MHz) | Active | Dump | Svalbard [NOR], Kiruna [SWE] |

| Instrument  | Status |
| ------------- | ------------- |
| POSEIDON 4| Working |
| AMR-C | Working |
| HRMR | Working |
| REM | Working |

## Geostationary satellites

### ELEKTRO-L2 [[Norad 41105](https://celestrak.org/NORAD/elements/gp.php?CATNR=41105)]

| Frequency  | Status |
| ------------- | ------------- |
| xRIT (1691MHz) | Inactive |
| L-Band CGAK (1693MHz) | Active |
| RDAS (7500MHz) | Active |

| Instrument  | Status |
| ------------- | ------------- |
| MSU-GS | Working (degraded) |
| GGAK-E | Working |
| SKIF-6 | Working |
| SKL-E | Working |
| ISP-2M | Working |

Annotation: RDAS is LHCP. The xRIT payload has failed.

### ELEKTRO-L3 [[Norad 44903](https://celestrak.org/NORAD/elements/gp.php?CATNR=44903)]

| Frequency  | Status |
| ------------- | ------------- |
| xRIT (1691MHz) | Active |
| L-Band CGAK (1693MHz) | Active |
| RDAS (7500 MHz) | Active |

| Instrument  | Status |
| ------------- | ------------- |
| MSU-GS | Working |
| GGAK-E | Working |
| SKIF-6 | Working |
| SKL-E | Working |
| ISP-2M | Working |

Annotation: HRIT transmissions at 00:12, 03:12, 06:12, 09:12, 12:12, 15:12, 18:12 and 21:12 UTC. LRIT same hours at XX:42.

Annotation: RDAS is RHCP.

### ELEKTRO-L4 [[Norad 55506](https://celestrak.org/NORAD/elements/gp.php?CATNR=55506)]

| Frequency  | Status |
| ------------- | ------------- |
| xRIT (1691MHz) | Active |
| L-Band CGAK (1693MHz) | Active |
| RDAS (7500 MHz) | Active |

| Instrument  | Status |
| ------------- | ------------- |
| MSU-GS | Working |
| GGAK-E | Working |
| SKIF-6 | Working |
| SKL-E | Working |
| ISP-2M | Working |

### EWS-G1 (GOES-13) [[Norad 29155](https://celestrak.org/NORAD/elements/gp.php?CATNR=29155)]

| Frequency  | Status |
| ------------- | ------------- |
| GVAR (1685.7MHz) | Active |
| SD (1676MHz) | Active |
| CDA (1694MHz) | Active |
| LRIT (1691MHz) | Inactive |
| MDL (1681.418MHz) | Inactive |

| Instrument  | Status |
| ------------- | ------------- |
| SXI | Defective |
| SEM | Working |
| Sounder  | Defective |
| Imager | Working (degraded) |
| S&R | Defective |

Annotation: The scan mechanism is failing. EWS-G1 will probably be decomissioned soon and replaced with GOES-15.

### GOES-14 [[Norad 35491](https://celestrak.org/NORAD/elements/gp.php?CATNR=35491)]

| Frequency  | Status |
| ------------- | ------------- |
| GVAR (1685.7MHz) | Inactive |
| SD (1676MHz) | Inactive |
| CDA (1694MHz) | Active |
| LRIT (1691MHz) | Active |
| MDL (1681.418MHz) | Inactive |

| Instrument  | Status |
| ------------- | ------------- |
| SXI | Working, Deactivated |
| SEM | Working, Deactivated |
| Sounder  | Working, Deactivated |
| Imager | Working, Deactivated |
| S&R | Working, Deactivated |

Annotation: Even though the LRIT transponder is active, it appears that no data is transmitted at the moment.

Update 03/02/2023: G14 has reached its new position and is now stable at 108.2°W.

Annotation: G14 is rarely active, booted up for a yearly check-up or support to GOES-16/17/18.

### GOES-15 [[Norad 36411](https://celestrak.org/NORAD/elements/gp.php?CATNR=36411)]

| Frequency  | Status |
| ------------- | ------------- |
| GVAR (1685.7MHz) | Inactive |
| SD (1676MHz) | Inactive |
| CDA (1694MHz) | Active |
| LRIT (1691MHz) | Active |
| MDL (1681.418MHz) | Inactive |

Annotation: Eventhough LRIT is active, it appears that no data is transmitted at the moment.
G15 is currently in in-orbit storage.

| Instrument  | Status |
| ------------- | ------------- |
| SXI | Working, Deactivated |
| SEM | Working, Deactivated |
| Sounder  | Working, Deactivated |
| Imager | Working, Deactivated |
| S&R | Working, Deactivated |

Annotation : GOES-15 being moved to become EWS-G2. Downlink activity to be determined once new operations begin.

### GOES-16 [[Norad 41866](https://celestrak.org/NORAD/elements/gp.php?CATNR=41866)]

| Frequency  | Status |
| ------------- | ------------- |
| HRIT (1694.1MHz) | Active |
| GRB (1686.6MHz) | Active |
| CDA (1693MHz) | Active |
| X-Band (8220MHz) | Active |

| Instrument  | Status |
| ------------- | ------------- |
| ABI | Working |
| SUVI | Working |
| EXIS  | Working |
| GLM | Working |
| SEISS | Working |
| MAG | Working |
| DCS | Working |

### GOES-17 [[Norad 43226](https://celestrak.org/NORAD/elements/gp.php?CATNR=43226)]

| Frequency  | Status |
| ------------- | ------------- |
| HRIT (1694.1MHz) | Inactive |
| GRB (1686.6MHz) | Inactive |
| CDA (1693MHz) | Active |
| X-Band (8220MHz) | Inactive |

| Instrument  | Status |
| ------------- | ------------- |
| ABI | Working (degraded), Deactivated |
| SUVI | Working, Deactivated |
| EXIS  | Working, Deactivated |
| GLM | Working, Deactivated |
| SEISS | Working, Deactivated |
| MAG | Working, Deactivated |
| DCS | Working, Deactivated |

Annotation: Due to a problem with the cooling system, GOES-17 was replaced with GOES-18 and is now a backup. 
That is why G17 is beeing moved to in-orbit storage at 104.7°W where GRB and HRIT will no longer be available.

### GOES-18 [[Norad 51850](https://celestrak.org/NORAD/elements/gp.php?CATNR=51850)]

| Frequency  | Status |
| ------------- | ------------- |
| HRIT (1694.1MHz) | Active |
| GRB (1686.6MHz) | Active |
| CDA (1693MHz) | Active |
| X-Band (8220MHz) | Active |

| Instrument  | Status |
| ------------- | ------------- |
| ABI | Working |
| SUVI | Working |
| EXIS  | Working |
| GLM | Working |
| SEISS | Working |
| MAG | Working |
| DCS | Working |

### GK-2A [[Norad 43823](https://celestrak.org/NORAD/elements/gp.php?CATNR=43823)]

| Frequency  | Status |
| ------------- | ------------- |
| LRIT (1692.14MHz) | Active |
| HRIT (1695.4MHz) | Active |
| CDAS (Unknown MHz) | Unknown |

### FENGYUN-2G [[Norad 40367](https://celestrak.org/NORAD/elements/gp.php?CATNR=40367)]

| Frequency  | Status |
| ------------- | ------------- |
| S-VISSR (1687.5MHz) | Active |

| Instrument  | Status |
| ------------- | ------------- |
| VISSR-II | Working |

### FENGYUN-2H [[Norad 43491](https://celestrak.org/NORAD/elements/gp.php?CATNR=43491)]

| Frequency  | Status |
| ------------- | ------------- |
| S-VISSR (1687.5MHz) | Active |

| Instrument  | Status |
| ------------- | ------------- |
| VISSR-II | Working |

### FENGYUN-4A [[Norad 41882](https://celestrak.org/NORAD/elements/gp.php?CATNR=41882)]

| Frequency  | Status |
| ------------- | ------------- |
| LRIT (1697MHz) | Active |
| HRIT (1679MHz) | Active |

| Instrument  | Status |
| ------------- | ------------- |
| AGRI | Working |
| GIIRS | Working |
| LMI | Working |
| SEP | Working |

### FENGYUN-4B [[Norad 48808](https://celestrak.org/NORAD/elements/gp.php?CATNR=48808)]

| Frequency  | Status |
| ------------- | ------------- |
| LRIT (1697MHz) | Active |
| HRIT (1679MHz) | Active |

| Instrument  | Status |
| ------------- | ------------- |
| AGRI | Working |
| GIIRS | Working |
| GHI | Working |
| SEP | Working |
