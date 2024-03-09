from dataclasses import dataclass, field
from typing import List, Optional

from .accesses_rel_structure import AccessesRelStructure
from .multilingual_string import MultilingualString
from .navigation_paths_rel_structure import NavigationPathsRelStructure
from .parking_areas_rel_structure import ParkingAreasRelStructure
from .parking_entrances_for_vehicles_rel_structure import (
    ParkingEntrancesForVehiclesRelStructure,
)
from .parking_layout_enumeration import ParkingLayoutEnumeration
from .parking_payment_process_enumeration import (
    ParkingPaymentProcessEnumeration,
)
from .parking_properties_rel_structure import ParkingPropertiesRelStructure
from .parking_reservation_enumeration import ParkingReservationEnumeration
from .parking_type_enumeration import ParkingTypeEnumeration
from .parking_vehicle_enumeration import ParkingVehicleEnumeration
from .path_junctions_rel_structure import PathJunctionsRelStructure
from .payment_by_mobile_structure import PaymentByMobileStructure
from .payment_method_enumeration import PaymentMethodEnumeration
from .site_path_links_rel_structure import SitePathLinksRelStructure
from .site_version_structure import SiteVersionStructure
from .transport_type_refs_rel_structure import TransportTypeRefsRelStructure
from .type_of_parking_ref import TypeOfParkingRef
from .type_of_payment_method_refs_rel_structure import (
    TypeOfPaymentMethodRefsRelStructure,
)

__NAMESPACE__ = "http://www.netex.org.uk/netex"


