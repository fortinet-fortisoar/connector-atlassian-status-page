
<h2>About the connector</h2>

<p>This connector enables automated operations such as creating incidents, retrieving incident lists, managing active maintenances, and more.</p>

<p>This document provides information about the Atlassian Status Page connector, which facilitates automated interactions, with a Atlassian Status Page server using FortiSOAR&trade; playbooks. Add the Atlassian Status Page connector as a step in FortiSOAR&trade; playbooks and perform automated operations with Atlassian Status Page.</p>

<h3>Version information</h3>

<p>Connector Version: 1.0.0</p>

<p>FortiSOAR&trade; Version Tested on: 7.4.1-3167</p>

<p>Atlassian Status Page Version Tested on: </p>

<p>Authored By: Fortinet</p>

<p>Certified: No</p>

<h2>Installing the connector</h2>

<p>Use the <strong>Content Hub</strong> to install the connector. For the detailed procedure to install a connector, click <a href="https://docs.fortinet.com/document/fortisoar/0.0.0/installing-a-connector/1/installing-a-connector" target="_top">here</a>.</p><p>You can also use the <code>yum</code> command as a root user to install the connector:</p>

<pre>yum install cyops-connector-atlassian-status-page</pre>

<h2>Prerequisites to configuring the connector</h2>

<ul>
<li>You must have the credentials of Atlassian Status Page server to which you will connect and perform automated operations.</li>
<li>The FortiSOAR&trade; server should have outbound connectivity to port 443 on the Atlassian Status Page server.</li>
</ul>

<h2>Minimum Permissions Required</h2>

<ul>
<li>Not applicable</li>
</ul>

<h2>Configuring the connector</h2>

<p>For the procedure to configure a connector, click <a href="https://docs.fortinet.com/document/fortisoar/0.0.0/configuring-a-connector/1/configuring-a-connector">here</a></p>

<h3>Configuration parameters</h3>

<p>In FortiSOAR&trade;, on the Connectors page, click the <strong>Atlassian Status Page</strong> connector row (if you are in the <strong>Grid</strong> view on the Connectors page) and in the <strong>Configurations</strong> tab enter the required configuration details:</p>

<table border=1><thead><tr><th>Parameter</th><th>Description</th></tr></thead><tbody><tr><td>Server URL</td><td>Specify the host or server URL to authenticate with the Atlassian Statuspage REST API endpoint.</td></tr>
<tr><td>API Key</td><td>Specify the API key to authenticate with the Atlassian Statuspage REST API endpoint.</td></tr>
<tr><td>Verify SSL</td><td>Specifies whether the SSL certificate for the server is to be verified. <br/>By default, this option is selected, i.e., set to <code>true</code>.</td></tr>
</tbody></table>

<h2>Actions supported by the connector</h2>

<p>You can use the following automated operations in playbooks and also use the annotations to access operations:</p>

<table border=1><thead><tr><th>Function</th><th>Description</th><th>Annotation and Category</th></tr></thead><tbody><tr><td>Create Incident</td><td>Creates an incident in Atlassian Statuspage based on the provided input parameters.</td><td>create_incident <br/>Investigation</td></tr>
<tr><td>Get Incident</td><td>Retrieve a specific incident from from Atlassian Statuspage.</td><td>get_incident <br/>Investigation</td></tr>
<tr><td>Update Incident</td><td>Updates the details of an existing incident on a specific status page. This can include modifying the incident’s name, status, impact, or other relevant fields.</td><td>update_incident <br/>Investigation</td></tr>
<tr><td>Delete Incident</td><td>Deletes a specific incident from a status page. This operation permanently removes the incident and all its associated updates from the page.</td><td>delete_incident <br/>Investigation</td></tr>
<tr><td>Get Status Pages</td><td>Retrieves a list of all status pages from Atlassian Statuspage.</td><td>get_status_pages <br/>Investigation</td></tr>
<tr><td>Get Incident List</td><td>Retrieves a list of active and historical incidents, including real-time outages and scheduled maintenance incidents associated with a specified Statuspage.</td><td>get_incident_list <br/>Investigation</td></tr>
<tr><td>Get Active Maintenance Incidents</td><td>Retrieves a list of all currently active scheduled maintenance incidents for the specified Statuspage.</td><td>get_active_maintenance <br/>Investigation</td></tr>
<tr><td>Get Upcoming Incidents</td><td>Retrieves a list of upcoming incidents scheduled for a specific status page. Upcoming incidents are those that have been created and scheduled but have not yet started.</td><td>get_upcoming_incidents <br/>Investigation</td></tr>
<tr><td>Get Scheduled Incidents</td><td>Retrieves a list of all scheduled incidents, including both upcoming and ongoing scheduled maintenance events, for a specific status page.</td><td>get_scheduled_incidents <br/>Investigation</td></tr>
<tr><td>Get Unresolved Incidents</td><td>Retrieves a list of all unresolved incidents for a specific status page. Unresolved incidents are those that are currently open and have not yet been marked as resolved</td><td>get_unresolved_incidents <br/>Investigation</td></tr>
<tr><td>Execute an API Request</td><td>Execute any Atlassian Status Page API endpoint using the specified API method, endpoint, and payload as input parameters.</td><td>execute_api_request <br/>Utilities</td></tr>
</tbody></table>

