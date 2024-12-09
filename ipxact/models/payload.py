from dataclasses import dataclass, field
from typing import Optional

from ipxact.models.payload_type import PayloadType
from ipxact.models.vendor_extensions import VendorExtensions

__NAMESPACE__ = "http://www.accellera.org/XMLSchema/IPXACT/1685-2022"


@dataclass
class Payload:
    """
    Defines the structure of data transported by this port.

    :ivar name: Defines the name of the payload. For example: TLM2 or
        TLM1
    :ivar type_value: Defines the type of the payload.
    :ivar extension: Defines the name of the payload extension. If
        attribute is not specified, it is by default optional.
    :ivar vendor_extensions:
    """

    class Meta:
        name = "payload"
        namespace = "http://www.accellera.org/XMLSchema/IPXACT/1685-2022"

    name: Optional[str] = field(
        default=None,
        metadata={
            "type": "Element",
        },
    )
    type_value: Optional[PayloadType] = field(
        default=None,
        metadata={
            "name": "type",
            "type": "Element",
            "required": True,
        },
    )
    extension: Optional["Payload.Extension"] = field(
        default=None,
        metadata={
            "type": "Element",
        },
    )
    vendor_extensions: Optional[VendorExtensions] = field(
        default=None,
        metadata={
            "name": "vendorExtensions",
            "type": "Element",
        },
    )

    @dataclass
    class Extension:
        """
        :ivar value:
        :ivar mandatory: True if the payload extension is mandatory.
        """

        value: str = field(
            default="",
            metadata={
                "required": True,
            },
        )
        mandatory: bool = field(
            default=False,
            metadata={
                "type": "Attribute",
            },
        )
