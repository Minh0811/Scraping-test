### In this article, we will cover OptiSigns’ ability to create custom news apps using the OptiSync feature.

* [SharePoint News Examples](#Examples)
* [How to Set Up a Custom News Feed](#Setup)
  + [Step 1: Setting Up an API Gateway (SharePoint Example)](#Gateway)
    - [Choosing the Correct URL Endpoint for Connection](#Endpoint)
    - [SharePoint API Authentication using OAuth 2.0 in Microsoft Azure](#Authentication)
  + [Step 2: Mapping the API to a DataSource](#DataSource)
  + [Step 3: Creating a News Feed Using Designer](#Designer)
    - [Element Mapping](#Element)
  + [Applying Filters to Customize Which News Stories to Display](#Filters)

It is common for companies to share their internal communications, including memos, news, announcements and more via intranet. Digital signage will heighten employee awareness of published company news and announcements.

Using OptiSync, it’s possible to create a custom news app to display company news stored on your company’s intranet. This is achieved by connecting an intranet API with OptiSync and choosing what data to display in the [OptiSigns Designer app](https://support.optisigns.com/hc/en-us/articles/4404151402899-How-to-use-OptiSigns-Template-Designer-app-to-make-your-Digital-Signs-in-minutes).

Creating news feeds with OptiSync has a key advantage: you have full control of the look and feel of your feed. You can create feeds that match your company branding and design guidelines no matter which news source you use. We will be using SharePoint here as an example, but you can use anything that can be input as a Datasource.

Before we get started, it will be helpful to familiarize yourself with a few other concepts which will be important to understand that we cover in other articles:

* [How to Integrate API and Publish API Data via OptiSync](https://support.optisigns.com/hc/en-us/articles/22875592994195-How-to-Integrate-API-and-Publish-API-Data-via-OptiSync)
* [How to Set Up Dynamic Data Mapping via OptiSync](https://support.optisigns.com/hc/en-us/articles/29217646663187-How-to-Set-Up-Dynamic-Data-Mapping-with-OptiSync)

The API article in particular will provide detailed instructions for how to pair an API and get its data on screen with automatic updates. Once you’ve got your API set up and its data saved as a data source, you can create some of the examples below using the Designer app.

The main example tackled in this article will be company news, but this feature can be used for far more, including:

* Custom RSS feeds
* Custom XML/JSON feeds
* Inventory management systems
* Point-of-sales updates across multiple locations
* Additional internal communications
* Other news sites

---

SharePoint News Examples
------------------------

Below are some examples using SharePoint. There are numerous possibilities of how to design and create engaging news feeds using SharePoint news or other intranet applications.

Here are a few examples: