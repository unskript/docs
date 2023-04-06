---
description: Use the same xRunBook in different settings with environments
---

# Environment

## # unSkript Environments

{% hint style="info" %}
NOTE: Environments are only available online, and not in the Docker deployment.
{% endhint %}

It is pretty common to have multiple environments for your cloud (dev, staging, production, etc.), each using similar infrastructure, but with different credentials.

With unSkript environments you can configure your xRunBooks to run in all of your environments with no modifications. This ensures that the XRunBook is the source of truth, and there is no worry about source control across your environments.

### Creating an Environment

1. Navigate to the Proxy you wish to add an environment to.  Click "+Add Environment." You'll be prompted to name your environment

<figure><img src="../../.gitbook/assets/Screenshot 2022-12-23 at 15.10.07.jpg" alt="Naming your environment"><figcaption></figcaption></figure>

2\. You'll next be prompted to select some of the services that will connect to the environment.  In the example below, AWS and Slack are selected:

<figure><img src="../../.gitbook/assets/Screenshot 2022-12-23 at 15.10.25.jpg" alt="Connection picker"><figcaption></figcaption></figure>

3\. Your environment will be created.  Now, it is time to edit your Connectors.  In the list of environments, click your new environment, and "Open Details."

<figure><img src="../../.gitbook/assets/Screenshot 2022-12-23 at 15.14.42 (1).jpg" alt="screenshot of a new environment"><figcaption></figcaption></figure>

Now, we will edit each Connection with the credentials needed to connect to the service.  We have [detailed instructions](../../guides/connectors/) for each connection type.  Additionally, add a ServiceId to each Connection.  In this case, we'll use ServiceId with the format "\<appname>\_\<connection>" - meaning that we'll  use 2 ServiceIds here: "test\_aws" and "test\_slack":

<figure><img src="../../.gitbook/assets/Screenshot 2022-12-23 at 15.27.46.jpg" alt="connectors with added credentials"><figcaption></figcaption></figure>

Now, you can create a similar environment called "test\_production", and add in different credentials for AWS and Slack (but be sure to use the same ServiceId value):

<figure><img src="../../.gitbook/assets/Screenshot 2022-12-23 at 15.35.29.jpg" alt=""><figcaption></figcaption></figure>
