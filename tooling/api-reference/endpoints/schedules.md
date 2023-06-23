---
description: Schedule your xRunBooks via our API
---

# Schedules

## List all Schedules

Example:

```shell
curl  'https://<your domain>/v1alpha1/schedules?pageSize=1&pageToken=1' \
      -H "X-unSkript-API-Key:>token>"
```

{% swagger src="../../../.gitbook/assets/schedule_api_updated.json" path="/v1alpha1/schedules" method="get" %}
[schedule_api_updated.json](../../../.gitbook/assets/schedule_api_updated.json)
{% endswagger %}

## Create a Schedule

This schedules "unSkript Rules" to run at 5 AM (GMT) every day:

```shell
curl  -X POST 'https://<api domain>/v1alpha1/schedules' \
      -H "X-unSkript-API-Key:<api token>" \
	  -d '{"schedule":{"proxyId":"1499f27c-640sdfds6-4fbd-bd1b-c6f92800018f", 
	       "runbookName":"unSkript rulez", 
	       "runbookId":"14fac589-5849-403b-afcf-ed80as79099500",  
	       "schedule":"* 5 * * *"}}'
```

{% swagger src="../../../.gitbook/assets/schedule_api_updated.json" path="/v1alpha1/schedules" method="post" %}
[schedule_api_updated.json](../../../.gitbook/assets/schedule_api_updated.json)
{% endswagger %}

## Get a Specific Schedule's details

```shell
curl  'https://<domain>/v1alpha1/schedules/97b8208a-7b05-4212-b1c3-2e0f0abe8060' \
      -H "X-unSkript-API-Key:<api key>"
	  

```

{% swagger src="../../../.gitbook/assets/schedule_api_updated.json" path="/v1alpha1/schedules/{scheduleId}" method="get" %}
[schedule_api_updated.json](../../../.gitbook/assets/schedule_api_updated.json)
{% endswagger %}

## Delete a schedule

```bash
curl  -X DELETE 'https://<domain>/v1alpha1/schedules/c67888f8-2df8-4248-9280-5c4b3589cf43' \
      -H "X-unSkript-API-Key:<api token>"
```

{% swagger src="../../../.gitbook/assets/schedule_api_updated.json" path="/v1alpha1/schedules/{scheduleId}" method="delete" %}
[schedule_api_updated.json](../../../.gitbook/assets/schedule_api_updated.json)
{% endswagger %}

## Update a Schedule

{% swagger src="../../../.gitbook/assets/schedule_api_updated.json" path="/v1alpha1/schedules/{scheduleId}" method="patch" %}
[schedule_api_updated.json](../../../.gitbook/assets/schedule_api_updated.json)
{% endswagger %}
