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


@dataclass(kw_only=True)
class TransportTypeVersionStructure(DataManagedObjectStructure):
    class Meta:
        name = "TransportType_VersionStructure"

    name: None | MultilingualString = field(
        default=None,
        metadata={
            "name": "Name",
            "type": "Element",
            "namespace": "http://www.netex.org.uk/netex",
        },
    )
    short_name: None | MultilingualString = field(
        default=None,
        metadata={
            "name": "ShortName",
            "type": "Element",
            "namespace": "http://www.netex.org.uk/netex",
        },
    )
    description: None | MultilingualString = field(
        default=None,
        metadata={
            "name": "Description",
            "type": "Element",
            "namespace": "http://www.netex.org.uk/netex",
        },
    )
    private_code: None | PrivateCode = field(
        default=None,
        metadata={
            "name": "PrivateCode",
            "type": "Element",
            "namespace": "http://www.netex.org.uk/netex",
        },
    )
    euro_class: None | str = field(
        default=None,
        metadata={
            "name": "EuroClass",
            "type": "Element",
            "namespace": "http://www.netex.org.uk/netex",
        },
    )
    reversing_direction: None | bool = field(
        default=None,
        metadata={
            "name": "ReversingDirection",
            "type": "Element",
            "namespace": "http://www.netex.org.uk/netex",
        },
    )
    self_propelled: None | bool = field(
        default=None,
        metadata={
            "name": "SelfPropelled",
            "type": "Element",
            "namespace": "http://www.netex.org.uk/netex",
        },
    )
    propulsion_type: None | PropulsionTypeEnumeration = field(
        default=None,
        metadata={
            "name": "PropulsionType",
            "type": "Element",
            "namespace": "http://www.netex.org.uk/netex",
        },
    )
    fuel_type_or_type_of_fuel: (
        None
        | TransportTypeVersionStructure.FuelType
        | TransportTypeVersionStructure.TypeOfFuel
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
    maximum_range: None | Decimal = field(
        default=None,
        metadata={
            "name": "MaximumRange",
            "type": "Element",
            "namespace": "http://www.netex.org.uk/netex",
        },
    )
    transport_mode: None | AllVehicleModesOfTransportEnumeration = field(
        default=None,
        metadata={
            "name": "TransportMode",
            "type": "Element",
            "namespace": "http://www.netex.org.uk/netex",
        },
    )
    passenger_capacity: None | PassengerCapacityStructure = field(
        default=None,
        metadata={
            "name": "PassengerCapacity",
            "type": "Element",
            "namespace": "http://www.netex.org.uk/netex",
        },
    )

    @dataclass(kw_only=True)
    class FuelType:
        value: FuelTypeEnumeration = field(
            metadata={
                "required": True,
            }
        )

    @dataclass(kw_only=True)
    class TypeOfFuel:
        value: FuelTypeEnumeration = field(
            metadata={
                "required": True,
            }
        )
