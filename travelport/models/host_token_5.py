from __future__ import annotations

from dataclasses import dataclass, field

from travelport.models.type_element_status_6 import TypeElementStatus6

__NAMESPACE__ = "http://www.travelport.com/schema/common_v34_0"


@dataclass
class HostToken5:
    """
    This is a host token.

    It contains some kind of payload we got from a host that must be passed
    in on successive calls they know who you are as our system does not
    maintain state. The format of this string isn't important as long as it
    is not altered in any way between calls. Since a host token is only
    valid on the host it is assocated with, there is also an attribute
    called Host so we know how to route the command(s). You can have
    multiple active sessions between one or more hosts.

    Parameters
    ----------
    value
    host
        The host associated with this token
    key
        Unique identifier for this token - use this key when a single
        HostToken is shared by multiple elements.
    el_stat
        This attribute is used to show the action results of an element.
        Possible values are "A" (when elements have been added to the UR)
        and "M" (when existing elements have been modified). Response only.
    key_override
        If a duplicate key is found where we are adding elements in some
        cases like URAdd, then instead of erroring out set this attribute to
        true.
    """

    class Meta:
        name = "HostToken"
        namespace = "http://www.travelport.com/schema/common_v34_0"

    value: str = field(
        default="",
        metadata={
            "required": True,
        },
    )
    host: None | str = field(
        default=None,
        metadata={
            "name": "Host",
            "type": "Attribute",
            "min_length": 2,
            "max_length": 5,
        },
    )
    key: None | object = field(
        default=None,
        metadata={
            "name": "Key",
            "type": "Attribute",
        },
    )
    el_stat: None | TypeElementStatus6 = field(
        default=None,
        metadata={
            "name": "ElStat",
            "type": "Attribute",
        },
    )
    key_override: None | bool = field(
        default=None,
        metadata={
            "name": "KeyOverride",
            "type": "Attribute",
        },
    )
