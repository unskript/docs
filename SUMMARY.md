# Table of contents

* [What is unSkript?](README.md)

## Guides

* [Getting started](guides/getting-started/README.md)
  * [Sign Up/Install](guides/getting-started/sign-up-install.md)
  * [Authentication](guides/getting-started/authentication/README.md)
    * [Okta configuration](guides/getting-started/authentication/okta-configuration/README.md)
      * [Okta Groups Sync](guides/getting-started/authentication/okta-configuration/okta-groups-sync.md)
  * [Create a Proxy](guides/getting-started/create-a-proxy.md)
  * [Add Credentials to Connect your Resources](guides/getting-started/add-credentials-to-connect-your-resources.md)
  * [Key Terms](guides/getting-started/key-terms.md)
* [xRunBooks](guides/xrunbooks/README.md)
  * [Prebuilt xRunBooks](lists/xRunBook\_list.md)
    * [xRunBooks for CloudOps](lists/runbook_CLOUDOPS.md)
    * [xRunBooks for Cost Optimization](lists/runbook_COST_OPT.md)
    * [xRunBooks for DevOps](lists/runbook_DEVOPS.md)
    * [xRunBooks for IAM](lists/runbook_IAM.md)
    * [xRunBooks for SecOps](lists/runbook_SECOPS.md)
    * [xRunBooks for SRE](lists/runbook_SRE.md)
    * [xRunBooks for Troubleshooting](lists/runbook_TROUBLESHOOTING.md)
  * [Importing unSkript xRunBooks](guides/xrunbooks/importing-unskript-xrunbooks.md)
  * [Create a xRunBook](guides/xrunbooks/create-a-xrunbook.md)
  * [Add an Action](guides/xrunbooks/add-an-action.md)
  * [Connecting Actions](guides/xrunbooks/connecting-actions.md)
  * [Create a Parameter](guides/xrunbooks/create-a-parameter.md)
  * [Create a Credential](guides/xrunbooks/create-a-credential.md)
  * [Writing Notes](guides/xrunbooks/writing-notes.md)
  * [Running XRunBooks](guides/xrunbooks/running-xrunbooks.md)
  * [xRunBook Executions](guides/xrunbooks/xrunbook-executions.md)
  * [Schedules](guides/xrunbooks/schedules.md)
  * [Alarms](guides/xrunbooks/alarms/README.md)
    * [Attaching runbooks to alarms](guides/xrunbooks/alarms/attaching-runbooks-to-alarms.md)
    * [Getting alerts via webhook for onprem](guides/xrunbooks/alarms/getting-alerts-via-webhook-for-onprem.md)
* [Actions](guides/actions/README.md)
  * [Create Custom Actions](guides/actions/create-custom-actions.md)
  * [All Pre-built Actions](lists/Action\_list.md)
  * [Action Configuration](guides/actions/action-configuration/README.md)
    * [Configure Action Inputs](guides/actions/action-configuration/configure-action-inputs.md)
    * [Add Action Inputs](guides/actions/action-configuration/action-inputs.md)
    * [Action Output](guides/actions/action-configuration/action-output.md)
    * [Action Iterator](guides/actions/action-configuration/action-iterator.md)
    * [Action Poll](guides/actions/action-configuration/action-poll.md)
    * [Action Start Condition](guides/actions/action-configuration/action-start-condition.md)
  * [Anatomy of an Action](guides/actions/anatomy-of-an-action.md)
* [Proxies](guides/proxies/README.md)
  * [Environment](fundamentals/unskript-framework/connect-your-environment.md)
    * [RunBooks Across Environments: ServiceIDs](guides/proxies/connect-your-environment/runbooks-across-environments-serviceids.md)
  * [unSkript Proxy](guides/proxies/unskript-proxy.md)
  * [AWS Proxy](guides/proxies/aws-proxy.md)
  * [GCP Proxy](guides/proxies/gcp-proxy.md)
