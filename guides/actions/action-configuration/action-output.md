# Action Output

The Output of an Action may be referenced later in the xRunBook. It will be saved in the variable name provided in the output configuration.

The string entered in this dialogue is the name of the output variable, and will contain the output of this task. You can use this variable as an input in any subsequent Action.&#x20;



For example, this Action **AWS List All Regions** places its output in the variable region.

![Action output is saved in the variable 'region'](<../../../.gitbook/assets/image (1).png>)

In the next Action, we can refer to the region variable to access the values. &#x20;

![printing the value of a variable](<../../../.gitbook/assets/image (6).png>)

