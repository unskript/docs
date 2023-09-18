# SSH

There are three methods that can be used to authenticate a SHH connection:

* Basic Auth
* PEM file
* Vault

### [Listing of all SSH Actions](action\_ssh/)


### Parameters

To connect via SSH you'll need to provide the following parameters (depending on your Authentication type, the requirements change):

| Name                          | Description                                                | Authentication Type |
| ----------------------------- | ---------------------------------------------------------- | ------------------- |
| Name                          | This credential will be listed using the name you provide  | All                 |
| Port                          | SSH port to connect to                                     | All                 |
| Username                      | User to connect as. Defaults to logged in user             | All                 |
| Password                      | Password to use for password authentication                | Basic Auth          |
| Proxy User                    | username for Proxy                                         | Basic Auth          |
| Proxy password                | password for Proxy                                         | Basic Auth          |
| Private Key File              | Contents of the Private Key File to use for authentication | PEM                 |
| Proxy Private Ket FileP       | PEM file for proxy authentication                          | PEM                 |
| Vault URL                     |                                                            | Vault               |
| <p>SSH Secret Path</p><p></p> |                                                            | Vault               |
| Vault Role                    |                                                            | Vault               |

