# Action Output

The Output of an Action may be referenced later in the xRunBook. To name the output of the action, click configurations to open the Action settings in the right nav.  The OutPUt tab will give a text box where you can bane the output.



The string entered in this dialogue is the name of the output variable, and will contain the output of this task (The output type is defined in the function of the Action.) You can use this variable as an input in any subsequent Action.&#x20;



For example, this Action **AWS List All Regions** places its output in the variable region.

![Action output is saved in the variable 'region'](<../../../.gitbook/assets/image (1).png>)

In the next Action, we can refer to the region variable to access the values. &#x20;

![printing the value of a variable](<../../../.gitbook/assets/image (6).png>)

