### Advanced Settings

![WIN_20250423_09_51_19_Pro - Copy (2).jpg](https://support.optisigns.com/hc/article_attachments/40595153623187)

On the **Advanced Settings** screen, you can perform various functions such as enabling/disabling Network Proxy, NTP, the On-screen Keyboard, SSH, and configuring a Static IP for either WLAN or Ethernet. Selecting any of these options will enable further options in the window:

![WIN_20250423_09_51_19_Pro - Copy.jpg](https://support.optisigns.com/hc/article_attachments/40595153623955)

* **Certificate File** **-** Allows you to [install a root certificate](https://support.optisigns.com/hc/en-us/articles/35184720136595-How-to-Install-a-Root-Certificate-and-Display-an-Internal-Website-on-Screens) for displaying an internal website. The certificate will need to be present locally on the device in order for it to be installed.
* **NTP Server** **-** Input server information for your Network Time Protocol (NTP). This can be used to ensure the OptiSigns Pro Player has its computer clock time with other time sources in your network.
* **WiFi SSH IP** - IP address associated with your SSH. Only appears when SSH is enabled.
* **Network Proxy** **-** Server information for any network proxy. This is a system or router which serves as a middleman between our Pro Player and the internet and can be used to enhance security, privacy, or efficiency.
* **KeyBoard Layout** **-** Choose between various international keyboard layouts. Default is US.
* **Static IP Information** **-** An IP address that remains the same over time. We allow two types of Static IP: WLAN or ETH. These can improve network performance. This screenshot shows WLAN; if Static ETH IP is chosen, these will be ETH IP Address, Default Gateway, Subnet Mask, and DNS Server.
  + **IP Address -**Set the Static IP address.
  + **Default Gateway**- Set the Default Gateway for the Static IP address. This is the IP address of your router.
  + **Subnet Mask**- Set the Subnet Mask for the Static IP. Usually, this number is 255.255.255.0 or some variant of this.
  + **DNS Server**- Lets you set up your DNS server for the Static IP address.

---

How to Bring Up the System Terminal
-----------------------------------

The OptiSigns Pro Player has a console you can use to input commands directly. This can be accessed through the OptiSigns portal. From the **Screens tab**, click the **3 Dots** **→ Execute Remote Commands**.

![](https://support.optisigns.com/hc/article_attachments/35577555693075)

You’ll be taken to the below screen:

![](https://support.optisigns.com/hc/article_attachments/35577555668755)

Target the screen you’ve paired with your OptiSigns Pro Player, then enter the **showTerminal** command in the highlighted field. After a few seconds, you should see the following:

![](https://support.optisigns.com/hc/article_attachments/35577511404819)

This means the OptiSigns Pro Player has received the command and executed it. Your console terminal should now be visible on your screen and can be interacted with.

---

How to Use SSH to Remote Into Device
------------------------------------

Pro Players allow remoting into devices using SSH. Here's how to set that up.

First, enable **SSH**in your Advanced Settings.

![ssh advanced settings](https://support.optisigns.com/hc/article_attachments/40985616289939)

This will provide you with the SSH IP and Port number. By default, the port is **3000**, but it can be changed to whatever you like.

![ssh ip and port](https://support.optisigns.com/hc/article_attachments/40985596548243)

Now that SSH is enabled and you have the IP and Port, you can use a computer terminal to remote into the device.

Type the following command:

```
SSH optisigns@<ip-address-here> -p <port-number-here>
```

When it asks for a password, type **optisigns**. This should connect you to the device via SSH.

To change the default password (which we ***highly******recommend***), type:

```
passwd
```

This will ask you to type the current password, then new, then to type in the new password again.

![](https://support.optisigns.com/hc/article_attachments/41021980486931)

|  |
| --- |
| **NOTE** |
| Restarting the OptiSigns Pro Player will cause SSH to automatically disable for security purposes. |

That's it! You should be able to use the SSH function now.

---

How to Perform a Factory Reset
------------------------------

Sometimes, it might be necessary to perform a factory reset on your OptiSigns Pro Player.

To do this, attach a keyboard to the Player. Then, **Reboot** it. As it restarts, rapidly tap the **↑ arrow**. It will boot into this screen:

![](https://support.optisigns.com/hc/article_attachments/35577555703187)

Here, you have several additional options. Hit **Factory Reset**. You’ll receive this prompt:

![](https://support.optisigns.com/hc/article_attachments/35577555704723)

You’ll need to enter your **admin password.**

Once entered, you’ll see a screen like this:

![](https://support.optisigns.com/hc/article_attachments/35577555707923)

Afterwards, your factory defaults will be restored.