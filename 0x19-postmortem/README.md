The postmortem analysis details a technical outage that affected a website due to issues with the Nginx server configuration. Here’s a concise summary of the key points:
Issue Summary
Outage Duration: From 11:45 AM to 12:45 PM West African Time.
Impact: The website was inaccessible as it was not listening on port 80.
Root Cause
The main issue stemmed from the Nginx server's configuration. Specifically, the settings in sites-available were not linked to sites-enabled, rendering the configuration inactive despite being correct.
Timeline of Events
11:45 AM: Outage detected when the platform attempted to access the site.
11:50 AM: Monitoring alerts confirmed the downtime.
11:55 AM: Initial checks showed no errors in Nginx configuration files.
12:15 PM: Investigation revealed the missing link between sites-available and sites-enabled.
12:30 PM: The correct configuration was linked, and Nginx was restarted.
12:45 PM: The site was back online.
Resolution
Linking the default configuration from sites-available to sites-enabled and restarting Nginx resolved the issue.
Preventative Measures
To prevent future occurrences, the following improvements were suggested:
Implement a script to automatically link configurations after changes.
Enhance monitoring systems for quicker detection of similar issues.
Example Script
bash
#!/usr/bin/env bash
# Ensure Nginx is properly configured and listening on port 80

cat /etc/nginx/sites-available/default > /etc/nginx/sites-enabled/default
sudo service nginx restart

This script ensures that the correct configuration is enabled and restarts Nginx to apply changes.
