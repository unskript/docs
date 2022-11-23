---
description: >-
  Simple access controls give your team access with just the right permission
  level
---

# Role Based Access Control

Role-based access control (RBAC) is a method of regulating access to your workflows and connections based on the roles of individual users within your organization.

This enables granularity and security for the workflows which restricts user movement across the platform.

{% hint style="info" %}
RBAC controls are only available in the Sandbox and Cloud versions of unSkript.
{% endhint %}

Our RBAC solution is built by adding Users to Groups, and then adding access and permissions to the group.



### View Users

In the unSkript dashboard, click "More" -> "User Management" from the top navigation.  A apge will load listing all of the Users in your instance of unSkript, along with their e-mail address and the Groups they are a member of.

You can invite new users from this page with the "+Invite User" button.



### **User Groups**

Access to workflows and executions are provided through the use of User Groups.  From the "User Management" page, click the "User Groups" tab to list all of the user groups in your instance.



In order to give permissions to a user, or group of users, yo must first create a Group and give it a descriptive name:

![](<../../.gitbook/assets/Screenshot 2022-08-02 at 6.41.23 PM.png>)

Select to user/users to be added to this new User Group:

![](<../../.gitbook/assets/Screenshot 2022-08-02 at 6.41.39 PM.png>)

Click create Group, and your new group will be created. &#x20;



Next, we will add privileges to the group.  Click the "+ Add Privileges" button  under the Access Control tab inside the User Group.

![](<../../.gitbook/assets/Screenshot 2022-08-02 at 6.42.26 PM.png>)

Select the roles based on requirements from the available list of roles. There are 5 main roles that can be assigned to a Group  on the unSkript platform:

#### List of Roles:

1. Viewer: Can view all of the xRunBooks in a Folder, but cannot run them
2. Executor: Can view and also execute xRunBooks, but cannot edit them.
3. Editor : Can view, execute and also make changes to xRunBooks.
4. Approver: Approvers can view xRunBooks, but have the additional privilege to approve the execution of xRunBooks that require approval.
5. Requestor: Can request a xRunBook to be run.  Requestors also have Executor permissions (view and execute xRunBooks).



![](<../../.gitbook/assets/Screenshot 2022-08-02 at 6.44.51 PM.png>)

Add the Folders which this User Group can access based on their privileges. Any RunBook in these folders will be visible at the access level given.

![](<../../.gitbook/assets/Screenshot 2022-08-02 at 6.46.25 PM.png>)

You can view/edit all the users under the User tab.  You can view (and remove) the User Groups to which they belong.

![](<../../.gitbook/assets/Screenshot 2022-08-02 at 6.47.17 PM.png>)

To directly add a user to an existing User Group, click on the Invite User button under Users tab.

![](<../../.gitbook/assets/Screenshot 2022-08-02 at 6.48.57 PM.png>)
