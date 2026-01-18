from dataclasses import dataclass, field

from .derived_view_structure import DerivedViewStructure
from .fare_classes import FareClasses
from .multilingual_string import MultilingualString
from .train_component_ref import TrainComponentRef
from .train_element_ref import TrainElementRef
from .train_element_type_enumeration import TrainElementTypeEnumeration

__NAMESPACE__ = "http://www.netex.org.uk/netex"


@dataclass
class TrainComponentDerivedViewStructure(DerivedViewStructure):
    class Meta:
        name = "TrainComponent_DerivedViewStructure"

    train_component_ref: TrainComponentRef | None = field(
        default=None,
        metadata={
            "name": "TrainComponentRef",
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
    description: MultilingualString | None = field(
        default=None,
        metadata={
            "name": "Description",
            "type": "Element",
            "namespace": "http://www.netex.org.uk/netex",
        },
    )
    train_element_ref: TrainElementRef | None = field(
        default=None,
        metadata={
            "name": "TrainElementRef",
            "type": "Element",
            "namespace": "http://www.netex.org.uk/netex",
        },
    )
    fare_classes: FareClasses | None = field(
        default=None,
        metadata={
            "name": "FareClasses",
            "type": "Element",
            "namespace": "http://www.netex.org.uk/netex",
        },
    )
    train_element_type: TrainElementTypeEnumeration | None = field(
        default=None,
        metadata={
            "name": "TrainElementType",
            "type": "Element",
            "namespace": "http://www.netex.org.uk/netex",
        },
    )
    order: int | None = field(
        default=None,
        metadata={
            "type": "Attribute",
        },
    )
