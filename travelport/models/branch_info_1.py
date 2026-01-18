from __future__ import annotations

from dataclasses import dataclass, field

from travelport.models.address_1 import Address1
from travelport.models.electronic_address_1 import ElectronicAddress1
from travelport.models.external_identifier_1 import ExternalIdentifier1
from travelport.models.phone_1 import Phone1
from travelport.models.provider_info_1 import ProviderInfo1
from travelport.models.type_profile_info_1 import TypeProfileInfo1

__NAMESPACE__ = "http://www.travelport.com/schema/sharedUprofile_v20_0"


@dataclass(kw_only=True)
class BranchInfo1(TypeProfileInfo1):
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
    provider_info: list[ProviderInfo1] = field(
        default_factory=list,
        metadata={
            "name": "ProviderInfo",
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
    name: str = field(
        metadata={
            "name": "Name",
            "type": "Attribute",
            "required": True,
            "min_length": 1,
            "max_length": 128,
        }
    )
    geo_city_code: str = field(
        metadata={
            "name": "GeoCityCode",
            "type": "Attribute",
            "required": True,
            "max_length": 10,
        }
    )
    control: bool = field(
        metadata={
            "name": "Control",
            "type": "Attribute",
            "required": True,
        }
    )
    branch_code: str = field(
        metadata={
            "name": "BranchCode",
            "type": "Attribute",
            "required": True,
            "min_length": 1,
            "max_length": 25,
        }
    )
    currency: str = field(
        metadata={
            "name": "Currency",
            "type": "Attribute",
            "required": True,
            "length": 3,
        }
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
