---
description: Use the same xRunBook in different settings with environments
---

# Proxy Environments

## # unSkript Environments

{% hint style="info" %}
NOTE: Environments are only available in our Cloud SAAS offering. Contact us for a demonstration.
{% endhint %}

It is pretty common to have multiple environments for your cloud (dev, staging, production, etc.), each using similar infrastructure, but wth different credentials.

With unSkript environments you can configure each of your xRunBooks to run in all of your environments with no modifications.  By using the same xRunBook in each environment, you are assured the same results.

### Creating an Environment

1. Navigate to the Proxy you wish to add an environment to.  Click "+Add Environment." You'll be prompted to name your environment

<figure><img src="../../.gitbook/assets/Screenshot 2022-12-23 at 15.10.07.jpg" alt="Naming your environment"><figcaption></figcaption></figure>

2\. You'll next be prompted to select some of the services that will connect to the environment.  In the example below, AWS and Slack are selected:

<figure><img src="../../.gitbook/assets/Screenshot 2022-12-23 at 15.10.25.jpg" alt="Connection picker"><figcaption></figcaption></figure>

3\. Your environment will be created.  Now, it is time to edit your Connectors.  In the list of environments, click your new environment, and "Open Details."

<figure><img src="../../.gitbook/assets/Screenshot 2022-12-23 at 15.14.42.jpg" alt="screenshot of a new environment"><figcaption></figcaption></figure>

Now, we will edit each Connection with the credentials needed to connect to the service.  We have [detailed instructions](../../guides/connectors/) for each connection type.  Additionally, add a ServiceId to each Connection.  In this case, we'll use ServiceId with the format "\<appname>\_\<connection>" - meaning that we'll  use 2 ServiceIds here: "test\_aws" and "test\_slack":

<figure><img src="../../.gitbook/assets/Screenshot 2022-12-23 at 15.27.46.jpg" alt="connectors with added credentials"><figcaption></figcaption></figure>

Now, you can create a similar environment called "test\_production", and add in different credentials for AWS and Slack (but be sure to use the same ServiceId value):

<figure><img src="../../.gitbook/assets/Screenshot 2022-12-23 at 15.35.29.jpg" alt=""><figcaption></figcaption></figure>

## Running xRunBooks across Environments

To demonstrate the power of environments, we'll use a pre-built xRunbook. &#x20;

1. Navigate to xRunbooks, click the "unSkript xRunBooks" tab.
2. Search for IAM, and the "Create IAM User" will appear. Click the menu button to the right, and import this xRunBook into your proxy.

Now, open the xRunBook ("My xRunBooks" and it'll be at the top of the list).  Click the menu button, and pick "Open Details."  on this page, select the "Enable environment selection" checkbox:

<figure><img src="../../.gitbook/assets/Screenshot 2022-12-23 at 15.40.40.jpg" alt="xRunBook with checkbox clicked"><figcaption></figcaption></figure>

Now, we can edit the Workflow - configuring each Action.  Click the Edit button.  For each Action, you can configure a SessionId for the Credential instead of the actual credential.\
\


<figure><img src="../../.gitbook/assets/Screenshot 2022-12-23 at 18.19.34.jpg" alt=""><figcaption></figcaption></figure>

Since the Credential is a variable that points to a credential in **BOTH** "test\_staging" and "test\_production", this xRunBook can be run in either environment.  Repeat for each Action in the xRunBook.

Save the xRunBook, and when you click "Run" in the xRunBook page, you will be prompted to choose the environment (or environments) you'd like to run the xRunBook:

<figure><img src="../../.gitbook/assets/Screenshot 2022-12-23 at 18.32.14.jpg" alt=""><figcaption></figcaption></figure>
