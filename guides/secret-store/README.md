# Secret store

The credentials are stored in the customer's configured secret store. We support the following secret stores:

* AWS Secrets Manager
* [Vault](vault.md)
* Redis
* Google Cloud Secrets Manager

{% hint style="info" %}
Note that the secret store is not supported in OSS or the Sandbox versions of unSkript.  To use secret variables in the OSS, use your local filestore to host variables.
{% endhint %}
