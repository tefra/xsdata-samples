from dataclasses import dataclass, field
from typing import Optional

from datexii.models.eu.datexii.v2.extension_type import ExtensionType
from datexii.models.eu.datexii.v2.operation_status_enum import (
    OperationStatusEnum,
)

__NAMESPACE__ = "http://datex2.eu/schema/2/2_0"


@dataclass
class ParkingUsageScenarioStatus:
    """
    The current status for this parking usage scenario.

    :ivar usage_scenario_operation_status: The current status for this
        parking usage scenario.
    :ivar parking_usage_scenario_status_extension:
    """

    usage_scenario_operation_status: OperationStatusEnum | None = field(
        default=None,
        metadata={
            "name": "usageScenarioOperationStatus",
            "type": "Element",
            "namespace": "http://datex2.eu/schema/2/2_0",
            "required": True,
        },
    )
    parking_usage_scenario_status_extension: ExtensionType | None = field(
        default=None,
        metadata={
            "name": "parkingUsageScenarioStatusExtension",
            "type": "Element",
            "namespace": "http://datex2.eu/schema/2/2_0",
        },
    )
