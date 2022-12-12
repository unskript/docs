# Executions

{% swagger src="../../.gitbook/assets/openapi2 (1).json" path="/v1alpha1/executions" method="get" %}
[openapi2 (1).json](<../../.gitbook/assets/openapi2 (1).json>)
{% endswagger %}

**Curl Example:**

`curl 'https://<domain>/v1alpha1/executions?pageSize=10'`\
`-H "X-unSkript-API-Key:<api token>"`

**`Response:`**

```bash
{
	"respHdr": {
		"tid": "b1c82f26-42be-46cf-a606-d9a216f95d4a",
		"requestTid": ""
	},
	"execution": [
		{
			"id": "10007ea-1b3ced62604e",
			"workflowName": "doug-stop mariah",
			"createTime": null,
			"startTime": "2022-12-12T00:47:54Z",
			"endTime": "2022-12-12T00:48:20Z",
			"duration": "25.862638738s",
			"version": "",
			"executionStatus": "EXECUTION_STATUS_SUCCEEDED",
			"inputs": "{}",
			"output": "",
			"executor": "Doug_api_testing",
			"approver": "",
			"reason": "",
			"executionType": "EXECUTION_TYPE_RUNBOOK"
		}
		]
		}
```

{% swagger src="../../.gitbook/assets/openapi2 (1).json" path="/v1alpha1/executions/{executionId}" method="get" %}
[openapi2 (1).json](<../../.gitbook/assets/openapi2 (1).json>)
{% endswagger %}

**Curl Example:**

```bash
curl  'https://<domain>/v1alpha1/executions/10007011-12a6-41c1-98ea-1b3ced62604e' \
      -H "X-unSkript-API-Key:<api token>"
      
```

**Response**:

```json
{
	"respHdr": {
		"tid": "776368bb-bbae-44cf-8dc2-7fc21800e2da",
		"requestTid": ""
	},
	"execution": {
		"id": "100070111c1-98ea-1b3ced62604e",
		"workflowName": "doug-stop mariah",
		"createTime": null,
		"startTime": "2022-12-12T00:47:54Z",
		"endTime": "2022-12-12T00:48:20Z",
		"duration": "25.862638738s",
		"version": "",
		"executionStatus": "EXECUTION_STATUS_SUCCEEDED",
		"inputs": "{}",
		"output": "<BASE64 RESPONSE>",
		"executor": "Doug_api_testing",
		"approver": "",
		"reason": "",
		"executionType": "EXECUTION_TYPE_RUNBOOK"
	}
}
```
