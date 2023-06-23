---
description: Configure input parameters in your RunBook Actions.
---

# Configure Action Inputs



{% embed url="https://youtu.be/7id_TS9EK_c" %}



Most Actions take Input parameters. An input parameter is a way to defined a variable that is submitted to the Action by the user. Action inputs might also be an output from another Action's result.

Allowing for variable input parameters is an important part of making Actions flexible and reusable.  Each Input parameter has a type (List, String, Number, etc.) to ensure that the correct data is being sent into the Action.



### Adding Inputs to an Action

If you are creating an Action, add an input from the three dot menu in the top bar of the Action.  Give the input a name, type, description, and indicate whether the input is required or optional for the Action to run. If you want to, you can provide a default value as well.



### Setting Action values

If you press the configuration button for your action, a menu will appear in the right navigation. The inputs are on the default screen:

<figure><img src="../../../.gitbook/assets/Screenshot 2023-04-13 at 09.47.53.jpg" alt=""><figcaption></figcaption></figure>

`In this case, the Region input is set to the String "us-west-2"`

Alternatively, we can assign the variable region, and now whatever string is in this variable can be applied to the Region input. &#x20;

<figure><img src="../../../.gitbook/assets/Screenshot 2023-04-13 at 09.48.00.jpg" alt=""><figcaption></figcaption></figure>

This allows for greater flexibility in your Action - as long as the region variable matches a AWS region, you can run this Action.

If you have multiple values for an input parameter, you can user [iteration](action-iterator/using-iterators.md) to run the same Action multiple times with different values.
