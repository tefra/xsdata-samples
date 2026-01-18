from __future__ import annotations

from collections.abc import Iterable
from dataclasses import dataclass, field
from typing import Any, ForwardRef

from .air_submode import AirSubmode
from .all_modes_enumeration import AllModesEnumeration
from .bus_submode import BusSubmode
from .coach_submode import CoachSubmode
from .contact_structure import ContactStructure
from .country_ref import CountryRef
from .departments_rel_structure import DepartmentsRelStructure
from .flexible_mode_of_operation_ref import FlexibleModeOfOperationRef
from .funicular_submode import FunicularSubmode
from .metro_submode import MetroSubmode
from .mode_refs_rel_structure import ModeRefsRelStructure
from .operator_activities_enumeration import OperatorActivitiesEnumeration
from .organisation_version_structure import OrganisationVersionStructure
from .personal_mode_of_operation_ref import PersonalModeOfOperationRef
from .postal_address import PostalAddress
from .postal_address_version_structure import PostalAddressVersionStructure
from .rail_submode import RailSubmode
from .road_address import RoadAddress
from .scheduled_mode_of_operation_ref import ScheduledModeOfOperationRef
from .self_drive_submode import SelfDriveSubmode
from .snow_and_ice_submode import SnowAndIceSubmode
from .taxi_submode import TaxiSubmode
from .telecabin_submode import TelecabinSubmode
from .tram_submode import TramSubmode
from .vehicle_pooling_ref import VehiclePoolingRef
from .vehicle_rental_ref import VehicleRentalRef
from .vehicle_sharing_ref import VehicleSharingRef
from .water_submode import WaterSubmode

__NAMESPACE__ = "http://www.netex.org.uk/netex"


