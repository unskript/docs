---
description: Skip an Action - or force it to run - based on the xRunBook Status
---

# Action Start Condition

Start conditions allow flexibility in the way RunBooks are executed.&#x20;



There may be times during a RunBook execution that a step can be skipped - based on different inputs, or values obtained during execution.&#x20;

{% embed url="https://youtu.be/NEJlkIBWHyw" %}

### Example

Let's look at the [`Delete Old EBS Snapshots`](https://github.com/unskript/Awesome-CloudOps-Automation/blob/master/AWS/AWS\_Delete\_Old\_EBS\_Snapshots.ipynb) RunBook (this is a built in RunBook that is part of every unSkript install).&#x20;

There are 3 input parameters for this RunBook:&#x20;

* AWS Region (optional)
* SnapshotID (optional)
* "days until old."

Here are the steps in the RunBook:

1. AWS List all Regions
2. [Iterate](action-iterator/) through each Region to get Snapshots
3. Delete the snapshots

If the RunBook has a Region supplied as input - there is no reason to run Step 1 - **AWS List all Regions**.  So we can enable a start Condition:

![](<../../../.gitbook/assets/image (5).png>)

This Action will run if there is no value in the region variable. If there is a value in region - we can skip this step.

Run 1: No region:

* Get all the regions
* Find all of the Snapshots in all regions
* Delete them

Run 2: region = "us-west-2":

* Skip "get all regions"
* Find the Snapshots in us-west-2
* Delete them.



