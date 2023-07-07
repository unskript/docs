# Create Custom Actions

While unSkript offers many Actions for your xRunBooks, it's probable that you'll want to create your own, or perhaps modify an existing Action for your specific needs.

For this, you can create a custom Action.

{% embed url="https://youtu.be/gorMpBJVFxU" %}



## Modify an Existing Action

You can modify the source code of a built-in Action to create your custom action.&#x20;

> For example, Perhaps the **List all AWS IAM Users** returns a list of usernames:
>
> ![](<../../.gitbook/assets/image (13) (2).png>)

What if we'd like to also retrieve the Arn for each user? We can just modify the existing code:

```
        for x in response['Users']:
            #users_list.append(x['UserName'])
            users_list.append({"name":x['UserName'], "arn":x['Arn']})
```

We have commented out the original code that returns just the name, and repalced it with a dictionary with the name and Arn values for each User in the list:

<figure><img src="../../.gitbook/assets/Screenshot 2023-06-16 at 18.38.54.jpg" alt=""><figcaption><p>Action Updated with refined code for your use case!</p></figcaption></figure>

## Creating a New Action: With Connector

Each Connector has a "handle" Action that has the basic connectivity built in.  Building on this Action allows you to make the API calls into your service as needed.



In the example below, the AWS boto3 handle Action is used as a base to create a new AWS Action to fetch all EC2 instances for that region.

![](<../../.gitbook/assets/image (1) (1) (1).png>)

The custom action can be renamed and saved as a new Action to fit your Task.&#x20;

![Save As](<../../.gitbook/assets/image (3).png>)

Fill out the details to save the new Action.

![](<../../.gitbook/assets/image (2) (1) (1).png>)

You can view all your Custom Actions in the Actions tab under myActions.

![](<../../.gitbook/assets/image (4) (1).png>)
