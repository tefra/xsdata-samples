from __future__ import annotations

from dataclasses import dataclass, field

from ipxact.models.mode_ref import ModeRef
from ipxact.models.unsigned_bit_vector_expression import (
    UnsignedBitVectorExpression,
)

__NAMESPACE__ = "http://www.accellera.org/XMLSchema/IPXACT/1685-2022"


@dataclass(kw_only=True)
class AccessRestrictionType:
    """
    :ivar mode_ref:
    :ivar read_access_mask: Mask to be anded with the readable bits in
        this field to determine the readabe bits in this access mode. If
        not present, the value defaults to "all ones" meaning that read
        access is not blocked.
    :ivar write_access_mask: Mask to be anded with the writable bits in
        this field to determine the writeable bits in this access mode.
        If not present, the value defaults to "all ones" meaning that
        write access is not blocked.
    :ivar id:
    """

    class Meta:
        name = "accessRestrictionType"

    mode_ref: list[ModeRef] = field(
        default_factory=list,
        metadata={
            "name": "modeRef",
            "type": "Element",
            "namespace": "http://www.accellera.org/XMLSchema/IPXACT/1685-2022",
        },
    )
    read_access_mask: None | UnsignedBitVectorExpression = field(
        default=None,
        metadata={
            "name": "readAccessMask",
            "type": "Element",
            "namespace": "http://www.accellera.org/XMLSchema/IPXACT/1685-2022",
        },
    )
    write_access_mask: None | UnsignedBitVectorExpression = field(
        default=None,
        metadata={
            "name": "writeAccessMask",
            "type": "Element",
            "namespace": "http://www.accellera.org/XMLSchema/IPXACT/1685-2022",
        },
    )
    id: None | str = field(
        default=None,
        metadata={
            "type": "Attribute",
            "namespace": "http://www.w3.org/XML/1998/namespace",
        },
    )
