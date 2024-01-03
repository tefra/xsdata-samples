from dataclasses import dataclass, field
from typing import Optional, Any
from .alternative_quay_descriptor_versioned_child_structure import (
    AlternativeQuayDescriptorVersionedChildStructure,
)

__NAMESPACE__ = "http://www.netex.org.uk/netex"


@dataclass
class AlternativeQuayDescriptor(
    AlternativeQuayDescriptorVersionedChildStructure
):
    class Meta:
        namespace = "http://www.netex.org.uk/netex"

    validity_conditions_or_valid_between: Any = field(
        init=False,
        metadata={
            "type": "Ignore",
        },
    )
    alternative_texts: Any = field(
        init=False,
        metadata={
            "type": "Ignore",
        },
    )
    name_type: Any = field(
        init=False,
        metadata={
            "type": "Ignore",
        },
    )
    type_of_name: Optional[str] = field(
        default=None,
        metadata={
            "name": "TypeOfName",
            "type": "Element",
            "required": True,
        },
    )
