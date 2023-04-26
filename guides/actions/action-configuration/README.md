# Action Configuration

Once the Action has been added to your xRunBook, There are a number of parameters that can be configured, giving you the flexibility you need to run your action in your xRunBook.&#x20;

To configure an Action, click on the configurations button for the Action in your xRunBook.

The following items can be configured for each Action:

1. [Name](./#name)
2. [Credential](./#credential)
3. [Input](action-inputs.md)
4. [Output](action-output.md)
5. [Iterator](action-iterator/)
6. [Poll](./#polls)
7. [Start Condition](./#start-condition)

### Name

The name of the Action. You can click the Edit icon next to the name on the right side bar and change the name as desired.

### Credential

If your Action is connecting to an external resource, it will likely require a credential to authenticate the connection. These are created in the Environments page. If you need to add a credential, you can [Create a Credential](../../xrunbooks/create-a-credential.md).

![](<../../../.gitbook/assets/Screenshot 2022-08-17 at 7.01.31 PM.png>)

Use the drop down to select the credential that you would like to use. You can also create a credential from the drop down.



### Polls

Polls can be used to wait for the function to return a specified expected condition. It takes in the output type, value, interval and timeout values.

Here is an example which ends the poll when an AWS EC2 instance is restarted successfully.

The  'Get AWS Instance Details' Action is modified to return True if the Status of the Instance is "Running". This passes the poll check.

![](<../../../.gitbook/assets/Screenshot 2022-08-10 at 6.06.21 PM.png>)

### **Start Condition**

A python condition can be given as a start condition to run the task.

![Configure a start condition](<../../../.gitbook/assets/Screenshot 2022-08-01 at 8.42.14 PM.png>)
