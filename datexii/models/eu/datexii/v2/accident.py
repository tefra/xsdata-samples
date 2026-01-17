from dataclasses import dataclass, field
from typing import Optional

from datexii.models.eu.datexii.v2.accident_cause_enum import AccidentCauseEnum
from datexii.models.eu.datexii.v2.accident_type_enum import AccidentTypeEnum
from datexii.models.eu.datexii.v2.extension_type import ExtensionType
from datexii.models.eu.datexii.v2.group_of_people_involved import (
    GroupOfPeopleInvolved,
)
from datexii.models.eu.datexii.v2.group_of_vehicles_involved import (
    GroupOfVehiclesInvolved,
)
from datexii.models.eu.datexii.v2.traffic_element import TrafficElement
from datexii.models.eu.datexii.v2.vehicle import Vehicle

__NAMESPACE__ = "http://datex2.eu/schema/2/2_0"


@dataclass
class Accident(TrafficElement):
    """
    Accidents are events where one or more vehicles are involved in
    collisions or in leaving the roadway.

    These include collisions between vehicles or with other road users or
    obstacles.

    :ivar accident_cause: A descriptor indicating the most significant
        factor causing an accident.
    :ivar accident_type: A characterization of the nature of the
        accident.
    :ivar total_number_of_people_involved: The total number of people
        that are involved.
    :ivar total_number_of_vehicles_involved: The total number of
        vehicles that are involved.
    :ivar vehicle_involved: The vehicle involved in the accident.
    :ivar group_of_vehicles_involved:
    :ivar group_of_people_involved:
    :ivar accident_extension:
    """

    accident_cause: Optional[AccidentCauseEnum] = field(
        default=None,
        metadata={
            "name": "accidentCause",
            "type": "Element",
            "namespace": "http://datex2.eu/schema/2/2_0",
        },
    )
    accident_type: list[AccidentTypeEnum] = field(
        default_factory=list,
        metadata={
            "name": "accidentType",
            "type": "Element",
            "namespace": "http://datex2.eu/schema/2/2_0",
            "min_occurs": 1,
        },
    )
    total_number_of_people_involved: Optional[int] = field(
        default=None,
        metadata={
            "name": "totalNumberOfPeopleInvolved",
            "type": "Element",
            "namespace": "http://datex2.eu/schema/2/2_0",
        },
    )
    total_number_of_vehicles_involved: Optional[int] = field(
        default=None,
        metadata={
            "name": "totalNumberOfVehiclesInvolved",
            "type": "Element",
            "namespace": "http://datex2.eu/schema/2/2_0",
        },
    )
    vehicle_involved: list[Vehicle] = field(
        default_factory=list,
        metadata={
            "name": "vehicleInvolved",
            "type": "Element",
            "namespace": "http://datex2.eu/schema/2/2_0",
        },
    )
    group_of_vehicles_involved: list[GroupOfVehiclesInvolved] = field(
        default_factory=list,
        metadata={
            "name": "groupOfVehiclesInvolved",
            "type": "Element",
            "namespace": "http://datex2.eu/schema/2/2_0",
        },
    )
    group_of_people_involved: list[GroupOfPeopleInvolved] = field(
        default_factory=list,
        metadata={
            "name": "groupOfPeopleInvolved",
            "type": "Element",
            "namespace": "http://datex2.eu/schema/2/2_0",
        },
    )
    accident_extension: Optional[ExtensionType] = field(
        default=None,
        metadata={
            "name": "accidentExtension",
            "type": "Element",
            "namespace": "http://datex2.eu/schema/2/2_0",
        },
    )
