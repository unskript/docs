# xRunBooks for SecOps

* AWS [AWS Access Key Rotation for IAM users](https://github.com/unskript/Awesome-CloudOps-Automation/tree/master/AWS/AWS\_Access\_Key\_Rotation.ipynb): This runbook can be used to configure AWS Access Key rotation. Changing access keys (which consist of an access key ID and a secret access key) on a regular schedule is a well-known security best practice because it shortens the period an access key is active and therefore reduces the business impact if they are compromised. Having an established process that is run regularly also ensures the operational steps around key rotation are verified, so changing a key is never a scary step.
* AWS [AWS Add Mandatory tags to EC2](https://github.com/unskript/Awesome-CloudOps-Automation/tree/master/AWS/AWS\_Add\_Mandatory\_tags\_to\_EC2.ipynb): This xRunBook is a set of example actions that could be used to establish mandatory tagging to EC2 instances. First testing instances for compliance, and creating reports of instances that are missing the required tags. There is also and action to add tags to an instance - to help bring them into tag compliance.
* AWS [Enforce HTTP Redirection across all AWS ALB instances](https://github.com/unskript/Awesome-CloudOps-Automation/tree/master/AWS/AWS\_Enforce\_HTTP\_Redirection\_across\_AWS\_ALB.ipynb): This runbook can be used to enforce HTTP redirection across all AWS ALBs. Web encryption protocols like SSL and TLS have been around for nearly three decades. By securing web data in transit, these security measures ensure that third parties can’t simply intercept unencrypted data and cause harm. HTTPS uses the underlying SSL/TLS technology and is the standard way to communicate web data in an encrypted and authenticated manner instead of using insecure HTTP protocol. In this runbook, we implement the industry best practice of redirecting all unencrypted HTTP data to the secure HTTPS protocol.
* AWS [Publicly Accessible Amazon RDS Instances](https://github.com/unskript/Awesome-CloudOps-Automation/tree/master/AWS/AWS\_Publicly\_Accessible\_Amazon\_RDS\_Instances.ipynb): This runbook can be used to find the publicly accessible RDS instances for the given AWS region.
* AWS [Remediate unencrypted S3 buckets](https://github.com/unskript/Awesome-CloudOps-Automation/tree/master/AWS/AWS\_Remediate\_unencrypted\_S3\_buckets.ipynb): This runbook can be used to filter all the S3 buckets which are unencrypted and apply encryption on unencrypted S3 buckets.
* AWS [Renew AWS SSL Certificates that are close to expiration](https://github.com/unskript/Awesome-CloudOps-Automation/tree/master/AWS/AWS\_Renew\_SSL\_Certificate.ipynb): This runbook can be used to list all AWS SSL (ACM) Certificates that need to be renewed within a given threshold number of days. Optionally it can renew the certificate using AWS ACM service.
* AWS [Restrict S3 Buckets with READ/WRITE Permissions to all Authenticated Users](https://github.com/unskript/Awesome-CloudOps-Automation/tree/master/AWS/AWS\_Restrict\_S3\_Buckets\_with\_READ\_WRITE\_Permissions.ipynb): This runbook will list all the S3 buckets.Filter buckets which has ACL public READ/WRITE permissions and Change the ACL Public READ/WRITE permissions to private in the given region.
* AWS [Secure Publicly accessible Amazon RDS Snapshot](https://github.com/unskript/Awesome-CloudOps-Automation/tree/master/AWS/AWS\_Secure\_Publicly\_accessible\_Amazon\_RDS\_Snapshot.ipynb): This lego can be used to list all the manual database snapshots in the given region. Get publicly accessible DB snapshots in RDS and Modify the publicly accessible DB snapshots in RDS to private.
* AWS [AWS Update RDS Instances from Old to New Generation](https://github.com/unskript/Awesome-CloudOps-Automation/tree/master/AWS/AWS\_Update\_RDS\_Instances\_from\_Old\_to\_New\_Generation.ipynb): This runbook can be used to find the old generation RDS instances for the given AWS region and modify then to the given instance class.
* AWS [Encrypt unencrypted S3 buckets](https://github.com/unskript/Awesome-CloudOps-Automation/tree/master/AWS/AWS\_encrypt\_unencrypted\_S3\_buckets.ipynb): This runbook can be used to filter all the S3 buckets which are unencrypted and apply encryption on unencrypted S3 buckets.
* AWS [Create a new AWS IAM User](https://github.com/unskript/Awesome-CloudOps-Automation/tree/master/AWS/Add\_new\_IAM\_user.ipynb): AWS has an inbuilt identity and access management system known as AWS IAM. IAM supports the concept of users, group, roles and privileges. IAM user is an identity that can be created and assigned some privileges. This runbook can be used to create an AWS IAM User
* AWS [Create an IAM user using Principle of Least Privilege](https://github.com/unskript/Awesome-CloudOps-Automation/tree/master/AWS/IAM\_security\_least\_privilege.ipynb): Extract usage details from Cloudtrail of an existing user. Apply the usage to a new IAM Policy, and connect it to a new IAM profile.