* [Connectors](guides/connectors/README.md)
  * [Airflow](guides/connectors/airflow.md)
    * [Airflow Actions](lists/action\_AIRFLOW.md)
  * [AWS](guides/connectors/aws.md)
    * [AWS Actions](lists/action\_AWS.md)
      * [AWS Cloudwatch Actions](lists/action\_AWS\_CLOUDWATCH.md)
      * [AWS EC2 Actions](lists/action\_AWS\_EC2.md)
      * [AWS ECS Actions](lists/action\_AWS\_ECS.md)
      * [AWS EKS Actions](lists/action\_AWS\_EKS.md)
      * [AWS ELB Actions](lists/action\_AWS\_ELB.md)
      * [AWS IAM Actions](lists/action\_AWS\_IAM.md)
      * [AWS RDS Actions](lists/action\_AWS\_RDS.md)
      * [AWS RedShift Actions](lists/action\_AWS\_REDSHIFT.md)
      * [AWS S3 Actions](lists/action\_AWS\_S3.md)
      * [AWS VPC Actions](lists/action\_AWS\_VPC.md)
  * [Azure](guides/connectors/azure.md)
    * [Azure Actions](lists/action\_AZURE.md)
  * [Datadog](guides/connectors/datadog/README.md)
    * [Configuring webhook in Datadog](guides/connectors/datadog/configuring-webhook-in-datadog.md)
    * [Datadog Actions](lists/action\_DATADOG.md)
      * [Datadog Alert Actions](lists/action\_DATADOG\_ALERTS.md)
      * [Datadog Metrics Actions](lists/action\_DATADOG\_METRICS.md)
      * [Datadog Monitor Actions](lists/action\_DATADOG\_MONITOR.md)
  * [Elasticsearch](guides/connectors/elasticsearch.md)
    * [Elasticsearch Actions](lists/action\_ES.md)
  * [GCP](guides/connectors/gcp.md)
    * [GCP Actions](lists/action\_GCP.md)
      * [GCP Bucket Actions](lists/action\_GCP\_BUCKET.md)
      * [GCP GKE Actions](lists/action\_GCP\_GKE.md)
      * [GCP IAM Actions](lists/action\_GCP\_IAM.md)
      * [GCP VM Actions](lists/action\_GCP\_VM.md)
  * [Github](guides/connectors/github.md)
    * [Github Actions](lists/action\_GITHUB.md)
  * [Grafana](guides/connectors/grafana.md)
    * [Grafana Actions](lists/action\_GRAFANA.md)
  * [Hadoop](guides/connectors/hadoop.md)
    * [Hadoop Actions](lists/action\_HADOOP.md)
  * [Jenkins](guides/connectors/jenkins.md)
    * [Jenkins Actions](lists/action\_JENKINS.md)
  * [Jira](guides/connectors/jira.md)
    * [Jira Actions](lists/action\_JIRA.md)
  * [Kafka](guides/connectors/apache-kafka.md)
    * [Kafka Actions](lists/action\_KAFKA.md)
  * [Kubernetes](guides/connectors/kubernetes.md)
    * [K8s Actions](guides/connectors/kubernetes/k8s-actions.md)
  * [MongoDB](guides/connectors/mongodb.md)
    * [MongoDB Actions](lists/action\_MONGODB.md)
  * [MS SQL](guides/connectors/ms-sql.md)
    * [MSSQL Actions](lists/action\_MSSQL.md)
  * [MySQL](guides/connectors/mysql.md)
    * [MySQL Actions](lists/action\_MYSQL.md)
  * [Netbox](guides/connectors/netbox.md)
    * [Netbox Actions](lists/action\_NETBOX.md)
  * [Nomad](guides/connectors/nomad/README.md)
    * [Nomad Actions](lists/action\_NOMAD.md)
  * [OpenSearch](guides/connectors/opensearch.md)
    * [opensearch Actions](lists/action\_OPENSEARCH.md)
  * [Pingdom](guides/connectors/pingdom.md)
    * [Pingdom Actions](lists/action\_PINGDOM.md)
  * [Postgres](guides/connectors/postgres.md)
    * [Postgres Actions](lists/action\_POSTGRESSQL.md)
  * [Prometheus](guides/connectors/prometheus.md)
    * [Prometheus Actions](lists/action\_PROMETHEUS.md)
  * [Redis](guides/connectors/redis.md)
    * [Redis Actions](lists/action\_REDIS.md)
  * [REST](guides/connectors/rest.md)
    * [REST Actions](lists/action\_REST.md)
  * [SalesForce](guides/connectors/salesforce.md)
    * [SalesForce Actions](lists/action\_SALESFORCE.md)
  * [Slack](guides/connectors/slack.md)
    * [Slack Actions](lists/action\_SLACK.md)
  * [Snowflake](guides/connectors/snowflake.md)
    * [Snowflake Actions](lists/action\_SNOWFLAKE.md)
  * [Splunk](guides/connectors/splunk.md)
    * [Splunk Actions](lists/action\_SPLUNK.md)
  * [SSH](guides/connectors/ssh.md)
    * [SSH Actions](lists/action\_SSH.md)
  * [Stripe](guides/connectors/stripe.md)
    * [Stripe Actions](lists/action\_STRIPE.md)
  * [Terraform](guides/connectors/terraform.md)
    * [Terraform Actions](lists/action\_TERRAFORM.md)
  * [Zabbix](guides/connectors/zabbix.md)
