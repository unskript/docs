# Using outputs from previous Actions

Action Output from One cell can be used as Input to the Next cell.  Lets us look at an example which will explain it better.&#x20;

<figure><img src="../../.gitbook/assets/Screen Shot 2022-09-27 at 9.02.47 PM.png" alt=""><figcaption><p>Example to show how to use Output of One Cell in the Next Cell</p></figcaption></figure>

Here in the example above, we have two Kubernetes Actions. The first cell check for unHealthy Nodes and stores the output in a variable `probeOutput`&#x20;

<figure><img src="../../.gitbook/assets/Screen Shot 2022-09-27 at 9.01.59 PM.png" alt=""><figcaption><p>Output being saved to probeOutput</p></figcaption></figure>

&#x20;`probeOutput` can be used as Input&#x20;

<figure><img src="../../.gitbook/assets/Screen Shot 2022-09-27 at 9.01.22 PM (1).png" alt=""><figcaption></figcaption></figure>

Or In Start Condition&#x20;

<figure><img src="../../.gitbook/assets/Screen Shot 2022-09-27 at 9.00.05 PM.png" alt=""><figcaption></figcaption></figure>

{% hint style="info" %}
The same way you can use the output variable in the next cells Iterator and Polling feature
{% endhint %}

