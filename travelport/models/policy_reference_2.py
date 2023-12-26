from __future__ import annotations
from dataclasses import dataclass, field
from travelport.models.type_key_element_2 import TypeKeyElement2

__NAMESPACE__ = "http://www.travelport.com/schema/uprofile_v37_0"


@dataclass
class PolicyReference2(TypeKeyElement2):
    """
    Used by the Traveler's employer to administer policy.

    Parameters
    ----------
    type_value
        A code for categorizing a reference for a Traveler's Policy. Valid
        values are Travelport Universal Policy and Other.
    value
        The value that the employer wants to be associated with the
        specified type.
    desc
        A description of the value being used.
    controlling_policy_id
        A specific reference to a particular profile that is a parent of the
        Traveler.
    priority_order
        Priority order associated with this PolicyReference.
    """

    class Meta:
        name = "PolicyReference"
        namespace = "http://www.travelport.com/schema/uprofile_v37_0"

    type_value: None | str = field(
        default=None,
        metadata={
            "name": "Type",
            "type": "Attribute",
            "required": True,
            "min_length": 1,
            "max_length": 128,
        },
    )
    value: None | str = field(
        default=None,
        metadata={
            "name": "Value",
            "type": "Attribute",
            "required": True,
            "min_length": 1,
            "max_length": 255,
        },
    )
    desc: None | str = field(
        default=None,
        metadata={
            "name": "Desc",
            "type": "Attribute",
            "min_length": 1,
            "max_length": 255,
        },
    )
    controlling_policy_id: None | int = field(
        default=None,
        metadata={
            "name": "ControllingPolicyID",
            "type": "Attribute",
        },
    )
    priority_order: None | int = field(
        default=None,
        metadata={
            "name": "PriorityOrder",
            "type": "Attribute",
            "min_inclusive": 1,
            "max_inclusive": 99,
        },
    )
