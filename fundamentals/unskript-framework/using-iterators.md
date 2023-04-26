# Using Iterators

There may be occasions where you'd like to run an unSkript Action multiple times.  Perhaps the Action takes one value as an input (for example one Kubernetes Namespace), but you need to run the Action across multiple K8s Namespaces.

Using the iterator feature on the "namespace" input variable allows you to send multiple requests to the same Action.  In the screenshot below, the list \['ns1', 'ns2'] is being sent to the Kubernetes Action.



![](<../../.gitbook/assets/Screen Shot 2022-05-28 at 10.25.19 AM.png>)

Rather than run one time, this Action will now run two times: once with the namespace 'ns1' and the second time with 'ns2.'  The output of these multiple runs will be saved in a Dictionary for later use.



### Multi way Iterator

A task may have more than one inputs that can be assigned together in a single iteration. Take the following example



`get-instance-from-pod` returns a an instance ID.&#x20;

`get-instance-details` needs two parameters region, instanceID

Assuming we assigned the output of the first Task in instance\_list, we can set up the iterator like this

`[ (region: inst.get('region'), instance: inst.get('instanceID')) for inst in instance_list]`



