from __future__ import annotations

from dataclasses import dataclass, field

from ipxact.models.payload import Payload
from ipxact.models.protocol_type_type import ProtocolTypeType

__NAMESPACE__ = "http://www.accellera.org/XMLSchema/IPXACT/1685-2022"


@dataclass(kw_only=True)
class Protocol:
    """
    defines the protocol type.

    Defaults to tlm_base_protocol_type for TLM sockets.
    """

    class Meta:
        name = "protocol"
        namespace = "http://www.accellera.org/XMLSchema/IPXACT/1685-2022"

    protocol_type: Protocol.ProtocolType = field(
        metadata={
            "name": "protocolType",
            "type": "Element",
            "required": True,
        }
    )
    payload: None | Payload = field(
        default=None,
        metadata={
            "type": "Element",
        },
    )

    @dataclass(kw_only=True)
    class ProtocolType:
        value: ProtocolTypeType = field(
            metadata={
                "required": True,
            }
        )
        custom: None | str = field(
            default=None,
            metadata={
                "type": "Attribute",
            },
        )
