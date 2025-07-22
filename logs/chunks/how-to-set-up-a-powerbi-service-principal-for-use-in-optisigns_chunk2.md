### Add the Service Principal to a Workspace

Now we need to assign service principal access to the workspaces you want to show in your PowerBI reports.

In the admin portal, click **Workspaces**. You’ll want to go to the workspace you want to assign service principal access to. Click the workspace, then hit **Access**.

![how to grant service principal access powerbi](https://support.optisigns.com/hc/article_attachments/32860610425107)

Add the service principal you created in the last step as a member of the workspace.

![how to add service principal as a member of powerbi workspace](https://support.optisigns.com/hc/article_attachments/32860569093139)

---

Authenticating OptiSigns via Service Principal
----------------------------------------------

In order to authenticate your PowerBI on OptiSigns via service principal, you’ll need four pieces of information:

1. Name of the service principal
2. Application (client) ID
3. Directory (tenant) ID
4. Application (client) secret

Since we’ve already created an Entra app in Azure, we already have access to the first three pieces of information. These can be found under **App Registrations** back in Azure.

![where to find app registration information in microsoft azure](https://support.optisigns.com/hc/article_attachments/32860569095571)

In this example, the values have been blurred, but on your Azure portal, these should be visible.

The only piece of information you won’t have is the client secret. To get that, click **Manage → Certificates & Secrets → Client Secrets → New Client Secret**

**![how to create new client secret in microsoft azure](https://support.optisigns.com/hc/article_attachments/32860569099411)**

Next, set the **Description** and **Expiry**, then click **Add**.

![how to add a client secret](https://support.optisigns.com/hc/article_attachments/32860569100947)

The **Value** present is the last piece of information you need.

Now, head into the OptiSigns app. Click your **Profile name → More → Integrations.**

![where to find integrations tab in optisigns](https://support.optisigns.com/hc/article_attachments/32860610434451)

A screen like the one below will appear. Click **Add Azure Service Principal.**

![how to add service principal in optisigns](https://support.optisigns.com/hc/article_attachments/32860569109011)

When the popup appears, collect the information mentioned above from Microsoft Azure and input it into OptiSigns. The values match up like this:

![inputting all the powerbi service principal information into optisigns](https://support.optisigns.com/hc/article_attachments/32860610442771)

Once all the information is input correctly, hit **Save**. Now your Service Principal is saved to the OptiSigns portal.

---

Getting PowerBI onto a Screen
-----------------------------

Now we’ll need to configure your PowerBI asset in OptiSigns for use with your screens.

In the OptiSigns portal, go to **Files/Assets → Apps → PowerBI**

**![how to find powerbi app in optisigns](https://support.optisigns.com/hc/article_attachments/32860569116691)**

Check **Use Service Principal** and select the service principal you set up in the last step, or whichever service principal you want to use.

|  |
| --- |
| **NOTE:** Using a service principal, the Power BI Dashboard URL link needs to include the actual **workspace (group)** ID instead of me. |

**![powerbi app information in optisigns](https://support.optisigns.com/hc/article_attachments/32860610472339)**

Finally, input the URL of whatever report you want to share. Name the app whatever you like, then hit **Preview** to view your report.

**![preview of powerbi app running in optisigns](https://support.optisigns.com/hc/article_attachments/32860610476307)**

Hit **Save**, then this PowerBI app will exist as an asset. It can be pushed to any of your screens individually, scheduled, or added to a Playlist.