# Connecting Actions

With a single Action, your xRunBook can be a powerful tool.  But to unleash the full potential of unSkript, we can connect multiple Actions.

![](<../../.gitbook/assets/Screen Shot 2022-05-16 at 12.47.30 PM.png>)

In the xRunBook, use the search box to search for S**lack** actions. Drag and drop the **Post Slack Message** Action onto the left pane. Use the configuration dialogue to configure the Action with appropriate inputs such as channel name to post to and the message.

{% hint style="info" %}
In order for your Slack Action to work, you'll need to add a Slack Credential with OAuth credentials from Slack.  We've got a tutorial on [connecting unSkript to Slack.](../connectors/slack.md)
{% endhint %}

For the message, we can get creative and post the name of the collection that was created. Let's assume that the collection name is same as the `customer_name` which was a parameter that we created when we created the xRunBook.

![](<../../.gitbook/assets/Screen Shot 2022-05-16 at 12.53.34 PM.png>)

unSkript Actions can be configured with input that derived from parameters or prior outputs. In this case, we configured the input **Message** to be a python expression

```
f"Collection {customer_name} was created"
```

Recall that `customer_name` was a parameter created earlier and will be filled with the value of the parameter when the xRunBook is executed.

![unSkript can post your messages to Slack](<../../.gitbook/assets/Screen Shot 2022-05-16 at 12.58.53 PM.png>)

On running the Action, we see that the message was posted to the `customer-ops` channel in Slack!  Or - run the entire xRunBook and see the same result.
