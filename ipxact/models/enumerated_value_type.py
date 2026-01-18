from __future__ import annotations

from dataclasses import dataclass, field

from ipxact.models.description import Description
from ipxact.models.display_name import DisplayName
from ipxact.models.enumerated_value_type_usage import EnumeratedValueTypeUsage
from ipxact.models.short_description import ShortDescription
from ipxact.models.unsigned_bit_vector_expression import (
    UnsignedBitVectorExpression,
)
from ipxact.models.vendor_extensions import VendorExtensions

__NAMESPACE__ = "http://www.accellera.org/XMLSchema/IPXACT/1685-2022"


@dataclass(kw_only=True)
class EnumeratedValueType:
    """
    Enumerates specific values that can be assigned to the bit field.

    The name of this enumerated value. This may be used as a token in
    generating code.

    :ivar name: Unique name
    :ivar display_name:
    :ivar short_description:
    :ivar description:
    :ivar value: Enumerated bit field value.
    :ivar vendor_extensions:
    :ivar usage: Usage for the enumeration. 'read' for a software read
        access. 'write' for a software write access. 'read-write' for a
        software read or write access.
    :ivar id:
    """

    class Meta:
        name = "enumeratedValueType"

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
    value: UnsignedBitVectorExpression = field(
        metadata={
            "type": "Element",
            "namespace": "http://www.accellera.org/XMLSchema/IPXACT/1685-2022",
            "required": True,
        }
    )
    vendor_extensions: None | VendorExtensions = field(
        default=None,
        metadata={
            "name": "vendorExtensions",
            "type": "Element",
            "namespace": "http://www.accellera.org/XMLSchema/IPXACT/1685-2022",
        },
    )
    usage: EnumeratedValueTypeUsage = field(
        default=EnumeratedValueTypeUsage.READ_WRITE,
        metadata={
            "type": "Attribute",
        },
    )
    id: None | str = field(
        default=None,
        metadata={
            "type": "Attribute",
            "namespace": "http://www.w3.org/XML/1998/namespace",
        },
    )
