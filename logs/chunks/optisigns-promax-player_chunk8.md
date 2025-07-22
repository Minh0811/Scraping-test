### Setting Up Security Protocol

You’ll need to select the appropriate Wi-Fi security protocol that matches your network configuration. The security protocol determines how your Wi-Fi network is protected and how devices communicate securely. The image below shows the available options:

![setting up wifi security protocol](https://support.optisigns.com/hc/article_attachments/39538703615635)

Here’s a brief overview of each option:

* **NONE**:

  + **Description**: This option indicates that the Wi-Fi network has no security, meaning no password is required to connect.
  + **Usage**: This is uncommon for most networks as it leaves your network vulnerable to unauthorized access. It's generally recommended to avoid using unsecured networks for your digital signage.
* **WPA2-PSK**:

  + **Description**: WPA2-PSK (Wi-Fi Protected Access 2 - Pre-Shared Key) is the most widely used security protocol for Wi-Fi networks. It provides strong encryption and requires a password to connect.
  + **Usage**: This is the default and most recommended option for both home and business networks due to its balance of security and compatibility.
* **WPA2-Enterprise**:

  + **Description**: WPA2-Enterprise is a more advanced security protocol often used in corporate environments. It requires a RADIUS server for authentication, offering individual credentials for users rather than a single shared password.
  + **Usage**: If your network is managed by an IT department with a RADIUS server, this is the option you’ll need to choose.
* **WPA3-Personal**:

  + **Description**: WPA3-Personal is the latest Wi-Fi security protocol, offering enhanced protection against brute-force attacks and stronger encryption than WPA2. It also simplifies the process of connecting devices without a display, like IoT devices.
  + **Usage**: Use this option if your network supports WPA3, providing the highest level of security for your digital signage setup.

|  |
| --- |
| Note: Make sure to select the security protocol that corresponds with your network settings. If you're unsure which one to choose, consult your network administrator or refer to your router’s settings. |

After selecting the appropriate Wi-Fi security protocol, proceed by entering your network’s password and click on the "**CONNECT**" button to complete the Wi-Fi setup.

---

Checking the Device's Detailed Information
------------------------------------------

Once connected, the device will display a pairing code on the screen, as shown below. This screen confirms that your device is now connected to the internet and is ready to be paired with your OptiSigns account. Follow [this guide](https://support.optisigns.com/hc/en-us/articles/360016374813) for assistance on pairing your screen.

![promax player pairing code screen](https://support.optisigns.com/hc/article_attachments/40217654048019)

After successfully pairing your OptiSigns ProMax Player, you may want to check more detailed information about your network connection. This can be especially useful if you're troubleshooting connectivity issues or just want to confirm the network settings.

![promax player side menu about](https://support.optisigns.com/hc/article_attachments/40217654049939)

To access the network details, follow these steps:

1. **Open the Settings Menu**: On your OptiSigns ProMax Player, navigate to the top-right corner of the screen and click on the menu icon.
2. **Go to the About Screen**: From the dropdown menu that appears, scroll down and select the "**About**" option. This will take you to a screen that displays various details about your OptiSigns ProMax Player, including network information.

In the "About" section, you'll be presented with detailed information about your device's network connection. This screen is a valuable resource for understanding and managing your connection, especially if you need to troubleshoot any issues. Below is what you can expect to see:

![promax player about menu](https://support.optisigns.com/hc/article_attachments/40217688490259)

Here’s a breakdown of the key information displayed:

* **Used Cache:** The amount of space being used by the device's cache.
* **Version:**The current version of the OptiSigns app being run.
* **Assigned Content**: The current content assigned to the device. This can be either an Asset or a Playlist.
* **Device Info**
  + **Platform:** The platform the device is running on.
  + **OSVersion:** The current version of the OS the device is running.
  + **HostName:** The name of the device on the network.
  + **Local Time:** The local date and time. This is used for Operational and general Scheduling.
* **Server and Internet Connection Status**: The screen will also indicate whether your device is connected to the OptiSigns server and the internet, displayed in green text as "Server Connected: true" and "Internet Connected: true." This is a quick way to confirm that your device is online and able to receive updates and content. If false, this text will be red and read "false."
* **CpuUsage**: The current CPU usage.
* **Network MACs**

  + **MAC Address**: This is the unique MAC (Media Access Control) address for your device's Wi-Fi connection. The MAC address can be useful for network administrators who may need to whitelist your device on certain networks.
  + **ETH1 MAC Address**: If your device is also connected via Ethernet, this section will show the MAC address for that connection. This is important if you have a wired connection in addition to Wi-Fi.
* **Network IPs**: Here, you will see the IP addresses assigned to your device. For Wi-Fi, the WLAN IP is shown along with the SSID (network name) your device is connected to. Knowing the IP address can help with advanced troubleshooting and network management.

In addition to network details, the "About" screen provides other useful information such as CPU and RAM usage, storage details, and the local time set on the device. These details can help you monitor the performance of your OptiSigns ProMax Player.

If you ever need to reboot your device, view logs, or revisit the Wi-Fi setup, you can do so directly from this screen by clicking on the corresponding options at the bottom.