---
description: Execute RunBooks based on external events such as Grafana or CloudWatch alarms
---

# Alarms

If an alarm is being fired at Grafana or Cloudwatch, configure a RunBook to run when the alarm fires.&#x20;

Creating a Grafana alert



To automate this RunBook feature, you'll need:

1. A connection to [Grafana](../../../connnecting/connectors/grafana/) or [AWS](../../../connnecting/connectors/aws/) set up.
2. A RunBook that you would like to run when the alert is sent from the external party.



* [AWS CloudWatch Alarms](./#aws-cloudwatch-alarms)
* [Grafana Alarms](./#grafana-alarms-webhook)





### AWS CloudWatch Alarms



### Grafana Alarms

unSkript can be attached to Grafana alarms using WebHooks. Here is the sequence of steps to perform to enable the notifications to flow from Grafana into unSkript.



Use the [Add credentials](../../../guides/getting-started/add-credentials-to-connect-your-resources.md) workflow to add the Grafana credential. If this was already added, then a Generate button shows up automatically in credential listing screen in front of Grafana.



<figure><img src="../../../.gitbook/assets/Screen Shot 2022-09-26 at 1.56.40 PM.png" alt=""><figcaption></figcaption></figure>

On clicking the Generate button, the system will display a Webhook URL which can be copied into clipboard by using the icon. Go to the Grafana console, and click Alerting > Contact Points

<figure><img src="../../../.gitbook/assets/Screen Shot 2022-09-26 at 2.13.41 PM.png" alt=""><figcaption></figcaption></figure>

Click New Contact Point and fill in the required details. Use contact point type as Webhook and fill in the URL from the clipboard. Exit configuration dialogue by hitting Save button.

<figure><img src="../../../.gitbook/assets/Screen Shot 2022-09-26 at 1.59.38 PM.png" alt=""><figcaption></figcaption></figure>

Use the notification policies to attach the unSkript notification to appropriate events.

