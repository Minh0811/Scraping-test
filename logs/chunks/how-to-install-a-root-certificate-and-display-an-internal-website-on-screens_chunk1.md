### In this article, we will explain how to install a root certificate on your devices to set up an internal website for use with OptiSigns.

* [Installing a Root Certificate on an OptiSigns Gen 3 Pro Player](#ProPlayer)
* [Installing a Root Certificate on a Linux/Ubuntu Device](#Ubuntu)
* [Installing a Root Certificate on a Windows Device](#Windows)
  + [Open the Microsoft Management Console (MMC)](#MMC)
  + [Add the Certificates Snap-in](#Snap-In)
  + [Import the Certificate](#Import)
  + [Verify the Installation](#Verify)
  + [Command Line Installation](#Command1)
* [Installing a Root Certificate on a MacOS Device](#MacOS)  
  + [Install Certificate](#Install)
  + [Command Line Installation](#Command2)
* [Installing a Root Certificate on Chrome-Based Web Browsers](#Chrome)
* [Setting Up an Internal Website for Use on OptiSigns Using the Website App](#InternalWebsite)
  + [Using Web Scripting to Bypass Logins](#WebScripting)

OptiSigns digital signage software is an extremely valuable tool for internal communication, capable of displaying internal memos, communications, and announcements across numerous locations and offices. Messaging can be tailored to specific audiences, scheduled, and automatically synced to data sources.

With all these capabilities, it stands to reason that some want to incorporate OptiSigns into their intranet, or internal website. These can be displayed on your screens using the OptiSigns Website app, or Advanced Website app in some cases.

However, in order to do this, you’ll need a trusted, self-signed root certificate installed on the platform you choose to run it on. Here, we’ll show you how to get that installed.

Please note that you’ll need to obtain a trusted certificate yourself. This will need to be some sort of key, usually denoted by a **.pem** file extension.

In this article, we will walk you through two main steps:

1. Installing a root certificate on your device of choice (OptiSigns Pro Player, Ubuntu, Windows, MacOS, or Chrome browser)
2. Configuring a Website app to display your internal website

|  |
| --- |
| **NOTE** |
| Before you start, make sure you’re connected to the same network as the server you’re trying to access. |

|  |
| --- |
| **Please note that Android devices are not supported at this time.** |

---

Installing a Root Certificate on an OptiSigns Gen3 Pro Player
-------------------------------------------------------------

In order to get your root certificate onto an OptiSigns Pro Digital Signage Player, you’ll need to manually add it. Find where your certificate is stored, then download it to a USB or MicroSD card. Plug the card into the Pro Player.

|  |
| --- |
| **IMPORTANT** |
| For installation on a Gen 3 Pro Player, your certificate must have a **.crt** extension. However, it is important that this certificate is signed and contains your public key. These are usually generated as **.pem** files. You’ll need to rename your certificate (.pem) file and change its extension to **.crt** for your internal website to properly display. |

Now, open your OptiSigns player menu. Go to **About → Advanced Settings**.

**![](https://support.optisigns.com/hc/article_attachments/35184705322515)**

Here, you’ll see a field called **Certificate File**.

![](https://support.optisigns.com/hc/article_attachments/35184705339539)

Simply locate your certificate on your USB or MicroSD card and select it. The certificate will automatically be downloaded to the appropriate location. This will allow your OptiSigns player to display your internal website.

---

Installing a Root Certificate on OptiSigns Gen 2 Pro Players and Linux/Ubuntu Devices
-------------------------------------------------------------------------------------

To install a root certificate on a Linux or Ubuntu device, you’ll need to make heavy use of the **Terminal.**

To begin, take your trusted, signed certificate (.pem file) and place it in the /usr/share/ca-certificates folder.

![](https://support.optisigns.com/hc/article_attachments/35184720058515)

|  |
| --- |
| **NOTE** |
| You will need to rename your **.pem** file to make it a **.crt** file, or else this will not work. |

After the certificate has been moved and renamed, you’ll need to refresh the installed certificates and hashes. Open your **Terminal** and type in this command:

```
sudo update-ca-certificates
```

Once this command is executed, it should say that it has installed 1 (or more) new certificate.

![](https://support.optisigns.com/hc/article_attachments/35184720067475)

This means the certificate has been added to the operating system and signed certificates will be trusted.

Now, you’ll want to install the certificate in the Chromium store using this command:

```
certutil -A -n "ROOT-CA" -t "TCu,Cu,Tu" -i /usr/share/ca-certificates/[name-of-cert].crt -d sql:/home/[user]/.pki/nssdb
```

The Linux-based OptiSigns app uses Chromium, so this will allow the certificate to pass through the OptiSigns app.

Now reboot your device.

Congratulations! You’ve successfully installed a root certificate on Ubuntu.

---

Installing a Root Certificate on a Windows Device
-------------------------------------------------

Broadly, there are four major steps to installing a root certificate locally on a Windows device:

1. Open the Microsoft Management Console (MMC)
2. Add the Certificates Snap-In
3. Import the Certificate
4. Verify the Installation

These same steps can be performed quickly using the Windows Terminal, if you’re so inclined.

Be cautious when installing root certificates, especially self-signed ones. Only install certificates from sources you trust completely.

|  |
| --- |
| **NOTE** |
| You need administrator privileges to install certificates in the Trusted Root Certification Authorities store. |