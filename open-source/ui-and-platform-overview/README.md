# UI and Platform Overview

unSkript offers an open source, low code, intelligent automation platform which is built on another open source platform- Jupyter Notebooks.

This section will explain the key components of our platform.

#### Add Action/ Note

<figure><img src="../../.gitbook/assets/456D64B6-BE1A-4E22-93F4-AC3CC3C88B3E.png" alt=""><figcaption></figcaption></figure>

This button enables the user to create their custom actions and custom notes.

* Custom Action

<figure><img src="../../.gitbook/assets/A87C94BE-5328-4BC6-9DF1-7580539AD725.png" alt=""><figcaption></figcaption></figure>

* Custom Note

<figure><img src="../../.gitbook/assets/9557A269-A38D-475C-AD4A-0CFD0E0BB77D.png" alt=""><figcaption></figcaption></figure>

#### Credentials

<figure><img src="../../.gitbook/assets/1CFA549C-361B-4EB8-9EC3-96F912033D65 (1) (1) (1) (1) (1) (1) (1) (1) (1) (1) (1) (1) (1) (1) (1) (1) (2) (1) (1).png" alt=""><figcaption></figcaption></figure>

This button can be used to add resources to your xRunBook. Credentials are used to authenticate the resource that you wish to connect to while running an action.

#### Parameters

<figure><img src="../../.gitbook/assets/40E0B776-C97F-4BFE-9CE6-6B8D17CDBF71.png" alt=""><figcaption></figcaption></figure>

This button allows us to pass parameters to the xRunbook if needed.

#### Actions

<figure><img src="../../.gitbook/assets/0D1F330B-8A89-483C-A3CA-60DE50463A45.png" alt=""><figcaption></figcaption></figure>

This section allows the user to search for a built-in action. Depending on your use case you can modify the sample runbook by dragging and dropping these actions.

#### Configurations

<figure><img src="../../.gitbook/assets/E5BC0F46-D206-4A68-A681-F87224BFDE00.png" alt=""><figcaption></figcaption></figure>

This button enables us to configure the action and select credentials.

#### Run Action

<figure><img src="../../.gitbook/assets/8003CF2D-7D01-40DA-BD8B-0AADA5A141CB.png" alt=""><figcaption></figcaption></figure>

This button is used to execute an action.

#### First Cell: unSkript Internal

<figure><img src="../../.gitbook/assets/C02C3270-C692-4DEE-A61C-9DF6C88667EA (1) (1) (1) (1) (1) (1) (1) (1) (1) (1) (1) (1) (1) (1) (1) (1) (1) (1) (1) (1).png" alt=""><figcaption></figcaption></figure>

This is the first action of every xRunbook. The unSkript Internal action initializes the kernel and prepares an environment based on which the next/ consecutive actions are run.

{% hint style="info" %}
unSkript Internal action needs to be executed prior to any other action in the runbook.
{% endhint %}
