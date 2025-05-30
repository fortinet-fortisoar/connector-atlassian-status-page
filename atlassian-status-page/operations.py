""" Copyright start
  MIT License
  Copyright (c) 2025 Fortinet Inc
  Copyright end """

import requests
from connectors.core.connector import ConnectorError, get_logger

logger = get_logger('atlassian-status-page')


class AtlassianStatusPage(object):
    def __init__(self, config):
        self.server_url = config.get("server_url").strip('/')
        if not self.server_url.startswith('https://') and not self.server_url.startswith('http://'):
            self.server_url = 'https://' + self.server_url
        self.api_key = config.get("api_key")
        self.verify_ssl = config.get('verify_ssl')
        self.headers = {'Authorization': 'OAuth {}'.format(self.api_key)}

    def make_api_call(self, method="GET", endpoint="", params=None, data=None, json_data=None,
                      verify_ssl=False):
        try:
            logger.debug(f"Method: {method}")
            logger.debug(f"Data: {data}")
            logger.debug(f"json_data: {json_data}")
            logger.debug(f"params: {params}")
            endpoint = self.server_url + endpoint
            logger.debug(f"RESP API Endpoint: {endpoint}")
            response = requests.request(method=method, url=endpoint, headers=self.headers, data=data, json=json_data,
                                        params=params, verify=verify_ssl)
            if response.ok:
                if response.content:
                    response = response.json()
                else:
                    response = {"result": "No Data Returned", "status": "success"}
                return response
            else:
                logger.error("Error: {0}".format(response.text))
                raise ConnectorError('{0}:{1}'.format(response.status_code, response.text))
        except requests.exceptions.SSLError as e:
            logger.exception('{0}'.format(e))
            raise ConnectorError('{0}'.format(e))
        except requests.exceptions.ConnectionError as e:
            logger.exception('{0}'.format(e))
            raise ConnectorError('{0}'.format(e))
        except Exception as e:
            logger.error('{0}'.format(e))
            raise ConnectorError('{0}'.format(e))


def build_incident_payload(params):
    params = {k: v for k, v in params.items() if v is not None and v != ''}
    status = params.get('status', '')
    if status:
        params['status'] = status.replace(' ', '_').lower()
    impact_override = params.get('impact_override', '')
    if impact_override:
        params['impact_override'] = impact_override.lower()
    component_ids = params.get('component_ids', '')
    if isinstance(component_ids, str):
        component_ids = component_ids.split(',')
    if isinstance(component_ids, list):
        component_ids = [x.strip() for x in component_ids]
    params['component_ids'] = component_ids
    additional_fields = params.pop('additional_fields', {})
    if additional_fields:
        params.update(additional_fields)
    return params


def create_incident(config, params):
    client = AtlassianStatusPage(config)
    page_id = params.pop('page_id', '')
    endpoint = f"/v1/pages/{page_id}/incidents"
    payload = build_incident_payload(params)
    return client.make_api_call(method="POST", endpoint=endpoint, data=payload)


def update_incident(config, params):
    client = AtlassianStatusPage(config)
    page_id = params.pop('page_id', '')
    incident_id = params.pop('incident_id', '')
    endpoint = f"/v1/pages/{page_id}/incidents/{incident_id}"
    payload = build_incident_payload(params)
    return client.make_api_call(method="PUT", endpoint=endpoint, data=payload)


def get_query_string_params(params):
    query_string_params = {k: v for k, v in params.items() if v is not None and v != ''}
    return query_string_params


def execute_request(config, params, endpoint):
    client = AtlassianStatusPage(config)
    query_string_params = get_query_string_params(params)
    return client.make_api_call(method="GET", endpoint=endpoint, params=query_string_params)


def get_list_incidents(config, params):
    page_id = params.pop('page_id', '')
    endpoint = f"/v1/pages/{page_id}/incidents"
    return execute_request(config, params, endpoint)


def get_active_maintenance(config, params):
    page_id = params.pop('page_id', '')
    endpoint = f"/v1/pages/{page_id}/incidents/active_maintenance"
    return execute_request(config, params, endpoint)


def get_upcoming_incidents(config, params):
    page_id = params.pop('page_id', '')
    endpoint = f"/v1/pages/{page_id}/incidents/upcoming"
    return execute_request(config, params, endpoint)


def get_scheduled_incidents(config, params):
    page_id = params.pop('page_id', '')
    endpoint = f"/v1/pages/{page_id}/incidents/scheduled"
    return execute_request(config, params, endpoint)


def get_unresolved_incidents(config, params):
    page_id = params.pop('page_id', '')
    endpoint = f"/v1/pages/{page_id}/incidents/unresolved"
    return execute_request(config, params, endpoint)


def delete_incident(config, params):
    client = AtlassianStatusPage(config)
    page_id = params.get('page_id')
    incident_id = params.get('incident_id')
    endpoint = f"/v1/pages/{page_id}/incidents/{incident_id}"
    return client.make_api_call(method="DELETE", endpoint=endpoint)


def get_incident(config, params):
    client = AtlassianStatusPage(config)
    page_id = params.get('page_id')
    incident_id = params.get('incident_id')
    endpoint = f"/v1/pages/{page_id}/incidents/{incident_id}"
    return client.make_api_call(method="GET", endpoint=endpoint)


def get_list_status_pages(config, params):
    client = AtlassianStatusPage(config)
    return client.make_api_call(method="GET", endpoint='/v1/pages')


def execute_api_request(config, params):
    client = AtlassianStatusPage(config)
    endpoint = params.get('endpoint')
    method = params.get('method')
    query_params = params.get('query_params')
    payload = params.get('payload')
    return client.make_api_call(method=method, endpoint=endpoint, params=query_params, data=payload)


def test_connectivity(config):
    return get_list_status_pages(config, {})


operations_map = {
    'get_list_status_pages': get_list_status_pages,
    'create_incident': create_incident,
    'get_incident': get_incident,
    'delete_incident': delete_incident,
    'update_incident': update_incident,
    'get_list_incidents': get_list_incidents,
    'get_active_maintenance': get_active_maintenance,
    'get_upcoming_incidents': get_upcoming_incidents,
    'get_scheduled_incidents': get_scheduled_incidents,
    'get_unresolved_incidents': get_unresolved_incidents,
    'execute_api_request': execute_api_request

}
