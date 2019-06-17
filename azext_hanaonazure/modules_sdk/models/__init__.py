# coding=utf-8
# --------------------------------------------------------------------------
# Copyright (c) Microsoft Corporation. All rights reserved.
# Licensed under the MIT License. See License.txt in the project root for
# license information.
#
# Code generated by Microsoft (R) AutoRest Code Generator.
# Changes may cause incorrect behavior and will be lost if the code is
# regenerated.
# --------------------------------------------------------------------------

try:
    from .resource_py3 import Resource
    from .hardware_profile_py3 import HardwareProfile
    from .disk_py3 import Disk
    from .storage_profile_py3 import StorageProfile
    from .os_profile_py3 import OSProfile
    from .ip_address_py3 import IpAddress
    from .network_profile_py3 import NetworkProfile
    from .hana_instance_py3 import HanaInstance
    from .display_py3 import Display
    from .operation_py3 import Operation
    from .error_response_py3 import ErrorResponse, ErrorResponseException
    from .tags_py3 import Tags
    from .monitoring_details_py3 import MonitoringDetails
except (SyntaxError, ImportError):
    from .resource import Resource
    from .hardware_profile import HardwareProfile
    from .disk import Disk
    from .storage_profile import StorageProfile
    from .os_profile import OSProfile
    from .ip_address import IpAddress
    from .network_profile import NetworkProfile
    from .hana_instance import HanaInstance
    from .display import Display
    from .operation import Operation
    from .error_response import ErrorResponse, ErrorResponseException
    from .tags import Tags
    from .monitoring_details import MonitoringDetails
from .operation_paged import OperationPaged
from .hana_instance_paged import HanaInstancePaged
from .hana_management_client_enums import (
    HanaHardwareTypeNamesEnum,
    HanaInstanceSizeNamesEnum,
    HanaInstancePowerStateEnum,
    HanaProvisioningStatesEnum,
)

__all__ = [
    'Resource',
    'HardwareProfile',
    'Disk',
    'StorageProfile',
    'OSProfile',
    'IpAddress',
    'NetworkProfile',
    'HanaInstance',
    'Display',
    'Operation',
    'ErrorResponse', 'ErrorResponseException',
    'Tags',
    'MonitoringDetails',
    'OperationPaged',
    'HanaInstancePaged',
    'HanaHardwareTypeNamesEnum',
    'HanaInstanceSizeNamesEnum',
    'HanaInstancePowerStateEnum',
    'HanaProvisioningStatesEnum',
]
