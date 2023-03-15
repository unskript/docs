# Credential Parameterization

Credential Parameterization allows an xRunBook to execute across multiple environments.

For this, we need to add 2 parameters while creating the credentials-

<figure><img src="../../.gitbook/assets/Screenshot 2022-09-14 at 4.41.19 PM.png" alt=""><figcaption></figcaption></figure>

1. Service ID - Service ID label allows us to dynamically select a credential for a runbook execution.
2. Environment - Environment acts as an Instance ID for a particular service ID. It is a differentiator label for multiple credentials for the same Service ID.

<figure><img src="../../.gitbook/assets/Credential 1.png" alt=""><figcaption></figcaption></figure>

As shown in the picture above, we can execute an xRunbook for multiple environments which are configured for different credentials of the same resource.

### Use

Reusability of a runbook with certain actions can be achieved with the use of Credential Parameterization. Therefore any reconstruction/ reconfiguration of an existing runbook can be avoided by simply selecting different environment(s) during execution.

### Example Scenario

#### xRunbook purpose

&#x20;To fetch and display a graph of the server statistics for servers A and B

#### Steps

1. Create credentials for server A and server B with the same Service ID
2. Give a different Environment name for servers A and B
3. While Executing the xRunbook, select the required Environment name for the corresponding server.

### Credential Parameterization in Play

We can enable environment selection by checking the box in Runbook details-

![Check/ Uncheck for Environment Selection](<../../.gitbook/assets/Screenshot 2022-08-17 at 6.29.54 PM.png>)

While configuring the actions, enable the Search using ServiceID option to allow this runbook to execute in multiple environment-

![](<../../.gitbook/assets/56B34840-9814-45EB-B8BE-78D13A3326D8 (1) (1) (1) (1) (1) (1) (1) (1) (1) (1) (1) (1) (1) (1).png>)

Then we can trigger the execution by clicking on the <mark style="color:orange;background-color:yellow;">`Run`</mark> button-

![unSkript can run xRunBooks interactively or non-interactively](<../../.gitbook/assets/Screenshot 2022-08-17 at 6.29.02 PM.png>)

This creates an execution of the xRunBook which will then ask for the environment(s) in which this runbook has to execute-&#x20;

![xRunBooks needs parameters](<../../.gitbook/assets/Screenshot 2022-08-17 at 6.29.28 PM.png>)

Here we have 2 environments in which this runbook can be executed under the same Service ID.&#x20;

The execution progress can be checked in the Executions tab.
