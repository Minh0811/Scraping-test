### In this article, we troubleshoot the most common issues our customers face when using an OptiSigns Pro or ProMax Player.

* [Best Practices](#BestPractices)
* [The Troubleshooting Option](#TroubleshootingOption)
* [Hardware Troubleshooting](#Hardware)
  + [Network Troubleshooting](#Network)
  + [Power, HDMI & TV Connection Troubleshooting](#Connection)
  + [Blank Screen Troubleshooting](#BlankScreen)
  + [Fixing the OnHold Warning](#OnHold)
  + [App Freezes, Video Assets not Playing full video or Asset Not Loaded Fully](#AppFreezes)
  + [How to Factory Reset the OptiSigns Android Player](#FactoryReset)
* [Security Settings Troubleshooting](#SecuritySettings)
  + [Using the Device Log](#DeviceLog)
  + [Static IP](#StaticIP)
  + [Internal Websites and Root Certificates](#InternalWebsite)
* [Pro/ProMax Player RMA Process](#RMAProcess)

If you’ve got an OptiSigns Pro or ProMax Player and you’re having issues, you’ve come to the right place. For first time setup, see our [**Set Up the OptiSigns Pro Player**](https://support.optisigns.com/hc/en-us/articles/32272215514131-Optisigns-Pro-Digital-Signage-Player) or **[Set Up the OptiSigns ProMax Player](https://support.optisigns.com/hc/en-us/articles/38680194603155-OptiSigns-ProMax-Player)** articles. For more on the Pro or ProMax player features, see our [**Advanced Features**](https://support.optisigns.com/hc/en-us/articles/35577511423635-OptiSigns-Pro-Player-Advanced-Features) article.

---

Best Practices
--------------

* Set up the [**Mobile Admin App**](https://support.optisigns.com/hc/en-us/articles/30003143806099-How-to-Use-the-OptiSigns-Mobile-Admin-App). This will allow you to use numerous features remotely, including the Remote Keyboard app and remote monitoring.
* Keep the player in an indoor, air conditioned environment
* Ensure your player is up-to-date. We release frequent OTA updates - see more below.

By default, our Pro Players are set to receive a weekly automatic OTA update at **Sunday 00:00** (also known as Saturday night). If the players are offline at that time, it’s possible to miss the OTA update. We recommend changing the OTA update to a time when the players are online, but not being used for anything mission critical.

These OTA updates often bring with them new and advanced features, stability updates, security updates, patches, and more, so we ***highly recommend*** scheduling an update time that works for you. If none do, be sure to occasionally **Check for Updates**.

---

The Troubleshooting Option
--------------------------

Your first stop when running into a problem with the OptiSigns Pro or ProMax player should be the **Troubleshooting** page. This is an option on the Side Menu:

![troubleshooting page menu location](https://support.optisigns.com/hc/article_attachments/40736654908563)

Choosing this option will open the Troubleshooting screen:

![troubleshooting screen](https://support.optisigns.com/hc/article_attachments/40736654909587)

* **Check Internet Connection**: Verifies whether the device has an active internet connection.
* **Check Connection to API Services**: Tests the device's connection to OptiSigns services, including APIs and MDMs.
  + **Note**: If this check fails, it may be due to a firewall blocking the connection. Refer to our **[Whitelist Article](https://support.optisigns.com/hc/en-us/articles/360047275934)** for the required URLs and ports.
* **Check File Downloading**: Confirms the status of downloadable files (e.g., images, videos) being downloaded to the device.
* **Network Information**: Displays the current network the device is connected to.
  + **WiFi/Ethernet Details**: Includes IP Address, SSID, Signal Strength, Channel, Connection Type, and MAC Address.
* **Device Information:**
  + Screen Name, Pairing Code, Screen Resolution, OptiSigns App Version, OptiSigns MDM App Version, OS Version, Manufacturer, Model, Serial Number
  + Heartbeat/Polling Interval: Indicates how frequently the device communicates with OptiSigns servers and the last received signal.
* **Running Time**: Shows how long the OptiSigns app has been running on the device.
* **Storage**: Displays used and total storage capacity.
* **Memory**: Displays used and total memory capacity.
* **Current System Time**: Shows the current system time on the device.
* **System Time Zone**: Displays the time zone configured on the device.
* **Assigned Content Type**: Indicates the type of content the device is playing (e.g., Asset, Playlist, Schedule).
* **Assigned Content Name**: Provides the name of the content being displayed.
* **Device Created Date**: Displays the date the device was activated.
* **Operational Schedule Assigned**: Shows whether an operational schedule is assigned (**Y/N**).
* **Mute Status**: Displays the current audio status of the device.
* **Heavy Content Status**: Indicates whether the device is handling heavy content (e.g., 4+ zones or SplitScreen with 4K video) (**Y/N**)

---

Hardware Troubleshooting
------------------------

Here we will cover the most common hardware troubleshooting issues our support team encounters with our OptiSigns Pro and ProMax players. Following these steps will resolve 90%+ of issues.