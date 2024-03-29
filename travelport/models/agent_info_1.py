from __future__ import annotations

from dataclasses import dataclass, field

from travelport.models.address_1 import Address1
from travelport.models.electronic_address_1 import ElectronicAddress1
from travelport.models.external_identifier_1 import ExternalIdentifier1
from travelport.models.phone_1 import Phone1
from travelport.models.type_profile_info_1 import TypeProfileInfo1

__NAMESPACE__ = "http://www.travelport.com/schema/sharedUprofile_v20_0"


@dataclass
class AgentInfo1(TypeProfileInfo1):
    """
    Agent specific profile information.

    Parameters
    ----------
    address
        Agent Address
    phone
        Agent Phone Number
    electronic_address
        Agent Electronic Address.
    external_identifier
        Agent External Identifier
    user_name
        The login name of the agent. Modifying this value requires special
        authorization.
    occupational_title
    title
    nickname
    given_name
        Given name of the agent. Modifying this value requires special
        authorization.
    other_name
    surname
        Surname of the agent. Modifying this value requires special
        authorization.
    suffix
    default_branch_id
        The profile ID of the branch assigned as the default branch for this
        agent. If both the profile ID and branch code of the default branch
        are specified, the ID will be used.
    default_branch_code
        The branch code of the branch assigned as the default branch for
        this agent. If both the profile ID and branch code of the default
        branch are specified, the ID will be used.
    alternate_agent_id
    """

    class Meta:
        name = "AgentInfo"
        namespace = "http://www.travelport.com/schema/sharedUprofile_v20_0"

    address: list[Address1] = field(
        default_factory=list,
        metadata={
            "name": "Address",
            "type": "Element",
        },
    )
    phone: list[Phone1] = field(
        default_factory=list,
        metadata={
            "name": "Phone",
            "type": "Element",
        },
    )
    electronic_address: list[ElectronicAddress1] = field(
        default_factory=list,
        metadata={
            "name": "ElectronicAddress",
            "type": "Element",
        },
    )
    external_identifier: list[ExternalIdentifier1] = field(
        default_factory=list,
        metadata={
            "name": "ExternalIdentifier",
            "type": "Element",
        },
    )
    user_name: None | str = field(
        default=None,
        metadata={
            "name": "UserName",
            "type": "Attribute",
            "required": True,
            "min_length": 1,
            "max_length": 128,
        },
    )
    occupational_title: None | str = field(
        default=None,
        metadata={
            "name": "OccupationalTitle",
            "type": "Attribute",
            "min_length": 1,
            "max_length": 255,
        },
    )
    title: None | str = field(
        default=None,
        metadata={
            "name": "Title",
            "type": "Attribute",
            "min_length": 1,
            "max_length": 128,
        },
    )
    nickname: None | str = field(
        default=None,
        metadata={
            "name": "Nickname",
            "type": "Attribute",
            "min_length": 1,
            "max_length": 128,
        },
    )
    given_name: None | str = field(
        default=None,
        metadata={
            "name": "GivenName",
            "type": "Attribute",
            "required": True,
            "min_length": 1,
            "max_length": 128,
        },
    )
    other_name: None | str = field(
        default=None,
        metadata={
            "name": "OtherName",
            "type": "Attribute",
            "min_length": 1,
            "max_length": 128,
        },
    )
    surname: None | str = field(
        default=None,
        metadata={
            "name": "Surname",
            "type": "Attribute",
            "required": True,
            "min_length": 1,
            "max_length": 128,
        },
    )
    suffix: None | str = field(
        default=None,
        metadata={
            "name": "Suffix",
            "type": "Attribute",
            "min_length": 1,
            "max_length": 128,
        },
    )
    default_branch_id: None | int = field(
        default=None,
        metadata={
            "name": "DefaultBranchID",
            "type": "Attribute",
        },
    )
    default_branch_code: None | str = field(
        default=None,
        metadata={
            "name": "DefaultBranchCode",
            "type": "Attribute",
            "min_length": 1,
            "max_length": 25,
        },
    )
    alternate_agent_id: None | str = field(
        default=None,
        metadata={
            "name": "AlternateAgentID",
            "type": "Attribute",
            "max_length": 128,
        },
    )
