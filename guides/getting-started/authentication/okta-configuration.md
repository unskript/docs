---
description: This page describes the steps required to be done inside Okta to enable SSO.
---

# Okta configuration

{% hint style="info" %}
NOTE: You need to be an admin to do the following steps in Okta
{% endhint %}

*   Login into Okta and go to **Applications** section in Admin Panel\


    <figure><img src="../../../.gitbook/assets/Screen_Shot_2023-01-19_at_11_23_54_AM.jpg" alt=""><figcaption></figcaption></figure>
*   Create a new SAML 2.0 app\
    \


    <figure><img src="../../../.gitbook/assets/Screen_Shot_2023-01-19_at_11_27_34_AM.jpg" alt=""><figcaption></figcaption></figure>

    <figure><img src="../../../.gitbook/assets/Screen_Shot_2023-01-19_at_11_27_46_AM.jpg" alt=""><figcaption></figcaption></figure>
*   Choose an appropriate name for the app (for eg. **unSkript-sso**) and click **Next**



    <figure><img src="../../../.gitbook/assets/Screen Shot 2023-01-19 at 11.31.00 AM.png" alt=""><figcaption></figcaption></figure>
*   On the **Configure SAML** tab, please fill in the highlighted fields\


    <figure><img src="../../../.gitbook/assets/Screen_Shot_2023-01-19_at_11_33_03_AM.jpg" alt=""><figcaption></figcaption></figure>

{% hint style="info" %}
Please reach out to unSkript team at support@unskript.com for the values of the above fields.
{% endhint %}

*   In the **Attribute statements** section of the form, please fill in the following 2 attributes\


    <figure><img src="../../../.gitbook/assets/Screen Shot 2023-01-19 at 1.48.51 PM.png" alt=""><figcaption></figcaption></figure>



    * The **name** attribute value will be  \
      `String.join(" ", user.firstName, user.lastName)`
    * The **email** attribute value will be **user.email** (Chose from the drop down)
    * Click **Next**
*   On the **Feedback** page, please check the highlighted option and click **Finish**\


    <figure><img src="../../../.gitbook/assets/Screen_Shot_2023-01-19_at_2_12_58_PM.jpg" alt=""><figcaption></figcaption></figure>
*   Next, we will need the Single sign-on URL and x.509 certificate to configure the SP on our side.   Click on the highlighted button to get the above values\


    <figure><img src="../../../.gitbook/assets/Screen_Shot_2023-01-19_at_2_17_04_PM.jpg" alt=""><figcaption></figcaption></figure>
*   Copy **Identity Provider Single Sign-On URL** and also download the certificate as highlighted below\


    <figure><img src="../../../.gitbook/assets/Screen_Shot_2023-01-19_at_2_24_45_PM.jpg" alt=""><figcaption></figcaption></figure>

{% hint style="info" %}
Please send the above 2 piece of information to support@unskript.com
{% endhint %}

*   Assign users to this new application, so that sign in into unSkript application using Okta SSO. Click on **Assignments** tab to accomplish this.\


    <figure><img src="../../../.gitbook/assets/Screen_Shot_2023-01-19_at_2_29_28_PM.jpg" alt=""><figcaption></figcaption></figure>
