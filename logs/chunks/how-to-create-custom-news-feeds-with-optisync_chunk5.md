#### Choosing the Correct URL Endpoint for SharePoint Connection

There are numerous options for connecting to SharePoint’s API endpoints, and making sure you have the correct one is critical for importing the correct data into OptiSigns. Click here to learn more about [Determine SharePoint REST service endpoint URIs](https://learn.microsoft.com/en-us/sharepoint/dev/sp-add-ins/determine-sharepoint-rest-service-endpoint-uris?tabs=http).

For the purposes of this example, we’ll be using “Site” feature area, meaning the access point will be:

```
https://{site_url}/_api/site
```