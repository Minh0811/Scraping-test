### In today's fast-paced digital environment, manually updating digital displays can be both tedious and error-prone. This guide will show you how to integrate live data into your digital screens, allowing for seamless automatic updates across your displays.

**In this article:**

* [What is OptiSync?](#What)
* [Adding Your Data Source](#Adding)
* [Inputting Your Data Source in Designer](#Inputting)
* [Editing and Designing Your Repeater in Designer](#Editing)
  + [How to use the Property Mapping Feature](#Property)
  + [How to use Display Format Options](#Display)
* [Push to Screens](#Push)

|  |
| --- |
| Note: OptiSync is only available on Pro Plus and above plans. |

What is OptiSync?
-----------------

OptiSync is an integrated solution designed to seamlessly connect with various data sources, including spreadsheets, APIs, and tables.

**Key Features:**

* **Easy Setup:** Setting up your data source requires low code or no code, ensuring a quick and straightforward process.
* **Automatic Updates:** You can link your data source directly to our Designer app, which will automatically update your content.
* **Real-Time Data:** This ensures your digital display always reflects the latest data, eliminating the need for manual entry, reducing errors, and saving time.

**Use Cases:**

OptiSync is ideal for a wide range of use cases, such as:

* Displaying employee birthdays
* Restaurant menus
* Work anniversaries
* Product catalogs
* Team introductions
* And, many more!

With OptiSync, your digital displays remain accurate and up-to-date, enhancing communication and engagement in various settings.

Adding Your Data Source
-----------------------

You can add your data source through **Account Settings** or through **Designer app**.

**Account Settings**

* Click on your account name in the top right corner
* Select **More**
* Select **DataSources**
* Select **Add DataSource**
* Choose your data source from the list of options and follow the instructions on how to import it
  + *If you fully open your account settings, it will be under "Advanced" in the column on the left*

**Designer App:**

* Open the Designer App
* Select **DataSources** from the column on the left
* Select **Add DataSource**
* Choose your data source from the list of options and follow the instructions on how to import it

You can add any data source, such as an Excel sheet, Google Sheet, POS system, inventory management system, HRIS, or other systems. You can also create a table directly in OptiSigns.

![](https://support.optisigns.com/hc/article_attachments/29687726573203)

**Please follow these guides to upload different kinds of DataSources:**

* [How to add Google Sheets as a DataSource for OptiSync](https://support.optisigns.com/hc/en-us/articles/29838866920211)
* [How to add a Microsoft 365 Excel Spreadsheet as a DataSource for OptiSync](https://support.optisigns.com/hc/en-us/articles/29863080711059)

In addition, you can integrate and test API requests, and execute any necessary pre- or post-request coding.

![](https://support.optisigns.com/hc/article_attachments/29217646654099)

Once your data source is set up, you can see **Where Used,** **Edit** the data source, and/or **Duplicate** it.

![](https://support.optisigns.com/hc/article_attachments/29689445946003)

* **Where Used:** This will show you which of your designs are using this Data Source. This is useful to track the use of this data source across different assets.
* **Edit Data:**Go into your data source and make any updates/changes.
* **Duplicate:**This will create a copy of your data source.

![](https://support.optisigns.com/hc/article_attachments/29689413996947)

Inputting Your Data Source in Designer
--------------------------------------

Once your Data Source is set up, you can connect it to the Designer app.

Go to **DataSource** on the left side of the Side Menu.

![datasource location designer](https://support.optisigns.com/hc/article_attachments/42703178733715)

As previously mentioned, you can add your DataSource here. Or, if you have already created it in the Data Source section of **Advanced**, then it should show up under **Other DataSources**.

**Select** your data source.

**Drag and drop** the data source elements onto the Designer canvas.

* You can either drag and drop an entire Row or the individual aspects within the rows.

A pop-up message will appear, asking "**Would you like to use this data in a Repeater or on its Own?**"

![on its own vs repeater gif](https://support.optisigns.com/hc/article_attachments/42703178736787)

* **Use on its own:** It will be an element on its own and will update automatically based on the data source.
* **Use in a Repeater:** This will include the data source element in a Repeater component.
  + **Repeater** is a tool that can be used on the Designer application to display and repeat a list of items dynamically.

|  |
| --- |
| **IMPORTANT** |
| OptiSync does not support special characters (i.e. anything outside the scope of an English-language keyboard). This will cause the system data to read as blank, and it will not show. |

Editing and Designing Your Repeater in Designer
-----------------------------------------------

You can edit both the template and the Repeater in Designer!

**The Repeater can be found on the side menu of the Designer application.**

![](https://support.optisigns.com/hc/article_attachments/42705270085523)

Within the Repeaters section, it will contain several ready to use "**Repeater components**" and "**Repeater Templates.**"

|  |
| --- |
| What is the Difference Between the two? |
| **Repeater Component:** designed to manage and display repeating elements along with some design elements. You can incorporate this Repeater component into any template design of your choice—it doesn't need to be a Repeater template. Once added, you simply connect it to your data source. Think of it as a widget that can be easily implemented and customized across different designs to dynamically display data. |
| **Repeater Template:** specifically designed to display repeating elements within a predefined template or design layout. Like other templates, it will replace any existed design when applied. You can still make edits and changes as desired. Again, users will only need to download it and connect to your desired data source. |

Any of these elements can have a DataSource mapped to them, then be edited in the same manner as any other Designer component.

For more information on this, see our guides:

* [**Getting Started with Designer**](https://support.optisigns.com/hc/en-us/articles/42087942047379-Getting-Started-with-Designer)
* [**Photos, GIFs, and QR Codes**](https://support.optisigns.com/hc/en-us/articles/42526907045651-Photos-GIFs-and-QR-Codes-in-Designer)
* [**Customizing Text**](https://support.optisigns.com/hc/en-us/articles/42157810188179-Customize-Text)
* [**Shapes and Elements**](https://support.optisigns.com/hc/en-us/articles/42307234534547-Shapes-and-Elements)

You can also adjust the formatting of a Repeater by selecting it, then selecting **Settings**.

![](https://support.optisigns.com/hc/article_attachments/42705270087059)

This will open up the **Data Mapping**section for the Repeater on the Side Menu:

![](https://support.optisigns.com/hc/article_attachments/42705284276243)

Then, these options will be presented:

* **Replace DataSource:** Change your DataSource
* **Manage:** Make changes to your DataSource's information.
* **Filter:** Apply condition based filters on the DataSource. Filter conditions can be applied using fixed value or device attributes.
* **Disconnect:** Disconnect your DataSource from the Repeater
* **Empty Data Handling:** When there is no DataSource element, the default behavior is to use a blank value. You can adjust this with the following options:
  + **Skip:** Skip it, or get rid of additional repeater items if there isn't enough data to reach the set "Total Items displayed per Page".
  + **Use Default Value:** Show default content, which is what your Repeater element looks like by itself.
  + **Use Blank:** The Repeater will show nothing.
* **Spacing Betwee****n** **Items:**Increase or decrease the space between the Repeater items.
* **Item Display Direction:** Change the positioning of the rows from your DataSource within the Repeater items.   
  + **Left To Right**: It will display the rows going from left to right.
  + **Top To Bottom**: It will display the rows going top to bottom.
* **Item Display Alignment:** Change the alignment of the remaining element items (less than the configured items) to be aligned left/center/right or top/center/bottom.
* **Total Items Displayed per Page:** Increase or decrease how many Repeater items you'd like to be shown.
* **Maximum Items in Each Row/Column:** Increase or decrease how many Repeater items you'd like shown in each row/column.
* **Additional Row/Column Spacing:** Increase or decrease the spacing between rows/columns.
* **Duration (seconds):** Adjust the duration of time for how long each Repeater item is shown before.
* **Shuffle:** Randomly shuffle the items in your DataSource to be displayed on the Repeater.

If you edit a Repeater, it will replicate your updates for each instance of data in the dataset.

* This allows for a consistent look across similar elements without the need to design each one individually.

If you want to use a specific Repeater Template or Component, and would like to update the sample DataSource to one of your DataSources, please follow the steps shown below: