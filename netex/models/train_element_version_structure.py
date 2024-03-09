from dataclasses import dataclass, field
from decimal import Decimal
from typing import Optional

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


@dataclass
class TrainElementVersionStructure(DataManagedObjectStructure):
    class Meta:
        name = "TrainElement_VersionStructure"

    name: Optional[MultilingualString] = field(
        default=None,
        metadata={
            "name": "Name",
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
    train_element_type: Optional[TrainElementTypeEnumeration] = field(
        default=None,
        metadata={
            "name": "TrainElementType",
            "type": "Element",
            "namespace": "http://www.netex.org.uk/netex",
        },
    )
    fare_classes: Optional[FareClasses] = field(
        default=None,
        metadata={
            "name": "FareClasses",
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
    capacities: Optional[PassengerCapacitiesRelStructure] = field(
        default=None,
        metadata={
            "type": "Element",
            "namespace": "http://www.netex.org.uk/netex",
        },
    )
    length: Optional[Decimal] = field(
        default=None,
        metadata={
            "name": "Length",
            "type": "Element",
            "namespace": "http://www.netex.org.uk/netex",
        },
    )
    width: Optional[Decimal] = field(
        default=None,
        metadata={
            "name": "Width",
            "type": "Element",
            "namespace": "http://www.netex.org.uk/netex",
        },
    )
    train_size: Optional[TrainSize] = field(
        default=None,
        metadata={
            "name": "TrainSize",
            "type": "Element",
            "namespace": "http://www.netex.org.uk/netex",
        },
    )
    facilities: Optional[ServiceFacilitySetsRelStructure] = field(
        default=None,
        metadata={
            "type": "Element",
            "namespace": "http://www.netex.org.uk/netex",
        },
    )
    equipments: Optional[EquipmentsRelStructure] = field(
        default=None,
        metadata={
            "type": "Element",
            "namespace": "http://www.netex.org.uk/netex",
        },
    )
