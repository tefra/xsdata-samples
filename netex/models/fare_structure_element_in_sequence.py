from __future__ import annotations

from dataclasses import dataclass, field
from typing import Any

from .fare_structure_element_in_sequence_versioned_child_structure import (
    FareStructureElementInSequenceVersionedChildStructure,
)

__NAMESPACE__ = "http://www.netex.org.uk/netex"


@dataclass(kw_only=True)
class FareStructureElementInSequence(
    FareStructureElementInSequenceVersionedChildStructure
):
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
