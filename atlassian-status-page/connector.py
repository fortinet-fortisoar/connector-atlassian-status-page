""" Copyright start
  MIT License
  Copyright (c) 2025 Fortinet Inc
  Copyright end """

from connectors.core.connector import Connector, ConnectorError, get_logger
from .operations import operations_map, test_connectivity

logger = get_logger('atlassian-status-page')

class AtlassianStatusPageConnector(Connector):
    def execute(self, config, operation, params, **kwargs):
        action = operations_map.get(operation)
        return action(config, params)

    def check_health(self, config):
        try:
           return test_connectivity(config)
        except Exception as err:
            logger.error("Check Health Failed. Error: {0}".format(str(err)))
            raise ConnectorError(str(err))

