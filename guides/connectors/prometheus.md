# Prometheus

![Information needed to onboard Prometheus connector](<../../.gitbook/assets/Screen Shot 2022-06-15 at 7.52.25 PM.png>)

| Name        | Description                                                                                                  |
| ----------- | ------------------------------------------------------------------------------------------------------------ |
| Name        | This credential will be listed using the name you provide                                                    |
| URL         | URL for the Prometheus host. Eg: http://localhost:9090                                                       |
| Headers     | <p>A dictionary of optional HTTP headers.</p><p>Eg: {“Authorization”: “Bearer eyh838rfsw”}</p>               |
| Disable ssl | When set to True, it will disable SSL certificate verification for HTTP requests made to the Prometheus host |

### Create a webhook for Prometheus alarms

Once your Prometheus credentials are added into unSkript, you'll want to create a webhook to receive alarms from Prometheus.

1. On the Proxy page, find the credential you just created, and click the button to generate a webhook. &#x20;
