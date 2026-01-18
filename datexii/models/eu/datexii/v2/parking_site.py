from __future__ import annotations

from dataclasses import dataclass, field

from datexii.models.eu.datexii.v2.contact import Contact
from datexii.models.eu.datexii.v2.extension_type import ExtensionType
from datexii.models.eu.datexii.v2.opening_times import OpeningTimes
from datexii.models.eu.datexii.v2.parking_access import ParkingAccess
from datexii.models.eu.datexii.v2.parking_layout_enum import ParkingLayoutEnum
from datexii.models.eu.datexii.v2.parking_record import ParkingRecord
from datexii.models.eu.datexii.v2.parking_site_scenario_index_parking_usage_scenario import (
    ParkingSiteScenarioIndexParkingUsageScenario,
)
from datexii.models.eu.datexii.v2.parking_standards_and_security import (
    ParkingStandardsAndSecurity,
)
from datexii.models.eu.datexii.v2.reservation_type_enum import (
    ReservationTypeEnum,
)

__NAMESPACE__ = "http://datex2.eu/schema/2/2_0"


@dataclass
class ParkingSite(ParkingRecord):
    """
    A record containing static details of a parking site.

    Must be specialised as an 'Urban-' or 'InterUrbanParkingSite' or a
    'SpecialLocationParkingSite'.

    :ivar parking_reservation: Indication of whether a parking
        reservation service is available and/or mandatory.
    :ivar parking_layout: Layout of the parking site.
    :ivar highest_floor: Highest floor of the parking site. It is
        possible to have negative values here in case it is underground
        only. Must be higher or equal than 'lowestFloor'.
    :ivar lowest_floor: Lowest floor of the parking site. Positive
        values may apply in case it is over ground only. Must be lower
        or equal than 'highestFloor'.
    :ivar temporary_parking: Indicates that the parking site is on a
        temporary basis. It might close permanently within short notice
        or might only be partial equipped. The physical parking
        possibilities might be provisional, too.
    :ivar parking_site_address: Information about the parking site
        itself (address etc.). The 'GroupOfLocations' association must
        not be used for this role.
    :ivar reservation_service: Reservation service (for end users). It
        is recommended to give URL and telephone.
    :ivar parking_usage_scenario:
    :ivar opening_times:
    :ivar parking_access: An exit from the parking facility onto the
        road network from any parking space unless separate exits are
        specified for assigned parking spaces, in which case this is an
        exit from only the principal parking spaces.
    :ivar parking_standards_and_security:
    :ivar parking_site_extension:
    """

    parking_reservation: None | ReservationTypeEnum = field(
        default=None,
        metadata={
            "name": "parkingReservation",
            "type": "Element",
            "namespace": "http://datex2.eu/schema/2/2_0",
        },
    )
    parking_layout: list[ParkingLayoutEnum] = field(
        default_factory=list,
        metadata={
            "name": "parkingLayout",
            "type": "Element",
            "namespace": "http://datex2.eu/schema/2/2_0",
        },
    )
    highest_floor: None | int = field(
        default=None,
        metadata={
            "name": "highestFloor",
            "type": "Element",
            "namespace": "http://datex2.eu/schema/2/2_0",
        },
    )
    lowest_floor: None | int = field(
        default=None,
        metadata={
            "name": "lowestFloor",
            "type": "Element",
            "namespace": "http://datex2.eu/schema/2/2_0",
        },
    )
    temporary_parking: None | bool = field(
        default=None,
        metadata={
            "name": "temporaryParking",
            "type": "Element",
            "namespace": "http://datex2.eu/schema/2/2_0",
        },
    )
    parking_site_address: list[Contact] = field(
        default_factory=list,
        metadata={
            "name": "parkingSiteAddress",
            "type": "Element",
            "namespace": "http://datex2.eu/schema/2/2_0",
        },
    )
    reservation_service: list[Contact] = field(
        default_factory=list,
        metadata={
            "name": "reservationService",
            "type": "Element",
            "namespace": "http://datex2.eu/schema/2/2_0",
        },
    )
    parking_usage_scenario: list[
        ParkingSiteScenarioIndexParkingUsageScenario
    ] = field(
        default_factory=list,
        metadata={
            "name": "parkingUsageScenario",
            "type": "Element",
            "namespace": "http://datex2.eu/schema/2/2_0",
        },
    )
    opening_times: None | OpeningTimes = field(
        default=None,
        metadata={
            "name": "openingTimes",
            "type": "Element",
            "namespace": "http://datex2.eu/schema/2/2_0",
        },
    )
    parking_access: list[ParkingAccess] = field(
        default_factory=list,
        metadata={
            "name": "parkingAccess",
            "type": "Element",
            "namespace": "http://datex2.eu/schema/2/2_0",
        },
    )
    parking_standards_and_security: None | ParkingStandardsAndSecurity = field(
        default=None,
        metadata={
            "name": "parkingStandardsAndSecurity",
            "type": "Element",
            "namespace": "http://datex2.eu/schema/2/2_0",
        },
    )
    parking_site_extension: None | ExtensionType = field(
        default=None,
        metadata={
            "name": "parkingSiteExtension",
            "type": "Element",
            "namespace": "http://datex2.eu/schema/2/2_0",
        },
    )
