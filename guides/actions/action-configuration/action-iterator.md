# Action Iterator

Iterator is a list of input parameters that can be configured to set a loop on the input schema field (Loop Parameter).

More than one item can be specified in the list for the iteration.&#x20;

For example- To create more than one collection in MongoDb we make use of the Iterator.

The list provided here will add two collections (employee, company) to the selected loop parameter (collection\_name). You can verify the items in the list in the source code under task.configure(iterJson...)

![](<../../../.gitbook/assets/Screenshot 2022-08-05 at 3.28.18 PM.png>)

The execution summary shows that the creation was successful. You can check this by fetching the list of collections using an inbuilt Action.&#x20;

![](<../../../.gitbook/assets/Screenshot 2022-08-05 at 3.18.05 PM.png>)

#### Dict type Iterator

<mark style="background-color:red;">To be added</mark>
