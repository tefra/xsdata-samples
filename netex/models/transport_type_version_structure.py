from __future__ import annotations

from dataclasses import dataclass, field
from decimal import Decimal
from typing import ForwardRef

from .all_vehicle_modes_of_transport_enumeration import (
    AllVehicleModesOfTransportEnumeration,
)
from .entity_in_version_structure import DataManagedObjectStructure
from .fuel_type_enumeration import FuelTypeEnumeration
from .multilingual_string import MultilingualString
from .passenger_capacity_structure import PassengerCapacityStructure
from .private_code import PrivateCode
from .propulsion_type_enumeration import PropulsionTypeEnumeration

__NAMESPACE__ = "http://www.netex.org.uk/netex"


@dataclass
class TransportTypeVersionStructure(DataManagedObjectStructure):
    class Meta:
        name = "TransportType_VersionStructure"

    name: MultilingualString | None = field(
        default=None,
        metadata={
            "name": "Name",
            "type": "Element",
            "namespace": "http://www.netex.org.uk/netex",
        },
    )
    short_name: MultilingualString | None = field(
        default=None,
        metadata={
            "name": "ShortName",
            "type": "Element",
            "namespace": "http://www.netex.org.uk/netex",
        },
    )
    description: MultilingualString | None = field(
        default=None,
        metadata={
            "name": "Description",
            "type": "Element",
            "namespace": "http://www.netex.org.uk/netex",
        },
    )
    private_code: PrivateCode | None = field(
        default=None,
        metadata={
            "name": "PrivateCode",
            "type": "Element",
            "namespace": "http://www.netex.org.uk/netex",
        },
    )
    euro_class: str | None = field(
        default=None,
        metadata={
            "name": "EuroClass",
            "type": "Element",
            "namespace": "http://www.netex.org.uk/netex",
        },
    )
    reversing_direction: bool | None = field(
        default=None,
        metadata={
            "name": "ReversingDirection",
            "type": "Element",
            "namespace": "http://www.netex.org.uk/netex",
        },
    )
    self_propelled: bool | None = field(
        default=None,
        metadata={
            "name": "SelfPropelled",
            "type": "Element",
            "namespace": "http://www.netex.org.uk/netex",
        },
    )
    propulsion_type: PropulsionTypeEnumeration | None = field(
        default=None,
        metadata={
            "name": "PropulsionType",
            "type": "Element",
            "namespace": "http://www.netex.org.uk/netex",
        },
    )
    fuel_type_or_type_of_fuel: (
        TransportTypeVersionStructure.FuelType
        | TransportTypeVersionStructure.TypeOfFuel
        | None
    ) = field(
        default=None,
        metadata={
            "type": "Elements",
            "choices": (
                {
                    "name": "FuelType",
                    "type": ForwardRef(
                        "TransportTypeVersionStructure.FuelType"
                    ),
                    "namespace": "http://www.netex.org.uk/netex",
                },
                {
                    "name": "TypeOfFuel",
                    "type": ForwardRef(
                        "TransportTypeVersionStructure.TypeOfFuel"
                    ),
                    "namespace": "http://www.netex.org.uk/netex",
                },
            ),
        },
    )
    maximum_range: Decimal | None = field(
        default=None,
        metadata={
            "name": "MaximumRange",
            "type": "Element",
            "namespace": "http://www.netex.org.uk/netex",
        },
    )
    transport_mode: AllVehicleModesOfTransportEnumeration | None = field(
        default=None,
        metadata={
            "name": "TransportMode",
            "type": "Element",
            "namespace": "http://www.netex.org.uk/netex",
        },
    )
    passenger_capacity: PassengerCapacityStructure | None = field(
        default=None,
        metadata={
            "name": "PassengerCapacity",
            "type": "Element",
            "namespace": "http://www.netex.org.uk/netex",
        },
    )

    @dataclass
    class FuelType:
        value: FuelTypeEnumeration | None = field(
            default=None,
            metadata={
                "required": True,
            },
        )

    @dataclass
    class TypeOfFuel:
        value: FuelTypeEnumeration | None = field(
            default=None,
            metadata={
                "required": True,
            },
        )
