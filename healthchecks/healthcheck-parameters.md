---
description: >-
  Each Healthcheck use parameters.  Most are optional, but can be configured if
  desired.
---

# HealthCheck Parameters

## Folder Configuration

By Placing your cursor over the folder, a settings gear will appear.  Clicking this will open the folder configurations:

![](<../.gitbook/assets/image (20).png>)

The parameters for the folder are broken into two sections:

* **Global:** Global parameters can be applied to all of the Checks in the folder.  For example, when using the AWS Connector, "**Region**" is a Global parameter.  If specified, all of the healthchecks will be run in that region.

<figure><img src="../.gitbook/assets/image (12) (2).png" alt=""><figcaption><p>By specifying a region, all of the checks will be run in us-west-2.</p></figcaption></figure>

* Connector Specific: These parameters are specific to the Connector.  In this case, we are specifying 14 days and us-west-2.
* ![](<../.gitbook/assets/image (10) (3).png>)
* Connector parameters override global. &#x20;
  * If the global "Region" is set to "us-west-2", but a check's region is set to "eu-west-1" the check's value will be used.
