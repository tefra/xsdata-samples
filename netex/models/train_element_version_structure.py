from dataclasses import dataclass, field
from decimal import Decimal
from typing import List, Optional
from .alternative_texts_rel_structure import DataManagedObjectStructure
from .equipments_rel_structure import EquipmentsRelStructure
from .fare_class_enumeration import FareClassEnumeration
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
    fare_classes: List[FareClassEnumeration] = field(
        default_factory=list,
        metadata={
            "name": "FareClasses",
            "type": "Element",
            "namespace": "http://www.netex.org.uk/netex",
            "tokens": True,
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
