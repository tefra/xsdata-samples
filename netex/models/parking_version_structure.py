from collections.abc import Iterable
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


@dataclass
class ParkingVersionStructure(SiteVersionStructure):
    class Meta:
        name = "Parking_VersionStructure"

    path_links: SitePathLinksRelStructure | None = field(
        default=None,
        metadata={
            "name": "pathLinks",
            "type": "Element",
            "namespace": "http://www.netex.org.uk/netex",
        },
    )
    path_junctions: PathJunctionsRelStructure | None = field(
        default=None,
        metadata={
            "name": "pathJunctions",
            "type": "Element",
            "namespace": "http://www.netex.org.uk/netex",
        },
    )
    accesses: AccessesRelStructure | None = field(
        default=None,
        metadata={
            "type": "Element",
            "namespace": "http://www.netex.org.uk/netex",
        },
    )
    navigation_paths: NavigationPathsRelStructure | None = field(
        default=None,
        metadata={
            "name": "navigationPaths",
            "type": "Element",
            "namespace": "http://www.netex.org.uk/netex",
        },
    )
    public_code: str | None = field(
        default=None,
        metadata={
            "name": "PublicCode",
            "type": "Element",
            "namespace": "http://www.netex.org.uk/netex",
        },
    )
    label: MultilingualString | None = field(
        default=None,
        metadata={
            "name": "Label",
            "type": "Element",
            "namespace": "http://www.netex.org.uk/netex",
        },
    )
    parking_type: ParkingTypeEnumeration | None = field(
        default=None,
        metadata={
            "name": "ParkingType",
            "type": "Element",
            "namespace": "http://www.netex.org.uk/netex",
        },
    )
    type_of_parking_ref: TypeOfParkingRef | None = field(
        default=None,
        metadata={
            "name": "TypeOfParkingRef",
            "type": "Element",
            "namespace": "http://www.netex.org.uk/netex",
        },
    )
    parking_vehicle_types: Iterable[ParkingVehicleEnumeration] = field(
        default_factory=list,
        metadata={
            "name": "ParkingVehicleTypes",
            "type": "Element",
            "namespace": "http://www.netex.org.uk/netex",
            "tokens": True,
        },
    )
    vehicle_types: TransportTypeRefsRelStructure | None = field(
        default=None,
        metadata={
            "name": "vehicleTypes",
            "type": "Element",
            "namespace": "http://www.netex.org.uk/netex",
        },
    )
    parking_layout: ParkingLayoutEnumeration | None = field(
        default=None,
        metadata={
            "name": "ParkingLayout",
            "type": "Element",
            "namespace": "http://www.netex.org.uk/netex",
        },
    )
    number_of_parking_levels: int | None = field(
        default=None,
        metadata={
            "name": "NumberOfParkingLevels",
            "type": "Element",
            "namespace": "http://www.netex.org.uk/netex",
        },
    )
    principal_capacity: int | None = field(
        default=None,
        metadata={
            "name": "PrincipalCapacity",
            "type": "Element",
            "namespace": "http://www.netex.org.uk/netex",
        },
    )
    total_capacity: int | None = field(
        default=None,
        metadata={
            "name": "TotalCapacity",
            "type": "Element",
            "namespace": "http://www.netex.org.uk/netex",
        },
    )
    overnight_parking_permitted: bool | None = field(
        default=None,
        metadata={
            "name": "OvernightParkingPermitted",
            "type": "Element",
            "namespace": "http://www.netex.org.uk/netex",
        },
    )
    prohibited_for_hazardous_materials: bool | None = field(
        default=None,
        metadata={
            "name": "ProhibitedForHazardousMaterials",
            "type": "Element",
            "namespace": "http://www.netex.org.uk/netex",
        },
    )
    recharging_available: bool | None = field(
        default=None,
        metadata={
            "name": "RechargingAvailable",
            "type": "Element",
            "namespace": "http://www.netex.org.uk/netex",
        },
    )
    secure: bool | None = field(
        default=None,
        metadata={
            "name": "Secure",
            "type": "Element",
            "namespace": "http://www.netex.org.uk/netex",
        },
    )
    real_time_occupancy_available: bool | None = field(
        default=None,
        metadata={
            "name": "RealTimeOccupancyAvailable",
            "type": "Element",
            "namespace": "http://www.netex.org.uk/netex",
        },
    )
    parking_payment_process: Iterable[ParkingPaymentProcessEnumeration] = (
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
    payment_methods: Iterable[PaymentMethodEnumeration] = field(
        default_factory=list,
        metadata={
            "name": "PaymentMethods",
            "type": "Element",
            "namespace": "http://www.netex.org.uk/netex",
            "tokens": True,
        },
    )
    types_of_payment_method: TypeOfPaymentMethodRefsRelStructure | None = (
        field(
            default=None,
            metadata={
                "name": "typesOfPaymentMethod",
                "type": "Element",
                "namespace": "http://www.netex.org.uk/netex",
            },
        )
    )
    default_currency: str | None = field(
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
    currencies_accepted: Iterable[str] = field(
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
    cards_accepted: Iterable[str] = field(
        default_factory=list,
        metadata={
            "name": "CardsAccepted",
            "type": "Element",
            "namespace": "http://www.netex.org.uk/netex",
            "tokens": True,
        },
    )
    parking_reservation: ParkingReservationEnumeration | None = field(
        default=None,
        metadata={
            "name": "ParkingReservation",
            "type": "Element",
            "namespace": "http://www.netex.org.uk/netex",
        },
    )
    booking_url: str | None = field(
        default=None,
        metadata={
            "name": "BookingUrl",
            "type": "Element",
            "namespace": "http://www.netex.org.uk/netex",
        },
    )
    payment_by_mobile: PaymentByMobileStructure | None = field(
        default=None,
        metadata={
            "name": "PaymentByMobile",
            "type": "Element",
            "namespace": "http://www.netex.org.uk/netex",
        },
    )
    free_parking_out_of_hours: bool | None = field(
        default=None,
        metadata={
            "name": "FreeParkingOutOfHours",
            "type": "Element",
            "namespace": "http://www.netex.org.uk/netex",
        },
    )
    parking_properties: ParkingPropertiesRelStructure | None = field(
        default=None,
        metadata={
            "name": "parkingProperties",
            "type": "Element",
            "namespace": "http://www.netex.org.uk/netex",
        },
    )
    parking_areas: ParkingAreasRelStructure | None = field(
        default=None,
        metadata={
            "name": "parkingAreas",
            "type": "Element",
            "namespace": "http://www.netex.org.uk/netex",
        },
    )
    vehicle_entrances: ParkingEntrancesForVehiclesRelStructure | None = field(
        default=None,
        metadata={
            "name": "vehicleEntrances",
            "type": "Element",
            "namespace": "http://www.netex.org.uk/netex",
        },
    )
