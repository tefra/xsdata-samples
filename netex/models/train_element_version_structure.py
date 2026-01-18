from __future__ import annotations

from dataclasses import dataclass, field
from decimal import Decimal

from .entity_in_version_structure import DataManagedObjectStructure
from .equipments_rel_structure import EquipmentsRelStructure
from .fare_classes import FareClasses
from .multilingual_string import MultilingualString
from .passenger_capacities_rel_structure import PassengerCapacitiesRelStructure
from .passenger_capacity_structure import PassengerCapacityStructure
from .service_facility_sets_rel_structure import (
    ServiceFacilitySetsRelStructure,
)
from .train_element_type_enumeration import TrainElementTypeEnumeration
from .train_size import TrainSize

__NAMESPACE__ = "http://www.netex.org.uk/netex"


@dataclass(kw_only=True)
class TrainElementVersionStructure(DataManagedObjectStructure):
    class Meta:
        name = "TrainElement_VersionStructure"

    name: None | MultilingualString = field(
        default=None,
        metadata={
            "name": "Name",
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
    train_element_type: None | TrainElementTypeEnumeration = field(
        default=None,
        metadata={
            "name": "TrainElementType",
            "type": "Element",
            "namespace": "http://www.netex.org.uk/netex",
        },
    )
    fare_classes: None | FareClasses = field(
        default=None,
        metadata={
            "name": "FareClasses",
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
    capacities: None | PassengerCapacitiesRelStructure = field(
        default=None,
        metadata={
            "type": "Element",
            "namespace": "http://www.netex.org.uk/netex",
        },
    )
    length: None | Decimal = field(
        default=None,
        metadata={
            "name": "Length",
            "type": "Element",
            "namespace": "http://www.netex.org.uk/netex",
        },
    )
    width: None | Decimal = field(
        default=None,
        metadata={
            "name": "Width",
            "type": "Element",
            "namespace": "http://www.netex.org.uk/netex",
        },
    )
    train_size: None | TrainSize = field(
        default=None,
        metadata={
            "name": "TrainSize",
            "type": "Element",
            "namespace": "http://www.netex.org.uk/netex",
        },
    )
    facilities: None | ServiceFacilitySetsRelStructure = field(
        default=None,
        metadata={
            "type": "Element",
            "namespace": "http://www.netex.org.uk/netex",
        },
    )
    equipments: None | EquipmentsRelStructure = field(
        default=None,
        metadata={
            "type": "Element",
            "namespace": "http://www.netex.org.uk/netex",
        },
    )
