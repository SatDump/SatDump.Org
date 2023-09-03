---
layout: post
title:  "Using the tracking widget"
date:   2023-09-03 10:00:00 -0600
tags: tutorial
authors: [kf0cjj, co2esp]
---

The tracking widget can be used to control a rotator and track a satellite.
It can also be used to predict when certain satellites will pass overhead, and automatically track it, control an sdr and recieve signals from it, 
and then process the data.

# Interface



![](/assets/tracking_widget/allWidget.png)

There are a few different sections of the widget, and we will go through them all

## Polar Plot

![](/assets/tracking_widget/polarPlot.png)

The polar plot is a chart of azimuth and elevation. The top of the plot is 360/0 deg azimuth,
the right is 90 deg azimuth, bottom is 180, and left is 270. The center of the plot
is 90 deg elevation. The first ring from the middle is 60 deg, and the second is 30 deg.

With this plot, we can see many things,
+ orange line, this is the satellites path
+ red dot, this is where the satellite currently is
+ blue cross, this is where the rotator is moving torwards
+ blue circle, this is where the rotator is currently pointing

In the top left corner, we can see some information about the spacecraft,
+ Spacecrafts name
+ Current location
+ Loss of signal/Acquisition of signal

## Satellite Selector

![](/assets/tracking_widget/satSelector1.png)

The satellite selector allows you to choose which object you are tracking. It has 2 modes, Satellites from tle,
and objects from JPL horizons.

##### TLE
The TLE mode will read from a list of TLEs in the satdump folder.

##### Horizons
The horizons mode will take a second to load, as it has to request data from the JPL horizons server. If you are
not connected to the internet, it will not work. This mode is useful for things that do not orbit earth, as you cant make a TLE for them.

## Object Information

![](/assets/tracking_widget/objectInfo.png)

This displays information about the object you are tracking, such as,
+ az and el
+ next AOS/LOS
+ the change in az and el over a second


## INTERFACING SATDUMP WITH A ROTOR
Satdump features support for satellite tracking using a generic rotor interfacing through third party rotor controller daemons like Hamlib’s rotctld
and YO3DMU’s PstRotator. While Hamlib rotctld and PstRotator handles the hardware communications requirements and the specific rotor protocols and 
configuration, Satdump communicates with these apps at software level in a common and more generic protocols. This allows to basically control and command 
every single type of rotor supported by Hamlib rotctld and PstRotator without having to deal with complex or specific rotor settings in Satdump.
Such option allows to have either the rotor controller connected directly to the same PC where Satdump is running but also to connect via network
to a remote different computer that handles the rotor.


![](/assets/tracking_widget/rotator1.png)

### Rotor UI

- Rotor positions. First Column shows the Azimut and Second Column the Elevation.
* First row is an editable text box that shows the latest commanded position: it will be automatically updated when a satellite is being tracked. If the selected satellite is bellow horizon or not being tracked you can manually enter and type the desired position.
* Second row shows the actual position reported by the rotor, where is it pointing currently (while it´s connected to Rotctld or PstRotator.
- Rotor Control. This section defines enables the level of control over the rotor as well the controller daemon protocol.
* Engage: it enables the sending of position commands to the rotor. Whenever a new position is written and Engage is enabled, the rotor will be commanded to go there.
* Track: it enables the satellite tracking. When it is enabled the position entry text box will be automatically updated with the satellite position while it is above the horizon or the expected AOS position if it’s not in sight yet.
* Protocol Selection box: Click and select the protocol or type of controller daemon you want to use, currently only Rotctl and PstRotator are supported. Rotctl is preferred and highly recommended because it performs better with Satdump.
- Controller Daemon TCP/IP Settings. This section allows to configure the network communication settings with the controller daemon.
* Address: IP address of the computer where is the controller daemon server running. Enter “127.0.0.1” if Rotctld or PstRotator are running on the same computer as Satdump is, or the remote computer IP if the daemon is running on a different computer.
* Port: Defines the TCP port where is listening the daemon server; 4533 is Rotctld’s default port, while 4002 is the default for PstRotator.
- Connect/Disconnect. This button Connects and Disconnects from the daemon server controller.

Finally at the end of both Tracking and Rotator Configuration panel there is the “Schedule and Config” button. This will open a pop up window containing the “Scheduling” tab (refer to the Scheduling Guide for Automatic Processing and Recording of Tracked Satellites [documentation to be added]), and also a “Rotator Config” tab
![](/assets/tracking_widget/rotor03.png)
The Rotator Config Tab contains the Update Period entry text box. Here is possible to select the refresh rate for the rotor controller in seconds, the current position will be polled at that interval and as well the rotor will be commanded to go to the position at that rate in seconds too.

### USING HAMLIB’S ROTCTLD

This guide only cover the basic instructions for Rotctld. Please refer to [Hamlib’s documentation and guide](https://hamlib.sourceforge.net/html/rotctld.1.html){:target="_blank"}{:rel="noopener noreferrer"} for details on how to download and install it, as well to setup your rotor.

+ Launch rotctld app with the settings required for your specific hardware rotor controller.
+ Go to Satdump and Select Rotctl on Satdump Rotator Configuration panel.
+ Type the IP Address and TCP port as required (4533 is Rotctl default port).
+ Click Connect.
+ Click Engage to start sending commands to the rotor.
    
![](/assets/tracking_widget/rotor04.png)
    
(rotor06.png & rotor07.png) side by side or up/down if it fits better…)

### USING PSTROTATOR

This guide only cover the basic instructions for PstRotator. Please refer to [YO3DMU’s PstRotator Website](https://www.pstrotator.com/){:target="_blank"}{:rel="noopener noreferrer"} for details on how to download and install it, as well to setup your rotor.
Most of the configuration steps in PstRotator only needs to be done one single time as it will save the settings when closed.

#### Using PstRotator protocol, not recommended

+ Launch PstRotator and configure the settings for your specific hardware rotor controller.
+ On the Communication Menu, select and enable RS232 / TCP Server. This setting should be enabled by default.

![](/assets/tracking_widget/rotor08.png)

+ In Mode box at PstRotator select “Manual”. While PstRotator includes internal modules for both satellite and astronomical objects tracking it’s highly recommended not using them when using it with Satdump to avoid conflicts.
+ It’s also recommended to enable in the PstRotator Setup Menu the options “Start in Manual Mode” and “Localized KBD Shortcuts” to avoid conflicts and tracking issues.
+ Go to Satdump and Select PstRotator on Satdump Rotator Configuration panel.
+ Type the IP Address and TCP port as required (4002 is default PstRotator port).
+ Click in Connect.
+ Click Engage to start sending commands to the rotor.

#### Using PstRotator Hamlib Rotctld protocol emulation, highly recommended!!!

+ Launch PstRotator and configure the settings for your specific hardware rotor controller.
+ Navigate into Setup Menu and click to enable “Rotctld Hamlib Server”. Be sure you don’t have an actual Rotctld instance running as both apps will try to use the same TCP port.
![](/assets/tracking_widget/rotor09.png)
+ On the Communication Menu, click at “Rotctld Server Setup” and check that default port 4533 is selected. Also uncheck and verify it is not selected “Extended protocol”. Click Save Settings and press Escape to close the config dialog. 

![](/assets/tracking_widget/rotor11.png)

+ Go to Satdump and Select ROTCTL on Satdump Rotator Configuration panel, do not select PstRotator, as it is now emulating a Rotctld Daemon Server.
+ Type the IP Address and TCP port as required (4533 is default Rotctl port).
+ Click in Connect.
+ Click Engage to start sending commands to the rotor.






