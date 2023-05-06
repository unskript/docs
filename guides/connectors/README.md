# Connectors

In order to interact with your cloud infrastructure, unSkript provides Connectors that securely handle your credentials, and allow RunBooks to interact with your systems.  \


unSkript supports the following Connectors-

* Data services like [Redis](redis.md), [MySQL](mysql.md), [Snowflake](snowflake.md), [MongoDB](mongodb.md), [Kafka](apache-kafka.md), [Postgresql](postgres.md), [Hadoop](hadoop.md), [MSSQL](ms-sql.md), [Splunk](splunk.md)
* Observability services like [Grafana](grafana.md), [Datadog](datadog/), [Zabbix](zabbix.md), [Pingdom](pingdom.md), [OpenSearch](opensearch.md), [Elasticsearch](elasticsearch.md), [Prometheus](prometheus.md)
* CI/CD platforms such as [Jenkins](jenkins.md), [Jira](jira.md), [GitHub](github.md), [Terraform](terraform.md)
* Infrastructure services such as [AWS](aws.md), [GCP](gcp.md), [Kubernetes](kubernetes.md), [Azure](azure.md)
* Utilities like [Airflow](airflow.md), [Slack](slack.md), [Stripe](stripe.md)
* Any API or application with a [REST API](rest.md) or [SSH](ssh.md) connectivity

The full list can be seen in the left navigation, and the links point to set up instructions to establish your connection.

### Credentials

Each Connector will have at least one set of credentials for authentication.  You may have multiple credentials in order to satisfy the Principle of Lease Privilege.  The type of credential will vary depending on the Authentication pathways provided by the connector: API tokens, keys & secrets, JSON config files. etc.  Each Connector page has details on how to add your credentials for that platform.

There may be times where there are multiple credentials to one Connector (Some xRunBooks or Actions may require different permissions, and using the [principles of least privilege](https://unskript.com/automate-the-creation-of-least-privileged-aws-security-profiles/), it may be better to have different credentials.

### Credentials as a Variable

To reuse an xRunBook across multiple environments, the credential can be set as a serviceID.  When the xRunBook is run in an environment - the credential with that serviceID is used to run the Actions.

For example, if there are 2 environments: _dev_ and _production,_ each with different AWS credentials (but the credentials use the same serviceID), a xRunBook can be run in either environment with zero modifications. Head to the section on [environments](../../fundamentals/unskript-framework/connect-your-environment.md) to learn more.



