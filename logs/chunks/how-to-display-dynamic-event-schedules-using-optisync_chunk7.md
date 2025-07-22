#### How to Set Up a Daily Event Schedule that Updates with the Passage of Time

With a Daily Event schedule, once an event happens, there’s no need to keep displaying the event. With OptiSync, you can configure your DataSource to ignore events which are now in the past.

To do this, we’ll need to set up an additional column in our spreadsheet. We’ll call it the **Event Over?** column.

**![google sheets with an additional event over? column](https://support.optisigns.com/hc/article_attachments/33468600323987)**

In the “Event Over?” column, put this formula:

```
=IF(B2<=NOW(),"Yes","No")
```

|  |
| --- |
| **NOTE:** This formula will only work if both the Date and Time are present in the Event Time cell. The “B2” part should match the actual event time, i.e. B3 for Zumba in the Example. |

B2 is your reference value, which maps up with the event time. This formula will work regardless of whether or not the current date is referenced in the “Event Time” column.

Within the settings of your Google Sheet, please ensure Recalculation is on (e.g., On change and every hour/minute), otherwise the formula won't recalculate.

![google sheets tutorial image with Calculation highlighted and red arrow pointing at On change and every minute option](https://support.optisigns.com/hc/article_attachments/33468569084819)

You can access this in your Google Sheet by selecting **File** **→** **Settings** **→** **Calculation.**

All the “Event Over?” column does is check whether or not the event time has passed with a simple yes or no. When this screenshot was taken, it was between 1:00 and 3:30, so the first event to be shown should be “Rowing,” followed by “Surrender Yoga.”

To do this, we’ll make use of the **DataSource** **Filter**.

To get started, highlight the data you want to filter, then hit **Settings.** Then, hit the **Filter** option under your DataSource.

![firefox_69WJbcItk0.gif](https://support.optisigns.com/hc/article_attachments/42920711657491)

This screen will appear:

![optisigns datasource filter](https://support.optisigns.com/hc/article_attachments/33468600337171)

What follows is, essentially, an [AND statement](https://support.microsoft.com/en-us/office/and-function-5f19b2e8-e1df-4408-897a-ce285a19e9d9) or an [OR statement](https://support.microsoft.com/en-us/office/and-function-5f19b2e8-e1df-4408-897a-ce285a19e9d9) you might use in Excel or Google Sheets. The easiest way to understand the Filter option is as an Excel or Google Sheet formula you input within OptiSigns.

You can add **Rules** or **RuleSets** to your filter to create as much complexity as you need:

![optisigns datasource filter with additional rules and rulesets](https://support.optisigns.com/hc/article_attachments/33468569116691)

In order to set up a Rule, you’ll need to configure three values.

Selecting the first box gives you these options:

![optisigns datasource filter first box options](https://support.optisigns.com/hc/article_attachments/33468569122707)

By default, these options equate to the **headers of your columns in the spreadsheet you have mapped.** This list will vary in length depending on how many headers you have. You can also input any value you wish by typing it in the box.

The second box is your **Variable.** OptiSigns provides these options:

![optisigns datasource filter second box options](https://support.optisigns.com/hc/article_attachments/33468569128851)

The final option provides the following default values:

![optisigns datasource filter third box options](https://support.optisigns.com/hc/article_attachments/33468569132819)

By default, these map to a screen or other device, allowing your filter to target only certain screens.

However, this value **can be changed to anything you want.** Simply type any value you wish.

For our purposes, we want to check to see if the “Event Over?” is equal to No:

![example of optisync datasource filter with first value set to Event Over?, second value set to Equals, third value set to No](https://support.optisigns.com/hc/article_attachments/33468569142163)

That removes every row where the “Event Over?” value is Yes. Now, your Event Schedule will display this:

![example of daily event schedule with filters applied](https://support.optisigns.com/hc/article_attachments/33468569144851)

There are dozens of possibilities using the OptiSync filter to show even more precise automated data on your screens.

---