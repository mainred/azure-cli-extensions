# coding=utf-8
# --------------------------------------------------------------------------
# Copyright (c) Microsoft Corporation. All rights reserved.
# Licensed under the MIT License. See License.txt in the project root for license information.
# Code generated by Microsoft (R) AutoRest Code Generator.
# Changes may cause incorrect behavior and will be lost if the code is regenerated.
# --------------------------------------------------------------------------

from typing import Any, Optional

from azure.mgmt.core import ARMPipelineClient
from msrest import Deserializer, Serializer

from ._configuration import LogicManagementClientConfiguration
from .operations import WorkflowOperations
from .operations import WorkflowVersionOperations
from .operations import WorkflowTriggerOperations
from .operations import WorkflowVersionTriggerOperations
from .operations import WorkflowTriggerHistoryOperations
from .operations import WorkflowRunOperations
from .operations import WorkflowRunActionOperations
from .operations import WorkflowRunActionRepetitionOperations
from .operations import WorkflowRunActionRepetitionRequestHistoryOperations
from .operations import WorkflowRunActionRequestHistoryOperations
from .operations import WorkflowRunActionScopeRepetitionOperations
from .operations import WorkflowRunOperationOperations
from .operations import IntegrationAccountOperations
from .operations import IntegrationAccountAssemblyOperations
from .operations import IntegrationAccountBatchConfigurationOperations
from .operations import IntegrationAccountSchemaOperations
from .operations import IntegrationAccountMapOperations
from .operations import IntegrationAccountPartnerOperations
from .operations import IntegrationAccountAgreementOperations
from .operations import IntegrationAccountCertificateOperations
from .operations import IntegrationAccountSessionOperations
from .operations import IntegrationServiceEnvironmentOperations
from .operations import IntegrationServiceEnvironmentSkuOperations
from .operations import IntegrationServiceEnvironmentNetworkHealthOperations
from .operations import IntegrationServiceEnvironmentManagedApiOperations
from .operations import IntegrationServiceEnvironmentManagedApiOperationOperations
from .operations import OperationOperations
from . import models