<h3>operation: Create Incident</h3>

<h4>Input parameters</h4>

<table border=1><thead><tr><th>Parameter</th><th>Description</th></tr></thead><tbody><tr><td>Page ID</td><td>Specify the unique identifier of the status page from which the incident should be created.</td></tr>
<tr><td>Name</td><td>Specify the name of the incident to be shown on Atlassian Statuspage.</td></tr>
<tr><td>Status</td><td>(Optional) Select the status of the incident you want to create. Note: For realtime incidents, valid values are investigating, identified, monitoring, and resolved. For scheduled incidents, valid values are scheduled, in_progress, verifying, and completed<br><strong>If you choose 'Scheduled'</strong><ul><li>Scheduled Start Time: Specifies the scheduled start time for the incident. This parameter is used when creating a scheduled incident (such as planned maintenance) rather than an active or real-time incident.</li><li>Scheduled End Time: Specifies the scheduled end time for the incident. This parameter is used when creating a scheduled incident (typically planned maintenance) and defines when the maintenance is expected to be completed.</li><li>Scheduled Remind Prior: Specifies whether a reminder notification should be sent to subscribers before a scheduled incident begins.</li><li>Auto Transition to Maintenance State: Specifies this parameter the incident will automatically change its status from scheduled to in_progress at the scheduled start time.</li><li>Scheduled Auto In-Progress: Determines whether the scheduled incident should automatically change its status to in_progress at the time specified in the scheduled_for field. Note: Atlassian may use scheduled_auto_in_progress in newer API versions or for backward compatibility with certain integrations, but auto_transition_to_maintenance_state is generally preferred in documentation.</li><li>Auto Transition Deliver Notifications Start: Specifying this parameter notifications should be automatically sent to subscribers when a scheduled incident transitions to a resolved state at the scheduled end time (scheduled_until).</li></ul></td></tr>
<tr><td>Impact Override</td><td>(Optional) Select the impact override for the incident.</td></tr>
<tr><td>Comment</td><td>(Optional) Specify the detailed description or comment message of the incident. Note: Maximum limit is 25000 characters.</td></tr>
<tr><td>Deliver Notifications</td><td>(Optional) Deliver notifications to subscribers if this is true. If this is false, create an incident without notifying customers.</td></tr>
<tr><td>Components</td><td>(Optional) Map of status changes to apply to affected components.</td></tr>
<tr><td>Component IDs</td><td>(Optional) Specify a CSV list of of component_ids affected by this incident.</td></tr>
<tr><td>Meta Data</td><td>(Optional) Specify additional structured information(In JSON format)related information about the incident that doesn't belong to the main incident fields like name, status, or impact.</td></tr>
<tr><td>Additional Fields</td><td>(Optional) Specify any additional parameters in JSON format to create an incident.</td></tr>
</tbody></table>

<h4>Output</h4>

<p>The output contains the following populated JSON schema:</p>

<pre>{
    "id": "",
    "components": [
        {
            "id": "",
            "page_id": "",
            "group_id": "",
            "created_at": "",
            "updated_at": "",
            "group": "",
            "name": "",
            "description": "",
            "position": "",
            "status": "",
            "showcase": "",
            "only_show_if_degraded": "",
            "automation_email": "",
            "start_date": ""
        }
    ],
    "created_at": "",
    "impact": "",
    "impact_override": "",
    "incident_updates": [
        {
            "id": "",
            "incident_id": "",
            "affected_components": [
                {
                    "code": "",
                    "name": "",
                    "old_status": "",
                    "new_status": ""
                }
            ],
            "body": "",
            "created_at": "",
            "custom_tweet": "",
            "deliver_notifications": "",
            "display_at": "",
            "status": "",
            "tweet_id": "",
            "twitter_updated_at": "",
            "updated_at": "",
            "wants_twitter_update": ""
        }
    ],
    "incident_impacts": [
        {
            "id": "",
            "tenant_id": "",
            "atlassian_organization_id": "",
            "product_name": "",
            "experiences": [
                []
            ],
            "created_at": ""
        }
    ],
    "metadata": {
        "jira": {
            "issue_id": ""
        }
    },
    "monitoring_at": "",
    "name": "",
    "page_id": "",
    "postmortem_body": "",
    "postmortem_body_last_updated_at": "",
    "postmortem_ignored": "",
    "postmortem_notified_subscribers": "",
    "postmortem_notified_twitter": "",
    "postmortem_published_at": "",
    "resolved_at": "",
    "scheduled_auto_completed": "",
    "scheduled_auto_in_progress": "",
    "scheduled_for": "",
    "auto_transition_deliver_notifications_at_end": "",
    "auto_transition_deliver_notifications_at_start": "",
    "auto_transition_to_maintenance_state": "",
    "auto_transition_to_operational_state": "",
    "scheduled_remind_prior": "",
    "scheduled_reminded_at": "",
    "scheduled_until": "",
    "shortlink": "",
    "status": "",
    "updated_at": "",
    "reminder_intervals": ""
}</pre>

