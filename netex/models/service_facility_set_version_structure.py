from dataclasses import dataclass, field
from typing import Optional

from .accommodation_access_list import AccommodationAccessList
from .accommodation_facility_list import AccommodationFacilityList
from .accommodations_rel_structure import AccommodationsRelStructure
from .boarding_permission import BoardingPermission
from .booking_process_facility_list import BookingProcessFacilityList
from .couchette_facility_list import CouchetteFacilityList
from .facility_set_version_structure import FacilitySetVersionStructure
from .group_booking_facility import GroupBookingFacility
from .luggage_carriage_facility_list import LuggageCarriageFacilityList
from .onboard_stays_rel_structure import OnboardStaysRelStructure
from .service_reservation_facility_list import ServiceReservationFacilityList
from .uic_product_characteristic_list import UicProductCharacteristicList
from .uic_train_rate import UicTrainRate
from .vehicle_access_facility_list import VehicleAccessFacilityList

__NAMESPACE__ = "http://www.netex.org.uk/netex"


@dataclass
class ServiceFacilitySetVersionStructure(FacilitySetVersionStructure):
    class Meta:
        name = "ServiceFacilitySet_VersionStructure"

    vehicle_access_facility_list: VehicleAccessFacilityList | None = field(
        default=None,
        metadata={
            "name": "VehicleAccessFacilityList",
            "type": "Element",
            "namespace": "http://www.netex.org.uk/netex",
        },
    )
    accommodation_access_list: AccommodationAccessList | None = field(
        default=None,
        metadata={
            "name": "AccommodationAccessList",
            "type": "Element",
            "namespace": "http://www.netex.org.uk/netex",
        },
    )
    accommodation_facility_list: AccommodationFacilityList | None = field(
        default=None,
        metadata={
            "name": "AccommodationFacilityList",
            "type": "Element",
            "namespace": "http://www.netex.org.uk/netex",
        },
    )
    boarding_permission: BoardingPermission | None = field(
        default=None,
        metadata={
            "name": "BoardingPermission",
            "type": "Element",
            "namespace": "http://www.netex.org.uk/netex",
        },
    )
    booking_process_facility_list: BookingProcessFacilityList | None = (
        field(
            default=None,
            metadata={
                "name": "BookingProcessFacilityList",
                "type": "Element",
                "namespace": "http://www.netex.org.uk/netex",
            },
        )
    )
    couchette_facility_list: CouchetteFacilityList | None = field(
        default=None,
        metadata={
            "name": "CouchetteFacilityList",
            "type": "Element",
            "namespace": "http://www.netex.org.uk/netex",
        },
    )
    group_booking_facility: GroupBookingFacility | None = field(
        default=None,
        metadata={
            "name": "GroupBookingFacility",
            "type": "Element",
            "namespace": "http://www.netex.org.uk/netex",
        },
    )
    luggage_carriage_facility_list: LuggageCarriageFacilityList | None = (
        field(
            default=None,
            metadata={
                "name": "LuggageCarriageFacilityList",
                "type": "Element",
                "namespace": "http://www.netex.org.uk/netex",
            },
        )
    )
    service_reservation_facility_list: ServiceReservationFacilityList | None = field(
        default=None,
        metadata={
            "name": "ServiceReservationFacilityList",
            "type": "Element",
            "namespace": "http://www.netex.org.uk/netex",
        },
    )
    uic_product_characteristic_list: UicProductCharacteristicList | None = (
        field(
            default=None,
            metadata={
                "name": "UicProductCharacteristicList",
                "type": "Element",
                "namespace": "http://www.netex.org.uk/netex",
            },
        )
    )
    uic_train_rate: UicTrainRate | None = field(
        default=None,
        metadata={
            "name": "UicTrainRate",
            "type": "Element",
            "namespace": "http://www.netex.org.uk/netex",
        },
    )
    accommodations: AccommodationsRelStructure | None = field(
        default=None,
        metadata={
            "type": "Element",
            "namespace": "http://www.netex.org.uk/netex",
        },
    )
    onboard_stays: OnboardStaysRelStructure | None = field(
        default=None,
        metadata={
            "name": "onboardStays",
            "type": "Element",
            "namespace": "http://www.netex.org.uk/netex",
        },
    )
