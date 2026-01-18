from __future__ import annotations

from dataclasses import dataclass, field

from ipxact.models.slices_type import SlicesType
from ipxact.models.vendor_extensions import VendorExtensions

__NAMESPACE__ = "http://www.accellera.org/XMLSchema/IPXACT/1685-2022"


@dataclass(kw_only=True)
class ClearboxElementRefType:
    """
    Reference to a clearboxElement within a view.

    The 'name' attribute must refer to a clearboxElement defined within
    this component.

    :ivar location: The contents of each location element can be used to
        specified one location (HDL Path) through the referenced
        clearBoxElement is accessible.
    :ivar vendor_extensions:
    :ivar name: Reference to a clearboxElement defined within this
        component.
    :ivar id:
    """

    class Meta:
        name = "clearboxElementRefType"

    location: list[SlicesType] = field(
        default_factory=list,
        metadata={
            "type": "Element",
            "namespace": "http://www.accellera.org/XMLSchema/IPXACT/1685-2022",
            "min_occurs": 1,
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
    name: str = field(
        metadata={
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
