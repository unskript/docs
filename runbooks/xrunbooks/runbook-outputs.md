---
description: >-
  If your RunBook is part of a pipeline you'll want the results of the RunBook
  execution to continue your process
---

# RunBook Outputs

RunBooks are able to publish output data.  The output is a JSON collection of data collected from the Actions inside your RunBook.



{% embed url="https://youtu.be/1l-giACuYPI" %}

## Define Output Parameters

To define your output parameters (these will be the "key" in the output JSON):

1. Click the Parameters option in the top navigation.
2. Choose the submenu "Output."
3. Select "Add Input Parameter."

![the Output parameter menu](<../../.gitbook/assets/image (5).png>)



A Dialogue will appear, where you can enter the values that correspond to the data you wish to add to the RunBook output:\
\
In this example, the output will have the name 'iam\_users', and will be a list.

<figure><img src="../../.gitbook/assets/Screenshot 2023-07-13 at 11.32.04.jpg" alt="" width="563"><figcaption><p>Output parameter addition dialogue</p></figcaption></figure>

## Connect Action outputs to the RunBook Output

Each Action has an Output section:

![](<../../.gitbook/assets/image (1) (2).png>)

To add the output from this action to the RunBook output, select the "RunBook Output" checkbox.

![](<../../.gitbook/assets/image (2).png>)

A new text box will appear.  Add the output parameter you wish to connect your Action output to.  In this case, we are connecting the output from "AWS List all IAM Users" to the "iam\_users" output.



## Adding outputs from Glue Actions

Glue Actions are Python code without a connector.  You can add output parmeters from glue actions with the following command:

```python
w.set_output("<output_parameter>", "<variable_to_output>")
```

For example, If we wanted to output a random IAM user, we could use the following glue Action

```python
import random
random_number = random.randint(0, len(iams)-1)
user= iams[random_number]
print(random_number, user)
w.set_output("random_number", "random_number")
w.set_output("random_user", "user")
```

This code reads in the list of IAM users, and randomly selects one of them.  The last two lines add RunBook outputs - "random\_number" and "random\_user".  For this to run successfully, both of these must be added as output parameters:

![](<../../.gitbook/assets/image (4).png>)



## Seeing RunBook Outputs

In the Execution menu of unSkript, find the RunBook execution you wish to examine.  Click the Output tab, and you will see the RunBook output:



<figure><img src="../../.gitbook/assets/Screenshot 2023-07-13 at 12.10.48.jpg" alt=""><figcaption><p>Screenshot of outputs tab of a RunBook execution</p></figcaption></figure>
