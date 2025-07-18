# Create and Using Schedules with OptiSigns

### OptiSigns offers flexible and powerful scheduling options, allowing you to schedule your content on a calendar. Schedule events to recur daily, on specific days and times, or any way you wish.

**In this article, we will cover:**

* [Creating a Schedule](#Create)
* [Generating a Recurring Schedule](#Generate)
* [Copying a Schedule](#Copy)
* [Handling Overlapping Schedules](#Overlapping)
* [Scheduling Around Time Zones](#Time)
* [Setting Live-Expire for your Schedules](#Set)
* [Assigning a Schedule to Your Screens](#Assign)
* [Playlist Item Scheduling](#Playlist)
* [Frequently Asked Questions About Schedules](#Common)

---

## Creating a Schedule

* Click on the Schedule tab on the top navigation bar.
* Click **Create Schedule**.
* Rename the schedule by clicking on its name.
* Add an event by clicking the **Add Event** button or by dragging and selecting the calendar view to create a schedule at your desired time.
* Fill out the details of your schedule item:  
  + Use assets or playlists in your schedules.
  + Fine-tune the time and set it to repeat daily, weekly, etc., or not at all.
* Click **Save**.

Your schedule item is created. You can edit the schedule item or add more schedule items as needed. It will look something like this:

![](https://support.optisigns.com/hc/article_attachments/30102229437587)

---

## Generating a Recurring Schedule

Follow the steps in the "Create a Schedule" section.

* **Set Recurrence:**
  + Choose from options like:
    - Repeat Daily
    - Repeat Weekly (you can select specific days like Sunday, Monday, etc.)
    - Repeat Monthly (on a specific date each month)
  + Create a Custom Recurrence:
    - Click on the **Custom** option.
    - Set up a more tailored schedule, such as repeating every other day, or specific days of the week on a bi-weekly basis.
    - Define the recurrence pattern according to your needs.
* Save the Recurring Schedule: After setting the recurrence pattern, click **Save** to finalize the recurring schedule.

![](https://support.optisigns.com/hc/article_attachments/30102229446803)

---

## Copying a Schedule

* Navigate to Schedules: Click on **Schedules** from the top menu.
* Select a Schedule: Choose the schedule you want to copy from the list.
* Copy Schedule: Click on the **Duplicate Schedule** button located at the top of the schedule.
* A copy of the schedule will populate. You can modify the copied schedule as desired.

![](https://support.optisigns.com/hc/article_attachments/30102222641555)

---

## Handling Overlapping Schedules

When creating or editing schedules, OptiSigns will notify you of any overlaps.

**Types of Overlaps:**

* **Unintentional Overlaps:**

  + Adjust the start and end times of the schedules to ensure there are no conflicts.
* **Intentional Overlaps:**

  + The last updated schedule will take priority during the conflicted time.

![](https://support.optisigns.com/hc/article_attachments/30102222645139)

---

## Scheduling Around Time Zones

The screens/devices will play according to their local time zones.

**Example:**

* You (and your computer) are in the CST time zone (GMT - 6).
* Device 1 is in the EST time zone (GMT - 5).
* Device 2 is in the PST time zone (GMT - 8).

You set a schedule item to play from 10 AM to 11 AM on 1/1/20XX.

* Device 1 will play the schedule item from 10 AM to 11 AM on 1/1/20XX in its local time (EST).
* Device 2 will play the schedule item from 10 AM to 11 AM on 1/1/20XX in its local time (PST).

Daylight saving time adjustments will be handled automatically.

---

## Setting Live-Expire for Your Schedules

You can use the [Set Asset to Live & Expire](https://support.optisigns.com/hc/en-us/articles/360042736794) feature to schedule content to go live or expire on specific dates.

---

## Assigning a Schedule to Your Screens

There are two ways to assign a schedule to your screens.

**Method 1:**

1. * Navigate to Screens: Click on the **Screens** tab.
   * Select Screen: Click **Edit** on the screens you'd like to assign the schedule to.
   * Assign Schedule: In the Edit Screen modal:
     + Select **Type = Schedule**.
     + Select the schedule you just created from the list of available schedules.
   * Click **Save**.

![](https://support.optisigns.com/hc/article_attachments/30102229471891)

**Method 2:**

* Navigate to Schedule: Click on the **Schedules** tab.
* Select Schedule: Select the schedule you would like to push to the screen(s).
* Push to Screen: Click on the **Push to Screen** icon on the top menu of your schedule.

![](https://support.optisigns.com/hc/article_attachments/30102222658963)

---

## Playlist Item Scheduling

Playlist item scheduling is a great tool for tailoring your content to different times of the day, week, or even specific dates.

* Create or Edit Playlist: Select the playlist you want to manage.
* Schedule Items: For each item in the playlist, set specific start and end times or days when they should be displayed.
* Save Playlist: Click **Save** to apply the item-specific scheduling.

---

## Frequently Asked Questions About Schedules

**What if there is a one-time schedule overlapping a recurring schedule?**

The one-time schedule will take priority.

**Example:**

* Recurring schedule A (9 AM - 5 PM daily) overlaps with a one-time schedule B (10 AM - 11 AM) today.

**Playback Order:**

* 9 AM - 10 AM: Recurring schedule A
* 10 AM - 11 AM: Single schedule B
* 11 AM - 5 PM: Recurring schedule A resumes

**What if there are two recurring schedules overlapping?**

The most recently created/ updated schedule will take priority.

**What happens when there's nothing scheduled?**

If there is no scheduled content, the screen will display a black screen by default. To avoid this, you can set default content. There are two ways to do this:

* **At the Schedule Level:** Edit the specific schedule, click on **Settings**, and select your preferred default content (None, Account Default, Asset, or Playlist).

![](https://support.optisigns.com/hc/article_attachments/30102222667539)

* **At the Account Level:** Apply a default content setting that will apply to all newly created schedules. The schedule-level setting will take priority if both are set.

![](https://support.optisigns.com/hc/article_attachments/30102229493651)

For detailed information, visit: [Assign Default Content for Schedules](https://support.optisigns.com/hc/en-us/articles/360040943374)

**Can I move an existing schedule to a folder I created?**  
Yes, you can click on **Move Schedule** on the top of the Schedule menu and then select the folder you wish to move the schedule to.

![](https://support.optisigns.com/hc/article_attachments/30102222683027)

**Is it possible to manage schedules for multiple locations from a single interface?**Yes, users can manage schedules for multiple locations from a central interface. This is particularly useful for organizations with screens in different geographical areas.

---

**That's it!**