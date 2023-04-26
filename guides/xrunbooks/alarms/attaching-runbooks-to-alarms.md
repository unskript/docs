# Attaching runbooks to alarms

Terminology: We will use alarms and rules interchangeably. Alert is an instantiation of an alarm.

On clicking the **Generate** webhook URL (explained in the Alarms section), unSkript will fetch all the configured alarms/rules for that credential.

It will show in the **Unattached** tab on the **Events** page as shown here:

<figure><img src="../../../.gitbook/assets/Screen Shot 2022-12-07 at 2.35.27 PM.png" alt=""><figcaption></figcaption></figure>

**Unattached** lists the alarms which we are configured, however they are not attached to any runbook.

In order to run a runbook automatically when an alert comes in, we should be able to attach which fields from the alert payload(json) map to the runbook parameters. We support[ ](https://stedolan.github.io/jq/)**jq** json processor to achieve this.

* Allow at least 1 alert to come in corresponding to the alarm you plan to attach runbook to. This is needed so that we have the alert payload and apply jq expression to map it to the runbook parameters.
* Once the alert count is greater than 0, we can attach a runbook to that alarm.
* Click on the checkbox next to the alarm and click on **Attach Runbook**
* Select the runbook you want to attach and click **Next**
* It will show the list of parameters for that runbook. Beside each parameter, you will see a toggle as shown below:

<figure><img src="../../../.gitbook/assets/Screen Shot 2022-12-08 at 11.20.35 AM (1).png" alt=""><figcaption></figcaption></figure>

* Note that some of the parameters can be constant too, that means they don't need to be derived from the payload. For eg, **Size** is a constant.
* **cluster\_id** needs to be derived from the payload. You can hover over the payload and select the field (lets say you chose **state**) you want to attach to cluster\_id and click on **Attach xrunbook.**
* Thats it!!! Now, every time an alert comes, **cluster\_id** will be the value of **state** field from the alert payload.

\\
