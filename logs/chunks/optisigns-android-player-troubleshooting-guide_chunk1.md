### In this article, we will troubleshoot the most common issues people encounter using our OptiSigns Android Player.

* [Identify Your Device](#Identify)
* [Best Practices](#BestPractices)
* [The Troubleshooting Option](#Troubleshooting)
* [Hardware Troubleshooting](#Hardware)
  + [Network Troubleshooting](#Network)
  + [Power Troubleshooting](#Power)
  + [HDMI & TV Connection Troubleshooting](#HDMI)
  + [Remote Control Troubleshooting](#RemoteControl)
  + [Changing Device Time Zone](#TimeZone)
  + [Blank Screen Troubleshooting](#BlankScreen)
  + [How to Factory Reset the OptiSigns Android Player](#FactoryReset)
* [Content Playback Troubleshooting](#ContentPlayback)
  + [Website display or sizing issues](#WebsiteDisplay)
  + [Designer or template sizing issues](#DesignerSizing)
  + [Screen color distortion](#ScreenColor)
  + [Fixing the OnHold warning](#OnHold)
  + [App crashing](#AppCrashing)
* [Android Player RMA Process](#RMA)

If you’ve got an OptiSigns Android Player and you’re having issues, you’ve come to the right place. For first time setup, see our article on how to [**Set Up the Android Digital Signage Player**](https://support.optisigns.com/hc/en-us/articles/27267311796243-OptiSigns-Android-Digital-Signage-Player).

---

Identify Your Device
--------------------

There have been several versions of the OptiSigns Android Stick over the years. The most common are the Gen 2 and Gen 3 devices:

![android player comparison gen2 vs gen3](https://support.optisigns.com/hc/article_attachments/40147900608403)

Functionally, these are quite similar. Both use the latest versions of the OptiSigns software. Most of their differences lie in **[Networking](#Network).**

---

Best Practices
--------------

We recommend certain best practices to keep your OptiSigns Android Player running at peak efficiency:

* Do not put too much pressure on the power cable, as this can cause the Player to get pulled from its HDMI socket.
* Keep the player in an indoor, air conditioned environment
* Run the Android Stick in fullscreen mode, or with a 2-3 zone Split Screen.

By default, an Android Player has an [**Operational Schedule**](https://support.optisigns.com/hc/en-us/articles/28598173096723-How-To-Create-and-Use-Operational-Schedules-HDMI-CEC-RS-232) built in to ensure it has 8 hours of downtime per day:

![operational schedule image](https://support.optisigns.com/hc/article_attachments/40147917435923)

If you require 24/7 uptime, more than 3 zones on a split screen, a heavy Website Dashboard (including Tableau or Power BI reports), or plan to use the player in hot or cold environments, consider the [**OptiSigns Pro Player**](https://shop.optisigns.com/products/optisigns-digital-signage-player) or [**ProMax Player**](https://shop.optisigns.com/products/optisigns-promax-signage-player).

---

The Troubleshooting Page
------------------------

Your first stop when running into a problem with the OptiSigns Android Player should be the **Troubleshooting Page.** This is an option on the side menu.

To access it, press the **Three-Bar button** on your remote to open the side menu of the OptiSigns app. Navigate to **Troubleshooting** under the **Advanced Options** section.

![open troubleshooting page optisigns app](https://support.optisigns.com/hc/article_attachments/40147917438355)

Now you can view detailed information about the app’s status and connectivity to assist with troubleshooting.

![troubleshooting page optisigns](https://support.optisigns.com/hc/article_attachments/40147917440787)

* **Check Internet Connection**: Verifies whether the device has an active internet connection.
* **Check Connection to API Services**: Tests the device's connection to OptiSigns services.
  + **Note**: If this check fails, it may be due to a firewall blocking the connection. Refer to our [**Whitelist Article**](https://support.optisigns.com/hc/en-us/articles/360047275934) for the required URLs and ports.
* **Check File Downloading**: Confirms the status of downloadable files (e.g., images, videos) being downloaded to the device.
* **Network Information**: Displays the current network the device is connected to.
  + **WiFi/Ethernet Details**: Includes IP Address, SSID, Signal Strength, Channel, Connection Type, and MAC Address.
* **Device Information:**
  + Screen Name, Pairing Code, Screen Resolution, OptiSigns App Version, OptiSigns MDM App Version, OS Version, Manufacturer, Model, Serial Number
  + Heartbeat/Polling Interval: Indicates how frequently the device communicates with OptiSigns servers and the last received signal.
* **Running Time**: Shows how long the OptiSigns app has been running on the device.
* **Storage**: Displays used and total storage capacity.
* **Memory**: Displays used and total memory capacity.
* **System Time**: Shows the current system time on the device.
* **System Time Zone**: Displays the time zone configured on the device.
* **Assigned Content Type**: Indicates the type of content the device is playing (e.g., Asset, Playlist, Schedule).
* **Assigned Content Name**: Provides the name of the content being displayed.
* **Device Created Date**: Displays the date the device was activated.
* **Operational Schedule Assigned**: Shows whether an operational schedule is assigned (**Y/N**).
* **Mute Status**: Displays the current audio status of the device.
* **Heavy Content Status**: Indicates whether the device is handling heavy content (e.g., 4+ zones or SplitScreen with 4K video) (**Y/N**). This will usually result in lag.

---

Hardware Troubleshooting
------------------------

Here we will cover the most common hardware troubleshooting issues our support team encounters.