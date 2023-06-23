# RunBooks

## List RunBooks

{% swagger src="../../../.gitbook/assets/openapi2 (1).json" path="/v1alpha1/workflows" method="get" %}
[openapi2 (1).json](<../../../.gitbook/assets/openapi2 (1).json>)
{% endswagger %}

**Curl Example (to get personal runBooks: isUnskript=false)**

```bash
curl  'https://<domain>/v1alpha1/workflows?pageSize=100&isUnskript=false' \
      -H "X-unSkript-API-Key:<apikey>" 

```

**Curl Example (isUnskript=true):**

```bash
https://tenant-staging.alpha.unskript.io/v1alpha1/workflows?pageSize=100&isUnskript=true' \
-H "X-unSkript-API-Key:<apikey>"

```

## Get RunBook Details

{% swagger src="../../../.gitbook/assets/openapi2 (1).json" path="/v1alpha1/workflows/{workflowId}" method="get" %}
[openapi2 (1).json](<../../../.gitbook/assets/openapi2 (1).json>)
{% endswagger %}

**Curl Example:**

This example gets the details of an unSkript XRunBook.  To get a custom/personal xRUnBook, use the workflowId, and remove  the isUnskript parameter.

```bash
'https://<domain>/v1alpha1/workflows/79c167af0209e60fc45455bf4943b733904d4ab8654028d8434d193d1bf8c16c?isUnskript=true' \
      -H "X-unSkript-API-Key:<apy key>" 
```

## Run a RunBook

{% swagger src="../../../.gitbook/assets/openapi2 (1).json" path="/v1alpha1/workflows/{workflowId}/run" method="post" %}
[openapi2 (1).json](<../../../.gitbook/assets/openapi2 (1).json>)
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
