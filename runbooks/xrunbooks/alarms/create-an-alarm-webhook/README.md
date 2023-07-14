---
description: >-
  Creating a webhook in unSkript allows for the external systems to report data
  securely to unSkript.  In this tutorial, we'll walk through the steps to
  create a webhook.
---

# Create an Alarm Webhook

unSkript currently supports webhooks for Grafana and AWS (Cloudwatch). The process for creating a webhook is the same.



1. In your unSkript dashboard, go to the proxies tab.  Choose the environment you wish to connect to and then find the Grafana or AWS connection that you wish add the Webhook to:
2. If there is no webhook created, there will be a "Generate" button in the webhook column.  If you have already created a webhook, the button will say "webhook details".



<figure><img src="../../../../.gitbook/assets/image (34).png" alt="" width="563"><figcaption><p>Connections in a proxy</p></figcaption></figure>

3. Click Generate to create the webhook:



<figure><img src="../../../../.gitbook/assets/Screenshot_2023-07-14_at_12_20_18.jpg" alt=""><figcaption></figcaption></figure>

Use these credentials to set up the alarming connection.

## Pull the Alarms

This step will sync the alarms you have created at Grafana and Cloudwatch to unSkript. &#x20;

Just to the right of the webhook details button, click the 3 dot menu, and choose "Pull Alarms."

![](<../../../../.gitbook/assets/image (1).png>)

