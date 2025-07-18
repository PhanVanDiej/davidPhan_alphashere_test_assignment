# How to use Emergency Feed App

Some Emergency Alert Systems or Emergency Mass Notification Systems do push out RSS feeds.

Using OptiSigns Emergency Feed app, you can have OptiSigns listen to an RSS feed, filter for certain types of messages, and target locations, and if there's matching content, it will take over screens to display emergency messages.

When the emergency is over, the feed returns blank, or no more matching content. OptiSigns will return to playing signage content as usual.

![](https://signagecloud-prd.s3.amazonaws.com/editor/5f1595d6020cce00136d5164/f37643a3bef24cb59f514684aa518c3d_5f1595d6020cce00136d5164.jpg)

## **Let's jump in and get started:**

First, you will need to have your screens set up and paired. For more information on how to do that, click [here](https://www.optisigns.com/blog/how-to-set-up-digital-signs-with-optisigns-and-amazon-fire-tv).

Then log on to our portal: <http://app.optisigns.com/>

Go to Files/Assets, Click on "App"

![](https://support.optisigns.com/hc/article_attachments/29815774668947)

Click Emergency Feed:

![](https://support.optisigns.com/hc/article_attachments/29815767093395)

Set up your Emergency Feed app:

![](https://support.optisigns.com/hc/article_attachments/29815776944787)

* **Name**: Name of your assets, this will not be displayed on the screens.
* **Target:** Select Screens or Tags.
* **Screens/Tags**: Select which screens or group of screens (tags) you want to target for this emergency. (i.e. Fire in building/location 1)
* **RSS URL:** the URL of your RSS feed

Advanced settings:

![](https://support.optisigns.com/hc/article_attachments/29815769407763)

* **Using Text Font, Color, Background Color, Text Alignment, and Background Image**, you can design the message as you desire (i.e. text shows up in the middle of the screen on top of your organization's branded image template)
* **Title Tag:** Message title from the RSS XML feed, default is <title> - you can change if your feed is different
* **Description Tag**: Message content from the RSS XML feed, default is <description> - you can change if your feed is different
* **Location (Screen Tags):** Some RSS can pass locations tag (i.e. emergency in a certain location only) default tag is <location> - you can change it if your feed is different
* **Filter content containing:** you can filter content based on specific words in the title or description. I.E: "fire", so if any title or description contains the word "fire" (non-case insensitive), the app will trigger the screen takeover.
* **Exclude title containing:** this filter will only apply to the title. You can hide all the old feeds by filtering with specific words in the title. I.E: “All Clear”, so after the emergency is gone, all the feeds before this title will be hidden, then the screen will revert to the original content or just display the new content after that.
* **Check RSS feed every:** default is 10s

Click Save.

After Saving, the app will start listening to the RSS feed, if the condition matches based on your settings, all will take over the screens you targeted and display the emergency messages from the RSS feed.

If you have any additional questions, concerns, or any feedback about OptiSigns, feel free to reach out to our support team at [support@optisigns.com](mailto:support@optisigns.com)