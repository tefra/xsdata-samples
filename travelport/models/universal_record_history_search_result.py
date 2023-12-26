from __future__ import annotations
from dataclasses import dataclass, field

__NAMESPACE__ = "http://www.travelport.com/schema/universal_v52_0"


@dataclass
class UniversalRecordHistorySearchResult:
    """
    Container for Universal Record history result.

    Parameters
    ----------
    old
        Representation of the element before the modification took place.
    new
        Representation of the element after the modification took place.
    modified_by
        The agent or entity that performed the modification
    modified_date
        When the Universal Record was modified.
    element_type
        The type of element that was added or deleted
    action
        The action that was taken on the defined element
    transaction_id
        System generated unique identifier for this atomic transaction.
        Travelport Internal Usage Only.
    agent_override
        AgentSine value that was used during PNR creation or End Transact.
    """

    class Meta:
        namespace = "http://www.travelport.com/schema/universal_v52_0"

    old: None | str = field(
        default=None,
        metadata={
            "name": "Old",
            "type": "Element",
        },
    )
    new: None | str = field(
        default=None,
        metadata={
            "name": "New",
            "type": "Element",
        },
    )
    modified_by: None | str = field(
        default=None,
        metadata={
            "name": "ModifiedBy",
            "type": "Attribute",
        },
    )
    modified_date: None | str = field(
        default=None,
        metadata={
            "name": "ModifiedDate",
            "type": "Attribute",
            "required": True,
        },
    )
    element_type: None | str = field(
        default=None,
        metadata={
            "name": "ElementType",
            "type": "Attribute",
            "required": True,
        },
    )
    action: None | str = field(
        default=None,
        metadata={
            "name": "Action",
            "type": "Attribute",
            "required": True,
        },
    )
    transaction_id: None | str = field(
        default=None,
        metadata={
            "name": "TransactionId",
            "type": "Attribute",
        },
    )
    agent_override: None | str = field(
        default=None,
        metadata={
            "name": "AgentOverride",
            "type": "Attribute",
            "min_length": 1,
            "max_length": 32,
        },
    )
