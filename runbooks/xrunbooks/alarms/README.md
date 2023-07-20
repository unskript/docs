---
description: Execute RunBooks based on external events such as Grafana or CloudWatch alarms
---

# Alarms

If an alarm is being fired at Grafana or Cloudwatch, configure a RunBook to run when the alarm fires.&#x20;



To automate this RunBook feature, you'll need:

1. A connection to [Grafana](../../../connnecting/connectors/grafana/) or [AWS](../../../connnecting/connectors/aws/).
   1. A [webhook](create-an-alarm-webhook/) added to your connection.
2. An alarm set at Cloudwatch or Grafana, configured to send alerts to the webhook:

* [AWS CloudWatch Alarms](./#aws-cloudwatch-alarms)
* [Grafana Alarms](./#grafana-alarms-webhook)

3. A RunBook that you would like to run when the alert is sent from the external party.



Once the alarm is created, we [pull the alarms](create-an-alarm-webhook/#pull-the-alarms) into unSkript.  We can then[ attach the alarm to your RunBook](attaching-runbooks-to-alarms.md).



When the alarm fires at Grafana or Cloudwatch, the webhook will receive the message, and initiate the execution of your RunBook.



{% embed url="https://youtu.be/kfsW7pHRqXc" %}

## Using Alarms

#### Auto-remediate:&#x20;

* Create a RunBook that can automatically remediate the issue. &#x20;
* Once the issue is remediated, send an alert to the team, and ensure that the alarms are no longer firing.

#### Diagnose:&#x20;

* Initiate RunBooks to diagnose the alarm.  With diagnostic information provided immedaitely after the alert sounds, the team will have a better idea of how to resolve the problem.



###

