from __future__ import annotations

from dataclasses import dataclass, field

__NAMESPACE__ = "http://www.travelport.com/schema/common_v33_0"


@dataclass
class OwnershipChange3:
    """Element to change the ownership of the PNR in the UR.

    PROVIDER SUPPORTED: Worldspan and JAL.

    Parameters
    ----------
    owning_pcc
        New owning PCC of the PNR.
    """

    class Meta:
        name = "OwnershipChange"
        namespace = "http://www.travelport.com/schema/common_v33_0"

    owning_pcc: None | str = field(
        default=None,
        metadata={
            "name": "OwningPCC",
            "type": "Attribute",
            "required": True,
        },
    )
