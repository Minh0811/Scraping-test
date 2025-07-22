### OptiSync allows you to create dynamic digital menus through API integration. Your POS systems can interface directly with OptiSigns to automatically update prices, track inventory, and more.

* [How to Integrate POS Systems Through API Requests](#Section%201)  
  + [Get API URL Endpoint and Set Up API Request DataSource](#Section%202)
  + [Additional Information on API Authentication](#Section%203)
  + [Handling Multiple Stores or POS Locations](#Section%204)
  + [How to Use Post-Request Processing to Convert API Data](#Section%205)
* [How to Build Digital Menu Boards in Designer with OptiSync](#Section%206)  
  + [Using DataSources and Repeaters](#Section%207)
  + [Element Mapping](#Section%208)  
    - [Adding Text Elements to Your Menu](#Section%209)
    - [Creating Strike Throughs and Sold Out Warnings](#Section%2010)
* [Pushing a Digital Menu Board to a Screen](#Section11)

In this article, we will create a real Digital Menu Board (DMB) integrated with a Clover POS system. The DMB pulls product info from Clover and display it onscreen. When an item is not available, it will display as "SOLD OUT."

|  |
| --- |
| **NOTE** |
| API Integration is only available with a **Pro Plus** plan or higher. |

---

How to Integrate POS Systems Through API Requests
-------------------------------------------------

Most POS systems have an API library which OptiSigns can use to get the relevant data from the system programmatically. This API can return menu items, item price, availability, and more.

With OptiSync, we can link APIs to the OptiSigns portal and push the data to screens as a Digital Menu Board (DMB) or any other type of screen you'd like without the need of human intervention.

![api optisigns integration diagram](https://support.optisigns.com/hc/article_attachments/31860108901523)

This article will focus on these POS specific wrinkles, and the process of mapping POS data to assets and pushing them to screens.

|  |
| --- |
| **IMPORTANT** |
| In order to integrate a POS system, you'll need to first set up an API Gateway request. A complete guide for how to do that can be found [here](https://support.optisigns.com/hc/en-us/articles/22875592994195-How-to-Integrate-API-and-Publish-API-Data-via-OptiSync). |

---