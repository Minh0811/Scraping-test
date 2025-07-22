### Command Line Installation

You can also use the **Terminal** to directly install the certificate. Simply open up the Terminal app with Administrator privileges after searching for it on your Start bar, and input the following command:

```
certutil –addstore –f "Root" “C:\path\to\your_certificate_file”
```

This will automatically install the certificate to the Trusted Root Certificates folder and you should be able to access the host domain in the same way as above.

---

Installing a Root Certificate on a MacOS Device
-----------------------------------------------

To prepare for the installation, make sure your device is connected to the same network of host servers you plan to use. Also, make sure your certificate is in a folder (the Download folder will work) on the device installing the certificates.