---
description: Why would I automate RunBooks?
---

# What is a RunBook?

[Wikipedia](https://en.wikipedia.org/wiki/Runbook)'s RunBook definition states :&#x20;

> A runbook is a compilation of routine procedures and operations that the system administrator or operator carries out. System administrators in IT departments and NOCs use runbooks as a reference.

### Why have a RunBook?

* **When there is an issue:** it is nice to have a ordered checklist of the steps that must be taken to remediate the problem.  Having everything written out lowers the stress of the situation, and lowers the time to resolution.
* **Training**: When onboarding a new member to the team, they have built in documentation on how to create, rebuild and fix parts of the cloud infra.
* **Collaboration:** Learn from other RunBooks, re-use and repurpose the team's RunBooks for additional purposes. &#x20;
* **Reduced Escalation:** If your NOC or on-call engineer has the RunBook - they can resolve the issue without escalating to the team.

### Why Automate RunBooks?

* **Reduce errors:** Automation will precisely complete the task at hand, and will be fast than a human.
* **Lower Time To Resolution:** Computers are fast = so the issue will be resolved faster than manually completing the tasks.
* **Reduce manual tasks (toil)**: Many provisioning or creation tasks are done daily or weekly.  By automating these tasks, you can reserve that time for other work.

### How do RunBooks Work?

As described above, RunBooks are a type of checklist - a series of steps, that when performed in order, will complete a desired task.  Another term that is commonly used is a workflow.  And when building a RunBook, that is term that describes the process well. &#x20;

Here are the basic steps to build (or execute) a RunBook:

1. **Start with** [**Inputs**](../guides/xrunbooks/)**.** You have some known parameters to feed into the RunBook, so create input parameters for these values.  They can then be used during the steps of the workflow/RunBook to create your desired outcome.
2. **Build** [**Action**](../guides/actions/) **Steps:** Build on your input parameters.  Make queries into your infrastructure based on the inputs to gain more knowledge or information.  Take that gained information and build on it to reach your desired outcome.
   1. RunBooks can have as many steps as you need to complete the task.  With unSkript's drag & drop interface, you can easily search for Actions, drag them into the RunBook, and the configure the input/output variables.
   2. Need to skip a step? unSkript's Start Condition can skip a step if certain conditions are met.
3. **Output:** Your RunBook will output the variables you request as an output.  Additionally, add Actions to "send to slack" for additional notifications.

Once you've created your first automated RunBook, and experienced the relief in stress and toil - you'll be hooked.  Every task will be evaluated for automation - and while you can't do them all at once, you'll begin creating your automation list of RunBooks to remove work from the team's plate.

### Starting A RunBook

Once you've built the RunBook, you'll want to execute it.  There are a number of ways to run your workflow:

* **Interactively**: Open the RunBook in unSkript and run each step individually, examining each step as it is completed.
* **From the UI:** Rather than run interactively, just kick of the run with a click of a button.
* [**Scheduled**](../guides/xrunbooks/schedules.md)**:** Collect data. run healthchecks on a schedule. Just configure the schedule in the UI.
* [**API call**](../api-reference/)**:** Use your API token, and send the input parameters via a REST call.
* [**Alarm**](../guides/xrunbooks/alarms/)**:** If your infrastructure fires an alarm - have a RunBook execute automatically to remediate the situation.&#x20;

### Playbooks: A Collection of RunBooks

You can have a herd of elephants, or a flamboyance of flamingos.  A collection of RunBooks is called a playbook.  Once you have more than one RunBook in a since place - you have a playbook. &#x20;

**Playbook**: the "go-to" reference guide for SREs/ DevOps.  When there is a task to be performed, or an issue to be resolved, the team should reach for (probably virtually) the playbook, find the task to be performed, and walk through the steps.

unSkript can be your Playbook.  With all your RunBooks in unSkript, the UI can become your playbook. Simply search for the RunBook you wish to run, and you're ready to go!
