from __future__ import annotations
from dataclasses import dataclass, field
from travelport.models.type_profile_info_1 import TypeProfileInfo1

__NAMESPACE__ = "http://www.travelport.com/schema/sharedUprofile_v20_0"


@dataclass
class TypeAgentInfoHistory1(TypeProfileInfo1):
    """
    History Element for Agent Info.

    Parameters
    ----------
    user_name
        The login name of the agent.
    occupational_title
    title
    nickname
    given_name
    other_name
    surname
    suffix
    default_branch_id
        The profile ID of the branch indicated as the default branch for
        this agent.  On create and modify either DefaultBranchID or
        DefaultBranchCode is required.  If both are indicated the ID will be
        used.
    default_branch_code
        The branch code of the branch indicated as the default branch for
        this agent.  On create and modify either DefaultBranchID or
        DefaultBranchCode is required.  If both are indicated the ID will be
        used.
    alternate_agent_id
    """
    class Meta:
        name = "typeAgentInfoHistory"

    user_name: None | str = field(
        default=None,
        metadata={
            "name": "UserName",
            "type": "Attribute",
            "min_length": 1,
            "max_length": 128,
        }
    )
    occupational_title: None | str = field(
        default=None,
        metadata={
            "name": "OccupationalTitle",
            "type": "Attribute",
            "min_length": 1,
            "max_length": 255,
        }
    )
    title: None | str = field(
        default=None,
        metadata={
            "name": "Title",
            "type": "Attribute",
            "min_length": 1,
            "max_length": 128,
        }
    )
    nickname: None | str = field(
        default=None,
        metadata={
            "name": "Nickname",
            "type": "Attribute",
            "min_length": 1,
            "max_length": 128,
        }
    )
    given_name: None | str = field(
        default=None,
        metadata={
            "name": "GivenName",
            "type": "Attribute",
            "min_length": 1,
            "max_length": 128,
        }
    )
    other_name: None | str = field(
        default=None,
        metadata={
            "name": "OtherName",
            "type": "Attribute",
            "min_length": 1,
            "max_length": 128,
        }
    )
    surname: None | str = field(
        default=None,
        metadata={
            "name": "Surname",
            "type": "Attribute",
            "min_length": 1,
            "max_length": 128,
        }
    )
    suffix: None | str = field(
        default=None,
        metadata={
            "name": "Suffix",
            "type": "Attribute",
            "min_length": 1,
            "max_length": 128,
        }
    )
    default_branch_id: None | int = field(
        default=None,
        metadata={
            "name": "DefaultBranchID",
            "type": "Attribute",
        }
    )
    default_branch_code: None | str = field(
        default=None,
        metadata={
            "name": "DefaultBranchCode",
            "type": "Attribute",
            "min_length": 1,
            "max_length": 25,
        }
    )
    alternate_agent_id: None | str = field(
        default=None,
        metadata={
            "name": "AlternateAgentID",
            "type": "Attribute",
            "max_length": 128,
        }
    )
