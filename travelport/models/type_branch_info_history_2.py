from __future__ import annotations
from dataclasses import dataclass, field
from travelport.models.type_profile_info_2 import TypeProfileInfo2
from travelport.models.type_provider_info_history_2 import (
    TypeProviderInfoHistory2,
)

__NAMESPACE__ = "http://www.travelport.com/schema/uprofile_v37_0"


@dataclass
class TypeBranchInfoHistory2(TypeProfileInfo2):
    """
    History Element for Branch Info.

    Parameters
    ----------
    provider_info
        Provider Info values associated to this entity.
    name
        Branch name
    geo_city_code
        Branch geo city code.  Codes can be found in Ref Pub.
    control
        Identify if the entity is a control branch or not.
    branch_code
        Zircon site ID
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
        name = "typeBranchInfoHistory"

    provider_info: list[TypeProviderInfoHistory2] = field(
        default_factory=list,
        metadata={
            "name": "ProviderInfo",
            "type": "Element",
            "namespace": "http://www.travelport.com/schema/uprofile_v37_0",
            "max_occurs": 999,
        },
    )
    name: None | str = field(
        default=None,
        metadata={
            "name": "Name",
            "type": "Attribute",
            "min_length": 1,
            "max_length": 128,
        },
    )
    geo_city_code: None | str = field(
        default=None,
        metadata={
            "name": "GeoCityCode",
            "type": "Attribute",
            "max_length": 10,
        },
    )
    control: None | bool = field(
        default=None,
        metadata={
            "name": "Control",
            "type": "Attribute",
        },
    )
    branch_code: None | str = field(
        default=None,
        metadata={
            "name": "BranchCode",
            "type": "Attribute",
            "min_length": 1,
            "max_length": 25,
        },
    )
    currency: None | str = field(
        default=None,
        metadata={
            "name": "Currency",
            "type": "Attribute",
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
    ursync_to: None | bool = field(
        default=None,
        metadata={
            "name": "URSyncTo",
            "type": "Attribute",
        },
    )
