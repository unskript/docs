---
description: How to Submit xRunBooks and Actions to Github
---

# Contribute to Open Source

## xRunBooks

If you have created a xRunBook in the SAAS/Sandbox, select the xRunBook's 3 dot menu and choose "Download."

<figure><img src="../.gitbook/assets/Screenshot 2022-12-14 at 20.53.19.jpg" alt=""><figcaption><p>the xRUnbook list</p></figcaption></figure>

The Three dot menu:

<figure><img src="../.gitbook/assets/Screenshot 2022-12-14 at 20.54.17.jpg" alt="menu screenshot"><figcaption></figcaption></figure>

In the repository, there is a sanitize.py script that will remove all of your parameters, credentials and outputs.  Run this script against your RunBook:\


```
python3 sanitize.py -f <ipynb file> 
```

#### RunBook JSON file

You'll need to create a \<RunBook name>.json file.  This JSON has several attributes:

* **Name**: the name of your xRunBook
* **Description:** a detailed description of your runbook.
* **uuid**: A unique Id.  Generate this using the description value, and running:

```bash
echo "DESCRIPTION OF THE RUNBOOK" | shasum -a 256

```

* **icon**: The connector type
* **categories**: the categories of the xRunBook.
* **connector\_types**: The connector type
* **version**: The version

Save this JSON file. With these 2 files, create a branch of the repo, and submit a PR.

## Actions

To submit a custom Action, first create a working version in unSkript.  To create an Action that can be submitted to Open Source:

1. Copy an existing "lego" in the[ Awesome-CloudOps-Automation](https://github.com/unskript/Awesome-CloudOps-Automation).
2. Rename the folder, and the .py and .json files with teh same name - that describes your action (for example: "aws\_get\_ec2\_instance\_age")
3.  Next we'll edit the files.  Copy the Python code of your Action into the .py file. &#x20;

    1. Add a Class called InputSchema that describes the inputs for your action:

    ```python
    class InputSchema(BaseModel):
        region: str = Field(
            title='Region',
            description='AWS Region of the ECS service')
    ```
4. Now Edit the JSON file (this is created for you when you save from Docker):
   1. Name: the Name of your Action,
   2. Description: the Description
   3. Type: what connector will it use (ex: "LEGO\_TYPE\_AWS")
   4. Entry Function: The name of the function called to run the Action.
   5. Needs Credential: Boolean
   6. Output\_Type: Dict, Array, String
   7. Supports polling: Boolean
   8. Supports Iteration: Boolean
5. Write a readme file (a template is created on save from Docker).  Attach images (save in the same directory) if helpful.
6. Once these files are completed, create a fork of the repo, and submit a PR to the Master branch. The unSkript team will promptly review your Action and provide comments, or accept your submission.
