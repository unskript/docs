# Create a RunBook Input Parameter

Parameters are the input key:value pairs that can be submitted with your xRunBook in order to run. Let's walk through the steps to create a Parameter for your xRunBook.

## Add Parameter

In this step we will define the key for an input (in the example below, we create a `customer` input key).  You can imagine that you might run a xRunBook with the key:value pair `customer: John Doe.`

{% hint style="info" %}
As a best practice, use snake case for parameter names.
{% endhint %}

To add a parameter to your xRunBook, click the Parameters button to reveal the drop down.&#x20;

![Adding a \`customer\` input parameter.](<../../.gitbook/assets/Screen Shot 2022-05-16 at 12.48.07 AM.png>)

Fill in the required information and click `CREATE`. Once created, the parameter is available to be used as a Python variable of the same name. You can use this in code for custom Actions that you create, or as arguments to the Actions you are using.

{% embed url="https://youtu.be/08L2CpWGWdg" %}
Example of adding an input parameter to a RunBook and Reusing it in Actions.
{% endembed %}

## Input Types

* string
* number
* boolean
* array
* object
* secret (string obfuscated with \*)
