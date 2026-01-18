from __future__ import annotations

from dataclasses import dataclass, field

from ipxact.models.description import Description
from ipxact.models.display_name import DisplayName
from ipxact.models.parameters import Parameters
from ipxact.models.short_description import ShortDescription
from ipxact.models.vendor_extensions import VendorExtensions

__NAMESPACE__ = "http://www.accellera.org/XMLSchema/IPXACT/1685-2022"


@dataclass(kw_only=True)
class BankedSubspaceType:
    """
    Subspace references inside banks do not specify an address.

    :ivar name: Unique name
    :ivar display_name:
    :ivar short_description:
    :ivar description:
    :ivar parameters: Any parameters that may apply to the subspace
        reference.
    :ivar vendor_extensions:
    :ivar initiator_ref: For subspaceMap elements, this attribute
        identifies the initiator that contains the address space to be
        mapped.
    :ivar id:
    """

    class Meta:
        name = "bankedSubspaceType"

    name: None | str = field(
        default=None,
        metadata={
            "type": "Element",
            "namespace": "http://www.accellera.org/XMLSchema/IPXACT/1685-2022",
        },
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
    parameters: None | Parameters = field(
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
    initiator_ref: str = field(
        metadata={
            "name": "initiatorRef",
            "type": "Attribute",
            "required": True,
        }
    )
    id: None | str = field(
        default=None,
        metadata={
            "type": "Attribute",
            "namespace": "http://www.w3.org/XML/1998/namespace",
        },
    )