* [Secret store](guides/secret-store/README.md)
  * [Vault](guides/secret-store/vault.md)
* [Notifications](guides/notifications.md)
* [Role Based Access Control](guides/role-based-access-control/README.md)
  * [RBAC Roles](guides/role-based-access-control/rbac-roles.md)
* [Command Line Tool](guides/command-line-tool.md)
* [Contribute to Open Source](guides/contribute-to-open-source.md)

## Fundamentals

* [unSkript Framework](fundamentals/unskript-framework/README.md)
  * [Using Iterators](fundamentals/unskript-framework/using-iterators.md)
  * [Using Poll](fundamentals/unskript-framework/using-poll.md)
  * [Using Start Conditions](fundamentals/unskript-framework/using-start-conditions.md)
  * [Saving output from Action](fundamentals/unskript-framework/saving-output-from-action.md)
  * [Using outputs from previous Actions](fundamentals/unskript-framework/using-outputs-from-previous-actions.md)
  * [Defining xRunBook Parameters](fundamentals/unskript-framework/defining-xrunbook-parameters.md)
  * [Credential Parameterization](fundamentals/unskript-framework/credential-parameterization.md)
  * [AWS hosted Proxy](fundamentals/unskript-framework/aws-hosted-proxy.md)
* [Folders](fundamentals/platform/folders.md)
* [Jupyter Notebook 101](fundamentals/jupyter-notebooks-101.md)

***

* [API reference](api-reference/README.md)
  * [Authentication](api-reference/authentication.md)
  * [Endpoints](api-reference/endpoints/README.md)
    * [Executions](api-reference/endpoints/executions.md)
    * [Workflows](api-reference/endpoints/workflows.md)
    * [Schedules](api-reference/endpoints/schedules.md)

## Use Cases

* [For DevOps](use-cases/for-devops/README.md)
  * [Chaos Engineering](use-cases/for-devops/chaos-engineering.md)
  * [Automate Cloud Operations](use-cases/for-devops/automate-cloud-operations.md)
* [For SRE](use-cases/for-sre/README.md)
  * [Chaos Engineering](use-cases/for-sre/chaos-engineering.md)
  * [Automate Troubleshooting](use-cases/for-sre/automate-troubleshooting.md)
* [For Customer Support](use-cases/for-customer-support/README.md)
  * [Automate Customer Onboarding](use-cases/for-customer-support/automate-customer-onboarding.md)

## Open source

* [CloudOps Automation with unSkript](open-source/cloudops-automation-with-unskript.md)
* [UI and Platform Overview](open-source/ui-and-platform-overview/README.md)
  * [Prerequisites](open-source/ui-and-platform-overview/prerequisites.md)
  * [Getting Started](open-source/ui-and-platform-overview/getting-started.md)

## Lists

