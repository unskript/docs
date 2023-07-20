---
description: >-
  In this document, we'll walk through the steps to create an alert with
  Grafana.
---

# Create a Grafana Alert

Use case: When the Grafana alert fires, we would like to run an unSkript RunBook to remediate the situation.

The high level steps for creating a Grafana alert:

1. [Creating a Grafana rule](create-a-grafana-alert.md#creating-grafana-rule)
   1. These are the parameters that will cause the alert to fire.
2. [Creating a Grafana Contact point](create-a-grafana-alert.md#create-the-contact-point) into unSkript
   1. The contact information - where should the alert fire?
3. [Notification Policy](create-a-grafana-alert.md#notification-policy)
   1. How often will the alert notify unSkript?
4. [Test the Alarm](create-a-grafana-alert.md#test-the-alarm)
   1. Sent test data to unSkript.



{% embed url="https://youtu.be/kfsW7pHRqXc" %}

Each of these high level steps are described in greater detail in this page:

## Creating Grafana Rule

First we must create the alert at Grafana. If you already have the alert you wish to use, you can skip this section.

To create a Grafana alert, log into your Grafana dashboard, and in the left navigation, click the alarm bell, and choose alert rules:\
![](<../../../.gitbook/assets/image (20).png>)

On this page, we will create a new rule.

1. Give your Rule a name, and rule type ('Grafana managed alert')

<figure><img src="../../../.gitbook/assets/image (21).png" alt=""><figcaption><p>Defining the rule type</p></figcaption></figure>

2. Create alert queries.
3.  This query is reading a Postgres database for the count of Github stars for [Awesome-Cloudops-Automation](https://github.com/unskript/Awesome-CloudOps-Automation) (click the link, and give us a star!)

    <figure><img src="../../../.gitbook/assets/image (10).png" alt=""><figcaption><p>Creating the query</p></figcaption></figure>
4.  The second query is going to take the results from the first query, and if the last value is over 200, the alert will fire.  (There are more than 200 stars, so this alert will begin firing immediately.)

    <figure><img src="../../../.gitbook/assets/image (15).png" alt=""><figcaption><p>refining the query for alert</p></figcaption></figure>
5. Define the alert conditions.  In the screenshot below, this will check every 1 minute, and begin firing the error after 5 minutes. &#x20;

> Note: This frequency is much too fast this alert.  This frequency will be useful while provisioning the alert. We will update the conditions once the alert is set.

<figure><img src="../../../.gitbook/assets/image (27).png" alt=""><figcaption><p>Defining alert conditions</p></figcaption></figure>

Step 4 of the process is to add details.  Add any details that you wish, and the save the alert.

## Create the Contact Point

Next, we need to connect the alert to unSkript. &#x20;

1. If you have not yet created a Grafana webhook, [Create a Webhook](create-an-alarm-webhook/) with one of your Grafana Credentials.
2. In the Grafana dashboard, we need to create a contact point.  This can be found in the alarms menu in the left navigation:
3.

    <figure><img src="../../../.gitbook/assets/image (7).png" alt=""><figcaption><p>Adding a contact point</p></figcaption></figure>


4. Create a new Contact point.
   1. Type: Webhook
   2. url: The webhook url provided by unSkript
   3. HTTP method: POST
   4. Username (from unskript webhook details)
   5. Password (from unSkriupt webhook details)
5.  &#x20;&#x20;

    <figure><img src="../../../.gitbook/assets/image (26).png" alt="" width="337"><figcaption><p>Inserting the webhook details</p></figcaption></figure>
6. Save your contact point.

## Notification Policy

Ok, so we've created an alert, and a connection to unSkript.  Now let's build a notification policy.



<figure><img src="../../../.gitbook/assets/image (19).png" alt=""><figcaption><p>Adding a Notification Policy</p></figcaption></figure>



Grafana is set with a default notification policy, or you can set an individual policy for specific alerts to be sent to unSkript.

Let's create a specific routing for this alert:&#x20;

1. **Matching rules: Select the alert.**  Set label to "alertname" and the Value to the name of your alert (in the screenshot below, the alert name is "Docs\_rule.")
2. **Contact Point:** Select the Contact point you created with unSkript webhook credentials.
3. **Override general settings.**  These settings will force the alarm to fire every 2 minutes.  That is very frequent, but useful when setting up your alerts.  Choose settings that make sense for your alert.\


<figure><img src="../../../.gitbook/assets/image.png" alt=""><figcaption><p>An example policy</p></figcaption></figure>

## Test the alarm

Send a test alarm message. In the Connection Points menu, select the connection pointing to unSkript, and click Edit. &#x20;

Click the test button, and use label "alertname" with value \<value of your alert>:\


<figure><img src="../../../.gitbook/assets/image (30).png" alt=""><figcaption><p>Testing the alarm</p></figcaption></figure>

This will send a test alert to unSkript.

