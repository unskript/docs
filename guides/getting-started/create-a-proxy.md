---
description: Proxies are dedicated runtime environments for your unSkript install
---

# Create a Proxy

{% hint style="info" %}
Note: There is no concept of a Proxy in the [open source version](https://github.com/unskript/Awesome-CloudOps-Automation) of unSkript, as it is assumed that your install will be behind your firewall.
{% endhint %}

unSkript needs a dedicated runtime environment where xRunBook workflows can be securely executed. This can be either on the unSkript SAAS side, or in your cloud (behind your cloud firewalls).

Customers who want to connect to resources and APIs that are not reachable from the Internet can use a customer hosted Proxy. unSkript offers an AMI (Amazon Machine Image) that can be used to bring up this proxy.

On the Proxies tab, click the `Add Proxy` button and select your Cloud provider. Complete the provided form fields to generate a CloudFormation template that you can use to bring up the proxy instance on an EC2 machine.

![Environment Bringup is done using CloudFormation or Terraform templates](<../../.gitbook/assets/Screenshot 2022-08-17 at 8.15.38 PM.png>)

Once you boot up the AMI, it establishes a secure connection with unSkript SaaS and the status will turn change to <mark style="color:green;background-color:yellow;">`READY`</mark>.

{% hint style="info" %}
In the [free cloud sandbox,](https://us.app.unskript.io/) only one proxy (that is hosted at`unSkript)` is available. Contact us for demos of our proxies in other clouds.
{% endhint %}

We also support environments other than AWS. Please contact support@unskript.com to schedule an onboarding call to bring up Non-AWS environments.