<h3>operation: Get Incident</h3>

<h4>Input parameters</h4>

<table border=1><thead><tr><th>Parameter</th><th>Description</th></tr></thead><tbody><tr><td>Page ID</td><td>Specify the unique identifier of the status page from which to retrieve the details of the specified incident.</td></tr>
<tr><td>Incident ID</td><td>Specify the unique identifier of the incident to retrieve its details.</td></tr>
</tbody></table>

<h4>Output</h4>

<p>The output contains the following populated JSON schema:</p>

<pre>{
    "id": "",
    "components": [
        {
            "id": "",
            "page_id": "",
            "group_id": "",
            "created_at": "",
            "updated_at": "",
            "group": "",
            "name": "",
            "description": "",
            "position": "",
            "status": "",
            "showcase": "",
            "only_show_if_degraded": "",
            "automation_email": "",
            "start_date": ""
        }
    ],
    "created_at": "",
    "impact": "",
    "impact_override": "",
    "incident_updates": [
        {
            "id": "",
            "incident_id": "",
            "affected_components": [
                {
                    "code": "",
                    "name": "",
                    "old_status": "",
                    "new_status": ""
                }
            ],
            "body": "",
            "created_at": "",
            "custom_tweet": "",
            "deliver_notifications": "",
            "display_at": "",
            "status": "",
            "tweet_id": "",
            "twitter_updated_at": "",
            "updated_at": "",
            "wants_twitter_update": ""
        }
    ],
    "incident_impacts": [
        {
            "id": "",
            "tenant_id": "",
            "atlassian_organization_id": "",
            "product_name": "",
            "experiences": [
                []
            ],
            "created_at": ""
        }
    ],
    "metadata": {
        "jira": {
            "issue_id": ""
        }
    },
    "monitoring_at": "",
    "name": "",
    "page_id": "",
    "postmortem_body": "",
    "postmortem_body_last_updated_at": "",
    "postmortem_ignored": "",
    "postmortem_notified_subscribers": "",
    "postmortem_notified_twitter": "",
    "postmortem_published_at": "",
    "resolved_at": "",
    "scheduled_auto_completed": "",
    "scheduled_auto_in_progress": "",
    "scheduled_for": "",
    "auto_transition_deliver_notifications_at_end": "",
    "auto_transition_deliver_notifications_at_start": "",
    "auto_transition_to_maintenance_state": "",
    "auto_transition_to_operational_state": "",
    "scheduled_remind_prior": "",
    "scheduled_reminded_at": "",
    "scheduled_until": "",
    "shortlink": "",
    "status": "",
    "updated_at": "",
    "reminder_intervals": ""
}</pre>

<h3>operation: Update Incident</h3>

<h4>Input parameters</h4>

