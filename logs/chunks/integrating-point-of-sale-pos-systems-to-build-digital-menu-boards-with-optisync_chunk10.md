#### Creating Strike Throughs and Sold Out Warnings

In the above example, we show a Sold Out warning. However, we don't want to display that all the time - only when the item isn't available. With OptiSync, this can be accomplished thanks to the Post-request processing we did earlier. Our code created this **"soldout: 0"** data. This is tied to our **"available"** data:

![](https://support.optisigns.com/hc/article_attachments/32077278913043)

When the "available" data reads "true," the "soldout" data reads 0. When your POS system detects items are unavailable, the "available" data will read "false". This will make the "soldout" data read 1.

We can use this knowledge to set up our Sold Out warnings and strike throughs to only appear when items are not available.

Going back to our Repeater Editor, we can click on a piece of text we want to strike through and hit **Settings**:

![](https://support.optisigns.com/hc/article_attachments/32077293399315)

In the Settings tab, hit **Advanced Options**.

![](https://support.optisigns.com/hc/article_attachments/32077801189779)

Under Advanced Options, hit **Property Mapping**.

![](https://support.optisigns.com/hc/article_attachments/31968071408915)

Two values will show up: **Property** and **Value**.

![](https://support.optisigns.com/hc/article_attachments/31968059040275)

Under Property, choose **Linethrough**.

![](https://support.optisigns.com/hc/article_attachments/31968450832915)

Under Value, choose **.soldout.** Before the "." will be the name of your API Request.

**![](https://support.optisigns.com/hc/article_attachments/32077293403411)**

This sets the text to be crossed out when the "soldout" data reads 1.

We can repeat this with the Sold Out reading, except instead of Linethrough, choose **Visible**.

![](https://support.optisigns.com/hc/article_attachments/31968463038227)

This will make the Sold Out text only appear when the "visible" data reads 1 - in other words, when your product is sold out.

Your final menu ought to look something like this:

![](https://support.optisigns.com/hc/article_attachments/32077820105875)

Finally, you're ready to Name and **Save** your Design.

Pushing Digital Menu Boards to Screens
--------------------------------------

Getting your new DMB onto a screen is relatively simple. Go back to the screens you set up with substitution parameters earlier. Then, hit **Edit Screen.**

![](https://support.optisigns.com/hc/article_attachments/31969909937299)

Under **Type**, choose asset, then select your DMB asset to play.

That's all!
-----------

You should be able to create an Digital Menu Board with dynamic data features.

If you have any additional questions, concerns or any feedback about OptiSigns, feel free to reach out to our support team at [support@optisigns.com](mailto:support@optisigns.com).