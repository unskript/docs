---
description: >-
  Actions are the building blocks for all Runbooks: Use our Open Source
  collection, or build your own!
---

# Actions

## [Prebuilt Action List](broken-reference)

<figure><img src="https://img.shields.io/endpoint?url=https://raw.githubusercontent.com/unskript/Awesome-CloudOps-Automation/master/.github/images/actionShield.json&#x26;style=for-the-badge" alt=""><figcaption></figcaption></figure>

These Actions are open source and ready to be integrated into your RunBooks. In your RunBook, search for the Action you wish to use, and then drag and drop it into your RunBook.  A few configuration steps, and the Action is ready to go!

## [Custom Actions](create-custom-actions.md)

Create your own Actions! &#x20;

* Perhaps there is an existing Action that you can customize to your exact needs.&#x20;
  * For example - **List Open GitHub Issues** can be easily modified to **List Closed GitHub Issues** by changing one parameter in the request ("OPEN" -> "CLOSED")
  * Or perhaps, you need an additional output from the Action, and you can modify the response to append that extra data.
* Create a small Python Script to manipulate the data you already have collected.
  * For example: Here's an Action where data collected from an Action in the RunBook converted into a chart using matplotlib:

![](<../../.gitbook/assets/image (1) (2).png>)



### [Configuring Actions](action-configuration/)

The following items can be configured for each Action:

1. [Name](./#name)
2. [Credential](broken-reference)
3. [Input](action-configuration/action-inputs.md)
4. [Output](action-configuration/action-output.md)
5. [Iterator](action-configuration/action-iterator/)
6. [Poll](action-configuration/action-poll.md)
7. [Start Condition](action-configuration/action-start-condition.md)
