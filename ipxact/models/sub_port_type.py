from __future__ import annotations

from dataclasses import dataclass, field
from typing import Optional

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


@dataclass
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

    name: str | None = field(
        default=None,
        metadata={
            "type": "Element",
            "namespace": "http://www.accellera.org/XMLSchema/IPXACT/1685-2022",
            "required": True,
            "white_space": "collapse",
            "pattern": r"\i[\p{L}\p{N}\.\-:_]*",
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
    wire: PortWireType | None = field(
        default=None,
        metadata={
            "type": "Element",
            "namespace": "http://www.accellera.org/XMLSchema/IPXACT/1685-2022",
        },
    )
    structured: PortStructuredType | None = field(
        default=None,
        metadata={
            "type": "Element",
            "namespace": "http://www.accellera.org/XMLSchema/IPXACT/1685-2022",
        },
    )
    arrays: Arrays | None = field(
        default=None,
        metadata={
            "type": "Element",
            "namespace": "http://www.accellera.org/XMLSchema/IPXACT/1685-2022",
        },
    )
    access: PortAccessType1 | None = field(
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
    is_io: bool | None = field(
        default=None,
        metadata={
            "name": "isIO",
            "type": "Attribute",
        },
    )


@dataclass
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

    struct: PortStructuredType.Struct | None = field(
        default=None,
        metadata={
            "type": "Element",
            "namespace": "http://www.accellera.org/XMLSchema/IPXACT/1685-2022",
        },
    )
    union: PortStructuredType.UnionType | None = field(
        default=None,
        metadata={
            "type": "Element",
            "namespace": "http://www.accellera.org/XMLSchema/IPXACT/1685-2022",
        },
    )
    interface: PortStructuredType.Interface | None = field(
        default=None,
        metadata={
            "type": "Element",
            "namespace": "http://www.accellera.org/XMLSchema/IPXACT/1685-2022",
        },
    )
    vectors: ExtendedVectorsType | None = field(
        default=None,
        metadata={
            "type": "Element",
            "namespace": "http://www.accellera.org/XMLSchema/IPXACT/1685-2022",
        },
    )
    sub_ports: PortStructuredType.SubPorts | None = field(
        default=None,
        metadata={
            "name": "subPorts",
            "type": "Element",
            "namespace": "http://www.accellera.org/XMLSchema/IPXACT/1685-2022",
        },
    )
    struct_port_type_defs: StructPortTypeDefs | None = field(
        default=None,
        metadata={
            "name": "structPortTypeDefs",
            "type": "Element",
            "namespace": "http://www.accellera.org/XMLSchema/IPXACT/1685-2022",
            "required": True,
        },
    )
    packed: bool = field(
        default=True,
        metadata={
            "type": "Attribute",
        },
    )

    @dataclass
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

    @dataclass
    class Struct:
        """
        :ivar direction: The direction of a wire style port. The basic
            directions for a port are 'in' for input ports, 'out' for
            output port and 'inout' for bidirectional and tristate
            ports. A value of 'phantom' is also allowed and define a
            port that exist on the IP-XACT component but not on the HDL
            model.
        """

        direction: ComponentPortDirectionType | None = field(
            default=None,
            metadata={
                "type": "Attribute",
            },
        )

    @dataclass
    class UnionType:
        """
        :ivar direction: The direction of a wire style port. The basic
            directions for a port are 'in' for input ports, 'out' for
            output port and 'inout' for bidirectional and tristate
            ports. A value of 'phantom' is also allowed and define a
            port that exist on the IP-XACT component but not on the HDL
            model.
        """

        direction: ComponentPortDirectionType | None = field(
            default=None,
            metadata={
                "type": "Attribute",
            },
        )

    @dataclass
    class Interface:
        phantom: bool | None = field(
            default=None,
            metadata={
                "type": "Attribute",
            },
        )
