# How to display Microsoft Power BI Dashboards & Reports on a TV

### In this article, we will show how to display Microsoft Power BI dashboards and reports on TVs and screens using OptiSigns.

* [What You'll Need](#WhatYouNeed)
* [Prepare Dashboard or Report for Sharing](#PrepareDashboard)
  + [Dashboard Hosted on Microsoft 365](#Microsoft365)
  + [Dashboard from Power BI Desktop App](#DesktopApp)
  + [Displaying Filtered Reports as a Report Bookmark (OPTIONAL)](#FilteredReports)
* [Add Power BI App on OptiSigns](#AddPowerBI)
* [Frequently Asked Questions](#FAQs)
  + [How does security work with OptiSigns Power BI integration?](#PowerBIintegration)
  + [How do I set up a Power BI service principal with OptiSigns?](#ServicePrincipal)
  + [How can I edit the size of the screen on my display?](#SizeofScreen)
  + [My embedded Power BI report shows on my portal, but won't display on my screen. Help?](#DisplayMode)
  + [My Power BI playback is having some issues. Is there any explanation for this?](#WontDisplayOnscreen)

|  |
| --- |
| **NOTE** |
| The **Power BI app** is available to customers with a **Pro Plus plan** **or above**. |

OptiSigns boasts integration with Microsoft Power BI, allowing secure sharing of Power BI Dashboards and Reports to large TVs and screens. This improves communication and information sharing across office spaces.

---

## What You'll Need

* An OptiSigns [Pro Plus plan](https://www.optisigns.com/pricing) subscription or above
* A screen, [set up and paired](https://www.optisigns.com/blog/how-to-set-up-digital-signs-with-optisigns-and-amazon-fire-tv) with OptiSigns
* A valid Microsoft username and password
* Appropriate Power BI Administrative permissions
* A Power BI URL

---

## Prepare Dashboard or Report for Sharing

We'll assume you already have a Power BI dashboard or report built out and ready to showcase to your team members or audience on a large screen.

### Dashboard Hosted on Microsoft 365

If your report or dashboard is hosted on **Microsoft 365**, simply copy the URL link in your Power BI dashboard.

![power bi desktop url](https://support.optisigns.com/hc/article_attachments/37495309620627)

|  |
| --- |
| **NOTE** |
| Make sure to use the URL from the browser address bar. The link from Report Share is a dynamic link, and is not a valid identifier for the dashboard. |

This URL is what you'll need to set up the Power BI app [in the next step.](https://support.optisigns.com/hc/en-us/articles/undefined#AddPowerBI)

### Dashboard from Power BI Desktop App

If your report or dashboard was created using the **Power BI Desktop app**, you need to click **Publish** from the top menu.

![publish button from power bi desktop app](https://support.optisigns.com/hc/article_attachments/37495325626515)

Select the Workspace where you want to publish it.

|  |
| --- |
| **IMPORTANT** |
| Your report must be in a group different from "My workspace" |

![workspace publish power bi](https://support.optisigns.com/hc/article_attachments/37495309627795)

Once it has successfully published, click on Open in Power BI and will be redirected to your report or dashboard.

![publishing to power bi](https://support.optisigns.com/hc/article_attachments/37495309647123)

Copy the URL in your Power BI dashboard.

![copy url power bi dashboard](https://support.optisigns.com/hc/article_attachments/37495309653267)

This URL is what you'll need to set up the Power BI app [in the next step.](https://support.optisigns.com/hc/en-us/articles/undefined#AddPowerBI)

### Displaying Filtered Reports as a Report Bookmark (OPTIONAL)

If you've configured a filter on your Power BI dashboard, OptiSigns can display your filtered report as a Report Bookmark.

Please note: the filter should be set under **Report Bookmark** instead of Personal Bookmark to ensure proper functionality. To create a **Report Bookmark** in Power BI:

* Open the report in "Edit mode".  ![edit mode](https://support.optisigns.com/hc/article_attachments/37495325657235)
* Click on "**View**" and toggle the "**Bookmarks pane**" to On.![](https://support.optisigns.com/hc/article_attachments/37495309664019)
* Choose "**Add**" from the Bookmarks pane. A new bookmark is created with a default name. Rename the bookmark by double-clicking on it.

![bookmarks pane](https://support.optisigns.com/hc/article_attachments/37495309677843)

* Once the bookmark is created, click on the new Bookmark and copy the **URL**.  
  ![copy bookmark url](https://support.optisigns.com/hc/article_attachments/37495325684115)

|  |
| --- |
| **NOTE** |
| Make sure to use the URL from the browser address bar. The link from Report Share is a dynamic link, and is not a valid identifier for the dashboard. |

This is the URL you will use to create a Power BI asset within OptiSigns.

---

## Add Power BI App on OptiSigns

Now, it's time to add an instance of the Power BI app to your OptiSigns account.

Navigate to the **[OptiSigns Portal](https://app.optisigns.com/),**then click **Files/Assets** → **Apps**.

![optisigns files assets apps](https://support.optisigns.com/hc/article_attachments/37495309686163)

Navigate to the **Power BI app**.

![optisigns power bi app location](https://support.optisigns.com/hc/article_attachments/37495309693203)

Enter your Power BI app details.

![optisigns power bi app setup](https://support.optisigns.com/hc/article_attachments/37495325705107)

* **Name -** Name of your Power BI app instance. This is the name of the app in your asset list. It will **not** be displayed on your screens.
* **URL -**  Paste in the Dashboard URL you copied in Step 1 here.
* **Update Interval -** Select how often you want the app to check for an update to the Dashboard. The Default is 600 seconds (10 minutes).
* **Use Service Principal -** When selected, uses a Microsoft Entra ID Service Principal to log in to Power BI. This requires additional setup. For more information, see [How to Set Up a Power BI Service Principal for Use with OptiSigns](https://support.optisigns.com/hc/en-us/articles/32860569148819-How-to-Set-Up-a-PowerBI-Service-Principal-for-Use-in-OptiSigns).
* **Login to Power BI -** In order to view your dashboard on any screen, OptiSigns requires you to authenticate via the pass-through to Microsoft's Power BI service. Simply input your Microsoft ID and password.

Once you are authenticated your app instance should look like this:

![optisigns power bi app fully setup](https://support.optisigns.com/hc/article_attachments/37495309708051)

Now you are ready to display. To confirm it is set up appropriately, you can preview it.

![power bi asset with preview highlighted](https://support.optisigns.com/hc/article_attachments/360061404994)

If it appears to your satisfaction, you can choose to assign your Power BI app instance either directly to a screen or as part of a [Playlist](https://support.optisigns.com/hc/en-us/articles/28295104605843-How-to-Create-Use-Playlists) and/or [Schedule](https://support.optisigns.com/hc/en-us/articles/360016981853-Create-and-Using-Schedules-with-OptiSigns).

This instance will display a single page of a report. You will need to create multiple instances to show multiple pages of a report. These can be placed into a Playlist to have a constantly rotating series of slides showing entire reports or dashboards, or sprinkled in with other Assets - however you like.

---

## Frequently Asked Questions

#### **How does security work with OptiSigns Power BI integration?**

OptiSigns integrates with and displays Power BI dashboards via an official Microsoft API, securely integrated through your Power BI or MS Azure portal. No usernames or passwords are stored in OptiSigns.

Your devices (screens) will display your Power BI report on the screens directly. Power BI data does not pass through our servers. There is no data-farming on our end of any kind.

OptiSigns uses Microsoft APIs for integration. In order for our integrations to work, the integration has to be approved by an administrator. This is the same across all integrations using Microsoft APIs.

This administrator access is only needed for first time access. Once the OptiSigns app is approved for use, other users can use OptiSigns directly.

Customers with MS Azure Enterprise Apps management can also [manage OptiSigns in your Enterprise App](https://support.optisigns.com/hc/en-us/articles/4403616315539) for even more control over security options.

#### **How do I set up a Power BI service principal with OptiSigns?**

We have an entire article dedicated to this process! Please see:

* [Set Up a Power BI Service Principal for Use in OptiSigns](https://support.optisigns.com/hc/en-us/articles/32860569148819-How-to-Set-Up-a-PowerBI-Service-Principal-for-Use-in-OptiSigns)

Please note that the service principal option is only available to customers with an **Enterprise** plan.

#### **How can I edit the size of the screen on my display?**

To make sure your Power BI app displays properly, go to **View** within the Power BI application you want to display. Then hit **Fit to Page**.

![power bi fit to page](https://support.optisigns.com/hc/article_attachments/37192704471315)

Certain display devices may have additional requirements for displaying the report at the proper resolution. For example, mobile devices display at a different resolution than typical HD devices, and so some display issues may arise when setting reports to display on a mobile device.

In addition, certain hardware is not optimized for displaying Power BI. In these cases, we recommend our [OptiSigns Android Player](https://www.optisigns.com/product/hardware/android-player), which guarantees the best support for our software and Power BI in particular.

If issues persist, we recommend contacting our support team at [support@optisigns.com](mailto:support@optisigns.com).

#### **When I put my Power BI URL into the app, a field called "Display Mode" appeared. Why does this appear and what does it do?**

After putting in your Power BI URL, our software will check for a **/dashboards/** folder in the URL text. This indicates that you are displaying a Dashboard report, and will allow you some additional options.

![power bi app display mode](https://support.optisigns.com/hc/article_attachments/37495325711763)

When you click the drop down, three options are available:

![power bi app display mode options](https://support.optisigns.com/hc/article_attachments/37495309725075)

* **Actual Size -** Displays the report in its native resolution.
* **Fit to Width -** The default display option - we recommend this option for most scenarios. It fits your dashboard to the width of the screen.
* **One Column -** Displays a single column of dashboard data.

These options allow additional customization for your Dashboard. Try them out using the Preview feature and see which one looks the best for your needs.

#### **My Power BI report displays on my portal, but won't display on my screen. Help?**

This issue is usually caused by network connectivity issues at the device. We recommend checking and validating your device/screen's network connection.

If you have a Samsung SSSP or LG WebOS TV, there might be a different issue. Microsoft requires a minimum Chromium version of 95 for their apps to display. These TVs typically don't update very often. This is a Microsoft issue, and there is little we can do on our end.

If you have one of these TVs and wish to display SharePoint, we recommend our [Android Player](https://www.optisigns.com/product/hardware/android-player).

If you're still having issues, feel free to contact our support team at [support@optisigns.com](mailto:support@optisigns.com).

### That's all!

OptiSigns is the leader in [digital signage software.](https://www.optisigns.com/) If you have any additional questions, concerns, or any feedback about OptiSigns, feel free to reach out to our support team at [support@optisigns.com](mailto:support@optisigns.com)

**For additional assistance with Power BI usage**Check out this guide here:  
[Publish and share in Power BI](https://docs.microsoft.com/en-us/power-bi/guided-learning/publishingandsharing?tutorial-step=11)