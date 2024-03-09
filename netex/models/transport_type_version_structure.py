from dataclasses import dataclass, field
from decimal import Decimal
from typing import Optional, Type, Union
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

    name: Optional[MultilingualString] = field(
        default=None,
        metadata={
            "name": "Name",
            "type": "Element",
            "namespace": "http://www.netex.org.uk/netex",
        },
    )
    short_name: Optional[MultilingualString] = field(
        default=None,
        metadata={
            "name": "ShortName",
            "type": "Element",
            "namespace": "http://www.netex.org.uk/netex",
        },
    )
    description: Optional[MultilingualString] = field(
        default=None,
        metadata={
            "name": "Description",
            "type": "Element",
            "namespace": "http://www.netex.org.uk/netex",
        },
    )
    private_code: Optional[PrivateCode] = field(
        default=None,
        metadata={
            "name": "PrivateCode",
            "type": "Element",
            "namespace": "http://www.netex.org.uk/netex",
        },
    )
    euro_class: Optional[str] = field(
        default=None,
        metadata={
            "name": "EuroClass",
            "type": "Element",
            "namespace": "http://www.netex.org.uk/netex",
        },
    )
    reversing_direction: Optional[bool] = field(
        default=None,
        metadata={
            "name": "ReversingDirection",
            "type": "Element",
            "namespace": "http://www.netex.org.uk/netex",
        },
    )
    self_propelled: Optional[bool] = field(
        default=None,
        metadata={
            "name": "SelfPropelled",
            "type": "Element",
            "namespace": "http://www.netex.org.uk/netex",
        },
    )
    propulsion_type: Optional[PropulsionTypeEnumeration] = field(
        default=None,
        metadata={
            "name": "PropulsionType",
            "type": "Element",
            "namespace": "http://www.netex.org.uk/netex",
        },
    )
    fuel_type_or_type_of_fuel: Optional[
        Union[
            "TransportTypeVersionStructure.FuelType",
            "TransportTypeVersionStructure.TypeOfFuel",
        ]
    ] = field(
        default=None,
        metadata={
            "type": "Elements",
            "choices": (
                {
                    "name": "FuelType",
                    "type": Type["TransportTypeVersionStructure.FuelType"],
                    "namespace": "http://www.netex.org.uk/netex",
                },
                {
                    "name": "TypeOfFuel",
                    "type": Type["TransportTypeVersionStructure.TypeOfFuel"],
                    "namespace": "http://www.netex.org.uk/netex",
                },
            ),
        },
    )
    maximum_range: Optional[Decimal] = field(
        default=None,
        metadata={
            "name": "MaximumRange",
            "type": "Element",
            "namespace": "http://www.netex.org.uk/netex",
        },
    )
    transport_mode: Optional[AllVehicleModesOfTransportEnumeration] = field(
        default=None,
        metadata={
            "name": "TransportMode",
            "type": "Element",
            "namespace": "http://www.netex.org.uk/netex",
        },
    )
    passenger_capacity: Optional[PassengerCapacityStructure] = field(
        default=None,
        metadata={
            "name": "PassengerCapacity",
            "type": "Element",
            "namespace": "http://www.netex.org.uk/netex",
        },
    )

    @dataclass
    class FuelType:
        value: Optional[FuelTypeEnumeration] = field(
            default=None,
            metadata={
                "required": True,
            },
        )

    @dataclass
    class TypeOfFuel:
        value: Optional[FuelTypeEnumeration] = field(
            default=None,
            metadata={
                "required": True,
            },
        )
