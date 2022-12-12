# Workflows

{% swagger src="../../.gitbook/assets/openapi2 (1).json" path="/v1alpha1/workflows" method="get" %}
[openapi2 (1).json](<../../.gitbook/assets/openapi2 (1).json>)
{% endswagger %}

**Curl Example (to get personal runBooks (isUnskript=false)**

```bash
curl  'https://<domain>/v1alpha1/workflows?pageSize=100&isUnskript=false' \
      -H "X-unSkript-API-Key:<apikey>" 

```

**Response:**

```json
{
	"respHdr": {
		"tid": "8f29c85f-7aad-489b-a728f727149829",
		"requestTid": ""
	},
	"workflows": [
		
		{
			"name": "gcp",
			"id": "f8ead207-81c0-414ab-76fcdefafe8d",
			"description": "",
			"tags": [

			],
			"currentVersion": "0.0.1",
			"createTime": "2022-10-11T00:19:52Z",
			"lastRun": "2022-10-12T14:09:07Z",
			"lastUpdated": "2022-10-11T20:56:10Z",
			"proxyId": "1499f27c-6406-4fbd-bd1b92800018f",
			"inputSchema": "",
			"requiresApproval": false,
			"runningDisabled": false,
			"parentId": "",
			"isFolder": false,
			"path": "/gcp/",
			"enableEnvironment": false,
			"executionDisabled": false,
			"connectorTypes": [

			],
			"categories": [

			],
			"icon": "",
			"environmentStatus": [
				{
					"environmentName": "Dev",
					"status": "Ready",
					"reason": [

					]
				},
				{
					"environmentName": "new",
					"status": "Ready",
					"reason": [

					]
				},
				{
					"environmentName": "Staging",
					"status": "Ready",
					"reason": [

					]
				}
			],
			"runningDisabledByFloatingEnv": false
		}
		<snip>
	],
	"nextPageToken": "1",
	"pageCount": 2,
	"totalCount": 173,
	"categoryCounts": [

	]
}
```

**Curl Example (isUnskript=true):**

```bash
https://tenant-staging.alpha.unskript.io/v1alpha1/workflows?pageSize=100&isUnskript=true' \
-H "X-unSkript-API-Key:<apikey>"

```

**Response:**

```json
{
	"respHdr": {
		"tid": "5b5453e3-ff22-42ca-ab56-ef3d147421fe",
		"requestTid": ""
	},
	"workflows": [
		{
			"name": "AWS Access Key Rotation for IAM users",
			"id": "a79201f821993867e23dd9603ed7ef5123325353d717c566f902f7ca6e471f5c",
			"description": "This runbook can be used to configure AWS Access Key rotation. Changing access keys (which consist of an access key ID and a secret access key) on a regular schedule is a well-known security best practice because it shortens the period an access key is active and therefore reduces the business impact if they are compromised. Having an established process that is run regularly also ensures the operational steps around key rotation are verified, so changing a key is never a scary step.",
			"tags": [

			],
			"currentVersion": "1.0.0",
			"createTime": "1970-01-01T00:00:00Z",
			"lastRun": "1970-01-01T00:00:00Z",
			"lastUpdated": "1970-01-01T00:00:00Z",
			"proxyId": "6818e908-e7a5-44a8-8cb5-5ea4a13de00b",
			"inputSchema": "",
			"requiresApproval": false,
			"runningDisabled": false,
			"parentId": "",
			"isFolder": false,
			"path": "",
			"enableEnvironment": false,
			"executionDisabled": false,
			"connectorTypes": [
				"CONNECTOR_TYPE_AWS"
			],
			"categories": [
				"CATEGORY_TYPE_IAM",
				"CATEGORY_TYPE_SECOPS"
			],
			"icon": "CONNECTOR_TYPE_AWS",
			"environmentStatus": [

			],
			"runningDisabledByFloatingEnv": false
		},
	<snip>
	],
	"nextPageToken": "1",
	"pageCount": 1,
	"totalCount": 42,
	"categoryCounts": [
		{
			"name": "CATEGORY_TYPE_SECOPS",
			"count": "8/8"
		},
		{
			"name": "CATEGORY_TYPE_CLOUDOPS",
			"count": "38/38"
		},
		{
			"name": "CATEGORY_TYPE_DEVOPS",
			"count": "30/30"
		},
		{
			"name": "CATEGORY_TYPE_SRE",
			"count": "29/29"
		},
		{
			"name": "CATEGORY_TYPE_COST_OPT",
			"count": "3/3"
		},
		{
			"name": "CATEGORY_TYPE_TROUBLESHOOTNG",
			"count": "6/6"
		},
		{
			"name": "CATEGORY_TYPE_IAM",
			"count": "3/3"
		}
	]
}
```

{% swagger src="../../.gitbook/assets/swagger.workflows" path="/v1alpha1/workflows/{workflowId}" method="get" %}
[swagger.workflows](../../.gitbook/assets/swagger.workflows)
{% endswagger %}

**Curl Example:**

This example gets the details of an unSkript XRunBook.  To get a custom/personal xRUnBook, use the workflowId, and remove  the isUnskript parameter.

```bash
'https://<domain>/v1alpha1/workflows/79c167af0209e60fc45455bf4943b733904d4ab8654028d8434d193d1bf8c16c?isUnskript=true' \
      -H "X-unSkript-API-Key:<apy key>" 
```

{% swagger src="../../.gitbook/assets/openapi2 (1).json" path="/v1alpha1/workflows/{workflowId}/run" method="post" %}
[openapi2 (1).json](<../../.gitbook/assets/openapi2 (1).json>)
{% endswagger %}

**Curl Example:**

This xRunBook requires no parameters.

```bash
curl  -X POST 'https://<domain>/v1alpha1/workflows/14fac589-5849-403b-afcf-ed8079099500/run' \
	-H "X-unSkript-API-Key:<apitoken>" \
-d '{"proxyId":"<proxyid>"}'
```

This xRunBook has input Parameters:

```json
curl -X POST '<domain>/v1alpha1/workflows/c5030e77-7b0a-6c4ca/run'
-H "<apitoken>"
-d '{"proxyId":"<proxyid)", "inputs":"{"tag_key":"Service","tag_value":"MongoDB", "user_name":"test123"}"}'
```
