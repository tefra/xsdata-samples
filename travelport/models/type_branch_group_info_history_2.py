from __future__ import annotations

from dataclasses import dataclass, field

from travelport.models.type_profile_info_2 import TypeProfileInfo2

__NAMESPACE__ = "http://www.travelport.com/schema/uprofile_v37_0"


@dataclass(kw_only=True)
class TypeBranchGroupInfoHistory2(TypeProfileInfo2):
    """
    History Element for BranchGroupInfo.

    Parameters
    ----------
    name
        Name of the BranchGroup
    branch_group_code
        Zircon site ID
    ursync_to
        Identify if Universal Record synch is activated at Branch Group
        Level.
    """

    class Meta:
        name = "typeBranchGroupInfoHistory"

    name: None | str = field(
        default=None,
        metadata={
            "name": "Name",
            "type": "Attribute",
            "min_length": 1,
            "max_length": 128,
        },
    )
    branch_group_code: None | str = field(
        default=None,
        metadata={
            "name": "BranchGroupCode",
            "type": "Attribute",
            "min_length": 1,
            "max_length": 25,
        },
    )
    ursync_to: None | bool = field(
        default=None,
        metadata={
            "name": "URSyncTo",
            "type": "Attribute",
        },
    )
