# AWS IAM Actions

* [AWS Start IAM Policy Generation ](https://github.com/unskript/Awesome-CloudOps-Automation/tree/master/AWS/legos/AWS\_Start\_IAM\_Policy\_Generation/README.md): Given a region, a CloudTrail ARN (where the logs are being recorded), a reference IAM ARN (whose usage we will parse), and a Service role, this will begin the generation of a IAM policy. The output is a String of the generation Id.
* [AWS Attach New Policy to User](https://github.com/unskript/Awesome-CloudOps-Automation/tree/master/AWS/legos/aws\_attach\_iam\_policy/README.md): AWS Attach New Policy to User
* [AWS Create IAM Policy](https://github.com/unskript/Awesome-CloudOps-Automation/tree/master/AWS/legos/aws\_create\_IAMpolicy/README.md): Given an AWS policy (as a string), and the name for the policy, this will create an IAM policy.
* [AWS Create Access Key](https://github.com/unskript/Awesome-CloudOps-Automation/tree/master/AWS/legos/aws\_create\_access\_key/README.md): Create a new Access Key for the User
* [Create New IAM User](https://github.com/unskript/Awesome-CloudOps-Automation/tree/master/AWS/legos/aws\_create\_iam\_user/README.md): Create New IAM User
* [Create Login profile for IAM User](https://github.com/unskript/Awesome-CloudOps-Automation/tree/master/AWS/legos/aws\_create\_user\_login\_profile/README.md): Create Login profile for IAM User
* [AWS Delete Access Key](https://github.com/unskript/Awesome-CloudOps-Automation/tree/master/AWS/legos/aws\_delete\_access\_key/README.md): Delete an Access Key for a User
* [AWS Get Generated Policy](https://github.com/unskript/Awesome-CloudOps-Automation/tree/master/AWS/legos/aws\_get\_generated\_policy/README.md): Given a Region and the ID of a policy generation job, this Action will return the policy (once it has been completed).
* [AWS Get IAM Users with Old Access Keys](https://github.com/unskript/Awesome-CloudOps-Automation/tree/master/AWS/legos/aws\_get\_users\_with\_old\_access\_keys/README.md): This Lego collects the access keys that have never been used or the access keys that have been used but are older than the threshold.
* [AWS List Access Key](https://github.com/unskript/Awesome-CloudOps-Automation/tree/master/AWS/legos/aws\_list\_access\_keys/README.md): List all Access Keys for the User
* [AWS List All IAM Users](https://github.com/unskript/Awesome-CloudOps-Automation/tree/master/AWS/legos/aws\_list\_all\_iam\_users/README.md): List all AWS IAM Users
* [AWS List Attached User Policies](https://github.com/unskript/Awesome-CloudOps-Automation/tree/master/AWS/legos/aws\_list\_attached\_user\_policies/README.md): AWS List Attached User Policies
* [AWS List Expiring Access Keys](https://github.com/unskript/Awesome-CloudOps-Automation/tree/master/AWS/legos/aws\_list\_expiring\_access\_keys/README.md): List Expiring IAM User Access Keys
* [AWS List IAM Users With Old Passwords](https://github.com/unskript/Awesome-CloudOps-Automation/tree/master/AWS/legos/aws\_list\_users\_with\_old\_passwords/README.md): This Lego filter gets all the IAM users' login profiles, and if the login profile is available, checks for the last password change if the password is greater than the given threshold, and lists those users.
* [AWS Update Access Key](https://github.com/unskript/Awesome-CloudOps-Automation/tree/master/AWS/legos/aws\_update\_access\_key/README.md): Update status of the Access Key
