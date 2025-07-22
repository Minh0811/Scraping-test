#### Adding Text Elements to a Digital Menu Board

First, create your design. You can create your menu within our Designer app.

![firefox_g87oDmb7i3.jpg](https://support.optisigns.com/hc/article_attachments/43051537968787)

The easiest way to set up a DMB is with a **Data Repeater**. For a full breakdown of a Repeater's capabilities, [see this article](https://support.optisigns.com/hc/en-us/articles/29217646663187). Here, we'll stick to teaching how to add information from your POS system.

To set up a Repeater, click **"Repeaters" → Add Blank Repeater**.

![](https://support.optisigns.com/hc/article_attachments/43051537970195)

With the Repeater selected, click **Settings**. Then select **Connect to DataSource** on the Side Menu.

![firefox_yX20kMKstf.jpg](https://support.optisigns.com/hc/article_attachments/43051537971219)

Select the DataSource you set up in the last set under **"Other DataSources"**.

You'll be taken back to the last pane with your DataSource now selected. Now, click **Edit** or double click the selected Repeater to head to the Repeater Editor. This is like a design-within-a-design, specifically for your Repeater (menu) items. With text selected, click the arrow on the left.

![](https://support.optisigns.com/hc/article_attachments/32078326973331)

That brings up the DataSource tab. Click on the DataSource Used in this Design and you'll see something like this:

![](https://support.optisigns.com/hc/article_attachments/31968058948371)

In this example, we want to display the name and the price, with the possibility of saying "SOLD OUT"

By creating text and dragging data points to it, we can create a menu item like this:

![](https://support.optisigns.com/hc/article_attachments/32060268861331)

This was created by finding data points from the API and dragging them into the desired text boxes. In this case, we only wish to display the "name" and "price," so those values were what we dragged into a blank or existing text box.

If your numbers need extra formatting, click on the number, then hit **Settings.**

**![](https://support.optisigns.com/hc/article_attachments/32077278901139)**

Click **Advanced Options →** **"Display Format"** and choose **"Number,"** then click **"Number Format"** and select the formatting you'd like. This will allow you to add dollar signs to your prices, with other options.

![ShareX_q0ybaobi0E.png](https://support.optisigns.com/hc/article_attachments/32060268867859)

Make sure to hit **Update** to make your new number format display.

![mraS5gfp1n.png](https://support.optisigns.com/hc/article_attachments/32060273056019)

The value of a repeater is that it will copy the format of this one cell, then replace the data points with others from your API. Done correctly, your menu should look something like this:

![](https://support.optisigns.com/hc/article_attachments/32077278906643)

The Repeater will pull as many data points as you have set up on your API. In this example, we've made a menu with 9 items, but with proper design you can put as many items as you'd like, with dynamic descriptions as well. If you have more items than what you've set to show on your screen at any one time, the items on the menu will rotate through them until they have all displayed.