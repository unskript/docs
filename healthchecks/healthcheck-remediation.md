---
description: One of your HealthChecks has failed. Let's remediate the issue.
---

# HealthCheck Remediation

<figure><img src="../.gitbook/assets/image (1).png" alt=""><figcaption><p>A failed Check</p></figcaption></figure>

Your HealthCheck has failed. Each check has a remediation RunBook that can work to resolve the issue.

## Remediate the Check

In the Screenshot above, the check has found EBS snapshots that are over 30 days old.

* The "Click here to fix" button will launch a RunBook to resolve the issue.
* In the case of "EBS Snapshots over 30 days old," the resolution is to delete the old snapshots.
* ![](<../.gitbook/assets/image (2).png>)

> The way EBS snapshots are deleted is that only redundant/overwritten data is removed. Any data that is current in the oldest backup is saved to a snapshot not being deleted.

* At the bottom of the menu are options to run the RunBook - -either automatically or interactively.

Upon completion of the remediation RunBook, this Check will be resolved. Repeat for all checks that have failed.
