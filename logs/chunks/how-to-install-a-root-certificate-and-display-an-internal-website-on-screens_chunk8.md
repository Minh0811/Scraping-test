### Command Line Installation

On MacOS, you can also use the Terminal to directly install the Certificate. Simply type in these commands:

**Use the following command to add a certificate:**

```
sudo security add-trusted-cert -d -r trustRoot -k /Library/Keychains/System.keychain “new-root-certificate”
```

**Use the following command to remove a certificate:**

```
sudo security delete-certificate -c "name of existing certificate"
```

---

Installing a Root Certificate on Chrome-Based Web Browsers
----------------------------------------------------------

Depending on the operating system, Chrome will use the system-wide certificates (such as the ones installed above) or its own certificates. If you are having trouble getting a system-wide certificate to work for your internal website, you may wish to try directly installing a root certificate to Chrome (or any Chromium browser) directly.

To begin, open the **Settings** tab in the Chrome browser.

![](https://support.optisigns.com/hc/article_attachments/35184720118803)

Next, click **Privacy and security** **→ Security → Manage Certificates**

**![](https://support.optisigns.com/hc/article_attachments/35184705392531)**

This will open the Certificates manager. You’ll need to add your internal website certificate as an authority. Here, click the **Trusted Root Certification Authorities** tab, then click **Import**.

![](https://support.optisigns.com/hc/article_attachments/35184720125715)

This will open the Certificate Import Wizard. Click **Browse** and locate the certificate necessary for your internal website. Then, click **Next**.

**![](https://support.optisigns.com/hc/article_attachments/35184720127635)**

On the next screen, **Place all certificates in the following store** and make sure it’s “Trusted Root Certification Authorities”. Then hit **Next**.

**![](https://support.optisigns.com/hc/article_attachments/35184705364115)**

Now you’ll be asked to confirm whether you want to complete the import. As long as you trust the certificate, agree to it by hitting **Finish**.

**![](https://support.optisigns.com/hc/article_attachments/35184705368339)**

Congratulations, you’ve installed your root certificate on your Chrome browser.

---

Setting an Internal Website Up for Use on OptiSigns Using the Website App
-------------------------------------------------------------------------

The OptiSigns Website app allows you to display an internal website on your screens once a valid private certificate (.pem file) has been installed on your device.

To set it up, navigate to **Files/Assets** in your OptiSigns portal. Find the **Website** app.

![](https://support.optisigns.com/hc/article_attachments/35184705404947)

Enter the **URL** of your webpage here. The Name field is irrelevant to the app’s function and will only make the asset easier to find in OptiSigns.

|  |
| --- |
| **NOTE** |
| If your internal website is large and complex, you can also display it using the **Advanced Website** app. If you’re having trouble displaying it on the basic Website app, create an Advanced Website asset and try again. |

Once the Website asset is created, it can be assigned to a screen.