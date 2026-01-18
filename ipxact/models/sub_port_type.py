from __future__ import annotations

from dataclasses import dataclass, field

from ipxact.models.arrays import Arrays
from ipxact.models.component_port_direction_type import (
    ComponentPortDirectionType,
)
from ipxact.models.description import Description
from ipxact.models.display_name import DisplayName
from ipxact.models.extended_vectors_type import ExtendedVectorsType
from ipxact.models.port_access_type_1 import PortAccessType1
from ipxact.models.port_wire_type import PortWireType
from ipxact.models.short_description import ShortDescription
from ipxact.models.struct_port_type_defs import StructPortTypeDefs
from ipxact.models.vendor_extensions import VendorExtensions

__NAMESPACE__ = "http://www.accellera.org/XMLSchema/IPXACT/1685-2022"


@dataclass(kw_only=True)
class SubPortType:
    """
    A port description, giving a name and an access type for high level
    ports.

    :ivar name: Unique name
    :ivar display_name:
    :ivar short_description:
    :ivar description:
    :ivar wire: Defines a port whose type resolves to simple bits.
    :ivar structured:
    :ivar arrays:
    :ivar access: Port access characteristics.
    :ivar vendor_extensions:
    :ivar id:
    :ivar is_io: When present and set to 'true' identifies this port as
        being an I/O to the containing structure port type.  Only valid
        for subPorts contained in a structured port with
        structType='interface'.
    """

    class Meta:
        name = "subPortType"

    name: str = field(
        metadata={
            "type": "Element",
            "namespace": "http://www.accellera.org/XMLSchema/IPXACT/1685-2022",
            "required": True,
            "white_space": "collapse",
            "pattern": r"\i[\p{L}\p{N}\.\-:_]*",
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
    wire: None | PortWireType = field(
        default=None,
        metadata={
            "type": "Element",
            "namespace": "http://www.accellera.org/XMLSchema/IPXACT/1685-2022",
        },
    )
    structured: None | PortStructuredType = field(
        default=None,
        metadata={
            "type": "Element",
            "namespace": "http://www.accellera.org/XMLSchema/IPXACT/1685-2022",
        },
    )
    arrays: None | Arrays = field(
        default=None,
        metadata={
            "type": "Element",
            "namespace": "http://www.accellera.org/XMLSchema/IPXACT/1685-2022",
        },
    )
    access: None | PortAccessType1 = field(
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
    id: None | str = field(
        default=None,
        metadata={
            "type": "Attribute",
            "namespace": "http://www.w3.org/XML/1998/namespace",
        },
    )
    is_io: None | bool = field(
        default=None,
        metadata={
            "name": "isIO",
            "type": "Attribute",
        },
    )


@dataclass(kw_only=True)
class PortStructuredType:
    """
    :ivar struct:
    :ivar union:
    :ivar interface:
    :ivar vectors: Vectored information.
    :ivar sub_ports:
    :ivar struct_port_type_defs:
    :ivar packed: When not present or set to 'true' indicates that this
        structured port is 'packed'.  If present and set to 'false',
        indicates that this structured port is 'unpacked'.
    """

    class Meta:
        name = "portStructuredType"

    struct: None | PortStructuredType.Struct = field(
        default=None,
        metadata={
            "type": "Element",
            "namespace": "http://www.accellera.org/XMLSchema/IPXACT/1685-2022",
        },
    )
    union: None | PortStructuredType.UnionType = field(
        default=None,
        metadata={
            "type": "Element",
            "namespace": "http://www.accellera.org/XMLSchema/IPXACT/1685-2022",
        },
    )
    interface: None | PortStructuredType.Interface = field(
        default=None,
        metadata={
            "type": "Element",
            "namespace": "http://www.accellera.org/XMLSchema/IPXACT/1685-2022",
        },
    )
    vectors: None | ExtendedVectorsType = field(
        default=None,
        metadata={
            "type": "Element",
            "namespace": "http://www.accellera.org/XMLSchema/IPXACT/1685-2022",
        },
    )
    sub_ports: None | PortStructuredType.SubPorts = field(
        default=None,
        metadata={
            "name": "subPorts",
            "type": "Element",
            "namespace": "http://www.accellera.org/XMLSchema/IPXACT/1685-2022",
        },
    )
    struct_port_type_defs: StructPortTypeDefs = field(
        metadata={
            "name": "structPortTypeDefs",
            "type": "Element",
            "namespace": "http://www.accellera.org/XMLSchema/IPXACT/1685-2022",
            "required": True,
        }
    )
    packed: bool = field(
        default=True,
        metadata={
            "type": "Attribute",
        },
    )

    @dataclass(kw_only=True)
    class SubPorts:
        sub_port: list[SubPortType] = field(
            default_factory=list,
            metadata={
                "name": "subPort",
                "type": "Element",
                "namespace": "http://www.accellera.org/XMLSchema/IPXACT/1685-2022",
                "min_occurs": 1,
            },
        )

    @dataclass(kw_only=True)
    class Struct:
        """
        :ivar direction: The direction of a wire style port. The basic
            directions for a port are 'in' for input ports, 'out' for
            output port and 'inout' for bidirectional and tristate
            ports. A value of 'phantom' is also allowed and define a
            port that exist on the IP-XACT component but not on the HDL
            model.
        """

        direction: None | ComponentPortDirectionType = field(
            default=None,
            metadata={
                "type": "Attribute",
            },
        )

    @dataclass(kw_only=True)
    class UnionType:
        """
        :ivar direction: The direction of a wire style port. The basic
            directions for a port are 'in' for input ports, 'out' for
            output port and 'inout' for bidirectional and tristate
            ports. A value of 'phantom' is also allowed and define a
            port that exist on the IP-XACT component but not on the HDL
            model.
        """

        direction: None | ComponentPortDirectionType = field(
            default=None,
            metadata={
                "type": "Attribute",
            },
        )

    @dataclass(kw_only=True)
    class Interface:
        phantom: None | bool = field(
            default=None,
            metadata={
                "type": "Attribute",
            },
        )
