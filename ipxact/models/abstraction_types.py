from dataclasses import dataclass, field
from typing import Optional

from ipxact.models.configurable_library_ref_type import (
    ConfigurableLibraryRefType,
)
from ipxact.models.part_select import PartSelect
from ipxact.models.range import Range
from ipxact.models.unsigned_bit_vector_expression import (
    UnsignedBitVectorExpression,
)
from ipxact.models.vendor_extensions import VendorExtensions
from ipxact.models.view_ref import ViewRef

__NAMESPACE__ = "http://www.accellera.org/XMLSchema/IPXACT/1685-2022"


@dataclass
class AbstractionTypes:
    """
    :ivar abstraction_type: The abstraction type/level of this
        interface. Refers to abstraction definition using vendor,
        library, name, version attributes along with any configurable
        element values needed to configure this abstraction. Bus
        definition can be found through a reference in this file.
    """

    class Meta:
        name = "abstractionTypes"
        namespace = "http://www.accellera.org/XMLSchema/IPXACT/1685-2022"

    abstraction_type: list["AbstractionTypes.AbstractionType"] = field(
        default_factory=list,
        metadata={
            "name": "abstractionType",
            "type": "Element",
            "min_occurs": 1,
        },
    )

    @dataclass
    class AbstractionType:
        """
        :ivar view_ref: A reference to a view name in the file for which
            this type applies.
        :ivar abstraction_ref: Provides the VLNV of the abstraction
            type.
        :ivar port_maps: Listing of maps between component ports and bus
            ports.
        :ivar id:
        """

        view_ref: list[ViewRef] = field(
            default_factory=list,
            metadata={
                "name": "viewRef",
                "type": "Element",
            },
        )
        abstraction_ref: Optional[ConfigurableLibraryRefType] = field(
            default=None,
            metadata={
                "name": "abstractionRef",
                "type": "Element",
                "required": True,
            },
        )
        port_maps: Optional["AbstractionTypes.AbstractionType.PortMaps"] = (
            field(
                default=None,
                metadata={
                    "name": "portMaps",
                    "type": "Element",
                },
            )
        )
        id: Optional[str] = field(
            default=None,
            metadata={
                "type": "Attribute",
                "namespace": "http://www.w3.org/XML/1998/namespace",
            },
        )

        @dataclass
        class PortMaps:
            """
            :ivar port_map: Maps a component's port to a port in a bus
                description. This is the logical to physical mapping.
                The logical pin comes from the bus interface and the
                physical pin from the component.
            """

            port_map: list[
                "AbstractionTypes.AbstractionType.PortMaps.PortMap"
            ] = field(
                default_factory=list,
                metadata={
                    "name": "portMap",
                    "type": "Element",
                    "min_occurs": 1,
                },
            )

            @dataclass
            class PortMap:
                """
                :ivar logical_port: Logical port from abstraction
                    definition
                :ivar physical_port: Physical port from this component
                :ivar logical_tie_off: Identifies a value to tie this
                    logical port to.
                :ivar is_informative: When true, indicates that this
                    portMap element is for information purpose only.
                :ivar vendor_extensions:
                :ivar id:
                :ivar invert: Indicates that the connection between the
                    logical and physical ports should include an
                    inversion.
                """

                logical_port: Optional[
                    "AbstractionTypes.AbstractionType.PortMaps.PortMap.LogicalPort"
                ] = field(
                    default=None,
                    metadata={
                        "name": "logicalPort",
                        "type": "Element",
                        "required": True,
                    },
                )
                physical_port: Optional[
                    "AbstractionTypes.AbstractionType.PortMaps.PortMap.PhysicalPort"
                ] = field(
                    default=None,
                    metadata={
                        "name": "physicalPort",
                        "type": "Element",
                    },
                )
                logical_tie_off: Optional[UnsignedBitVectorExpression] = field(
                    default=None,
                    metadata={
                        "name": "logicalTieOff",
                        "type": "Element",
                    },
                )
                is_informative: Optional[bool] = field(
                    default=None,
                    metadata={
                        "name": "isInformative",
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
                id: Optional[str] = field(
                    default=None,
                    metadata={
                        "type": "Attribute",
                        "namespace": "http://www.w3.org/XML/1998/namespace",
                    },
                )
                invert: object = field(
                    default="false",
                    metadata={
                        "type": "Attribute",
                    },
                )

                @dataclass
                class LogicalPort:
                    """
                    :ivar name: Bus port name as specified inside the
                        abstraction definition
                    :ivar range:
                    :ivar id:
                    """

                    name: Optional[str] = field(
                        default=None,
                        metadata={
                            "type": "Element",
                            "required": True,
                        },
                    )
                    range: Optional[Range] = field(
                        default=None,
                        metadata={
                            "type": "Element",
                        },
                    )
                    id: Optional[str] = field(
                        default=None,
                        metadata={
                            "type": "Attribute",
                            "namespace": "http://www.w3.org/XML/1998/namespace",
                        },
                    )

                @dataclass
                class PhysicalPort:
                    """
                    :ivar name: Component port name as specified inside
                        the model port section
                    :ivar part_select:
                    :ivar sub_port:
                    :ivar id:
                    """

                    name: Optional[str] = field(
                        default=None,
                        metadata={
                            "type": "Element",
                            "required": True,
                            "white_space": "collapse",
                            "pattern": r"\i[\p{L}\p{N}\.\-:_]*",
                        },
                    )
                    part_select: Optional[PartSelect] = field(
                        default=None,
                        metadata={
                            "name": "partSelect",
                            "type": "Element",
                        },
                    )
                    sub_port: list[
                        "AbstractionTypes.AbstractionType.PortMaps.PortMap.PhysicalPort.SubPort"
                    ] = field(
                        default_factory=list,
                        metadata={
                            "name": "subPort",
                            "type": "Element",
                        },
                    )
                    id: Optional[str] = field(
                        default=None,
                        metadata={
                            "type": "Attribute",
                            "namespace": "http://www.w3.org/XML/1998/namespace",
                        },
                    )

                    @dataclass
                    class SubPort:
                        """
                        :ivar name: Component port subPort name as
                            specified inside the model port section
                        :ivar part_select:
                        :ivar id:
                        """

                        name: Optional[str] = field(
                            default=None,
                            metadata={
                                "type": "Element",
                                "required": True,
                                "white_space": "collapse",
                                "pattern": r"\i[\p{L}\p{N}\.\-:_]*",
                            },
                        )
                        part_select: Optional[PartSelect] = field(
                            default=None,
                            metadata={
                                "name": "partSelect",
                                "type": "Element",
                            },
                        )
                        id: Optional[str] = field(
                            default=None,
                            metadata={
                                "type": "Attribute",
                                "namespace": "http://www.w3.org/XML/1998/namespace",
                            },
                        )
