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

<figure><img src="../.gitbook/assets/image (4).png" alt=""><figcaption><p>A new GenAI Action</p></figcaption></figure>

In addition to the Configurations and Run Action buttons, there is a new Chat GenAI button.  When this button is clicked, a new interface opens in thr right column of the dashboard:

![](<../.gitbook/assets/image (2).png>)

At the top of this Navigation are two selections:&#x20;

* Action Type: This specifies the Connector to be used in your Action
* HealthCheck Action: When checked, the Action will be built as a HealthCheck Action.  The output will be a Tuple, first value is Boolean (pass/fail) and the 2nd value is the result.

At the bottom of the Navigation is the chat box where we described the Action that is being built.



## Testing your Action



## ChatGPT Tips
