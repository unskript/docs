# Connectors

In order to interact with your cloud infrastructure, unSkript has to be able to connect to your cloud tooling. &#x20;

Connectors securely handle your Cloud credentials without exposing them in the code.  Using credentials allows unSkript's RunBooks to interact with your systems.  \


unSkript supports the following Connectors-

* Data services like [Redis](redis/), [MySQL](mysql/), [Snowflake](snowflake/), [MongoDB](mongodb/), [Kafka](apache-kafka/), [Postgresql](postgres/), [Hadoop](hadoop/), [MSSQL](ms-sql/), [Splunk](splunk/)
* Observability services like [Grafana](grafana/), [Datadog](datadog/), [Zabbix](zabbix.md), [Pingdom](pingdom/), [OpenSearch](opensearch/), [Elasticsearch](elasticsearch/), [Prometheus](prometheus/)
* CI/CD platforms such as [Jenkins](jenkins/), [Jira](jira/), [GitHub](github/), [Terraform](terraform/)
* Infrastructure services such as [AWS](aws/), [GCP](gcp/), [Kubernetes](kubernetes/), [Azure](azure/)
* Utilities like [Airflow](airflow/), [Slack](slack/), [Stripe](stripe/)
* Any API or application with a [REST API](rest/) or [SSH](ssh/) connectivity

The full list can be seen in the left navigation, and the links point to set up instructions to establish your connection.

### Credentials

Credential types vary depending on the Authentication pathways provided by the connector: API tokens, keys & secrets, JSON config files. etc.  Each Connector page has details on how to add your credentials for that platform.

There may be times where there are multiple credentials to one Connector (Some xRunBooks or Actions may require different permissions, and using the [principles of least privilege](https://unskript.com/blog/automate-the-creation-of-least-privileged-aws-security-profiles), it may be better to have different credentials.

### Credentials as a Variable

To reuse an xRunBook across multiple environments, the credential can be set as a serviceID.  This of a serviceID as a variable. In each unSkript environment, assign a credential to the serviceID.  When the xRunBook is run in an environment - the credential with that serviceID is used to run the Actions.

For example, if there are 2 environments: _dev_ and _production,_ each with different AWS credentials. If the credentials in dev and production have the same serviceID, each Action in a RunBook can use the serviceId variable for authentication. A new Runbook input parameter "environment" is added.  Specifying "Dev" will use the dev credentials, while using "production will use the production serviceID credentials.

Head to the section on [environments](../proxies/connect-your-environment/) to learn more.



