---
description: Run your RunBook across multiple environments
---

# RunBooks Across Environments: ServiceIDs

## Running xRunBooks across Environments

Often, you'll need to run the same RunBook in multiple environments.  Using the ServiceId, the RUnBook remains the source of truth, and one RunBook run against multiple environments. &#x20;

To make this work, we'll move away from distinct credentials for each Action, and switch to ServiceIds:

<figure><img src="../../../.gitbook/assets/Screenshot 2023-04-05 at 13.06.37.jpg" alt=""><figcaption></figcaption></figure>

Before we get ahead of ourselves, let's take a step back and start from the beginning.

### Credential Setup

In each environment you wish to run the xRunBook in, you'll need a credential for each service.  For each of these credentials, create a ServiceId (that is the same across environments.)

{% hint style="info" %}
For example: you have an AWS credential in two environments: _dev_ and _prod_ with the names _AWS\_EC2\_dev_ and _AWS\_EC2\_prod_. Give each of these credentials a serviceId (for example _AWS\_EC2)._
{% endhint %}

### xRunBook Setup

In order to run a xRunBook multiple environments, you'll need to 'Enable Environment Selection" on the RunBook Details page.

<figure><img src="../../../.gitbook/assets/Screenshot 2023-04-05 at 13.41.18.jpg" alt="enable environment"><figcaption></figcaption></figure>

Next - open the xRunBook Editor.  For each Action change from Credential to serviceId, and select the serviceID.

Now, when you run the xRunBook, you'll need to add the environment as an input parameter.



## Example:

1. Navigate to xRunbooks, click the "unSkript xRunBooks" tab.
2. Search for IAM, and the "Create IAM User" will appear. Click the menu button to the right, and import this xRunBook into your proxy.

Now, open the xRunBook ("My xRunBooks" and it'll be at the top of the list).  Click the menu button, and pick "Open Details."  on this page, select the "Enable environment selection" checkbox:

<figure><img src="../../../.gitbook/assets/Screenshot 2022-12-23 at 15.40.40.jpg" alt="xRunBook with checkbox clicked"><figcaption></figcaption></figure>

Now, we can edit the Workflow - configuring each Action.  Click the Edit button.  For each Action, you can configure a SessionId for the Credential instead of the actual credential.\
\


<figure><img src="../../../.gitbook/assets/Screenshot 2022-12-23 at 18.19.34.jpg" alt=""><figcaption></figcaption></figure>

Since the Credential is a variable that points to a credential in **BOTH** "test\_staging" and "test\_production", this xRunBook can be run in either environment.  Repeat for each Action in the xRunBook.

Save the xRunBook, and when you click "Run" in the xRunBook page, you will be prompted to choose the environment (or environments) you'd like to run the xRunBook:

<figure><img src="../../../.gitbook/assets/Screenshot 2022-12-23 at 18.32.14.jpg" alt=""><figcaption></figcaption></figure>
