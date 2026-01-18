from __future__ import annotations

from dataclasses import dataclass, field
from typing import Any

from .type_of_link_sequence_value_structure import (
    TypeOfLinkSequenceValueStructure,
)

__NAMESPACE__ = "http://www.netex.org.uk/netex"


@dataclass(kw_only=True)
class TypeOfLinkSequence(TypeOfLinkSequenceValueStructure):
    class Meta:
        namespace = "http://www.netex.org.uk/netex"

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
    name_of_classified_entity_class: str = field(
        init=False,
        default="LinkSequence",
        metadata={
            "name": "nameOfClassifiedEntityClass",
            "type": "Attribute",
        },
    )
