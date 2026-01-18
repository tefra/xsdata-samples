from __future__ import annotations

from dataclasses import dataclass, field

from xsdata.models.datatype import XmlDateTime

from travelport.models.type_action_1 import TypeAction1
from travelport.models.type_history_sub_element_1 import TypeHistorySubElement1

__NAMESPACE__ = "http://www.travelport.com/schema/sharedUprofile_v20_0"


@dataclass
class HistoryElement1:
    """
    The history of a particular element at a particular point in time.

    Parameters
    ----------
    original
        The orignal values of the element before the change.
    new
        The new updated values of the element.
    action
        The action made on the element.
    modified_by_agent_id
        Agent who modified this element
    modified_by_agent_user_name
        Agent who last modified the profile
    modified_date
        When this element was modified
    component
        The corresponding name of the element that this field refers to in
        the profile message. This is a read only attribute.
    correlation_element
        The name of an attribute on the profile element that defines a
        "type".  This is a read-only attribute.
    correlation_value
        The value that should be put in the attribute that the
        CorrelationElement defines.  This is a read-only attribute.
    """

    class Meta:
        name = "HistoryElement"
        namespace = "http://www.travelport.com/schema/sharedUprofile_v20_0"

    original: None | TypeHistorySubElement1 = field(
        default=None,
        metadata={
            "name": "Original",
            "type": "Element",
        },
    )
    new: None | TypeHistorySubElement1 = field(
        default=None,
        metadata={
            "name": "New",
            "type": "Element",
        },
    )
    action: None | TypeAction1 = field(
        default=None,
        metadata={
            "name": "Action",
            "type": "Attribute",
            "required": True,
        },
    )
    modified_by_agent_id: None | int = field(
        default=None,
        metadata={
            "name": "ModifiedByAgentID",
            "type": "Attribute",
            "required": True,
        },
    )
    modified_by_agent_user_name: None | str = field(
        default=None,
        metadata={
            "name": "ModifiedByAgentUserName",
            "type": "Attribute",
            "required": True,
            "pattern": r"[a-zA-Z0-9\-_\.@ ]{1,128}",
        },
    )
    modified_date: None | XmlDateTime = field(
        default=None,
        metadata={
            "name": "ModifiedDate",
            "type": "Attribute",
            "required": True,
        },
    )
    component: None | str = field(
        default=None,
        metadata={
            "name": "Component",
            "type": "Attribute",
            "required": True,
            "max_length": 50,
        },
    )
    correlation_element: None | str = field(
        default=None,
        metadata={
            "name": "CorrelationElement",
            "type": "Attribute",
            "max_length": 50,
        },
    )
    correlation_value: None | str = field(
        default=None,
        metadata={
            "name": "CorrelationValue",
            "type": "Attribute",
            "min_length": 1,
            "max_length": 128,
        },
    )
