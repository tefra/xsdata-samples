from dataclasses import dataclass, field
from typing import Optional
from datexii.models.eu.datexii.v2.extension_type import ExtensionType
from datexii.models.eu.datexii.v2.network_management import NetworkManagement
from datexii.models.eu.datexii.v2.speed_management_type_enum import (
    SpeedManagementTypeEnum,
)

__NAMESPACE__ = "http://datex2.eu/schema/2/2_0"


@dataclass
class SpeedManagement(NetworkManagement):
    """
    Speed management action that is instigated by the network/road operator.

    :ivar speed_management_type: Type of speed management action
        instigated by operator.
    :ivar temporary_speed_limit: Temporary limit defining the maximum
        advisory or mandatory speed of vehicles.
    :ivar speed_management_extension:
    """

    speed_management_type: Optional[SpeedManagementTypeEnum] = field(
        default=None,
        metadata={
            "name": "speedManagementType",
            "type": "Element",
            "namespace": "http://datex2.eu/schema/2/2_0",
        },
    )
    temporary_speed_limit: Optional[float] = field(
        default=None,
        metadata={
            "name": "temporarySpeedLimit",
            "type": "Element",
            "namespace": "http://datex2.eu/schema/2/2_0",
        },
    )
    speed_management_extension: Optional[ExtensionType] = field(
        default=None,
        metadata={
            "name": "speedManagementExtension",
            "type": "Element",
            "namespace": "http://datex2.eu/schema/2/2_0",
        },
    )
