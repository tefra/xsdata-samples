from __future__ import annotations

from dataclasses import dataclass, field

from .connection_end_structure import ConnectionEndStructure
from .external_object_ref_structure import ExternalObjectRefStructure
from .transfer_version_structure import TransferVersionStructure

__NAMESPACE__ = "http://www.netex.org.uk/netex"


@dataclass(kw_only=True)
class ConnectionVersionStructure(TransferVersionStructure):
    class Meta:
        name = "Connection_VersionStructure"

    external_connection_link_ref: None | ExternalObjectRefStructure = field(
        default=None,
        metadata={
            "name": "ExternalConnectionLinkRef",
            "type": "Element",
            "namespace": "http://www.netex.org.uk/netex",
        },
    )
    from_value: None | ConnectionEndStructure = field(
        default=None,
        metadata={
            "name": "From",
            "type": "Element",
            "namespace": "http://www.netex.org.uk/netex",
        },
    )
    to: None | ConnectionEndStructure = field(
        default=None,
        metadata={
            "name": "To",
            "type": "Element",
            "namespace": "http://www.netex.org.uk/netex",
        },
    )
    transfer_only: None | bool = field(
        default=None,
        metadata={
            "name": "TransferOnly",
            "type": "Element",
            "namespace": "http://www.netex.org.uk/netex",
        },
    )
