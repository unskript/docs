---
description: Run your Terraform Script in an xRunBook
---

# Terraform

The Action **Execute Terraform Command** allows you to run your Terraform scripts inside an unSkript xRunBook.

### Add & Configure the Action

Add the Action to your xRunBook by searching for **Execute Terraform Command**  and dragging the Action into your xRunBook.

Click the Configuration button to set up your Action. There are four parameters you must add:

1. **Credential**: Add the Cloud credential (AWS, GCP) that has access to perform the Terraform action in your Cloud.
2. **Git repository**: Enter the `.git` url for your Terraform script repository, e.g. [https://github.com/unskript/Awesome-CloudOps-Automation.git](https://github.com/unskript/Awesome-CloudOps-Automation.git). This field is **required**.
3. **Directory Path**: The path in your Git repo where your script resides.  This field is **optional**.
4. **Terraform Command**: Enter the command to be executed. This field is **required**.

