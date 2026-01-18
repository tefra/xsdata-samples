from dataclasses import dataclass, field
from typing import Optional

from .connection_end_structure import ConnectionEndStructure
from .external_object_ref_structure import ExternalObjectRefStructure
from .transfer_version_structure import TransferVersionStructure

__NAMESPACE__ = "http://www.netex.org.uk/netex"


@dataclass
class ConnectionVersionStructure(TransferVersionStructure):
    class Meta:
        name = "Connection_VersionStructure"

    external_connection_link_ref: ExternalObjectRefStructure | None = field(
        default=None,
        metadata={
            "name": "ExternalConnectionLinkRef",
            "type": "Element",
            "namespace": "http://www.netex.org.uk/netex",
        },
    )
    from_value: ConnectionEndStructure | None = field(
        default=None,
        metadata={
            "name": "From",
            "type": "Element",
            "namespace": "http://www.netex.org.uk/netex",
        },
    )
    to: ConnectionEndStructure | None = field(
        default=None,
        metadata={
            "name": "To",
            "type": "Element",
            "namespace": "http://www.netex.org.uk/netex",
        },
    )
    transfer_only: bool | None = field(
        default=None,
        metadata={
            "name": "TransferOnly",
            "type": "Element",
            "namespace": "http://www.netex.org.uk/netex",
        },
    )
