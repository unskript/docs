# Schedules

Some RunBooks need to be run on a regular cadence - for collecting data, checking status or other tasks.  Using the unSkript scheduler, you can easily schedule Runbook executions at any desired cadence.

To enter the scheduler, Click Events in the top menu, and then choose schedule from the top of the resulting page.

To create a schedule, click the **Add Schedule** button.



![](<../../.gitbook/assets/Screen Shot 2022-05-24 at 12.43.00 PM.png>)

The schedule is configured in a [cron](https://crontab.guru/)-like fashion, with different frequencies for minute, hour, day MOnth and day of week. When you make your selection a text display that describes the schedule in words and the next execution time appears. On clicking Apply, the system will ask for xRunBook parameters if any were configured.&#x20;

![](<../../.gitbook/assets/Screen Shot 2022-05-24 at 12.44.10 PM.png>)

Once the parameter values have been provided, the schedule is created and the xRunBook will be run according to the configuration.
