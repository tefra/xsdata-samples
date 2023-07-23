from __future__ import annotations
from dataclasses import dataclass, field

__NAMESPACE__ = "http://www.travelport.com/schema/uprofile_v37_0"


@dataclass
class TypeBridgeBranchCmd:
    """
    Base type for both BridgeBranchAdd and BridgeBranchDelete.

    Parameters
    ----------
    branch_id
        The Branch Profile ID
    branch_code
        The Branch Provisioning Code
    """
    class Meta:
        name = "typeBridgeBranchCmd"

    branch_id: None | int = field(
        default=None,
        metadata={
            "name": "BranchID",
            "type": "Element",
            "namespace": "http://www.travelport.com/schema/uprofile_v37_0",
        }
    )
    branch_code: None | str = field(
        default=None,
        metadata={
            "name": "BranchCode",
            "type": "Element",
            "namespace": "http://www.travelport.com/schema/uprofile_v37_0",
            "min_length": 1,
            "max_length": 25,
        }
    )