<table border=1><thead><tr><th>Parameter</th><th>Description</th></tr></thead><tbody><tr><td>Page ID</td><td>Specify the unique identifier of the status page from which the incident should be updated.</td></tr>
<tr><td>Incident ID</td><td>Specify the unique identifier of the incident to be updated.</td></tr>
<tr><td>Name</td><td>(Optional) Specify the name of the incident to be updated.</td></tr>
<tr><td>Status</td><td>(Optional) Select the status of the incident you want to update. Note: For realtime incidents, valid values are investigating, identified, monitoring, and resolved. For scheduled incidents, valid values are scheduled, in_progress, verifying, and completed<br><strong>If you choose 'Scheduled'</strong><ul><li>Scheduled Start Time: Specifies the scheduled start time for the incident. This parameter is used when creating a scheduled incident (such as planned maintenance) rather than an active or real-time incident.</li><li>Scheduled End Time: Specifies the scheduled end time for the incident. This parameter is used when creating a scheduled incident (typically planned maintenance) and defines when the maintenance is expected to be completed.</li><li>Scheduled Remind Prior: Specifies whether a reminder notification should be sent to subscribers before a scheduled incident begins.</li><li>Auto Transition to Maintenance State: Specifies this parameter the incident will automatically change its status from scheduled to in_progress at the scheduled start time.</li><li>Scheduled Auto In-Progress: Determines whether the scheduled incident should automatically change its status to in_progress at the time specified in the scheduled_for field. Note: Atlassian may use scheduled_auto_in_progress in newer API versions or for backward compatibility with certain integrations, but auto_transition_to_maintenance_state is generally preferred in documentation.</li><li>Auto Transition Deliver Notifications Start: Specifying this parameter notifications should be automatically sent to subscribers when a scheduled incident transitions to a resolved state at the scheduled end time (scheduled_until).</li></ul></td></tr>
<tr><td>Impact Override</td><td>(Optional) Select the impact override for the incident.</td></tr>
<tr><td>Comment</td><td>(Optional) Specify the detailed description or comment message of the incident. Note: Maximum limit is 25000 characters.</td></tr>
<tr><td>Deliver Notifications</td><td>(Optional) Deliver notifications to subscribers if this is true. If this is false, create an incident without notifying customers.</td></tr>
<tr><td>Components</td><td>(Optional) Map of status changes to apply to affected components.</td></tr>
<tr><td>Component IDs</td><td>(Optional) Specify a CSV list of of component ids affected by this incident.</td></tr>
<tr><td>Meta Data</td><td>(Optional) Specify additional structured information(In JSON format)related information about the incident that doesn't belong to the main incident fields like name, status, or impact.</td></tr>
<tr><td>Additional Fields</td><td>(Optional) Specify any additional parameters in JSON format to create an incident.</td></tr>
</tbody></table>

<h4>Output</h4>

<p>The output contains the following populated JSON schema:</p>

<pre>{
    "incident": {
        "name": "",
        "status": "",
        "impact_override": "",
        "scheduled_for": "",
        "scheduled_until": "",
        "scheduled_remind_prior": "",
        "auto_transition_to_maintenance_state": "",
        "auto_transition_to_operational_state": "",
        "scheduled_auto_in_progress": "",
        "scheduled_auto_completed": "",
        "auto_transition_deliver_notifications_at_start": "",
        "auto_transition_deliver_notifications_at_end": "",
        "reminder_intervals": "",
        "metadata": {},
        "deliver_notifications": "",
        "auto_tweet_at_beginning": "",
        "auto_tweet_on_completion": "",
        "auto_tweet_on_creation": "",
        "auto_tweet_one_hour_before": "",
        "backfill_date": "",
        "backfilled": "",
        "body": "",
        "components": {
            "01sfln3x1y16": ""
        },
        "component_ids": [],
        "scheduled_auto_transition": ""
    }
}</pre>

<h3>operation: Delete Incident</h3>

<h4>Input parameters</h4>

<table border=1><thead><tr><th>Parameter</th><th>Description</th></tr></thead><tbody><tr><td>Page ID</td><td>Specify the unique identifier of the status page from which you want to delete the specified incident.</td></tr>
<tr><td>Incident ID</td><td>Specify the unique identifier of the incident which you want to delete.</td></tr>
</tbody></table>

<h4>Output</h4>

<p>The output contains the following populated JSON schema:</p>

<pre>{
    "id": "",
    "components": [
        {
            "id": "",
            "page_id": "",
            "group_id": "",
            "created_at": "",
            "updated_at": "",
            "group": "",
            "name": "",
            "description": "",
            "position": "",
            "status": "",
            "showcase": "",
            "only_show_if_degraded": "",
            "automation_email": "",
            "start_date": ""
        }
    ],
    "created_at": "",
    "impact": "",
    "impact_override": "",
    "incident_updates": [
        {
            "id": "",
            "incident_id": "",
            "affected_components": [
                {
                    "code": "",
                    "name": "",
                    "old_status": "",
                    "new_status": ""
                }
            ],
            "body": "",
            "created_at": "",
            "custom_tweet": "",
            "deliver_notifications": "",
            "display_at": "",
            "status": "",
            "tweet_id": "",
            "twitter_updated_at": "",
            "updated_at": "",
            "wants_twitter_update": ""
        }
    ],
    "incident_impacts": [
        {
            "id": "",
            "tenant_id": "",
            "atlassian_organization_id": "",
            "product_name": "",
            "experiences": [
                []
            ],
            "created_at": ""
        }
    ],
    "metadata": {
        "jira": {
            "issue_id": ""
        }
    },
    "monitoring_at": "",
    "name": "",
    "page_id": "",
    "postmortem_body": "",
    "postmortem_body_last_updated_at": "",
    "postmortem_ignored": "",
    "postmortem_notified_subscribers": "",
    "postmortem_notified_twitter": "",
    "postmortem_published_at": "",
    "resolved_at": "",
    "scheduled_auto_completed": "",
    "scheduled_auto_in_progress": "",
    "scheduled_for": "",
    "auto_transition_deliver_notifications_at_end": "",
    "auto_transition_deliver_notifications_at_start": "",
    "auto_transition_to_maintenance_state": "",
    "auto_transition_to_operational_state": "",
    "scheduled_remind_prior": "",
    "scheduled_reminded_at": "",
    "scheduled_until": "",
    "shortlink": "",
    "status": "",
    "updated_at": "",
    "reminder_intervals": ""
}</pre>

