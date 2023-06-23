# Executions

## List all Executions

{% swagger src="../../../.gitbook/assets/openapi2 (1).json" path="/v1alpha1/executions" method="get" %}
[openapi2 (1).json](<../../../.gitbook/assets/openapi2 (1).json>)
{% endswagger %}

**Curl Example:**

`curl 'https://<domain>/v1alpha1/executions?pageSize=10'`\
`-H "X-unSkript-API-Key:<api token>"`

## Get Details of a Specific Execution

{% swagger src="../../../.gitbook/assets/openapi2 (1).json" path="/v1alpha1/executions/{executionId}" method="get" %}
[openapi2 (1).json](<../../../.gitbook/assets/openapi2 (1).json>)
{% endswagger %}

**Curl Example:**

```bash
curl  'https://<domain>/v1alpha1/executions/10007011-12a6-41c1-98ea-1b3ced62604e' \
      -H "X-unSkript-API-Key:<api token>"
      
```
