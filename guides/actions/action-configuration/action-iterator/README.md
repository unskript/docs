---
description: Run the same action multiple times with different input parameters
---

# Action Iterator

### Reuse the same Action multiple times

{% embed url="https://youtu.be/7id_TS9EK_c?t=149" %}

Action inputs are generally designed for a single value.&#x20;

> For example, a string input named _**AWS Region**_ will accept "us-west-2". &#x20;

<figure><img src="../../../../.gitbook/assets/configuration.jpg" alt="screenshot of an Action&#x27;s input configuration." width="375"><figcaption><p>Action using a single reagion as input</p></figcaption></figure>

But what if you need to test the same action across \*many regions\*? Rather than hardcoding multiple instances of the same action, you can use the Iterator to execute the same action multiple times.



> Example: Using the iterator. The **List to iterate** entry has 2 values: 'us-west-2' and 'us-east-1'.  The iterator will iterate over the parameter 'region'. This action will be run twice (serially) with each value for region.

<figure><img src="../../../../.gitbook/assets/iteration.jpg" alt="screenshot of an iteration configuration" width="375"><figcaption></figcaption></figure>

<figure><img src="../../../../.gitbook/assets/Screenshot 2022-12-29 at 17.28.49.jpg" alt=""><figcaption></figcaption></figure>

The values of the iteration are stored in a Dict:



```json
{'us-west-2': 
		{<us-west-2 values>}, 
'us-east-1': 
		{<us-east-1 values>}
}
```

### Iteration with a variable

The List Item can also be a variable. Below, \*\*regionList\*\* is used. The Action will run once for each value in the list.

<figure><img src="../../../../.gitbook/assets/Screenshot 2023-06-16 at 16.37.03.jpg" alt="" width="375"><figcaption></figcaption></figure>

### Iteration with multiple values.

Imagine that you have an Action that takes in two parameters, and you want to iterate through several permutations.  This can be done with a list of Dictionaries:

Example:  We would like to update the tags of various resources at AWS.  If we build a list of dictionaries as follows:

```
[ {'arn': ['arn:aws:ec2:us-west-2::image/instance'], 
    'value': 'unskript'
   }, 
  {'arn': ['arn:aws:ec2:us-west-2::image/instance2'],
   'value': 'unskript'
   }
]
```

Here we have 2 AWS arn values, and two tag values.&#x20;

In the **Add Tag to AWS Resources,** we can iterate over this list as follows:

<figure><img src="../../../../.gitbook/assets/Screenshot 2023-06-16 at 18.14.26.jpg" alt="" width="375"><figcaption></figcaption></figure>

This reads the output\_list, and places the value for 'arn' in the 'resource\_arn' parameter, and 'value' in the 'tag\_value' parameter.\
\
