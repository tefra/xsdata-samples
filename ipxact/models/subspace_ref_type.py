from dataclasses import dataclass, field
from typing import Optional

from ipxact.models.description import Description
from ipxact.models.display_name import DisplayName
from ipxact.models.parameters import Parameters
from ipxact.models.short_description import ShortDescription
from ipxact.models.signed_longint_expression import SignedLongintExpression
from ipxact.models.vendor_extensions import VendorExtensions

__NAMESPACE__ = "http://www.accellera.org/XMLSchema/IPXACT/1685-2022"


@dataclass
class SubspaceRefType:
    """
    Address subspace type.

    Its subspaceReference attribute references the subspace from which the
    dimensions are taken.

    :ivar name: Unique name
    :ivar display_name:
    :ivar short_description:
    :ivar description:
    :ivar base_address: Base of a subspace map. Expressed as the number
        of addressable units from the containing memoryMap.
    :ivar parameters: Any parameters that may apply to the subspace
        reference.
    :ivar vendor_extensions:
    :ivar initiator_ref: For subspaceMap elements, this attribute
        identifies the initiator that contains the address space to be
        mapped.
    :ivar segment_ref: Refernce to a segment of the addressSpace of the
        initiatorRef attribute.
    :ivar id:
    """

    class Meta:
        name = "subspaceRefType"

    name: str | None = field(
        default=None,
        metadata={
            "type": "Element",
            "namespace": "http://www.accellera.org/XMLSchema/IPXACT/1685-2022",
            "required": True,
        },
    )
    display_name: DisplayName | None = field(
        default=None,
        metadata={
            "name": "displayName",
            "type": "Element",
            "namespace": "http://www.accellera.org/XMLSchema/IPXACT/1685-2022",
        },
    )
    short_description: ShortDescription | None = field(
        default=None,
        metadata={
            "name": "shortDescription",
            "type": "Element",
            "namespace": "http://www.accellera.org/XMLSchema/IPXACT/1685-2022",
        },
    )
    description: Description | None = field(
        default=None,
        metadata={
            "type": "Element",
            "namespace": "http://www.accellera.org/XMLSchema/IPXACT/1685-2022",
        },
    )
    base_address: SignedLongintExpression | None = field(
        default=None,
        metadata={
            "name": "baseAddress",
            "type": "Element",
            "namespace": "http://www.accellera.org/XMLSchema/IPXACT/1685-2022",
            "required": True,
        },
    )
    parameters: Parameters | None = field(
        default=None,
        metadata={
            "type": "Element",
            "namespace": "http://www.accellera.org/XMLSchema/IPXACT/1685-2022",
        },
    )
    vendor_extensions: VendorExtensions | None = field(
        default=None,
        metadata={
            "name": "vendorExtensions",
            "type": "Element",
            "namespace": "http://www.accellera.org/XMLSchema/IPXACT/1685-2022",
        },
    )
    initiator_ref: str | None = field(
        default=None,
        metadata={
            "name": "initiatorRef",
            "type": "Attribute",
            "required": True,
        },
    )
    segment_ref: str | None = field(
        default=None,
        metadata={
            "name": "segmentRef",
            "type": "Attribute",
        },
    )
    id: str | None = field(
        default=None,
        metadata={
            "type": "Attribute",
            "namespace": "http://www.w3.org/XML/1998/namespace",
        },
    )
