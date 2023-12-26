from __future__ import annotations
from dataclasses import dataclass, field
from xsdata.models.datatype import XmlDate, XmlDateTime
from travelport.models.history_element_2 import HistoryElement2
from travelport.models.type_profile_type_7 import TypeProfileType7

__NAMESPACE__ = "http://www.travelport.com/schema/uprofile_v37_0"


@dataclass
class ProfileHistory2:
    """
    The profile history.

    Parameters
    ----------
    history_element
    profile_id
        The system-assigned, unique ID of the profile.
    profile_type
        The type of profile this profile is for (e.g., branch, account,
        traveler). The profile type identifies which default
        attributes/elements (minimum data set) the system will insert.
    profile_name
        The name of the profile. Either the the organization name, or the
        concatenated first and last names of a profile representing a person
        (agent or traveler).
    created_by_agent_id
        Agent who created the Profile
    created_by_agent_user_name
        Agent who created the Profile
    created_date
        Date that the profile was created
    last_modified_by_agent_id
        Agent who last modified the profile
    last_modified_by_agent_user_name
        Agent who last modified the profile
    last_modified_date
        The date that the profile was last modified
    """

    class Meta:
        name = "ProfileHistory"
        namespace = "http://www.travelport.com/schema/uprofile_v37_0"

    history_element: list[HistoryElement2] = field(
        default_factory=list,
        metadata={
            "name": "HistoryElement",
            "type": "Element",
            "max_occurs": 999,
        },
    )
    profile_id: None | int = field(
        default=None,
        metadata={
            "name": "ProfileID",
            "type": "Attribute",
            "required": True,
        },
    )
    profile_type: None | TypeProfileType7 = field(
        default=None,
        metadata={
            "name": "ProfileType",
            "type": "Attribute",
            "required": True,
        },
    )
    profile_name: None | object = field(
        default=None,
        metadata={
            "name": "ProfileName",
            "type": "Attribute",
            "required": True,
        },
    )
    created_by_agent_id: None | int = field(
        default=None,
        metadata={
            "name": "CreatedByAgentID",
            "type": "Attribute",
        },
    )
    created_by_agent_user_name: None | str = field(
        default=None,
        metadata={
            "name": "CreatedByAgentUserName",
            "type": "Attribute",
            "pattern": r"[a-zA-Z0-9\-_\.@ ]{1,128}",
        },
    )
    created_date: None | XmlDateTime = field(
        default=None,
        metadata={
            "name": "CreatedDate",
            "type": "Attribute",
        },
    )
    last_modified_by_agent_id: None | int = field(
        default=None,
        metadata={
            "name": "LastModifiedByAgentID",
            "type": "Attribute",
        },
    )
    last_modified_by_agent_user_name: None | str = field(
        default=None,
        metadata={
            "name": "LastModifiedByAgentUserName",
            "type": "Attribute",
            "pattern": r"[a-zA-Z0-9\-_\.@ ]{1,128}",
        },
    )
    last_modified_date: None | XmlDateTime = field(
        default=None,
        metadata={
            "name": "LastModifiedDate",
            "type": "Attribute",
        },
    )
