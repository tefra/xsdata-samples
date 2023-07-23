from __future__ import annotations
from dataclasses import dataclass, field

__NAMESPACE__ = "http://www.travelport.com/schema/uprofile_v37_0"


@dataclass
class BridgeBranch:
    """
    Summary information for the Bridge Branch.

    Parameters
    ----------
    profile_id
        The Bridge Branch Profile ID
    branch_code
        The Bridge Branch Provisioning Code
    name
        The Bridge Branch Name
    default
        Indicates that this branch is the default branch. The default is
        false.
    """
    class Meta:
        namespace = "http://www.travelport.com/schema/uprofile_v37_0"

    profile_id: None | int = field(
        default=None,
        metadata={
            "name": "ProfileID",
            "type": "Attribute",
            "required": True,
        }
    )
    branch_code: None | str = field(
        default=None,
        metadata={
            "name": "BranchCode",
            "type": "Attribute",
            "required": True,
            "min_length": 1,
            "max_length": 25,
        }
    )
    name: None | str = field(
        default=None,
        metadata={
            "name": "Name",
            "type": "Attribute",
            "required": True,
            "min_length": 1,
            "max_length": 128,
        }
    )
    default: bool = field(
        default=False,
        metadata={
            "name": "Default",
            "type": "Attribute",
        }
    )
