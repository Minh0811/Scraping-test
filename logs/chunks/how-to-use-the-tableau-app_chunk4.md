#### Note 3:

[Tableau currently limits](https://help.tableau.com/current/online/en-us/to_site_capacity.htm) its maximum number of refresh requests to 600 per hour/user. This means you'll want to be careful on how you set the "Update Interval," especially if you have numerous devices wanting to display Tableau reports.

We have several recommendations on how to handle this with multiple devices:

1. Set the Update Interval to match the number of devices. For example, if you have 50 devices, you can have a maximum Update Interval of 5 minutes (300 s) for a single report. With more devices this Update Interval will need to be longer, with less, it can be shorter.
2. For using Reports in a Playlist, the Report will update each time it is played. You'll need to set the proper duration, factoring in the number of reports and the number of devices. For example, if you have 10 reports on a single playlist across 5 devices, you can have a Playlist duration of 5 minutes (300 s).
3. To scale beyond these limitations, you'll need to create more connected apps under different Tableau Cloud users. Each Tableau Cloud user will have 600 requests an hour.