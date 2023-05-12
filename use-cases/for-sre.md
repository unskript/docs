---
description: Automate away your Toil with RunBooks
---

# SRE

**With unSkript:**

* All your RunBooks and Actions are in one place for easy collaboration, sharing, and updating.
* &#x20;With [Role Based Access Control](../guides/role-based-access-control/) -give teams run access only to resolve issues.
* For sensitive RunBooks - require an [approval](../guides/role-based-access-control/rbac-roles.md) before the RunBook can be processed.
* [Schedule](../guides/xrunbooks/schedules.md) RunBooks for regular tasks.
* Connect the same RunBook to multiple [environments](../fundamentals/unskript-framework/connect-your-environment.md) - dev, staging and production using ServiceIds.  No issues with version control in different environments.
* RunBooks can be completely automated, or run interactively in a step-by-step process.



### Selected RunBooks included in unSkript:

* [Copy AMI to all Given AWS Regions](https://github.com/unskript/Awesome-CloudOps-Automation/tree/master/AWS/Copy\_ami\_to\_all\_given\_AWS\_regions.ipynb): This runbook can be used to copy AMI from one region to multiple AWS regions using unSkript legos with AWS CLI commands.We can get all the available regions by using AWS CLI Commands.
* [Create new IAM user with a security Policy](https://github.com/unskript/Awesome-CloudOps-Automation/tree/master/AWS/Create\_IAM\_User\_with\_policy.ipynb). Sends confirmation to Slack.
* [Restart EC2 Instances](https://github.com/unskript/Awesome-CloudOps-Automation/tree/master/AWS/Restart\_AWS\_EC2\_Instances\_By\_Tag.ipynb): This runbook can be used to Restart AWS EC2 Instances
* [Visualize Jira Ticket Time to Resolution](https://github.com/unskript/Awesome-CloudOps-Automation/blob/master/Jira/jira\_visualize\_time\_to\_resolution.ipynb):  Using the Panel Library - visualize the time it takes for issues to close over a specifict timeframe
* [Rollback Kubernetes Deployment](https://github.com/unskript/Awesome-CloudOps-Automation/tree/master/Kubernetes/Rollback\_k8s\_Deployment\_and\_Update\_Jira.ipynb): This runbook can be used to rollback Kubernetes Deployment
* [Full List of SRE RunBooks](../guides/xrunbook\_list/runbook\_sre.md)
* [Create your own RunBook](../guides/xrunbooks/)
