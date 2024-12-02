from dataclasses import dataclass, field
from typing import Optional

from datexii.models.eu.datexii.v2.extension_type import ExtensionType
from datexii.models.eu.datexii.v2.overall_period import OverallPeriod
from datexii.models.eu.datexii.v2.parking_usage_scenario_enum import (
    ParkingUsageScenarioEnum,
)
from datexii.models.eu.datexii.v2.public_event_type2_enum import (
    PublicEventType2Enum,
)
from datexii.models.eu.datexii.v2.public_event_type_enum import (
    PublicEventTypeEnum,
)
from datexii.models.eu.datexii.v2.truck_parking_dynamic_management_enum import (
    TruckParkingDynamicManagementEnum,
)

__NAMESPACE__ = "http://datex2.eu/schema/2/2_0"


@dataclass
class ParkingUsageScenario:
    """A special type of usage available for the parking site or the group of
    parking spaces.

    In the 'ParkingStatusPublication', the operation type (in operation
    or not) can be defined.

    :ivar parking_usage_scenario: A special type of usage available for
        the parking site or a group of parking spaces. In the
        'ParkingStatusPublication', the operation type (in operation or
        not) can be defined.
    :ivar truck_parking_dynamic_management: Two modes for parking
        lorries in a efficient way according to their departure times.
        May only be used for parking scenario 'truckParking'.
    :ivar event_parking_type: Parking associated with an event. May only
        be used for parking scenario 'eventParking'.
    :ivar event_parking_type2: Parking associated with an event. May
        only be used for parking scenario 'eventParking'.
    :ivar scenario_availability:
    :ivar parking_usage_scenario_extension:
    """

    parking_usage_scenario: Optional[ParkingUsageScenarioEnum] = field(
        default=None,
        metadata={
            "name": "parkingUsageScenario",
            "type": "Element",
            "namespace": "http://datex2.eu/schema/2/2_0",
            "required": True,
        },
    )
    truck_parking_dynamic_management: list[
        TruckParkingDynamicManagementEnum
    ] = field(
        default_factory=list,
        metadata={
            "name": "truckParkingDynamicManagement",
            "type": "Element",
            "namespace": "http://datex2.eu/schema/2/2_0",
        },
    )
    event_parking_type: Optional[PublicEventTypeEnum] = field(
        default=None,
        metadata={
            "name": "eventParkingType",
            "type": "Element",
            "namespace": "http://datex2.eu/schema/2/2_0",
        },
    )
    event_parking_type2: Optional[PublicEventType2Enum] = field(
        default=None,
        metadata={
            "name": "eventParkingType2",
            "type": "Element",
            "namespace": "http://datex2.eu/schema/2/2_0",
        },
    )
    scenario_availability: Optional[OverallPeriod] = field(
        default=None,
        metadata={
            "name": "scenarioAvailability",
            "type": "Element",
            "namespace": "http://datex2.eu/schema/2/2_0",
        },
    )
    parking_usage_scenario_extension: Optional[ExtensionType] = field(
        default=None,
        metadata={
            "name": "parkingUsageScenarioExtension",
            "type": "Element",
            "namespace": "http://datex2.eu/schema/2/2_0",
        },
    )
