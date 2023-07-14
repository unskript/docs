---
description: >-
  Connecting Actions to build on one another unleashes the full power of your
  RunBook
---

# Connecting Actions

With a single Action, your xRunBook can be a powerful tool.  But to unleash the full potential of unSkript, we can connect multiple Actions. We do this by placing the output of an Action into a variable, and accessing this variable in subsequent Actions.



Each Action can have it's output saved into a variable for later use. In this example the List of IAM users is saved in the List `users`:

<figure><img src="../../.gitbook/assets/image (9) (1).png" alt=""><figcaption></figcaption></figure>



### Example:

{% embed url="https://youtu.be/Vo1wxjDCj2A" %}

Our first step is to get a list of all the IAM users in our AWS account.  Drag the "List all IAM Users" Action to your RunBook.\


<figure><img src="../../.gitbook/assets/image (12) (1).png" alt=""><figcaption><p>List all IAM Users Action</p></figcaption></figure>

Next, we'll configure this action with credentials (to access our AWS account).  There are no required inputs for this action, but let's name the output of the Action "users."

<figure><img src="../../.gitbook/assets/image (10) (1).png" alt=""><figcaption><p>Configuring the Credentials and output of the Action</p></figcaption></figure>

When we run this Action, the list of users will be saved in the List `users`.

<figure><img src="../../.gitbook/assets/image (2) (1).png" alt=""><figcaption><p>A partial listing of the users in the list.</p></figcaption></figure>

We can now use the data in `users` to build on our RunBook.

In step 2, we'll add a simple Action to the Runbook by clicking  `+ Add -> + Action` in the top navigation.

<figure><img src="../../.gitbook/assets/image (7) (1).png" alt=""><figcaption><p>Modifying the list</p></figcaption></figure>

This code loops through all of the users, and creates another list of the users with "doug" in the name.

Finally, let's send a message to Slack:

<figure><img src="../../.gitbook/assets/image (11).png" alt=""><figcaption><p>Slack Configuration</p></figcaption></figure>

This Action takes the list of doug\_users, finds the length of the list and sends a message to the "devrel\_doug\_test1" channel announcing the number of users.

<figure><img src="../../.gitbook/assets/image (13) (1) (1).png" alt=""><figcaption><p>The Slack Message</p></figcaption></figure>

By naming the output of our Action, we can use that variable in subsequent Actions to manipulate the data, and complete further tasks. &#x20;
