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

# CLI (Aang23)

The Command-Line Interface (CLI) was also entirely reworked, and some major new features were added... That also clearly did cause some confusion so I thought it was also better to cover it here!   
First advice : forget how it *used* to work!

So, first of all now everything is handled through the main `satdump` command, which comprises 3 modes.

## Offline Processing

Just like in the UI, this mode assumes you already have a file to process. The general usage is :
```
satdump pipeline_name input_level input_file.xxx path/to/output_directory [options / parameters]
```

 - `pipeline_name` : Pipeline ID, as displayed when SatDump loads or in pipelines files (pipelines/*.json files)
 - `input_level` : Input level. This can be `baseband`, `cadu`, `frm`, `soft`, or even `products` depending on the input file. If providing a baseband that is **not** WAV / ZIQ, you will need to specify the format and samplerate manually with parameters
 - `input_file.xxx` : The input file. Either a baseband, demodulated symbols or frames (Or processed products, providing the dataset.json)
 - `path/to/output_directory` :  Directory where SatDump should write all processed/decoded files

 As for parameters, they can in reality be anything you see set in pipelines .json files. But usually, you will not need to change them manually. Though, some demodulator parameters may need to be set manually in many cases :
 - `samplerate` : If providing a baseband file, the samplerate of the input baseband file, in Samples Per Second (SPS) or Hz
 - `baseband_format` : If providing a baseband file, the baseband format, which can be :
    - `f32` : 32-bits IEEE Floats
    - `s16` : 16-bits signed integers (used in 16-bits WAV files)
    - `s8` : 8-bits signed integers
    - `u8` : 8-bits unsigned integers (used by 8-bits WAV files)
    - `ziq` : Custom ZIQ Baseband format, supporting ZSTD compression
- `dc_block` : If your SDR has a carrier at DC due to I/Q Imbalance (eg, HackRF) messing up the demodulator, this should be enabled
- `freq_shift` : Usually this should NOT be required, but it allows shfiting the baseband in frequency in case the recorded signal is not at DC (center)
- `iq_swap` : If your file has I & Q inverted. This will happen if using a downconverter with a "High" LO, that is, above the received frequency

And for a few real-world examples :
- `satdump metop_ahrpt baseband MetOp_Baseband.wav decoded_data/metop_baseband`   
  Decodes a MetOp AHRPT baseband. As the baseband is in WAV format, the samplerate and format will automatically be read from the header
- `satdump elektro_lrit baseband elektro_l3_lrit.s16 decoded_data/l3_lrit_baseband --samplerate 3e6 --baseband_format s16`  
  Decodes the provided ELEKTRO-L3 LRIT Baseband recorded in s16 format at 3MSPS
- `satdump npp_hrd cadu old_data/jpss1_data.cadu decoded_data/jpss1_hrd_data`  
  Decode instruments from an already decoded .cadu file. No other parameter is required

## Baseband Recording

While before baseband recording was in a separate tool, that is not the case anymore. Instead :  
`satdump record output_baseband_name --source src_name --samplerate device_samplerate --frequency device_frequency --baseband_format format [others parameters]`

 - `record` : Indicates SatDump you want to use the recording mode.
 - `output_baseband_name` : The output baseband name, without the extension. The extension will be set depending on the baseband format you set.

For parameters, you will at least need the following :
 - `source` : Source to use, eg `sdrplay`, `airspy`, `rtlsdr`, etc
 - `samplerate` : Samplerate to record at, in SPS or Hz
 - `frequency` : Frequency to tune the device at, in Hz
 - `baseband_format` : Same as for offline processing, with a few differences
   - `wav16` : To record in .wav format (s16, 16-bits)
   - `ziq` : This default to 8-bits. If you want to use another depth, you can add `--bit_depth 16` (can be 8, 16, or 32)
 - `timeout` : Entirely optional, but sets for how long, in seconds, SatDump should record for

Additionally, you will need to specify parameters for your specific SDR Device. A list can be found [here on GitHub](https://github.com/altillimity/SatDump/blob/master/docs/SDR-Options.md).

## Live Processing

### Normal Use

Live processing is *not* done through the ingestor as it used to be done. Instead it is done in a very similar way to the recorder and offline processing.
```
satdump live pipeline_name path/to/output_directory --source src_name --samplerate device_samplerate --frequency device_frequency [options / parameters]
```

As you may see, no input level has to be set, as it will always be baseband. See above for a detailled description of every option. The `timeout` feature is also available.

Additionally, live-processing in CLI mode can provide current status over HTTP. To do so, you need to set `--http_server 0.0.0.0:port` (eg, `--http_server 0.0.0.0:8080`). Once started, you will be able to access a http server providing the live state of the demodulator and decoder(s). That can useful for 24/7 setups where contant monitoring may be required.

For example, on GOES-R HRIT :
```
satdump live goes_hrit output_test_wtf --source rtlsdr --samplerate 2.4e6 --frequency 1694.1 --gain 40 --http_server 0.0.0.0:8080
```
Running `curl https://0.0.0.0:8080` will show the following, which can be fed into Grafana or other similar tools for monitoring.
```
{
    "ccsds_conv_r2_concat_decoder": {
        "deframer_lock": false,
        "rs_avg": 0,
        "viterbi_ber": 0.169677734375,
        "viterbi_lock": 1
    },
    "psk_demod": {
        "freq": 1096.974853515625,
        "peak_snr": 2.214721202850342,
        "snr": 0.1323898881673813
    }
}
```

### Server/Client - Network streaming

Another pretty requested features was the ability to only perform some of the steps locally, and forward to another SatDump instance(s) over the network. Perhaps to have a computer near your antenna decoding down to frames (CADUs for example) and another inside processing imagery. This is mostly intended for 24/7 Geo setups (LRIT, HRIT, GRB, HimawariCast, etc).  
The "server" is what would run on the side demodulating from an SDR, and the client what receives the data and finishes processing.

Do note that NOT all pipelines are currently supported in this mode. If you wish for one to be added, please open an issue on Github and it will be added.

Otherwise, starting the server-side is done in the same way as live processing and all flags still apply, except you will need to add the following flags :
 - `server_adress` : Adress to bind to. Usually 0.0.0.0 is fine
 - `server_port` : Port to bind to. You can use whatever you want!

Example for GOES-R GRB (with the http status server as well) :
```
satdump live goes_grb goes_grb_live_test --source bladerf --frequency 1686.6e6 --general_gain 28 --dc_block --samplerate 14e6 --server_address 0.0.0.0 --server_port 5004 --http_server 0.0.0.0:8081
``` 

The client will also be started in a very similar way, except of course all SDR-related parameters can be omitted. The `client` flag has to be passed alongside the `server_address` (with the IP address of the machine running the server) and `server_port`. Multiple clients can be connecting to the same server at the same time.  

Example :
```
./satdump live goes_grb goes_grb_live_test_client --server_address 192.168.1.54 --server_port 5004 --client
```