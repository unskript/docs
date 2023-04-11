# Connectors

unSkript provides Connectors to various components like data sources, external systems, and API’s which can be used to simplify and speed up workflow deployment.

Actions in a workflow are specific to performing tasks depending on the Resource we use. Resources can be connected using Connectors.

unSkript supports the following Connectors-

* Data services like [Redis](redis.md), [MySQL](mysql.md), Snowflake, [MongoDB](mongodb.md), [Kafka](apache-kafka/), [Postgresql](postgres.md), [Hadoop](hadoop.md), [MSSQL](ms-sql.md), Splunk
* Observability services like [Grafana](grafana.md), [Datadog](datadog/), [Zabbix](zabbix.md), [Pingdom](pingdom.md), [OpenSearch](opensearch.md), [Elasticsearch](elasticsearch.md), [Prometheus](prometheus.md)
* CI/CD platforms such as [Jenkins](jenkins.md), [Jira](jira.md), [GitHub](github.md)
* Infrastructure services such as [AWS](aws.md), [GCP](gcp.md), [Kubernetes](kubernetes.md)
* Utilities like [Airflow](airflow.md), [Slack](slack.md), [Stripe](stripe.md)
* Any API or application with a [REST API](rest.md) or [SSH](ssh.md) connectivity

### Credentials

Each Connector will have credentials to authenticate with the Connector.  The type of credential will vary depending on the Authentication pathways provided by the connector: API tokens, keys & secrets, etc.  Each Connector page has details on how to add your credentials.

There may be times where there are multiple credentials to one Connector (Some xRunBooks or Actions may require different permissions, and using the principles of least privilege, it may be better to have different credentials.

### Credentials as a Variable

To reuse an xRunBook across multiple environments, the credential can be set as a serviceID.  When the xRunBook is run in an envirnment - the credential with that serviceID is used to run the Actions.

For example, if there are 2 environments _dev_ and _production -_ each with different AWS credentials (but the credentials use the same serviceID), a xRunBook can be run in either environment with zero modifications.





