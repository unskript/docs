---
description: Run the same action multiple times with different input parameters
---

# Action Iterator

### Reuse the same Action multiple times

{% embed url="https://youtu.be/7id_TS9EK_c?t=149" %}

Action inputs are generally designed for a single value. For example, an input named _**AWS Region**_ will accept a string like "us-west-2". &#x20;

But what if you need to test the same action across \*many regions\*? Rather than hardcoding multiple instances of the same action, you can use the Iterator to execute the same action multiple times.



Example: This Action gives an array of Public AWS EC2 instances for a given region.  Configured as below, it will list the instances for "us-west-2":

<figure><img src="../../../../.gitbook/assets/configuration.jpg" alt="screenshot of an Action&#x27;s input configuration." width="375"><figcaption><p>Action using a single reagion as input</p></figcaption></figure>

However, we can run this across multiple regions by changing the Region input to an iterator:

<figure><img src="../../../../.gitbook/assets/iteration.jpg" alt="screenshot of an iteration configuration"><figcaption></figcaption></figure>

We set the Loop Parameter to region &#x20;

The List item contains the values for the Loop Parameter (in the above example there are 2 regions:`["us-west-2","us-east-1"]`. &#x20;

Note, the List Item can also be a variable.

When the Action is run with the above iterator, it will run twice:

<figure><img src="../../../../.gitbook/assets/Screenshot 2022-12-29 at 17.28.49.jpg" alt=""><figcaption></figcaption></figure>

The values of the iteration are stored in a Dict:

```json
{'us-west-2': 
		{<us-west-2 values>}, 
'us-east-1': 
		{<us-east-1 values>}
}
```









### Dict type Iterator

<mark style="background-color:red;">To be added</mark>