@dataclass
class TransportOrganisationVersionStructure(OrganisationVersionStructure):
    class Meta:
        name = "TransportOrganisation_VersionStructure"

    country_ref: CountryRef | None = field(
        default=None,
        metadata={
            "name": "CountryRef",
            "type": "Element",
            "namespace": "http://www.netex.org.uk/netex",
        },
    )
    address: (
        PostalAddress
        | RoadAddress
        | TransportOrganisationVersionStructure.Address
        | None
    ) = field(
        default=None,
        metadata={
            "type": "Elements",
            "choices": (
                {
                    "name": "PostalAddress",
                    "type": PostalAddress,
                    "namespace": "http://www.netex.org.uk/netex",
                },
                {
                    "name": "RoadAddress",
                    "type": RoadAddress,
                    "namespace": "http://www.netex.org.uk/netex",
                },
                {
                    "name": "Address",
                    "type": ForwardRef(
                        "TransportOrganisationVersionStructure.Address"
                    ),
                    "namespace": "http://www.netex.org.uk/netex",
                },
            ),
        },
    )
    primary_mode: AllModesEnumeration | None = field(
        default=None,
        metadata={
            "name": "PrimaryMode",
            "type": "Element",
            "namespace": "http://www.netex.org.uk/netex",
        },
    )
    choice: (
        AirSubmode
        | BusSubmode
        | CoachSubmode
        | FunicularSubmode
        | MetroSubmode
        | TramSubmode
        | TelecabinSubmode
        | RailSubmode
        | WaterSubmode
        | SnowAndIceSubmode
        | TaxiSubmode
        | SelfDriveSubmode
        | None
    ) = field(
        default=None,
        metadata={
            "type": "Elements",
            "choices": (
                {
                    "name": "AirSubmode",
                    "type": AirSubmode,
                    "namespace": "http://www.netex.org.uk/netex",
                },
                {
                    "name": "BusSubmode",
                    "type": BusSubmode,
                    "namespace": "http://www.netex.org.uk/netex",
                },
                {
                    "name": "CoachSubmode",
                    "type": CoachSubmode,
                    "namespace": "http://www.netex.org.uk/netex",
                },
                {
                    "name": "FunicularSubmode",
                    "type": FunicularSubmode,
                    "namespace": "http://www.netex.org.uk/netex",
                },
                {
                    "name": "MetroSubmode",
                    "type": MetroSubmode,
                    "namespace": "http://www.netex.org.uk/netex",
                },
                {
                    "name": "TramSubmode",
                    "type": TramSubmode,
                    "namespace": "http://www.netex.org.uk/netex",
                },
                {
                    "name": "TelecabinSubmode",
                    "type": TelecabinSubmode,
                    "namespace": "http://www.netex.org.uk/netex",
                },
                {
                    "name": "RailSubmode",
                    "type": RailSubmode,
                    "namespace": "http://www.netex.org.uk/netex",
                },
                {
                    "name": "WaterSubmode",
                    "type": WaterSubmode,
                    "namespace": "http://www.netex.org.uk/netex",
                },
                {
                    "name": "SnowAndIceSubmode",
                    "type": SnowAndIceSubmode,
                    "namespace": "http://www.netex.org.uk/netex",
                },
                {
                    "name": "TaxiSubmode",
                    "type": TaxiSubmode,
                    "namespace": "http://www.netex.org.uk/netex",
                },
                {
                    "name": "SelfDriveSubmode",
                    "type": SelfDriveSubmode,
                    "namespace": "http://www.netex.org.uk/netex",
                },
            ),
        },
    )
    mode_of_operation_ref_or_alternative_mode_of_operation_ref_or_conventional_mode_of_operation_ref: (
        PersonalModeOfOperationRef
        | VehiclePoolingRef
        | VehicleSharingRef
        | VehicleRentalRef
        | FlexibleModeOfOperationRef
        | ScheduledModeOfOperationRef
        | None
    ) = field(
        default=None,
        metadata={
            "type": "Elements",
            "choices": (
                {
                    "name": "PersonalModeOfOperationRef",
                    "type": PersonalModeOfOperationRef,
                    "namespace": "http://www.netex.org.uk/netex",
                },
                {
                    "name": "VehiclePoolingRef",
                    "type": VehiclePoolingRef,
                    "namespace": "http://www.netex.org.uk/netex",
                },
                {
                    "name": "VehicleSharingRef",
                    "type": VehicleSharingRef,
                    "namespace": "http://www.netex.org.uk/netex",
                },
                {
                    "name": "VehicleRentalRef",
                    "type": VehicleRentalRef,
                    "namespace": "http://www.netex.org.uk/netex",
                },
                {
                    "name": "FlexibleModeOfOperationRef",
                    "type": FlexibleModeOfOperationRef,
                    "namespace": "http://www.netex.org.uk/netex",
                },
                {
                    "name": "ScheduledModeOfOperationRef",
                    "type": ScheduledModeOfOperationRef,
                    "namespace": "http://www.netex.org.uk/netex",
                },
            ),
        },
    )
    operator_activities: Iterable[OperatorActivitiesEnumeration] = field(
        default_factory=list,
        metadata={
            "name": "OperatorActivities",
            "type": "Element",
            "namespace": "http://www.netex.org.uk/netex",
            "tokens": True,
        },
    )
    customer_service_contact_details: ContactStructure | None = field(
        default=None,
        metadata={
            "name": "CustomerServiceContactDetails",
            "type": "Element",
            "namespace": "http://www.netex.org.uk/netex",
        },
    )
    departments: DepartmentsRelStructure | None = field(
        default=None,
        metadata={
            "type": "Element",
            "namespace": "http://www.netex.org.uk/netex",
        },
    )
    other_modes: ModeRefsRelStructure | None = field(
        default=None,
        metadata={
            "name": "otherModes",
            "type": "Element",
            "namespace": "http://www.netex.org.uk/netex",
        },
    )

    @dataclass
    class Address(PostalAddressVersionStructure):
        members: Any = field(
            init=False,
            default=None,
            metadata={
                "type": "Ignore",
            },
        )
        key_list: Any = field(
            init=False,
            default=None,
            metadata={
                "type": "Ignore",
            },
        )
        extensions: Any = field(
            init=False,
            default=None,
            metadata={
                "type": "Ignore",
            },
        )
        branding_ref: Any = field(
            init=False,
            default=None,
            metadata={
                "type": "Ignore",
            },
        )
        validity_conditions_or_valid_between: Any = field(
            init=False,
            default=None,
            metadata={
                "type": "Ignore",
            },
        )
        alternative_texts: Any = field(
            init=False,
            default=None,
            metadata={
                "type": "Ignore",
            },
        )
