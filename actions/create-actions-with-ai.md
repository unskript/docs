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

## Testing your Action



## ChatGPT Tips
