from __future__ import annotations

from dataclasses import dataclass, field

from travelport.models.address_1 import Address1
from travelport.models.electronic_address_1 import ElectronicAddress1
from travelport.models.external_identifier_1 import ExternalIdentifier1
from travelport.models.phone_1 import Phone1
from travelport.models.type_profile_info_1 import TypeProfileInfo1

__NAMESPACE__ = "http://www.travelport.com/schema/sharedUprofile_v20_0"


@dataclass
class BranchGroupInfo1(TypeProfileInfo1):
    """
    Branch group specific profile information.

    Parameters
    ----------
    address
        Branch Group Address
    phone
        Branch Group  Phone Number
    electronic_address
        Branch Group Electronic Address
    external_identifier
        Branch Group External Identifier
    name
        Branch group name. Modifying this value requires special
        authorization.
    branch_group_code
        Zircon site ID. Modifying this value requires special authorization.
    profile_sync_to
        Identify if profile sync to operation can be performed.Ignored in
        request message.
    profile_sync_from
        Identify if profile sync from operation can be performed.Ignored in
        request message.
    ursync_to
        Identify if Universal Record synch is activated at Branch Group
        Level.
    """

    class Meta:
        name = "BranchGroupInfo"
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
    name: None | str = field(
        default=None,
        metadata={
            "name": "Name",
            "type": "Attribute",
            "required": True,
            "min_length": 1,
            "max_length": 128,
        },
    )
    branch_group_code: None | str = field(
        default=None,
        metadata={
            "name": "BranchGroupCode",
            "type": "Attribute",
            "required": True,
            "min_length": 1,
            "max_length": 25,
        },
    )
    profile_sync_to: None | bool = field(
        default=None,
        metadata={
            "name": "ProfileSyncTo",
            "type": "Attribute",
        },
    )
    profile_sync_from: None | bool = field(
        default=None,
        metadata={
            "name": "ProfileSyncFrom",
            "type": "Attribute",
        },
    )
    ursync_to: bool = field(
        default=False,
        metadata={
            "name": "URSyncTo",
            "type": "Attribute",
        },
    )
