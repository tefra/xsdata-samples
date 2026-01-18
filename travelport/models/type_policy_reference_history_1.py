from __future__ import annotations

from dataclasses import dataclass, field

from travelport.models.type_key_element_1 import TypeKeyElement1

__NAMESPACE__ = "http://www.travelport.com/schema/sharedUprofile_v20_0"


@dataclass(kw_only=True)
class TypePolicyReferenceHistory1(TypeKeyElement1):
    """
    History Element for Accounting Reference.

    Parameters
    ----------
    type_value
        A code used to reference a traveler's policy. Valid values are
        Travelport Universal Policy and Other.
    value
        The number or alphanumeric code for an employer reference.
    controlling_profile_id
        A list of policies are created in a parent of a traveler, then one
        of those is applied to the traveler. This profileID is to contain
        the ID of the Parent who has the list of policies
    priority_order
        Priority order associated with this AccountingReference.
    desc
        An optional description.
    """

    class Meta:
        name = "typePolicyReferenceHistory"

    type_value: None | str = field(
        default=None,
        metadata={
            "name": "Type",
            "type": "Attribute",
        },
    )
    value: None | str = field(
        default=None,
        metadata={
            "name": "Value",
            "type": "Attribute",
            "min_length": 1,
            "max_length": 255,
        },
    )
    controlling_profile_id: None | int = field(
        default=None,
        metadata={
            "name": "ControllingProfileID",
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
    desc: None | str = field(
        default=None,
        metadata={
            "name": "Desc",
            "type": "Attribute",
            "min_length": 1,
            "max_length": 255,
        },
    )