<h3>operation: Get Status Pages</h3>

<h4>Input parameters</h4>

<p>None.</p>

<h4>Output</h4>

<p>The output contains the following populated JSON schema:</p>

<pre>[
    {
        "id": "",
        "created_at": "",
        "updated_at": "",
        "name": "",
        "page_description": "",
        "headline": "",
        "branding": "",
        "subdomain": "",
        "domain": "",
        "url": "",
        "support_url": "",
        "hidden_from_search": "",
        "allow_page_subscribers": "",
        "allow_incident_subscribers": "",
        "allow_email_subscribers": "",
        "allow_sms_subscribers": "",
        "allow_rss_atom_feeds": "",
        "allow_webhook_subscribers": "",
        "notifications_from_email": "",
        "notifications_email_footer": "",
        "activity_score": "",
        "twitter_username": "",
        "viewers_must_be_team_members": "",
        "ip_restrictions": "",
        "city": "",
        "state": "",
        "country": "",
        "time_zone": "",
        "css_body_background_color": "",
        "css_font_color": "",
        "css_light_font_color": "",
        "css_greens": "",
        "css_yellows": "",
        "css_oranges": "",
        "css_blues": "",
        "css_reds": "",
        "css_border_color": "",
        "css_graph_color": "",
        "css_link_color": "",
        "css_no_data": "",
        "favicon_logo": "",
        "transactional_logo": "",
        "hero_cover": "",
        "email_logo": "",
        "twitter_logo": ""
    }
]</pre>

<h3>operation: Get Incident List</h3>

<h4>Input parameters</h4>

<table border=1><thead><tr><th>Parameter</th><th>Description</th></tr></thead><tbody><tr><td>Page ID</td><td>Specify the unique identifier of the Statuspage from which you want to retrieve the list of incidents.</td></tr>
<tr><td>Query</td><td>(Optional) If this is specified, search for the text query string in the incidents' name, status, postmortem_body, and incident_updates fields.</td></tr>
<tr><td>Limit</td><td>(Optional) The maximum number of rows to return per page. The default and maximum limit is 100.</td></tr>
<tr><td>Offset</td><td>(Optional) Specify the page offset for pagination.</td></tr>
</tbody></table>

<h4>Output</h4>

<p>The output contains the following populated JSON schema:</p>

<pre>[
    {
        "id": "",
        "components": [
            {
                "id": "",
                "page_id": "",
                "group_id": "",
                "created_at": "",
                "updated_at": "",
                "group": "",
                "name": "",
                "description": "",
                "position": "",
                "status": "",
                "showcase": "",
                "only_show_if_degraded": "",
                "automation_email": "",
                "start_date": ""
            }
        ],
        "created_at": "",
        "impact": "",
        "impact_override": "",
        "incident_updates": [
            {
                "id": "",
                "incident_id": "",
                "affected_components": [
                    {
                        "code": "",
                        "name": "",
                        "old_status": "",
                        "new_status": ""
                    }
                ],
                "body": "",
                "created_at": "",
                "custom_tweet": "",
                "deliver_notifications": "",
                "display_at": "",
                "status": "",
                "tweet_id": "",
                "twitter_updated_at": "",
                "updated_at": "",
                "wants_twitter_update": ""
            }
        ],
        "incident_impacts": [
            {
                "id": "",
                "tenant_id": "",
                "atlassian_organization_id": "",
                "product_name": "",
                "experiences": [
                    []
                ],
                "created_at": ""
            }
        ],
        "metadata": {
            "jira": {
                "issue_id": ""
            }
        },
        "monitoring_at": "",
        "name": "",
        "page_id": "",
        "postmortem_body": "",
        "postmortem_body_last_updated_at": "",
        "postmortem_ignored": "",
        "postmortem_notified_subscribers": "",
        "postmortem_notified_twitter": "",
        "postmortem_published_at": "",
        "resolved_at": "",
        "scheduled_auto_completed": "",
        "scheduled_auto_in_progress": "",
        "scheduled_for": "",
        "auto_transition_deliver_notifications_at_end": "",
        "auto_transition_deliver_notifications_at_start": "",
        "auto_transition_to_maintenance_state": "",
        "auto_transition_to_operational_state": "",
        "scheduled_remind_prior": "",
        "scheduled_reminded_at": "",
        "scheduled_until": "",
        "shortlink": "",
        "status": "",
        "updated_at": "",
        "reminder_intervals": ""
    }
]</pre>