@dataclass
class ParkingVersionStructure(SiteVersionStructure):
    class Meta:
        name = "Parking_VersionStructure"

    path_links: Optional[SitePathLinksRelStructure] = field(
        default=None,
        metadata={
            "name": "pathLinks",
            "type": "Element",
            "namespace": "http://www.netex.org.uk/netex",
        },
    )
    path_junctions: Optional[PathJunctionsRelStructure] = field(
        default=None,
        metadata={
            "name": "pathJunctions",
            "type": "Element",
            "namespace": "http://www.netex.org.uk/netex",
        },
    )
    accesses: Optional[AccessesRelStructure] = field(
        default=None,
        metadata={
            "type": "Element",
            "namespace": "http://www.netex.org.uk/netex",
        },
    )
    navigation_paths: Optional[NavigationPathsRelStructure] = field(
        default=None,
        metadata={
            "name": "navigationPaths",
            "type": "Element",
            "namespace": "http://www.netex.org.uk/netex",
        },
    )
    public_code: Optional[str] = field(
        default=None,
        metadata={
            "name": "PublicCode",
            "type": "Element",
            "namespace": "http://www.netex.org.uk/netex",
        },
    )
    label: Optional[MultilingualString] = field(
        default=None,
        metadata={
            "name": "Label",
            "type": "Element",
            "namespace": "http://www.netex.org.uk/netex",
        },
    )
    parking_type: Optional[ParkingTypeEnumeration] = field(
        default=None,
        metadata={
            "name": "ParkingType",
            "type": "Element",
            "namespace": "http://www.netex.org.uk/netex",
        },
    )
    type_of_parking_ref: Optional[TypeOfParkingRef] = field(
        default=None,
        metadata={
            "name": "TypeOfParkingRef",
            "type": "Element",
            "namespace": "http://www.netex.org.uk/netex",
        },
    )
    parking_vehicle_types: List[ParkingVehicleEnumeration] = field(
        default_factory=list,
        metadata={
            "name": "ParkingVehicleTypes",
            "type": "Element",
            "namespace": "http://www.netex.org.uk/netex",
            "tokens": True,
        },
    )
    vehicle_types: Optional[TransportTypeRefsRelStructure] = field(
        default=None,
        metadata={
            "name": "vehicleTypes",
            "type": "Element",
            "namespace": "http://www.netex.org.uk/netex",
        },
    )
    parking_layout: Optional[ParkingLayoutEnumeration] = field(
        default=None,
        metadata={
            "name": "ParkingLayout",
            "type": "Element",
            "namespace": "http://www.netex.org.uk/netex",
        },
    )
    number_of_parking_levels: Optional[int] = field(
        default=None,
        metadata={
            "name": "NumberOfParkingLevels",
            "type": "Element",
            "namespace": "http://www.netex.org.uk/netex",
        },
    )
    principal_capacity: Optional[int] = field(
        default=None,
        metadata={
            "name": "PrincipalCapacity",
            "type": "Element",
            "namespace": "http://www.netex.org.uk/netex",
        },
    )
    total_capacity: Optional[int] = field(
        default=None,
        metadata={
            "name": "TotalCapacity",
            "type": "Element",
            "namespace": "http://www.netex.org.uk/netex",
        },
    )
    overnight_parking_permitted: Optional[bool] = field(
        default=None,
        metadata={
            "name": "OvernightParkingPermitted",
            "type": "Element",
            "namespace": "http://www.netex.org.uk/netex",
        },
    )
    prohibited_for_hazardous_materials: Optional[bool] = field(
        default=None,
        metadata={
            "name": "ProhibitedForHazardousMaterials",
            "type": "Element",
            "namespace": "http://www.netex.org.uk/netex",
        },
    )
    recharging_available: Optional[bool] = field(
        default=None,
        metadata={
            "name": "RechargingAvailable",
            "type": "Element",
            "namespace": "http://www.netex.org.uk/netex",
        },
    )
    secure: Optional[bool] = field(
        default=None,
        metadata={
            "name": "Secure",
            "type": "Element",
            "namespace": "http://www.netex.org.uk/netex",
        },
    )
    real_time_occupancy_available: Optional[bool] = field(
        default=None,
        metadata={
            "name": "RealTimeOccupancyAvailable",
            "type": "Element",
            "namespace": "http://www.netex.org.uk/netex",
        },
    )
    parking_payment_process: List[ParkingPaymentProcessEnumeration] = field(
        default_factory=list,
        metadata={
            "name": "ParkingPaymentProcess",
            "type": "Element",
            "namespace": "http://www.netex.org.uk/netex",
            "tokens": True,
        },
    )
    payment_methods: List[PaymentMethodEnumeration] = field(
        default_factory=list,
        metadata={
            "name": "PaymentMethods",
            "type": "Element",
            "namespace": "http://www.netex.org.uk/netex",
            "tokens": True,
        },
    )
    types_of_payment_method: Optional[TypeOfPaymentMethodRefsRelStructure] = (
        field(
            default=None,
            metadata={
                "name": "typesOfPaymentMethod",
                "type": "Element",
                "namespace": "http://www.netex.org.uk/netex",
            },
        )
    )
    default_currency: Optional[str] = field(
        default=None,
        metadata={
            "name": "DefaultCurrency",
            "type": "Element",
            "namespace": "http://www.netex.org.uk/netex",
            "min_length": 3,
            "max_length": 3,
            "pattern": r"[A-Z][A-Z][A-Z]",
        },
    )
    currencies_accepted: List[str] = field(
        default_factory=list,
        metadata={
            "name": "CurrenciesAccepted",
            "type": "Element",
            "namespace": "http://www.netex.org.uk/netex",
            "min_length": 3,
            "max_length": 3,
            "pattern": r"[A-Z][A-Z][A-Z]",
            "tokens": True,
        },
    )
    cards_accepted: List[str] = field(
        default_factory=list,
        metadata={
            "name": "CardsAccepted",
            "type": "Element",
            "namespace": "http://www.netex.org.uk/netex",
            "tokens": True,
        },
    )
    parking_reservation: Optional[ParkingReservationEnumeration] = field(
        default=None,
        metadata={
            "name": "ParkingReservation",
            "type": "Element",
            "namespace": "http://www.netex.org.uk/netex",
        },
    )
    booking_url: Optional[str] = field(
        default=None,
        metadata={
            "name": "BookingUrl",
            "type": "Element",
            "namespace": "http://www.netex.org.uk/netex",
        },
    )
    payment_by_mobile: Optional[PaymentByMobileStructure] = field(
        default=None,
        metadata={
            "name": "PaymentByMobile",
            "type": "Element",
            "namespace": "http://www.netex.org.uk/netex",
        },
    )
    free_parking_out_of_hours: Optional[bool] = field(
        default=None,
        metadata={
            "name": "FreeParkingOutOfHours",
            "type": "Element",
            "namespace": "http://www.netex.org.uk/netex",
        },
    )
    parking_properties: Optional[ParkingPropertiesRelStructure] = field(
        default=None,
        metadata={
            "name": "parkingProperties",
            "type": "Element",
            "namespace": "http://www.netex.org.uk/netex",
        },
    )
    parking_areas: Optional[ParkingAreasRelStructure] = field(
        default=None,
        metadata={
            "name": "parkingAreas",
            "type": "Element",
            "namespace": "http://www.netex.org.uk/netex",
        },
    )
    vehicle_entrances: Optional[ParkingEntrancesForVehiclesRelStructure] = (
        field(
            default=None,
            metadata={
                "name": "vehicleEntrances",
                "type": "Element",
                "namespace": "http://www.netex.org.uk/netex",
            },
        )
    )
