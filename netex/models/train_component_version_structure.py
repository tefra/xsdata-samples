from dataclasses import dataclass, field
from typing import Optional, Union
from .alternative_texts_rel_structure import DataManagedObjectStructure
from .multilingual_string import MultilingualString
from .train_element import TrainElement
from .train_element_ref import TrainElementRef
from .train_ref import TrainRef
from .vehicle_orientation_enumeration import VehicleOrientationEnumeration

__NAMESPACE__ = "http://www.netex.org.uk/netex"


@dataclass
class TrainComponentVersionStructure(DataManagedObjectStructure):
    class Meta:
        name = "TrainComponent_VersionStructure"

    label: Optional[MultilingualString] = field(
        default=None,
        metadata={
            "name": "Label",
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
    train_ref: Optional[TrainRef] = field(
        default=None,
        metadata={
            "name": "TrainRef",
            "type": "Element",
            "namespace": "http://www.netex.org.uk/netex",
        },
    )
    train_element_ref_or_train_element: Optional[
        Union[TrainElementRef, TrainElement]
    ] = field(
        default=None,
        metadata={
            "type": "Elements",
            "choices": (
                {
                    "name": "TrainElementRef",
                    "type": TrainElementRef,
                    "namespace": "http://www.netex.org.uk/netex",
                },
                {
                    "name": "TrainElement",
                    "type": TrainElement,
                    "namespace": "http://www.netex.org.uk/netex",
                },
            ),
        },
    )
    operational_orientation: Optional[VehicleOrientationEnumeration] = field(
        default=None,
        metadata={
            "name": "OperationalOrientation",
            "type": "Element",
            "namespace": "http://www.netex.org.uk/netex",
        },
    )
    order: Optional[int] = field(
        default=None,
        metadata={
            "type": "Attribute",
        },
    )
