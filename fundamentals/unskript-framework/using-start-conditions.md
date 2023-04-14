# Using Start Conditions

A Task can be attached a Condition such that only if the condition is satisfied, the task is executed. You can think of it as a condition to start executing the Task.

The start condition is any Python expression like `variable == True` or `numInstances > 6` or `instance_name == "i-123453456"` . unSkript infrastructure takes the condition and executes it like a Phython Expression and based on the result, it would proceed with executing the Task.

You can use this feature in combination of `Output from Previous Action` to decide whether to run the current Task or not.

Examples:

<figure><img src="../../.gitbook/assets/Screen Shot 2022-09-27 at 8.43.08 PM (1).png" alt=""><figcaption><p>Creating a Start Condition</p></figcaption></figure>

<figure><img src="../../.gitbook/assets/Screen Shot 2022-09-27 at 8.43.01 PM.png" alt=""><figcaption><p>Skipping the Execution due to start condition not met</p></figcaption></figure>

<figure><img src="../../.gitbook/assets/Screen Shot 2022-09-27 at 8.44.49 PM.png" alt=""><figcaption><p>More Complex Start Condition</p></figcaption></figure>

<figure><img src="../../.gitbook/assets/Screen Shot 2022-09-27 at 8.44.42 PM.png" alt=""><figcaption><p>Skipping due to Start Condition not Met</p></figcaption></figure>

{% hint style="info" %}
Pro Tip: As can be seen above, any expression that can be executed using the python "eval" statement can be used as the start condition.
{% endhint %}