<h3>operation: Get Active Maintenance Incidents</h3>

<h4>Input parameters</h4>

<table border=1><thead><tr><th>Parameter</th><th>Description</th></tr></thead><tbody><tr><td>Page ID</td><td>Specify the unique identifier of the status page for which you want to retrieve the list of active maintenance incidents.</td></tr>
<tr><td>Limit</td><td>(Optional) The maximum number of rows to return per page. The default and maximum limit is 100.</td></tr>
<tr><td>Offset</td><td>(Optional) Specify the page offset for pagination.</td></tr>
</tbody></table>

<h4>Output</h4>

<p>The output contains the following populated JSON schema:</p>

<pre>[
    {
        "id": "",
        "components": [
            {
                "id": "",
                "page_id": "",
                "group_id": "",
                "created_at": "",
                "updated_at": "",
                "group": "",
                "name": "",
                "description": "",
                "position": "",
                "status": "",
                "showcase": "",
                "only_show_if_degraded": "",
                "automation_email": "",
                "start_date": ""
            }
        ],
        "created_at": "",
        "impact": "",
        "impact_override": "",
        "incident_updates": [
            {
                "id": "",
                "incident_id": "",
                "affected_components": [
                    {
                        "code": "",
                        "name": "",
                        "old_status": "",
                        "new_status": ""
                    }
                ],
                "body": "",
                "created_at": "",
                "custom_tweet": "",
                "deliver_notifications": "",
                "display_at": "",
                "status": "",
                "tweet_id": "",
                "twitter_updated_at": "",
                "updated_at": "",
                "wants_twitter_update": ""
            }
        ],
        "incident_impacts": [
            {
                "id": "",
                "tenant_id": "",
                "atlassian_organization_id": "",
                "product_name": "",
                "experiences": [
                    []
                ],
                "created_at": ""
            }
        ],
        "metadata": {
            "jira": {
                "issue_id": ""
            }
        },
        "monitoring_at": "",
        "name": "",
        "page_id": "",
        "postmortem_body": "",
        "postmortem_body_last_updated_at": "",
        "postmortem_ignored": "",
        "postmortem_notified_subscribers": "",
        "postmortem_notified_twitter": "",
        "postmortem_published_at": "",
        "resolved_at": "",
        "scheduled_auto_completed": "",
        "scheduled_auto_in_progress": "",
        "scheduled_for": "",
        "auto_transition_deliver_notifications_at_end": "",
        "auto_transition_deliver_notifications_at_start": "",
        "auto_transition_to_maintenance_state": "",
        "auto_transition_to_operational_state": "",
        "scheduled_remind_prior": "",
        "scheduled_reminded_at": "",
        "scheduled_until": "",
        "shortlink": "",
        "status": "",
        "updated_at": "",
        "reminder_intervals": ""
    }
]</pre>

<h3>operation: Get Upcoming Incidents</h3>

<h4>Input parameters</h4>

<table border=1><thead><tr><th>Parameter</th><th>Description</th></tr></thead><tbody><tr><td>Page ID</td><td>Specify the unique identifier of the status page for which you want to retrieve the list of active upcoming incidents.</td></tr>
<tr><td>Limit</td><td>(Optional) The maximum number of rows to return per page. The default and maximum limit is 100.</td></tr>
<tr><td>Offset</td><td>(Optional) Specify the page offset for pagination.</td></tr>
</tbody></table>

<h4>Output</h4>

<p>The output contains the following populated JSON schema:</p>

