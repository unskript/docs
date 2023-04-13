---
description: learn how to configure the Actions in your RunBook
---

# Configure Action Inputs

{% embed url="https://youtu.be/7id_TS9EK_c" %}



Most Actions take Input parameters. This makes them flexible and reusable.  Each Input parameter has a type (List, String, Number, etc.) to ensure that the correct data is being sent into the Action.

You can set the value right in the right navigation:

<figure><img src="../../../.gitbook/assets/Screenshot 2023-04-13 at 09.47.53.jpg" alt=""><figcaption></figcaption></figure>

`In this case, the Region input is set to the String "us-west-2"`

Alternatively, we can assign the variable region, and now whatever string is in this variable can be applied to the Region input. &#x20;

<figure><img src="../../../.gitbook/assets/Screenshot 2023-04-13 at 09.48.00.jpg" alt=""><figcaption></figcaption></figure>

This allows for greater flexibility in your RunBook - it can now be run in any AWS Region.
