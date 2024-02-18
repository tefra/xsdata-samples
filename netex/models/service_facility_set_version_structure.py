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

    vehicle_access_facility_list: Optional[VehicleAccessFacilityList] = field(
        default=None,
        metadata={
            "name": "VehicleAccessFacilityList",
            "type": "Element",
            "namespace": "http://www.netex.org.uk/netex",
        },
    )
    accommodation_access_list: Optional[AccommodationAccessList] = field(
        default=None,
        metadata={
            "name": "AccommodationAccessList",
            "type": "Element",
            "namespace": "http://www.netex.org.uk/netex",
        },
    )
    accommodation_facility_list: Optional[AccommodationFacilityList] = field(
        default=None,
        metadata={
            "name": "AccommodationFacilityList",
            "type": "Element",
            "namespace": "http://www.netex.org.uk/netex",
        },
    )
    boarding_permission: Optional[BoardingPermission] = field(
        default=None,
        metadata={
            "name": "BoardingPermission",
            "type": "Element",
            "namespace": "http://www.netex.org.uk/netex",
        },
    )
    booking_process_facility_list: Optional[
        BookingProcessFacilityList
    ] = field(
        default=None,
        metadata={
            "name": "BookingProcessFacilityList",
            "type": "Element",
            "namespace": "http://www.netex.org.uk/netex",
        },
    )
    couchette_facility_list: Optional[CouchetteFacilityList] = field(
        default=None,
        metadata={
            "name": "CouchetteFacilityList",
            "type": "Element",
            "namespace": "http://www.netex.org.uk/netex",
        },
    )
    group_booking_facility: Optional[GroupBookingFacility] = field(
        default=None,
        metadata={
            "name": "GroupBookingFacility",
            "type": "Element",
            "namespace": "http://www.netex.org.uk/netex",
        },
    )
    luggage_carriage_facility_list: Optional[
        LuggageCarriageFacilityList
    ] = field(
        default=None,
        metadata={
            "name": "LuggageCarriageFacilityList",
            "type": "Element",
            "namespace": "http://www.netex.org.uk/netex",
        },
    )
    service_reservation_facility_list: Optional[
        ServiceReservationFacilityList
    ] = field(
        default=None,
        metadata={
            "name": "ServiceReservationFacilityList",
            "type": "Element",
            "namespace": "http://www.netex.org.uk/netex",
        },
    )
    uic_product_characteristic_list: Optional[
        UicProductCharacteristicList
    ] = field(
        default=None,
        metadata={
            "name": "UicProductCharacteristicList",
            "type": "Element",
            "namespace": "http://www.netex.org.uk/netex",
        },
    )
    uic_train_rate: Optional[UicTrainRate] = field(
        default=None,
        metadata={
            "name": "UicTrainRate",
            "type": "Element",
            "namespace": "http://www.netex.org.uk/netex",
        },
    )
    accommodations: Optional[AccommodationsRelStructure] = field(
        default=None,
        metadata={
            "type": "Element",
            "namespace": "http://www.netex.org.uk/netex",
        },
    )
    onboard_stays: Optional[OnboardStaysRelStructure] = field(
        default=None,
        metadata={
            "name": "onboardStays",
            "type": "Element",
            "namespace": "http://www.netex.org.uk/netex",
        },
    )
