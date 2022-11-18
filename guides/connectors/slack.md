---
description: Connect your xRunBook Actions to Slack. Message your team!
---

# Slack

![Information needed to onboard Slack connector](<../../.gitbook/assets/Screen Shot 2022-06-14 at 6.22.14 PM.png>)

| Name               | Description                                               |
| ------------------ | --------------------------------------------------------- |
| Name               | This credential will be listed using the name you provide |
| OAuth Access Token | OAuth Access Token of the Slack app                       |

### Creating a Slack OAuth Access Token

To Obtain a Slack Access Token, you'll need to complete a few steps with Slack:

1. Create a [Slack Application](https://api.slack.com/apps). Choose "from a manifest".

![](<../../.gitbook/assets/Screenshot 2022-11-03 at 6.49.11 PM.jpg>)

2\. Pick the workspace you'd like to send messages to:  (If you have yet, join our [Cloud-ops-community](https://join.slack.com/t/cloud-ops-community/shared\_invite/zt-1fvuobp10-\~r\_KyK9BxPhGiebOvl3h\_w) workspace)

<figure><img src="../../.gitbook/assets/Screenshot 2022-11-03 at 6.52.28 PM.jpg" alt=""><figcaption></figcaption></figure>

3\. In the manifest file, you can name your application:

<figure><img src="../../.gitbook/assets/Screenshot 2022-11-03 at 6.55.02 PM.jpg" alt=""><figcaption></figcaption></figure>

4\.  Click through the rest of the steps, and then you'll land at a page with many configuration options. Under "add features and functionality," click "Permissions."

5\. Scroll to "Scopes."  We need to add 2 scopes for the app to send messages to our Slack Channel: `channels:read` and `chat:write`.

6\.  We're now ready to create the OAuth token.  Scroll to the top of the page, and click the green "Install to Workspace" (if you make changes, you'll have a "reinstall app" option).

7\. This will create your OAuth token that you can insert into your unSkript Credentials.
