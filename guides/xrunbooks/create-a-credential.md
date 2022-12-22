---
description: Connecting your Actions to external services
---

# Create a Credential

Any Action that connects to an external service will require a Credential.  To learn how to create a credential to a specific provider, check the section on [Connectors](../connectors/).  Each Connector service has instructions on how to add a Credential.

### ServiceID

When adding a Credential, a serviceID can be added. ServiceID is a variable abstraction of the Credential. &#x20;

When a xRunBook is run in multiple environments, different credentials might be used (for example - the AWS connection in dev might be different than the one used in production). &#x20;

It would be possible to have 2 instances of the xRunBook - one for deva and one for production - but this could introduce errors.  Instead, if the dev & prod credentials share a serviceID, and the xRunBook can be configured to use the serviceID for the credentials.  Now, the xRunbook can be run in either environment without any changes, using the correct credentials in both environments.
