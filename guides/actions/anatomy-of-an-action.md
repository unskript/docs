# Anatomy of an Action

When You create (and save) a new Action in unSkript, a directory will be created with a number of files. In this document, we describe  each file, and how they work.

Each Action is in a directory.  The directory is a descriptive name of the Action, with "\_" replacing spaces.  Inside this directory are the files that make up the Action:

1. [init.py](anatomy-of-an-action.md#undefined)
2. [README.md](anatomy-of-an-action.md#readme.md)
3. [JSON file](anatomy-of-an-action.md#json-file)
4. [py file](anatomy-of-an-action.md#py-file)

### init.py

This is an empty file that is required to distinguish the module/sub-module. &#x20;

### README.md

The README.md explains what the Action is supposed to do.  When you create a new action - a skeleton README is created, but you will need to fill in a few details to create a full README.



It should contain:

1.  **Action Title**

    ```
      Example:
        <h2>Delete AWS EBS Volume </h2>
    ```
2.  **Description**: explains what the Action is intended to do.

    ```
    This Action deletes AWS EBS volume and gives a list of deletion status.
    ```
3.  **Action Details**: here we explain the Action signature, what are the different input fields to the Action. It's also nice to add an example of how the Action might be used:

    ```
    aws_delete_volumes(handle: object, volume_id: str, region: str)

    handle: Object of type unSkript AWS Connector
    volume_id: Volume ID needed to delete particular volume
    region: Used to filter the volume for specific region
    ```

    Example Usage:

    ```
      aws_delete_volumes(handle,
                      "vol-039ce61146a4d7901",
                      "us-west-2")
    ```
4. **Action Input**: explains how many parameters are needed for the Lego. Which of them are Mandatory, which of them are optional.

```
This Lego take three inputs handle, volume_id and region. All three are required.
```

1. **Lego Output** A sample output from the Lego/Action upon completion. Ensure to remove sensitive values.

### JSON File



The JSON file lists Example:

```
{
    "action_title": "Delete AWS EBS Volume by Volume ID",
    "action_description": "Delete AWS Volume by Volume ID",
    "action_type": "LEGO_TYPE_AWS",
    "action_entry_function": "aws_delete_volumes",
    "action_needs_credential": true,
    "action_output_type": "ACTION_OUTPUT_TYPE_LIST",
    "action_supports_poll": true,
    "action_supports_iteration": true,
    "action_categories": [  "CATEGORY_TYPE_DEVOPS", "CATEGORY_TYPE_SRE","CATEGORY_TYPE_AWS","CATEGORY_TYPE_AWS_EBS"]
  }
  
```

All of these fields are Mandatory.

* **Action Title**: The human readable title of your Action
* **Action Description**: a text description of what the Action does
* **Action Type**: Format is "LEGO\_TYPE\_\[CONNECTOR\_TYPE]" where CONNECTOR\_TYPE is AWS, GCP, Slack, etc.
* **Action Entry Function**: This is a Python function name that executes the Action Step by Step
* **Action Needs Credential**: Boolean - are the credentials for this connector required?
* **Action Output Type**: one of:&#x20;
  * ACTION\_OUTPUT\_TYPE\_STR
  * ACTION\_OUTPUT\_TYPE\_INT
  * ACTION\_OUTPUT\_TYPE\_BOOL
  * ACTION\_OUTPUT\_TYPE\_LIST
  * ACTION\_OUTPUT\_TYPE\_DICT
  * ACTION\_OUTPUT\_TYPE\_BYTES
  * ACTION\_OUTPUT\_TYPE\_NONE
* **Action Supports Poll**: Can this Action be polled?
* **Action Supports Iteration:** Can the Action be used to iterate over a list of values?
* **Action Categories:** List of categories that fit the Action - used for discoverability.

### py file

This is the Python file that runs the Action in the xRunBook.&#x20;

The python code has several Classes and Functions that are required to run in unSkript:

#### InputSchema

```python
class InputSchema(BaseModel):
```

The InputSchema lists all of the input parameters for the Action.

#### Printer

```python
def aws_service_quota_limits_vpc_printer(output):
```

The Printer Function defines what is printed into the Jupyter Notebook as output of the Action

#### Function

```python
def aws_service_quota_limits_vpc(handle, region: str, warning_percentage: float) -> List:
```

The function is what "does the work" for the action.  The example above has the following inputs:

* handle: The Credentials used to make calls to the Connector. handle does the authentication for you.
* region - a String input parameter
* warning\_percentage: a float input parameter.

The output of this function will be a List.
