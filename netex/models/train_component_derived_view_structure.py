from dataclasses import dataclass, field
from typing import List, Optional
from .derived_view_structure import DerivedViewStructure
from .fare_class_enumeration import FareClassEnumeration
from .multilingual_string import MultilingualString
from .train_component_ref import TrainComponentRef
from .train_element_ref import TrainElementRef
from .train_element_type_enumeration import TrainElementTypeEnumeration

__NAMESPACE__ = "http://www.netex.org.uk/netex"


@dataclass
class TrainComponentDerivedViewStructure(DerivedViewStructure):
    class Meta:
        name = "TrainComponent_DerivedViewStructure"

    train_component_ref: Optional[TrainComponentRef] = field(
        default=None,
        metadata={
            "name": "TrainComponentRef",
            "type": "Element",
            "namespace": "http://www.netex.org.uk/netex",
        },
    )
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
    train_element_ref: Optional[TrainElementRef] = field(
        default=None,
        metadata={
            "name": "TrainElementRef",
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
    train_element_type: Optional[TrainElementTypeEnumeration] = field(
        default=None,
        metadata={
            "name": "TrainElementType",
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
