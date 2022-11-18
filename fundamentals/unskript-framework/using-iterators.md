# Using Iterators

A Task can be configured to run using an iterator. This means that one or more of the input parameters of the Task will be supplied by a list.

![](<../../.gitbook/assets/Screen Shot 2022-05-28 at 10.25.19 AM.png>)

In the example above, the input parameter `namespace` is being filled up from the list`['ns1', 'ns2']`. When this task is run, the output will show the summary of execution when detailed printing is disabled.&#x20;



### Multi way Iterator

A task may have more than one inputs that can be assigned together in a single iteration. Take the following example



`get-instance-from-pod` returns a an instance ID.&#x20;

`get-instance-details` needs two parameters region, instanceID

Assuming we assigned the output of the first Task in instance\_list, we can set up the iterator like this

`[ (region: inst.get('region'), instance: inst.get('instanceID')) for inst in instance_list]`



