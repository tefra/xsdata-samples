from dataclasses import dataclass, field

from datexii.models.eu.datexii.v2.extension_type import ExtensionType
from datexii.models.eu.datexii.v2.parking_equipment_or_service_facility import (
    ParkingEquipmentOrServiceFacility,
)
from datexii.models.eu.datexii.v2.service_facility_type_enum import (
    ServiceFacilityTypeEnum,
)

__NAMESPACE__ = "http://datex2.eu/schema/2/2_0"


@dataclass
class ServiceFacility(ParkingEquipmentOrServiceFacility):
    """
    One type of service facility that is available on the parking site or
    located next to it.

    You can specify the number of this service facility type (e.g. 5
    restaurants) as well as the number of subitems (e.g. 200 restaurant
    places).

    :ivar service_facility_type: One type of service, that is available
        on the parking site.
    :ivar number_of_subitems: The quantity of sub items to this service
        facility type, e.g. the total number of restaurant places or
        fuel dispensers etc.
    :ivar distance_from_parking_site: If the service facility is not
        located on the parking site itself, its distance can be
        specified here in metres.
    :ivar service_facility_extension:
    """

    service_facility_type: ServiceFacilityTypeEnum | None = field(
        default=None,
        metadata={
            "name": "serviceFacilityType",
            "type": "Element",
            "namespace": "http://datex2.eu/schema/2/2_0",
            "required": True,
        },
    )
    number_of_subitems: int | None = field(
        default=None,
        metadata={
            "name": "numberOfSubitems",
            "type": "Element",
            "namespace": "http://datex2.eu/schema/2/2_0",
        },
    )
    distance_from_parking_site: int | None = field(
        default=None,
        metadata={
            "name": "distanceFromParkingSite",
            "type": "Element",
            "namespace": "http://datex2.eu/schema/2/2_0",
        },
    )
    service_facility_extension: ExtensionType | None = field(
        default=None,
        metadata={
            "name": "serviceFacilityExtension",
            "type": "Element",
            "namespace": "http://datex2.eu/schema/2/2_0",
        },
    )
