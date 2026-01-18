from __future__ import annotations

from dataclasses import dataclass, field

from ipxact.models.description import Description
from ipxact.models.display_name import DisplayName
from ipxact.models.short_description import ShortDescription
from ipxact.models.value import Value
from ipxact.models.vendor_extensions import VendorExtensions

__NAMESPACE__ = "http://www.accellera.org/XMLSchema/IPXACT/1685-2022"


@dataclass(kw_only=True)
class NameValuePairType:
    """
    Name and value type for use in resolvable elements.

    :ivar name: Unique name
    :ivar display_name:
    :ivar short_description:
    :ivar description:
    :ivar value:
    :ivar vendor_extensions:
    :ivar id:
    """

    class Meta:
        name = "nameValuePairType"

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
    value: Value = field(
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
    id: None | str = field(
        default=None,
        metadata={
            "type": "Attribute",
            "namespace": "http://www.w3.org/XML/1998/namespace",
        },
    )
