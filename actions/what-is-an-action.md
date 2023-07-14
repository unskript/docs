---
description: Actions are reusable code segments that complete a specific task
---

# What is an Action?

Actions are the base unit of code used in unSkript.  Actions take [inputs](actions/action-configuration/action-inputs.md), complete a task, and [output](actions/action-configuration/action-output.md) a result.

unSkript comes with hundreds of [Prebuilt Actions](action-list.md) that are ready for immediate use.

### Types of Actions

* **Connector Actions**: Connector Actions interface with an external tool (for example [AWS](../connnecting/connectors/aws/action\_aws/) or [Datadog](../connnecting/connectors/datadog/action\_datadog/)), and performs an Action with that tooling.
  * Connector Actions are added by searching in the right navigation.
  * ![search for postgres actions](<../.gitbook/assets/image (23).png>)
* **Glue Actions:** Glue Actions are Python code used to manipulate and work with the data. Glue Actions are created from the "Add" button at the top of the RunBook. &#x20;
  * Simplify a data output to a different format.
  * Chart results
  * Build interactive selections
  * ![Adding a Glue Action](<../.gitbook/assets/image (19) (1).png>)
