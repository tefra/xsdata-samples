from __future__ import annotations
from dataclasses import dataclass, field
from travelport.models.address_2 import Address2
from travelport.models.electronic_address_2 import ElectronicAddress2
from travelport.models.external_identifier_2 import ExternalIdentifier2
from travelport.models.phone_2 import Phone2
from travelport.models.provider_info_2 import ProviderInfo2
from travelport.models.type_profile_info_2 import TypeProfileInfo2

__NAMESPACE__ = "http://www.travelport.com/schema/uprofile_v37_0"


@dataclass
class BranchInfo2(TypeProfileInfo2):
    """
    Information relating to Branch.

    Parameters
    ----------
    address
        Branch Address.
    phone
        Branch Phone Number.
    electronic_address
        Branch Electronic Address
    provider_info
        PCCs and IATAs associated to the branch. Note that this profile
        information is not used to transact with host systems. The data is
        specified in the profile only to support searching for the branch
        profile by PCC/IATA. Modifying this data requires special
        authorization.
    external_identifier
        Branch External Identifier
    name
        Branch name. Modifying this value requires special authorization.
    geo_city_code
        Branch geo city code.  Codes can be found in Ref Pub.
    control
        Identifies whether the entity is a control branch. Modifying this
        value requires special authorization.
    branch_code
        Zircon site ID. Modifying this value requires special authorization.
    currency
        Default currency specified for the branch.
    profile_sync_to
        Identify if profile sync to operation can be performed.Ignored in
        request message.
    profile_sync_from
        Identify if profile sync from operation can be performed.Ignored in
        request message.
    ursync_to
        Identify if Universal Record synch is activated at Branch Level.
    """

    class Meta:
        name = "BranchInfo"
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
    provider_info: list[ProviderInfo2] = field(
        default_factory=list,
        metadata={
            "name": "ProviderInfo",
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
    geo_city_code: None | str = field(
        default=None,
        metadata={
            "name": "GeoCityCode",
            "type": "Attribute",
            "required": True,
            "max_length": 10,
        },
    )
    control: None | bool = field(
        default=None,
        metadata={
            "name": "Control",
            "type": "Attribute",
            "required": True,
        },
    )
    branch_code: None | str = field(
        default=None,
        metadata={
            "name": "BranchCode",
            "type": "Attribute",
            "required": True,
            "min_length": 1,
            "max_length": 25,
        },
    )
    currency: None | str = field(
        default=None,
        metadata={
            "name": "Currency",
            "type": "Attribute",
            "required": True,
            "length": 3,
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
