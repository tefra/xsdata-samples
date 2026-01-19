from __future__ import annotations

from collections.abc import Sequence
from dataclasses import dataclass, field

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


@dataclass(kw_only=True)
class ParkingVersionStructure(SiteVersionStructure):
    class Meta:
        name = "Parking_VersionStructure"

    path_links: None | SitePathLinksRelStructure = field(
        default=None,
        metadata={
            "name": "pathLinks",
            "type": "Element",
            "namespace": "http://www.netex.org.uk/netex",
        },
    )
    path_junctions: None | PathJunctionsRelStructure = field(
        default=None,
        metadata={
            "name": "pathJunctions",
            "type": "Element",
            "namespace": "http://www.netex.org.uk/netex",
        },
    )
    accesses: None | AccessesRelStructure = field(
        default=None,
        metadata={
            "type": "Element",
            "namespace": "http://www.netex.org.uk/netex",
        },
    )
    navigation_paths: None | NavigationPathsRelStructure = field(
        default=None,
        metadata={
            "name": "navigationPaths",
            "type": "Element",
            "namespace": "http://www.netex.org.uk/netex",
        },
    )
    public_code: None | str = field(
        default=None,
        metadata={
            "name": "PublicCode",
            "type": "Element",
            "namespace": "http://www.netex.org.uk/netex",
        },
    )
    label: None | MultilingualString = field(
        default=None,
        metadata={
            "name": "Label",
            "type": "Element",
            "namespace": "http://www.netex.org.uk/netex",
        },
    )
    parking_type: None | ParkingTypeEnumeration = field(
        default=None,
        metadata={
            "name": "ParkingType",
            "type": "Element",
            "namespace": "http://www.netex.org.uk/netex",
        },
    )
    type_of_parking_ref: None | TypeOfParkingRef = field(
        default=None,
        metadata={
            "name": "TypeOfParkingRef",
            "type": "Element",
            "namespace": "http://www.netex.org.uk/netex",
        },
    )
    parking_vehicle_types: Sequence[ParkingVehicleEnumeration] = field(
        default_factory=list,
        metadata={
            "name": "ParkingVehicleTypes",
            "type": "Element",
            "namespace": "http://www.netex.org.uk/netex",
            "tokens": True,
        },
    )
    vehicle_types: None | TransportTypeRefsRelStructure = field(
        default=None,
        metadata={
            "name": "vehicleTypes",
            "type": "Element",
            "namespace": "http://www.netex.org.uk/netex",
        },
    )
    parking_layout: None | ParkingLayoutEnumeration = field(
        default=None,
        metadata={
            "name": "ParkingLayout",
            "type": "Element",
            "namespace": "http://www.netex.org.uk/netex",
        },
    )
    number_of_parking_levels: None | int = field(
        default=None,
        metadata={
            "name": "NumberOfParkingLevels",
            "type": "Element",
            "namespace": "http://www.netex.org.uk/netex",
        },
    )
    principal_capacity: None | int = field(
        default=None,
        metadata={
            "name": "PrincipalCapacity",
            "type": "Element",
            "namespace": "http://www.netex.org.uk/netex",
        },
    )
    total_capacity: None | int = field(
        default=None,
        metadata={
            "name": "TotalCapacity",
            "type": "Element",
            "namespace": "http://www.netex.org.uk/netex",
        },
    )
    overnight_parking_permitted: None | bool = field(
        default=None,
        metadata={
            "name": "OvernightParkingPermitted",
            "type": "Element",
            "namespace": "http://www.netex.org.uk/netex",
        },
    )
    prohibited_for_hazardous_materials: None | bool = field(
        default=None,
        metadata={
            "name": "ProhibitedForHazardousMaterials",
            "type": "Element",
            "namespace": "http://www.netex.org.uk/netex",
        },
    )
    recharging_available: None | bool = field(
        default=None,
        metadata={
            "name": "RechargingAvailable",
            "type": "Element",
            "namespace": "http://www.netex.org.uk/netex",
        },
    )
    secure: None | bool = field(
        default=None,
        metadata={
            "name": "Secure",
            "type": "Element",
            "namespace": "http://www.netex.org.uk/netex",
        },
    )
    real_time_occupancy_available: None | bool = field(
        default=None,
        metadata={
            "name": "RealTimeOccupancyAvailable",
            "type": "Element",
            "namespace": "http://www.netex.org.uk/netex",
        },
    )
    parking_payment_process: Sequence[ParkingPaymentProcessEnumeration] = (
        field(
            default_factory=list,
            metadata={
                "name": "ParkingPaymentProcess",
                "type": "Element",
                "namespace": "http://www.netex.org.uk/netex",
                "tokens": True,
            },
        )
    )
    payment_methods: Sequence[PaymentMethodEnumeration] = field(
        default_factory=list,
        metadata={
            "name": "PaymentMethods",
            "type": "Element",
            "namespace": "http://www.netex.org.uk/netex",
            "tokens": True,
        },
    )
    types_of_payment_method: None | TypeOfPaymentMethodRefsRelStructure = (
        field(
            default=None,
            metadata={
                "name": "typesOfPaymentMethod",
                "type": "Element",
                "namespace": "http://www.netex.org.uk/netex",
            },
        )
    )
    default_currency: None | str = field(
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
    currencies_accepted: Sequence[str] = field(
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
    cards_accepted: Sequence[str] = field(
        default_factory=list,
        metadata={
            "name": "CardsAccepted",
            "type": "Element",
            "namespace": "http://www.netex.org.uk/netex",
            "tokens": True,
        },
    )
    parking_reservation: None | ParkingReservationEnumeration = field(
        default=None,
        metadata={
            "name": "ParkingReservation",
            "type": "Element",
            "namespace": "http://www.netex.org.uk/netex",
        },
    )
    booking_url: None | str = field(
        default=None,
        metadata={
            "name": "BookingUrl",
            "type": "Element",
            "namespace": "http://www.netex.org.uk/netex",
        },
    )
    payment_by_mobile: None | PaymentByMobileStructure = field(
        default=None,
        metadata={
            "name": "PaymentByMobile",
            "type": "Element",
            "namespace": "http://www.netex.org.uk/netex",
        },
    )
    free_parking_out_of_hours: None | bool = field(
        default=None,
        metadata={
            "name": "FreeParkingOutOfHours",
            "type": "Element",
            "namespace": "http://www.netex.org.uk/netex",
        },
    )
    parking_properties: None | ParkingPropertiesRelStructure = field(
        default=None,
        metadata={
            "name": "parkingProperties",
            "type": "Element",
            "namespace": "http://www.netex.org.uk/netex",
        },
    )
    parking_areas: None | ParkingAreasRelStructure = field(
        default=None,
        metadata={
            "name": "parkingAreas",
            "type": "Element",
            "namespace": "http://www.netex.org.uk/netex",
        },
    )
    vehicle_entrances: None | ParkingEntrancesForVehiclesRelStructure = field(
        default=None,
        metadata={
            "name": "vehicleEntrances",
            "type": "Element",
            "namespace": "http://www.netex.org.uk/netex",
        },
    )