*
*
*
* [Azure](lists/action\_AZURE.md)
* [ChatGPT](lists/chatgpt.md)
*
* [ElasticSearch](lists/elasticsearch.md)
*
*
*
*
*
*
*
* [Kubernetes](lists/kubernetes.md)
* [Mantishub](lists/mantishub.md)
* [Mongo](lists/mongo.md)
*
*
*
*
*
* [Postgresql](lists/action\_POSTGRESQL.md)
*
*
*
*
*
*
*
* [Splunk](lists/splunk.md)
*
*
* [Zabbix](lists/zabbix.md)
* [infra](lists/action\_INFRA.md)
* [opensearch](lists/opensearch.md)
* [SECOPS](lists/action\_SECOPS.md)
* [DEVOPS](lists/action\_DEVOPS.md)
* [SRE](lists/action\_SRE.md)
*
*
*
* [IAM](lists/action\_IAM.md)
*
* [COST\_OPT](lists/action\_COST\_OPT.md)
* [AWS\_ACM](lists/action\_AWS\_ACM.md)
*
*
*
* [AWS\_EBS](lists/action\_AWS\_EBS.md)
*
*
* [AWS\_EMR](lists/action\_AWS\_EMR.md)
* [AWS\_CLI](lists/action\_AWS\_CLI.md)
* [AWS\_SSM](lists/action\_AWS\_SSM.md)
* [DB](lists/action\_DB.md)
* [AWS\_EBC](lists/action\_AWS\_EBC.md)
*
* [CLOUDOPS](lists/action\_CLOUDOPS.md)
* [AWS\_ASG](lists/action\_AWS\_ASG.md)
* [AWS\_LOGS](lists/action\_AWS\_LOGS.md)
* [AWS\_NAT\_GATEWAY](lists/action\_AWS\_NAT\_GATEWAY.md)
* [AWS\_CLOUDTRAIL](lists/action\_AWS\_CLOUDTRAIL.md)
* [AWS\_DYNAMODB](lists/action\_AWS\_DYNAMODB.md)
* [AWS\_LAMBDA](lists/action\_AWS\_LAMBDA.md)
*
* [AWS\_SQS](lists/action\_AWS\_SQS.md)
* [TROUBLESHOOTING](lists/action\_TROUBLESHOOTING.md)
* [AWS\_SECRET\_MANAGER](lists/action\_AWS\_SECRET\_MANAGER.md)
* [AWS\_STS](lists/action\_AWS\_STS.md)
* [AWS\_POSTGRES](lists/action\_AWS\_POSTGRES.md)
*
*
*
* [DATADOG\_INCIDENT](lists/action\_DATADOG\_INCIDENT.md)
* [DATADOG\_EVENT](lists/action\_DATADOG\_EVENT.md)
*
*
*
*
*
*
*
* [GCP\_FILE\_STORE](lists/action\_GCP\_FILE\_STORE.md)
*
*
* [GCP\_VPC](lists/action\_GCP\_VPC.md)
* [GCP\_SECRET](lists/action\_GCP\_SECRET.md)
* [GCP\_SHEETS](lists/action\_GCP\_SHEETS.md)
*
* [GITHUB\_ISSUE](lists/action\_GITHUB\_ISSUE.md)
* [GITHUB\_PR](lists/action\_GITHUB\_PR.md)
* [GITHUB\_REPO](lists/action\_GITHUB\_REPO.md)
* [GITHUB\_TEAM](lists/action\_GITHUB\_TEAM.md)
* [GITHUB\_USER](lists/action\_GITHUB\_USER.md)
* [GITHUB\_ORG](lists/action\_GITHUB\_ORG.md)
*
*
*
*
*
* [K8S](lists/action\_K8S.md)
* [K8S\_CLUSTER](lists/action\_K8S\_CLUSTER.md)
* [K8S\_NODE](lists/action\_K8S\_NODE.md)
* [K8S\_POD](lists/action\_K8S\_POD.md)
* [K8S\_KUBECTL](lists/action\_K8S\_KUBECTL.md)
* [K8S\_PVC](lists/action\_K8S\_PVC.md)
* [K8S\_NAMESPACE](lists/action\_K8S\_NAMESPACE.md)
* [MONGODB](lists/action\_MONGODB.md)
* [MONGODB\_COLLECTION](lists/action\_MONGODB\_COLLECTION.md)
* [MONGODB\_CLUSTER](lists/action\_MONGODB\_CLUSTER.md)
* [MONGODB\_DOCUMENT](lists/action\_MONGODB\_DOCUMENT.md)
* [MONGODB\_QUERY](lists/action\_MONGODB\_QUERY.md)
*
* [MSSQL\_QUERY](lists/action\_MSSQL\_QUERY.md)
*
* [MYSQL\_QUERY](lists/action\_MYSQL\_QUERY.md)
*
*
*
*
* [POSTGRESQL\_QUERY](lists/action\_POSTGRESQL\_QUERY.md)
* [POSTGRESQL\_TABLE](lists/action\_POSTGRESQL\_TABLE.md)
*
*
*
*
*
*
*
*
* [STRIPE\_CHARGE](lists/action\_STRIPE\_CHARGE.md)
* [STRIPE\_DISPUTE](lists/action\_STRIPE\_DISPUTE.md)
* [STRIPE\_REFUND](lists/action\_STRIPE\_REFUND.md)
*
*
*
* [AWS Service Quota list](lists/test.md)
