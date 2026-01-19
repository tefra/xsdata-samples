from __future__ import annotations

from collections.abc import Sequence
from dataclasses import dataclass, field

from .one_to_many_relationship_structure import OneToManyRelationshipStructure
from .validity_trigger_ref import ValidityTriggerRef

__NAMESPACE__ = "http://www.netex.org.uk/netex"


@dataclass(kw_only=True)
class ValidityTriggerRefsRelStructure(OneToManyRelationshipStructure):
    class Meta:
        name = "validityTriggerRefs_RelStructure"

    validity_trigger_ref: Sequence[ValidityTriggerRef] = field(
        default_factory=list,
        metadata={
            "name": "ValidityTriggerRef",
            "type": "Element",
            "namespace": "http://www.netex.org.uk/netex",
            "min_occurs": 1,
        },
    )
