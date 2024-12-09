from dataclasses import dataclass, field
from typing import Optional

from ipxact.models.description import Description
from ipxact.models.interface_type import InterfaceType
from ipxact.models.vendor_extensions import VendorExtensions

__NAMESPACE__ = "http://www.accellera.org/XMLSchema/IPXACT/1685-2022"


@dataclass
class ActiveInterface(InterfaceType):
    """
    :ivar description:
    :ivar exclude_ports: The list of physical ports to be excluded from
        an interface based connection. Analogous to the removing the
        port map element for the named ports.
    :ivar vendor_extensions:
    """

    class Meta:
        name = "activeInterface"
        namespace = "http://www.accellera.org/XMLSchema/IPXACT/1685-2022"

    description: Optional[Description] = field(
        default=None,
        metadata={
            "type": "Element",
        },
    )
    exclude_ports: Optional["ActiveInterface.ExcludePorts"] = field(
        default=None,
        metadata={
            "name": "excludePorts",
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
    class ExcludePorts:
        """
        :ivar exclude_port: The name of a physical port to be excluded
            from the interface based connection.
        """

        exclude_port: list["ActiveInterface.ExcludePorts.ExcludePort"] = field(
            default_factory=list,
            metadata={
                "name": "excludePort",
                "type": "Element",
                "min_occurs": 1,
            },
        )

        @dataclass
        class ExcludePort:
            value: str = field(
                default="",
                metadata={
                    "required": True,
                    "white_space": "collapse",
                    "pattern": r"\i[\p{L}\p{N}\.\-:_]*",
                },
            )
            id: Optional[str] = field(
                default=None,
                metadata={
                    "type": "Attribute",
                    "namespace": "http://www.w3.org/XML/1998/namespace",
                },
            )