<pre>[
    {
        "id": "",
        "components": [
            {
                "id": "",
                "page_id": "",
                "group_id": "",
                "created_at": "",
                "updated_at": "",
                "group": "",
                "name": "",
                "description": "",
                "position": "",
                "status": "",
                "showcase": "",
                "only_show_if_degraded": "",
                "automation_email": "",
                "start_date": ""
            }
        ],
        "created_at": "",
        "impact": "",
        "impact_override": "",
        "incident_updates": [
            {
                "id": "",
                "incident_id": "",
                "affected_components": [
                    {
                        "code": "",
                        "name": "",
                        "old_status": "",
                        "new_status": ""
                    }
                ],
                "body": "",
                "created_at": "",
                "custom_tweet": "",
                "deliver_notifications": "",
                "display_at": "",
                "status": "",
                "tweet_id": "",
                "twitter_updated_at": "",
                "updated_at": "",
                "wants_twitter_update": true
            }
        ],
        "incident_impacts": [
            {
                "id": "",
                "tenant_id": "",
                "atlassian_organization_id": "",
                "product_name": "",
                "experiences": [
                    []
                ],
                "created_at": ""
            }
        ],
        "metadata": {
            "jira": {
                "issue_id": ""
            }
        },
        "monitoring_at": "",
        "name": "",
        "page_id": "",
        "postmortem_body": "",
        "postmortem_body_last_updated_at": "",
        "postmortem_ignored": "",
        "postmortem_notified_subscribers": "",
        "postmortem_notified_twitter": "",
        "postmortem_published_at": "",
        "resolved_at": "",
        "scheduled_auto_completed": "",
        "scheduled_auto_in_progress": "",
        "scheduled_for": "",
        "auto_transition_deliver_notifications_at_end": "",
        "auto_transition_deliver_notifications_at_start": "",
        "auto_transition_to_maintenance_state": "",
        "auto_transition_to_operational_state": "",
        "scheduled_remind_prior": "",
        "scheduled_reminded_at": "",
        "scheduled_until": "",
        "shortlink": "",
        "status": "",
        "updated_at": "",
        "reminder_intervals": ""
    }
]</pre>

<h3>operation: Get Scheduled Incidents</h3>

<h4>Input parameters</h4>

<table border=1><thead><tr><th>Parameter</th><th>Description</th></tr></thead><tbody><tr><td>Page ID</td><td>Specify the unique identifier of the status page for which you want to retrieve the list of scheduled incidents.</td></tr>
<tr><td>Limit</td><td>(Optional) The maximum number of rows to return per page. The default and maximum limit is 100.</td></tr>
<tr><td>Offset</td><td>(Optional) Specify the page offset for pagination.</td></tr>
</tbody></table>

<h4>Output</h4>

<p>The output contains the following populated JSON schema:</p>

<pre>[
    {
        "id": "",
        "components": [
            {
                "id": "",
                "page_id": "",
                "group_id": "",
                "created_at": "",
                "updated_at": "",
                "group": "",
                "name": "",
                "description": "",
                "position": "",
                "status": "",
                "showcase": "",
                "only_show_if_degraded": "",
                "automation_email": "",
                "start_date": ""
            }
        ],
        "created_at": "",
        "impact": "",
        "impact_override": "",
        "incident_updates": [
            {
                "id": "",
                "incident_id": "",
                "affected_components": [
                    {
                        "code": "",
                        "name": "",
                        "old_status": "",
                        "new_status": ""
                    }
                ],
                "body": "",
                "created_at": "",
                "custom_tweet": "",
                "deliver_notifications": "",
                "display_at": "",
                "status": "",
                "tweet_id": "",
                "twitter_updated_at": "",
                "updated_at": "",
                "wants_twitter_update": ""
            }
        ],
        "incident_impacts": [
            {
                "id": "",
                "tenant_id": "",
                "atlassian_organization_id": "",
                "product_name": "",
                "experiences": [
                    []
                ],
                "created_at": ""
            }
        ],
        "metadata": {
            "jira": {
                "issue_id": ""
            }
        },
        "monitoring_at": "",
        "name": "",
        "page_id": "",
        "postmortem_body": "",
        "postmortem_body_last_updated_at": "",
        "postmortem_ignored": "",
        "postmortem_notified_subscribers": "",
        "postmortem_notified_twitter": "",
        "postmortem_published_at": "",
        "resolved_at": "",
        "scheduled_auto_completed": "",
        "scheduled_auto_in_progress": "",
        "scheduled_for": "",
        "auto_transition_deliver_notifications_at_end": "",
        "auto_transition_deliver_notifications_at_start": "",
        "auto_transition_to_maintenance_state": "",
        "auto_transition_to_operational_state": "",
        "scheduled_remind_prior": "",
        "scheduled_reminded_at": "",
        "scheduled_until": "",
        "shortlink": "",
        "status": "",
        "updated_at": "",
        "reminder_intervals": ""
    }
]</pre>

<h3>operation: Get Unresolved Incidents</h3>

<h4>Input parameters</h4>

