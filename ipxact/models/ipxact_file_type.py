from dataclasses import dataclass, field

from ipxact.models.description import Description
from ipxact.models.ipxact_uri import IpxactUri
from ipxact.models.library_ref_type import LibraryRefType
from ipxact.models.vendor_extensions import VendorExtensions

__NAMESPACE__ = "http://www.accellera.org/XMLSchema/IPXACT/1685-2022"


@dataclass
class IpxactFileType:
    """
    :ivar vlnv: VLNV of the IP-XACT file being cataloged.
    :ivar name: Name of the IP-XACT file being cataloged.
    :ivar description:
    :ivar vendor_extensions:
    :ivar id:
    """

    class Meta:
        name = "ipxactFileType"

    vlnv: LibraryRefType | None = field(
        default=None,
        metadata={
            "type": "Element",
            "namespace": "http://www.accellera.org/XMLSchema/IPXACT/1685-2022",
            "required": True,
        },
    )
    name: IpxactUri | None = field(
        default=None,
        metadata={
            "type": "Element",
            "namespace": "http://www.accellera.org/XMLSchema/IPXACT/1685-2022",
            "required": True,
        },
    )
    description: Description | None = field(
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
    id: str | None = field(
        default=None,
        metadata={
            "type": "Attribute",
            "namespace": "http://www.w3.org/XML/1998/namespace",
        },
    )
