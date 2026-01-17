from dataclasses import dataclass, field
from typing import Optional

from ipxact.models.description import Description
from ipxact.models.interface_type import InterfaceType
from ipxact.models.vendor_extensions import VendorExtensions

__NAMESPACE__ = "http://www.accellera.org/XMLSchema/IPXACT/1685-2022"


@dataclass
class MonitorInterfaceType(InterfaceType):
    """
    Hierarchical reference to an interface being monitored or monitoring
    another interface.

    :ivar description:
    :ivar vendor_extensions:
    :ivar path: A decending hierarchical (slash separated - example
        x/y/z) path to the component instance containing the specified
        component instance in componentInterfaceRef. If not specified
        the componentInterfaceRef instance shall exist in the current
        design.
    """

    class Meta:
        name = "monitorInterfaceType"

    description: Optional[Description] = field(
        default=None,
        metadata={
            "type": "Element",
            "namespace": "http://www.accellera.org/XMLSchema/IPXACT/1685-2022",
        },
    )
    vendor_extensions: Optional[VendorExtensions] = field(
        default=None,
        metadata={
            "name": "vendorExtensions",
            "type": "Element",
            "namespace": "http://www.accellera.org/XMLSchema/IPXACT/1685-2022",
        },
    )
    path: Optional[str] = field(
        default=None,
        metadata={
            "type": "Attribute",
            "white_space": "collapse",
            "pattern": r"\i[\p{L}\p{N}\.\-:_]*|\i[\p{L}\p{N}\.\-:_]*/\i[\p{L}\p{N}\.\-:_]*|(\i[\p{L}\p{N}\.\-:_]*/)+[\i\p{L}\p{N}\.\-:_]*",
        },
    )
