from __future__ import annotations

from dataclasses import dataclass, field

from ipxact.models.description import Description
from ipxact.models.display_name import DisplayName
from ipxact.models.endianess_type import EndianessType
from ipxact.models.qualifier_type import QualifierType
from ipxact.models.short_description import ShortDescription
from ipxact.models.unresolved_unsigned_positive_int_expression import (
    UnresolvedUnsignedPositiveIntExpression,
)
from ipxact.models.unsigned_bit_vector_expression import (
    UnsignedBitVectorExpression,
)
from ipxact.models.vendor_extensions import VendorExtensions

__NAMESPACE__ = "http://www.accellera.org/XMLSchema/IPXACT/1685-2022"


@dataclass(kw_only=True)
class PortPacketFieldType:
    """
    :ivar name: Unique name
    :ivar display_name:
    :ivar short_description:
    :ivar description:
    :ivar width:
    :ivar value:
    :ivar endianness:
    :ivar qualifier: The type of information this port carries a wire
        port can carry both address and data, but may not mix this with
        a clock or reset.
    :ivar vendor_extensions:
    :ivar id:
    """

    class Meta:
        name = "portPacketFieldType"

    name: str = field(
        metadata={
            "type": "Element",
            "namespace": "http://www.accellera.org/XMLSchema/IPXACT/1685-2022",
            "required": True,
        }
    )
    display_name: None | DisplayName = field(
        default=None,
        metadata={
            "name": "displayName",
            "type": "Element",
            "namespace": "http://www.accellera.org/XMLSchema/IPXACT/1685-2022",
        },
    )
    short_description: None | ShortDescription = field(
        default=None,
        metadata={
            "name": "shortDescription",
            "type": "Element",
            "namespace": "http://www.accellera.org/XMLSchema/IPXACT/1685-2022",
        },
    )
    description: None | Description = field(
        default=None,
        metadata={
            "type": "Element",
            "namespace": "http://www.accellera.org/XMLSchema/IPXACT/1685-2022",
        },
    )
    width: UnresolvedUnsignedPositiveIntExpression = field(
        metadata={
            "type": "Element",
            "namespace": "http://www.accellera.org/XMLSchema/IPXACT/1685-2022",
            "required": True,
        }
    )
    value: None | UnsignedBitVectorExpression = field(
        default=None,
        metadata={
            "type": "Element",
            "namespace": "http://www.accellera.org/XMLSchema/IPXACT/1685-2022",
        },
    )
    endianness: None | EndianessType = field(
        default=None,
        metadata={
            "type": "Element",
            "namespace": "http://www.accellera.org/XMLSchema/IPXACT/1685-2022",
        },
    )
    qualifier: None | QualifierType = field(
        default=None,
        metadata={
            "type": "Element",
            "namespace": "http://www.accellera.org/XMLSchema/IPXACT/1685-2022",
        },
    )
    vendor_extensions: None | VendorExtensions = field(
        default=None,
        metadata={
            "name": "vendorExtensions",
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
