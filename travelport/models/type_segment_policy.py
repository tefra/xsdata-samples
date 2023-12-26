from __future__ import annotations
from dataclasses import dataclass, field
from travelport.models.preference import Preference

__NAMESPACE__ = "http://www.travelport.com/schema/universal_v52_0"


@dataclass
class TypeSegmentPolicy:
    """
    Parameters
    ----------
    preference
    segment_ref
        Reference to the original segment.
    in_policy
        Determine if this segment is In or Out of policy. By default it is
        InPolicy.
    in_contract
        Determine if this segment is In or Out of contract. By default it is
        InContract.
    """

    class Meta:
        name = "typeSegmentPolicy"

    preference: list[Preference] = field(
        default_factory=list,
        metadata={
            "name": "Preference",
            "type": "Element",
            "namespace": "http://www.travelport.com/schema/universal_v52_0",
            "max_occurs": 999,
        },
    )
    segment_ref: None | str = field(
        default=None,
        metadata={
            "name": "SegmentRef",
            "type": "Attribute",
            "required": True,
        },
    )
    in_policy: bool = field(
        default=True,
        metadata={
            "name": "InPolicy",
            "type": "Attribute",
        },
    )
    in_contract: bool = field(
        default=True,
        metadata={
            "name": "InContract",
            "type": "Attribute",
        },
    )
