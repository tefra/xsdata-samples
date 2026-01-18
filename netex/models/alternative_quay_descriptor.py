from __future__ import annotations

from dataclasses import dataclass, field
from typing import Any

from .alternative_quay_descriptor_versioned_child_structure import (
    AlternativeQuayDescriptorVersionedChildStructure,
)

__NAMESPACE__ = "http://www.netex.org.uk/netex"


@dataclass(kw_only=True)
class AlternativeQuayDescriptor(
    AlternativeQuayDescriptorVersionedChildStructure
):
    class Meta:
        namespace = "http://www.netex.org.uk/netex"

    name_type: Any = field(
        init=False,
        default=None,
        metadata={
            "type": "Ignore",
        },
    )
    validity_conditions_or_valid_between: Any = field(
        init=False,
        default=None,
        metadata={
            "type": "Ignore",
        },
    )
    alternative_texts: Any = field(
        init=False,
        default=None,
        metadata={
            "type": "Ignore",
        },
    )
    type_of_name: str = field(
        metadata={
            "name": "TypeOfName",
            "type": "Element",
            "required": True,
        }
    )
