#### SharePoint API Authentication using OAuth 2.0 in Microsoft Azure

Authentication for SharePoint can be carried out using different methods, but OAuth 2.0 has become the recommended standard. To get started using OAuth 2.0, you’ll need to [register your application in Azure Active Directory](https://learn.microsoft.com/en-us/azure/healthcare-apis/register-application).

Once that's done, you'll need:

* [**Client ID**](https://learn.microsoft.com/en-us/azure/healthcare-apis/register-application#application-id-client-id)
* [**Client Secret Value**](https://learn.microsoft.com/en-us/azure/healthcare-apis/register-application#certificates--secrets)

These are required for authentication. Any further authentication can be done in the Pre-Request stage to obtain access tokens. These authentication tokens will need to be kept refreshed: see [Microsoft's article on identity platform certificate credentials](https://learn.microsoft.com/en-us/entra/identity-platform/certificate-credentials) for more information.

When paired with an “Accept” value, this will provide authentication for your API request. You’ll need the following values:

```
Authorization: "Bearer " + accessToken  
Accept: "application/json;odata=verbose"
```

These values should be input under the **Header** tab when setting up your API request:

![api gateway header tab](https://support.optisigns.com/hc/article_attachments/35337756499091)

Be sure to **Enable this Request** before moving to the next step.

![api gateway enable this request](https://support.optisigns.com/hc/article_attachments/35337746496019)