class LogicManagementClient(object):
    """REST API for Azure Logic Apps.

    :ivar workflow: WorkflowOperations operations
    :vartype workflow: azure.mgmt.logic.operations.WorkflowOperations
    :ivar workflow_version: WorkflowVersionOperations operations
    :vartype workflow_version: azure.mgmt.logic.operations.WorkflowVersionOperations
    :ivar workflow_trigger: WorkflowTriggerOperations operations
    :vartype workflow_trigger: azure.mgmt.logic.operations.WorkflowTriggerOperations
    :ivar workflow_version_trigger: WorkflowVersionTriggerOperations operations
    :vartype workflow_version_trigger: azure.mgmt.logic.operations.WorkflowVersionTriggerOperations
    :ivar workflow_trigger_history: WorkflowTriggerHistoryOperations operations
    :vartype workflow_trigger_history: azure.mgmt.logic.operations.WorkflowTriggerHistoryOperations
    :ivar workflow_run: WorkflowRunOperations operations
    :vartype workflow_run: azure.mgmt.logic.operations.WorkflowRunOperations
    :ivar workflow_run_action: WorkflowRunActionOperations operations
    :vartype workflow_run_action: azure.mgmt.logic.operations.WorkflowRunActionOperations
    :ivar workflow_run_action_repetition: WorkflowRunActionRepetitionOperations operations
    :vartype workflow_run_action_repetition: azure.mgmt.logic.operations.WorkflowRunActionRepetitionOperations
    :ivar workflow_run_action_repetition_request_history: WorkflowRunActionRepetitionRequestHistoryOperations operations
    :vartype workflow_run_action_repetition_request_history: azure.mgmt.logic.operations.WorkflowRunActionRepetitionRequestHistoryOperations
    :ivar workflow_run_action_request_history: WorkflowRunActionRequestHistoryOperations operations
    :vartype workflow_run_action_request_history: azure.mgmt.logic.operations.WorkflowRunActionRequestHistoryOperations
    :ivar workflow_run_action_scope_repetition: WorkflowRunActionScopeRepetitionOperations operations
    :vartype workflow_run_action_scope_repetition: azure.mgmt.logic.operations.WorkflowRunActionScopeRepetitionOperations
    :ivar workflow_run_operation: WorkflowRunOperationOperations operations
    :vartype workflow_run_operation: azure.mgmt.logic.operations.WorkflowRunOperationOperations
    :ivar integration_account: IntegrationAccountOperations operations
    :vartype integration_account: azure.mgmt.logic.operations.IntegrationAccountOperations
    :ivar integration_account_assembly: IntegrationAccountAssemblyOperations operations
    :vartype integration_account_assembly: azure.mgmt.logic.operations.IntegrationAccountAssemblyOperations
    :ivar integration_account_batch_configuration: IntegrationAccountBatchConfigurationOperations operations
    :vartype integration_account_batch_configuration: azure.mgmt.logic.operations.IntegrationAccountBatchConfigurationOperations
    :ivar integration_account_schema: IntegrationAccountSchemaOperations operations
    :vartype integration_account_schema: azure.mgmt.logic.operations.IntegrationAccountSchemaOperations
    :ivar integration_account_map: IntegrationAccountMapOperations operations
    :vartype integration_account_map: azure.mgmt.logic.operations.IntegrationAccountMapOperations
    :ivar integration_account_partner: IntegrationAccountPartnerOperations operations
    :vartype integration_account_partner: azure.mgmt.logic.operations.IntegrationAccountPartnerOperations
    :ivar integration_account_agreement: IntegrationAccountAgreementOperations operations
    :vartype integration_account_agreement: azure.mgmt.logic.operations.IntegrationAccountAgreementOperations
    :ivar integration_account_certificate: IntegrationAccountCertificateOperations operations
    :vartype integration_account_certificate: azure.mgmt.logic.operations.IntegrationAccountCertificateOperations
    :ivar integration_account_session: IntegrationAccountSessionOperations operations
    :vartype integration_account_session: azure.mgmt.logic.operations.IntegrationAccountSessionOperations
    :ivar integration_service_environment: IntegrationServiceEnvironmentOperations operations
    :vartype integration_service_environment: azure.mgmt.logic.operations.IntegrationServiceEnvironmentOperations
    :ivar integration_service_environment_sku: IntegrationServiceEnvironmentSkuOperations operations
    :vartype integration_service_environment_sku: azure.mgmt.logic.operations.IntegrationServiceEnvironmentSkuOperations
    :ivar integration_service_environment_network_health: IntegrationServiceEnvironmentNetworkHealthOperations operations
    :vartype integration_service_environment_network_health: azure.mgmt.logic.operations.IntegrationServiceEnvironmentNetworkHealthOperations
    :ivar integration_service_environment_managed_api: IntegrationServiceEnvironmentManagedApiOperations operations
    :vartype integration_service_environment_managed_api: azure.mgmt.logic.operations.IntegrationServiceEnvironmentManagedApiOperations
    :ivar integration_service_environment_managed_api_operation: IntegrationServiceEnvironmentManagedApiOperationOperations operations
    :vartype integration_service_environment_managed_api_operation: azure.mgmt.logic.operations.IntegrationServiceEnvironmentManagedApiOperationOperations
    :ivar operation: OperationOperations operations
    :vartype operation: azure.mgmt.logic.operations.OperationOperations
    :param credential: Credential needed for the client to connect to Azure.
    :type credential: azure.core.credentials.TokenCredential
    :param subscription_id: The subscription id.
    :type subscription_id: str
    :param str base_url: Service URL
    """

    def __init__(
        self,
        credential,  # type: "TokenCredential"
        subscription_id,  # type: str
        base_url=None,  # type: Optional[str]
        **kwargs  # type: Any
    ):
        # type: (...) -> None
        if not base_url:
            base_url = 'https://management.azure.com'
        self._config = LogicManagementClientConfiguration(credential, subscription_id, **kwargs)
        self._client = ARMPipelineClient(base_url=base_url, config=self._config, **kwargs)

        client_models = {k: v for k, v in models.__dict__.items() if isinstance(v, type)}
        self._serialize = Serializer(client_models)
        self._deserialize = Deserializer(client_models)

        self.workflow = WorkflowOperations(
            self._client, self._config, self._serialize, self._deserialize)
        self.workflow_version = WorkflowVersionOperations(
            self._client, self._config, self._serialize, self._deserialize)
        self.workflow_trigger = WorkflowTriggerOperations(
            self._client, self._config, self._serialize, self._deserialize)
        self.workflow_version_trigger = WorkflowVersionTriggerOperations(
            self._client, self._config, self._serialize, self._deserialize)
        self.workflow_trigger_history = WorkflowTriggerHistoryOperations(
            self._client, self._config, self._serialize, self._deserialize)
        self.workflow_run = WorkflowRunOperations(
            self._client, self._config, self._serialize, self._deserialize)
        self.workflow_run_action = WorkflowRunActionOperations(
            self._client, self._config, self._serialize, self._deserialize)
        self.workflow_run_action_repetition = WorkflowRunActionRepetitionOperations(
            self._client, self._config, self._serialize, self._deserialize)
        self.workflow_run_action_repetition_request_history = WorkflowRunActionRepetitionRequestHistoryOperations(
            self._client, self._config, self._serialize, self._deserialize)
        self.workflow_run_action_request_history = WorkflowRunActionRequestHistoryOperations(
            self._client, self._config, self._serialize, self._deserialize)
        self.workflow_run_action_scope_repetition = WorkflowRunActionScopeRepetitionOperations(
            self._client, self._config, self._serialize, self._deserialize)
        self.workflow_run_operation = WorkflowRunOperationOperations(
            self._client, self._config, self._serialize, self._deserialize)
        self.integration_account = IntegrationAccountOperations(
            self._client, self._config, self._serialize, self._deserialize)
        self.integration_account_assembly = IntegrationAccountAssemblyOperations(
            self._client, self._config, self._serialize, self._deserialize)
        self.integration_account_batch_configuration = IntegrationAccountBatchConfigurationOperations(
            self._client, self._config, self._serialize, self._deserialize)
        self.integration_account_schema = IntegrationAccountSchemaOperations(
            self._client, self._config, self._serialize, self._deserialize)
        self.integration_account_map = IntegrationAccountMapOperations(
            self._client, self._config, self._serialize, self._deserialize)
        self.integration_account_partner = IntegrationAccountPartnerOperations(
            self._client, self._config, self._serialize, self._deserialize)
        self.integration_account_agreement = IntegrationAccountAgreementOperations(
            self._client, self._config, self._serialize, self._deserialize)
        self.integration_account_certificate = IntegrationAccountCertificateOperations(
            self._client, self._config, self._serialize, self._deserialize)
        self.integration_account_session = IntegrationAccountSessionOperations(
            self._client, self._config, self._serialize, self._deserialize)
        self.integration_service_environment = IntegrationServiceEnvironmentOperations(
            self._client, self._config, self._serialize, self._deserialize)
        self.integration_service_environment_sku = IntegrationServiceEnvironmentSkuOperations(
            self._client, self._config, self._serialize, self._deserialize)
        self.integration_service_environment_network_health = IntegrationServiceEnvironmentNetworkHealthOperations(
            self._client, self._config, self._serialize, self._deserialize)
        self.integration_service_environment_managed_api = IntegrationServiceEnvironmentManagedApiOperations(
            self._client, self._config, self._serialize, self._deserialize)
        self.integration_service_environment_managed_api_operation = IntegrationServiceEnvironmentManagedApiOperationOperations(
            self._client, self._config, self._serialize, self._deserialize)
        self.operation = OperationOperations(
            self._client, self._config, self._serialize, self._deserialize)

    def close(self):
        # type: () -> None
        self._client.close()

    def __enter__(self):
        # type: () -> LogicManagementClient
        self._client.__enter__()
        return self

    def __exit__(self, *exc_details):
        # type: (Any) -> None
        self._client.__exit__(*exc_details)