<table border=1><thead><tr><th>Parameter</th><th>Description</th></tr></thead><tbody><tr><td>Page ID</td><td>Specify the unique identifier of the status page for which you want to retrieve the list of unresolved incidents.</td></tr>
<tr><td>Limit</td><td>(Optional) The maximum number of rows to return per page. The default and maximum limit is 100.</td></tr>
<tr><td>Offset</td><td>(Optional) Specify the page offset for pagination.</td></tr>
</tbody></table>

<h4>Output</h4>

<p>The output contains the following populated JSON schema:</p>

<pre>[
    {
        "id": "",
        "components": [
            {
                "id": "",
                "page_id": "",
                "group_id": "",
                "created_at": "",
                "updated_at": "",
                "group": "",
                "name": "",
                "description": "",
                "position": "",
                "status": "",
                "showcase": "",
                "only_show_if_degraded": "",
                "automation_email": "",
                "start_date": ""
            }
        ],
        "created_at": "",
        "impact": "",
        "impact_override": "",
        "incident_updates": [
            {
                "id": "",
                "incident_id": "",
                "affected_components": [
                    {
                        "code": "",
                        "name": "",
                        "old_status": "",
                        "new_status": ""
                    }
                ],
                "body": "",
                "created_at": "",
                "custom_tweet": "",
                "deliver_notifications": "",
                "display_at": "",
                "status": "",
                "tweet_id": "",
                "twitter_updated_at": "",
                "updated_at": "",
                "wants_twitter_update": ""
            }
        ],
        "incident_impacts": [
            {
                "id": "",
                "tenant_id": "",
                "atlassian_organization_id": "",
                "product_name": "",
                "experiences": [
                    []
                ],
                "created_at": ""
            }
        ],
        "metadata": {
            "jira": {
                "issue_id": ""
            }
        },
        "monitoring_at": "",
        "name": "",
        "page_id": "",
        "postmortem_body": "",
        "postmortem_body_last_updated_at": "",
        "postmortem_ignored": "",
        "postmortem_notified_subscribers": "",
        "postmortem_notified_twitter": "",
        "postmortem_published_at": "",
        "resolved_at": "",
        "scheduled_auto_completed": "",
        "scheduled_auto_in_progress": "",
        "scheduled_for": "",
        "auto_transition_deliver_notifications_at_end": "",
        "auto_transition_deliver_notifications_at_start": "",
        "auto_transition_to_maintenance_state": "",
        "auto_transition_to_operational_state": "",
        "scheduled_remind_prior": "",
        "scheduled_reminded_at": "",
        "scheduled_until": "",
        "shortlink": "",
        "status": "",
        "updated_at": "",
        "reminder_intervals": ""
    }
]</pre>

<h3>operation: Execute an API Request</h3>

<h4>Input parameters</h4>

<table border=1><thead><tr><th>Parameter</th><th>Description</th></tr></thead><tbody><tr><td>Endpoint</td><td>Specify the REST API endpoint for the action to perform. Note: Do not include the host URL in the endpoint. ex /v1/pages/{page_id}/incidents/unresolved or /v1/pages/{page_id}/incidents/{incident_id}.</td></tr>
<tr><td>Method</td><td>The HTTP Method to use</td></tr>
<tr><td>Query Parameters</td><td>(Optional) Specify the he Rest API query parameters object in JSON format.</td></tr>
<tr><td>Request Body/Payload</td><td>(Optional) The payload needed for the call. Use empty brackets if there is no payload.</td></tr>
</tbody></table>

<h4>Output</h4>

<p>The output contains a non-dictionary value.</p>

<h2>Included playbooks</h2>

<p>The <code>Sample - Atlassian Status Page - 1.0.0</code> playbook collection comes bundled with the Atlassian Status Page connector. These playbooks contain steps using which you can perform all supported actions. You can see bundled playbooks in the <strong>Automation</strong> &gt; <strong>Playbooks</strong> section in FortiSOAR&trade; after importing the Atlassian Status Page connector.</p>

<ul>
<li>Create Incident</li>
<li>Delete Incident</li>
<li>Execute an API Request</li>
<li>Get Active Maintenance Incidents</li>
<li>Get Incident</li>
<li>Get Incident List</li>
<li>Get Scheduled Incidents</li>
<li>Get Status Pages</li>
<li>Get Unresolved Incidents</li>
<li>Get Upcoming Incidents</li>
<li>Update Incident</li>
</ul>

<p><strong>Note</strong>: If you are planning to use any of the sample playbooks in your environment, ensure that you clone those playbooks and move them to a different collection since the sample playbook collection gets deleted during connector upgrade and delete.</p>
