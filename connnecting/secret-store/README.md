---
description: Keeping your credentials safe
---

# Secret store

Credentials for your connectors are stored a secret store. We support the following secret stores:

* AWS Secrets Manager
* [Vault](vault.md)
* Redis
* Google Cloud Secrets Manager

{% hint style="info" %}
Note that the secret store is not supported in the Docker versions of unSkript.  Your credentials are stored in the local file directory.
{% endhint %}
