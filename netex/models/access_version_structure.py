from dataclasses import dataclass, field
from typing import Optional

from .access_end_structure import AccessEndStructure
from .transfer_version_structure import TransferVersionStructure

__NAMESPACE__ = "http://www.netex.org.uk/netex"


@dataclass
class AccessVersionStructure(TransferVersionStructure):
    class Meta:
        name = "Access_VersionStructure"

    from_value: Optional[AccessEndStructure] = field(
        default=None,
        metadata={
            "name": "From",
            "type": "Element",
            "namespace": "http://www.netex.org.uk/netex",
            "required": True,
        },
    )
    to: Optional[AccessEndStructure] = field(
        default=None,
        metadata={
            "name": "To",
            "type": "Element",
            "namespace": "http://www.netex.org.uk/netex",
            "required": True,
        },
    )
