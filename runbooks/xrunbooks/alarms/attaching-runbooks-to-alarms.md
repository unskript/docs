---
description: >-
  You've created an alert, and connected to an unSkript Webhook. Let's connect
  it to a RunBook!
---

# Attaching runbooks to alarms

In order to connect an alarm to a RunBook you must have first completed the following steps:

1. [Create an Alarm Webhook](create-an-alarm-webhook/)
2. Create an alert
   1. [Create a Grafana Alert](create-a-grafana-alert.md)
   2. Create a Cloudwatch Alert
3. [Sync the alerts](create-an-alarm-webhook/#pull-the-alarms) into unSkript
   1. In your Proxies tab, find the connection with your webhook, and click the "Pull Alarms" options from the 3 dot menu:\
      ![](<../../../.gitbook/assets/image (15).png>)
4. The Alarm must have fired at least once.  You can test the alert from [Grafana](create-a-grafana-alert.md#test-the-alarm) or Cloudwatch as a proxy.
5. Have a RunBook in mind to connect to the alert.

## Attaching your Alarm to a RunBook

1.  **Find your Alarms:** Click the Events button in the top navigation of unSkript. You'll land on the listing of alarms that are already attached to RunBooks (if this is the first alarm, the table will be empty).

    <figure><img src="../../../.gitbook/assets/image (19).png" alt=""><figcaption></figcaption></figure>
2.  **Alarms not attached to RunBooks:** Since your alarms are not yet attached to a RunBook, click "unattached" on the top right of the table.  This will give you a list of all alarms that have been synced into unSkript, but do not yet have a RunBook connected. You can use the search box to filter the results.  The the screenshot below, we have filtered on the term "docs."

    <figure><img src="../../../.gitbook/assets/image (10).png" alt=""><figcaption></figcaption></figure>
3. **Attach your alarm:** Click the checkbox to select the alarms you'd like to connect to a RunBook, and then click the "attach RunBook" button that is above the table.
4.  **Select your RunBook:** Select the RunBook you'd like to connect to the alarm

    <figure><img src="../../../.gitbook/assets/image (17).png" alt=""><figcaption></figcaption></figure>


5. If your alarm has fired, you will be prompted to connect the output of the alarm to the input parameters of your RunBook. &#x20;

> If your alarm has not fired, you can TEST your alarm. &#x20;
>
> * [Send a Grafana test](create-a-grafana-alert.md#test-the-alarm)
> * Send a Cloudwatch test

6.  To connect alarm parameters to RunBook input parameters, we will use JQ commands:\


    <figure><img src="../../../.gitbook/assets/image (13).png" alt=""><figcaption></figcaption></figure>
7. In the screenshot above, the left side shows the input parameters for the RunBook (in this case "alarm\_name" and "alarm\_value."  The right side shows the 5 most recent alerts from the alarm.
   1. Use JQ commands to select the items from the JSON to populate the RunBook inputs.
   2. if you have never used jq, there is an autofill feature.  Type a period into the box, and a set of options will appear. &#x20;
   3. Once you have chosen the desired path, click return, and the value will appear below the field.
8. Click attach RunBook to connect the alert to the RunBook.

