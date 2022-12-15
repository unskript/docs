---
description: How to Submit xRunBooks and Actions to Github
---

# Contribute to Open Source

## xRunBooks

If you have created a xRunBook in the SAAS/Sandbox, select the xRunBook's 3 dot menu and choose "Download."

<figure><img src="../.gitbook/assets/Screenshot 2022-12-14 at 20.53.19.jpg" alt=""><figcaption><p>the xRUnbook list</p></figcaption></figure>

The Three dot menu:

<figure><img src="../.gitbook/assets/Screenshot 2022-12-14 at 20.54.17.jpg" alt="menu screenshot"><figcaption></figcaption></figure>

Now that your file is downloaded, copy it into the folder for the connector your xRunBook uses (for example GCP or AWS).

You'll need to create a \<runbook name>.json file.  This JSON has several attributes:

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

Coming soon!
