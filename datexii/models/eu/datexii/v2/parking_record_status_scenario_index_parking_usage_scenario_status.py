from dataclasses import dataclass, field
from typing import Optional
from datexii.models.eu.datexii.v2.parking_usage_scenario_status import (
    ParkingUsageScenarioStatus,
)

__NAMESPACE__ = "http://datex2.eu/schema/2/2_0"


@dataclass
class ParkingRecordStatusScenarioIndexParkingUsageScenarioStatus:
    class Meta:
        name = "_ParkingRecordStatusScenarioIndexParkingUsageScenarioStatus"

    parking_usage_scenario_status: Optional[
        ParkingUsageScenarioStatus
    ] = field(
        default=None,
        metadata={
            "name": "parkingUsageScenarioStatus",
            "type": "Element",
            "namespace": "http://datex2.eu/schema/2/2_0",
            "required": True,
        },
    )
    scenario_index: Optional[int] = field(
        default=None,
        metadata={
            "name": "scenarioIndex",
            "type": "Attribute",
            "required": True,
        },
    )
