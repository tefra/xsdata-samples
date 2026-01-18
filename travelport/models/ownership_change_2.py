from __future__ import annotations

from dataclasses import dataclass, field

__NAMESPACE__ = "http://www.travelport.com/schema/common_v32_0"


@dataclass(kw_only=True)
class OwnershipChange2:
    """
    Element to change the ownership of the PNR in the UR.

    PROVIDER SUPPORTED: Worldspan and JAL.

    Parameters
    ----------
    owning_pcc
        New owning PCC of the PNR.
    """

    class Meta:
        name = "OwnershipChange"
        namespace = "http://www.travelport.com/schema/common_v32_0"

    owning_pcc: str = field(
        metadata={
            "name": "OwningPCC",
            "type": "Attribute",
            "required": True,
        }
    )
