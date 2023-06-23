# Vault

For Vault, we use the [`kv engine`](https://developer.hashicorp.com/vault/docs/secrets/kv/kv-v2)  (version 2) for storing the credentials.  When creating your proxy, add the Vault information in order to connect your Secret storage to unSkript.

{% hint style="info" %}
Vault connectivity is only available in the full SAAS implementation, and not in the free Sandbox. Contact us for a demo.
{% endhint %}

<figure><img src="../../.gitbook/assets/Screen Shot 2022-10-19 at 10.32.02 AM.png" alt=""><figcaption></figcaption></figure>

| Name                | Description                                                                                                                  |
| ------------------- | ---------------------------------------------------------------------------------------------------------------------------- |
| Host                | Hostname of the vault server, along with the port number. For eg: _https://vault.example.com:8200_                           |
| Token               | Service Token to authenticate to Vault. This token should have CRUD access to the KV store.                                  |
| Mount Dir Name      | Path where the KV backend is mounted.                                                                                        |
| Vault Secret Prefix | User defined secret prefix to use when storing credentials. This prefix will be added to all the secrets added in the Vault. |
