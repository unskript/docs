---
description: >-
  Sometimes a RunBook has advanced privileges, and should have a 2nd pari of
  eyes check each execution.
---

# Running RunBooks with Approvals

When a RunBook with advanced privileges needs to be run, it makes sense to have another pair of eyes double check the execution. &#x20;



Using [Role Based Access Control](../../../tooling/role-based-access-control/), this is possible.  In our example, we'll be looking at a RunBook that Drops all tables:

<figure><img src="../../../.gitbook/assets/Screenshot 2023-05-17 at 13.10.43.jpg" alt="The Drop all Tables Runbook"><figcaption><p>Drop all Tables Runbook</p></figcaption></figure>



Step 1: Move your RunBook to a new folder.  In this case, the Runbook is in the NuclearOptions folder:

<figure><img src="../../../.gitbook/assets/Screenshot 2023-05-17 at 13.12.34.jpg" alt=""><figcaption></figcaption></figure>

Step 2: open the RunBook details (in the right menu), and choose the  "requires approval" checkbox.

<figure><img src="../../../.gitbook/assets/Screenshot 2023-05-17 at 13.13.51.jpg" alt=""><figcaption><p>Click this checkbox to require approvals</p></figcaption></figure>

Step 3: Return to the list of Runbooks, and the "Run" button has changed to "Request":

<figure><img src="../../../.gitbook/assets/Screenshot 2023-05-17 at 13.16.53.jpg" alt=""><figcaption></figcaption></figure>

When you click this button, you will enter the input values, and your Runbook will be placed in the approver queue.

### Approving a RunBook

Under "Requests" in the top navigation, there is a page listing all RunBook requests:

![](<../../../.gitbook/assets/image (8).png>)

An [authorized approver](../../../tooling/role-based-access-control/rbac-roles.md) must approve (or reject) the RunBook execution.  Using the User Management, add users to a group with "Approver" permissions for the directory with the RunBook.  Those users will be able to approve the execution





