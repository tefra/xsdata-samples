from __future__ import annotations

from dataclasses import dataclass, field

from travelport.models.address_2 import Address2
from travelport.models.electronic_address_2 import ElectronicAddress2
from travelport.models.external_identifier_2 import ExternalIdentifier2
from travelport.models.phone_2 import Phone2
from travelport.models.type_profile_info_2 import TypeProfileInfo2

__NAMESPACE__ = "http://www.travelport.com/schema/uprofile_v37_0"


@dataclass
class BranchGroupInfo2(TypeProfileInfo2):
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
        namespace = "http://www.travelport.com/schema/uprofile_v37_0"

    address: list[Address2] = field(
        default_factory=list,
        metadata={
            "name": "Address",
            "type": "Element",
            "max_occurs": 999,
        },
    )
    phone: list[Phone2] = field(
        default_factory=list,
        metadata={
            "name": "Phone",
            "type": "Element",
            "max_occurs": 999,
        },
    )
    electronic_address: list[ElectronicAddress2] = field(
        default_factory=list,
        metadata={
            "name": "ElectronicAddress",
            "type": "Element",
            "max_occurs": 999,
        },
    )
    external_identifier: list[ExternalIdentifier2] = field(
        default_factory=list,
        metadata={
            "name": "ExternalIdentifier",
            "type": "Element",
            "max_occurs": 999,
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
