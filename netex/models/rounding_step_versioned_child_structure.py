from dataclasses import dataclass, field
from decimal import Decimal
from typing import Optional
from .alternative_texts_rel_structure import VersionedChildStructure
from .rounding_step_ref import RoundingStepRef

__NAMESPACE__ = "http://www.netex.org.uk/netex"


@dataclass
class RoundingStepVersionedChildStructure(VersionedChildStructure):
    class Meta:
        name = "RoundingStep_VersionedChildStructure"

    rounding_step_ref: Optional[RoundingStepRef] = field(
        default=None,
        metadata={
            "name": "RoundingStepRef",
            "type": "Element",
            "namespace": "http://www.netex.org.uk/netex",
        }
    )
    round_if_greater_than: Optional[Decimal] = field(
        default=None,
        metadata={
            "name": "RoundIfGreaterThan",
            "type": "Element",
            "namespace": "http://www.netex.org.uk/netex",
            "required": True,
        }
    )
    round_to: Optional[Decimal] = field(
        default=None,
        metadata={
            "name": "RoundTo",
            "type": "Element",
            "namespace": "http://www.netex.org.uk/netex",
            "required": True,
        }
    )
