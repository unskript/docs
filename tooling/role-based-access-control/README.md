---
description: >-
  Simple access controls give your team access with just the right permission
  level
---

# Role Based Access Control

Role-based access control (RBAC) is a method of regulating access to your RunBooks and connections based on the roles of individual users within your organization.

This enables granularity and security for the workflows which restricts user movement across the platform.

{% hint style="info" %}
RBAC controls are only available in the Sandbox and Cloud versions of unSkript.
{% endhint %}

Our RBAC solution is built by adding Users to Groups, and then adding access and permissions to the group.  Groups have different access levels to directories in your unSkript RunBook collection.

### Users

In the unSkript dashboard, click "More" -> "User Management" from the top navigation.  A page will load listing all of the Users in your instance of unSkript, along with their e-mail address and the Groups they are a member of.

You can invite new users from this page with the "+Invite User" button.



### **User Groups**

Access to workflows and executions are provided through the use of User Groups.  From the "User Management" page, click the "User Groups" tab to list all of the user groups in your instance.



#### Create a Group

Click the **Add Group** button.  In Step 1, you name the Group.

![](<../../.gitbook/assets/Screenshot 2022-08-02 at 6.41.23 PM.png>)

In Step 2, you add users to the Group.  You can always add/remove users later in the Group settings.

![](<../../.gitbook/assets/Screenshot 2022-08-02 at 6.41.39 PM.png>)



#### Adding Access

Next, we will add [access roles](rbac-roles.md) to the group.  Access roles are based on the level of access for a directory of RunBooks.  If you wish to limit access to a subset of RunBooks, place them in a unique directory. We can then limit access to this directory to different groups of users.



1. Select the User Group you wish to grant credentials.
2. Click the **+ Add Privileges** button under the Access Control tab inside the User Group.

![](<../../.gitbook/assets/Screenshot 2022-08-02 at 6.42.26 PM.png>)

3. Select the roles based on requirements from the [available list of roles](rbac-roles.md).&#x20;



![](<../../.gitbook/assets/Screenshot 2022-08-02 at 6.44.51 PM.png>)

4. Add the Folders which this User Group can access based on their privileges. Any RunBook in these folders will be visible at the access level given.

![](<../../.gitbook/assets/Screenshot 2022-08-02 at 6.46.25 PM.png>)

5. You can view/edit all the users under the User tab.  You can view (and remove) the User Groups to which they belong.

![](<../../.gitbook/assets/Screenshot 2022-08-02 at 6.47.17 PM.png>)

6. To directly add a user to an existing User Group, click on the Invite User button under Users tab.

![](<../../.gitbook/assets/Screenshot 2022-08-02 at 6.48.57 PM.png>)
