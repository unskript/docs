# AWS hosted Proxy

unSkript's Runtime Environment works like a proxy and can be hosted seamlessly like a virtual machine in the client's environment.

In this tutorial, we'll establish a connection to your proxy in your AWS environment, by deploying the proxy to an AWS EC2 instance using CloudFormation.

![](<../../.gitbook/assets/Screenshot 2022-08-11 at 1.02.07 PM.png>)

Follow the steps as given for the proxy deployment.

![](<../../.gitbook/assets/Screenshot 2022-08-09 at 3.10.53 PM.png>)

Step 2 of the Proxy Deployment Instructions as on the AWS CloudFormation console-

![](../../.gitbook/assets/12650EB1-C77C-4240-AA7F-16D9BF5FBF3B.png)

Step 3 can be filled out this way-

![Part 1 of the stack details](<../../.gitbook/assets/Screenshot 2022-08-09 at 3.15.42 PM.png>)

![Part 2 of the stack details](../../.gitbook/assets/F5C2A6FB-AD12-40CB-AD6C-979E3209823C.png)

Please note-

1. You can choose any permissible name for `IAMPolicyName`, `IAMRoleName`, `IAMInstanceName`, and `SecurityGroupName`.
2. `InstanceType` will be <mark style="color:orange;">t2.large</mark> and `VolumeSize` will be <mark style="color:orange;">64</mark> which will be pre-filled from the template that was uploaded in Step1.
3. For `KeyName` you can create your public and private keys by following these [steps](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/cfn-console-create-keypair.html) or use an existing one.
4. While choosing a `Subnet` and `VPC`, make sure to-

* Install the unSkript proxy where the resource needs to be merged
* The resource can dial out from VPC to reach to our application

There is no need to additionally configure the stack options so you can skip to reviewing the details of the stack.

![](<../../.gitbook/assets/Screenshot 2022-08-09 at 3.16.21 PM (1).png>)

And voilà, once the proxy is successfully deployed in the client environment, you should see the status <mark style="color:green;background-color:yellow;">`READY`</mark> for your proxy.

<figure><img src="../../.gitbook/assets/Screenshot 2022-09-01 at 7.51.13 PM.png" alt=""><figcaption></figcaption></figure>
