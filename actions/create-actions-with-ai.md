---
description: Use ChatGPT's generative AI to quickly build Actions
---

# Create Actions with AI

If you require an acton that is not yet included in unSkript, you can create your own.  The quickest way to go from Zero to Action is to use ChatGPT's generative AI to create an Action.



## Adding your ChatGPT API Key

In order to interact with ChatGPT's API, you will need an [API key](https://platform.openai.com/account/api-keys) from OpenAI.

Adding your API key:

{% tabs %}
{% tab title="Docker" %}
Your API Key and your organization are entered as parameters when starting your Docker image:\


```
docker run -it -p 8888:8888 \
 -v $HOME/Awesome-CloudOps-Automation/custom:/data \
 -v $HOME/.unskript:/unskript \
 -e ACA_AWESOME_MODE=1 \
 -e OPENAI_ORGANIZATION_ID=<your openAI org> \
 -e OPENAI_API_KEY=<your API key> \
 --user root \
 docker.io/unskript/awesome-runbooks:1221

```

If you do not include the OPENAI\_ORGANIZATION\_ID or OPENAI\_API\_KEY, unSkript will run with all the features and tools, except the ChatGPT GenAI tool.
{% endtab %}

{% tab title="SAAS/Online" %}
In the online version of unSkript, choose More->Settings from the top navigation.&#x20;

Under Integrations, add your organization and API key.
{% endtab %}
{% endtabs %}



## Creating an Action with ChatGPT

In an open RunBook, Click the **+ Add GenAI Action**.  This will add a new Action in your RunBook.

<figure><img src="../.gitbook/assets/image (22).png" alt=""><figcaption><p>A new GenAI Action</p></figcaption></figure>

In addition to the Configurations and Run Action buttons, there is a new Chat GenAI button.  When this button is clicked, a new interface opens in thr right column of the dashboard:

![](<../.gitbook/assets/image (5).png>)

At the top of this Navigation are two selections:&#x20;

* Action Type: This specifies the Connector to be used in your Action
* HealthCheck Action: When checked, the Action will be built as a HealthCheck Action.  The output will be a Tuple, first value is Boolean (pass/fail) and the 2nd value is the result.

At the bottom of the Navigation is the chat box where we described the Action that is being built.



### Creating an Action

* Type a complete sentence or two of what you would like your Action to do. &#x20;
* Describe any input parameters, whether or not they are required or not, and their initial values.

> Example: for an AWS Action, you could say _"list all the S3 buckets that are in region, where region is a required parameter."_  Chat GPT will take this input and generate the Python code to complete this action.  When the code has been created, open the Configurations tab, and add an AWS credential and a region. Upon execution, the Action will return a list of Buckets in the region:

<figure><img src="../.gitbook/assets/image (4).png" alt=""><figcaption><p>Results from </p></figcaption></figure>



### Modifying your Action&#x20;

The code generated may do exactly what you need.  However, you may wish to add another input parameter, or slightly change the output of the Action.  For example, we could make two modifications to the Action above with the following prompt:

> "Return each bucket as a dict with the bucket name and the created date. Add a filter input that returns buckets with that string in the name."

This returns an Action with 2 inputs - Region and Filter.  On running this Action we can get all Buckets with 'unskript' in the name:\


<figure><img src="../.gitbook/assets/image (36).png" alt=""><figcaption></figcaption></figure>

## Testing your Action



## ChatGPT Tips
