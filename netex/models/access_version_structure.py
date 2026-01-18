from __future__ import annotations

from dataclasses import dataclass, field

from .access_end_structure import AccessEndStructure
from .transfer_version_structure import TransferVersionStructure

__NAMESPACE__ = "http://www.netex.org.uk/netex"


@dataclass(kw_only=True)
class AccessVersionStructure(TransferVersionStructure):
    class Meta:
        name = "Access_VersionStructure"

    from_value: AccessEndStructure = field(
        metadata={
            "name": "From",
            "type": "Element",
            "namespace": "http://www.netex.org.uk/netex",
            "required": True,
        }
    )
    to: AccessEndStructure = field(
        metadata={
            "name": "To",
            "type": "Element",
            "namespace": "http://www.netex.org.uk/netex",
            "required": True,
        }
    )
