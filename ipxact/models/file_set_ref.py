from __future__ import annotations

from dataclasses import dataclass, field

from ipxact.models.vendor_extensions import VendorExtensions

__NAMESPACE__ = "http://www.accellera.org/XMLSchema/IPXACT/1685-2022"


@dataclass(kw_only=True)
class FileSetRef:
    """
    A reference to a fileSet.

    :ivar local_name: Refers to a fileSet defined within this
        description.
    :ivar vendor_extensions:
    :ivar id:
    """

    class Meta:
        name = "fileSetRef"
        namespace = "http://www.accellera.org/XMLSchema/IPXACT/1685-2022"

    local_name: str = field(
        metadata={
            "name": "localName",
            "type": "Element",
            "required": True,
        }
    )
    vendor_extensions: None | VendorExtensions = field(
        default=None,
        metadata={
            "name": "vendorExtensions",
            "type": "Element",
        },
    )
    id: None | str = field(
        default=None,
        metadata={
            "type": "Attribute",
            "namespace": "http://www.w3.org/XML/1998/namespace",
        },
    )
