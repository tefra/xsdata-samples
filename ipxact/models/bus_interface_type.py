from __future__ import annotations

from dataclasses import dataclass, field
from typing import Optional

from ipxact.models.abstraction_types import AbstractionTypes
from ipxact.models.addr_space_ref_type import AddrSpaceRefType
from ipxact.models.bits_in_lau import BitsInLau
from ipxact.models.configurable_library_ref_type import (
    ConfigurableLibraryRefType,
)
from ipxact.models.description import Description
from ipxact.models.display_name import DisplayName
from ipxact.models.endianess_type import EndianessType
from ipxact.models.file_set_ref import FileSetRef
from ipxact.models.group import Group
from ipxact.models.memory_map_ref import MemoryMapRef
from ipxact.models.mode_ref import ModeRef
from ipxact.models.monitor_interface_mode import MonitorInterfaceMode
from ipxact.models.parameters import Parameters
from ipxact.models.short_description import ShortDescription
from ipxact.models.signed_longint_expression import SignedLongintExpression
from ipxact.models.transparent_bridge import TransparentBridge
from ipxact.models.unsigned_bit_expression import UnsignedBitExpression
from ipxact.models.unsigned_longint_expression import UnsignedLongintExpression
from ipxact.models.unsigned_positive_longint_expression import (
    UnsignedPositiveLongintExpression,
)
from ipxact.models.vendor_extensions import VendorExtensions

__NAMESPACE__ = "http://www.accellera.org/XMLSchema/IPXACT/1685-2022"


@dataclass
class BusInterfaceType:
    """
    Type definition for a busInterface in a component.

    :ivar name: Unique name
    :ivar display_name:
    :ivar short_description:
    :ivar description:
    :ivar bus_type: The bus type of this interface. Refers to bus
        definition using vendor, library, name, version attributes along
        with any configurable element values needed to configure this
        interface.
    :ivar abstraction_types:
    :ivar initiator: If this element is present, the bus interface can
        serve as a initiator.  This element encapsulates additional
        information related to its role as initiator.
    :ivar target: If this element is present, the bus interface can
        serve as a target.
    :ivar system: If this element is present, the bus interface is a
        system interface, neither initiator nor target, with a specific
        function on the bus.
    :ivar mirrored_target: If this element is present, the bus interface
        represents a mirrored target interface. All directional
        constraints on ports are reversed relative to the specification
        in the bus definition.
    :ivar mirrored_initiator: If this element is present, the bus
        interface represents a mirrored initiator interface. All
        directional constraints on ports are reversed relative to the
        specification in the bus definition.
    :ivar mirrored_system: If this element is present, the bus interface
        represents a mirrored system interface. All directional
        constraints on ports are reversed relative to the specification
        in the bus definition.
    :ivar monitor: Indicates that this is a (passive) monitor interface.
        All of the ports in the interface must be inputs. The type of
        interface to be monitored is specified with the required
        interfaceType attribute. The ipxact:group element must be
        specified if monitoring a system interface.
    :ivar connection_required: Indicates whether a connection to this
        interface is required for proper component functionality.
    :ivar bits_in_lau:
    :ivar bit_steering: Indicates whether bit steering should be used to
        map this interface onto a bus of different data width. Values
        are "0", "1" (defaults to "0").
    :ivar endianness: 'big': means the most significant element of any
        multi-element  data field is stored at the lowest memory
        address. 'little' means the least significant element of any
        multi-element data field is stored at the lowest memory address.
        If this element is not present the default is 'little' endian.
    :ivar parameters:
    :ivar vendor_extensions:
    :ivar id:
    :ivar other_attributes:
    """

    class Meta:
        name = "busInterfaceType"

    name: str | None = field(
        default=None,
        metadata={
            "type": "Element",
            "namespace": "http://www.accellera.org/XMLSchema/IPXACT/1685-2022",
            "required": True,
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
    bus_type: ConfigurableLibraryRefType | None = field(
        default=None,
        metadata={
            "name": "busType",
            "type": "Element",
            "namespace": "http://www.accellera.org/XMLSchema/IPXACT/1685-2022",
            "required": True,
        },
    )
    abstraction_types: AbstractionTypes | None = field(
        default=None,
        metadata={
            "name": "abstractionTypes",
            "type": "Element",
            "namespace": "http://www.accellera.org/XMLSchema/IPXACT/1685-2022",
        },
    )
    initiator: BusInterfaceType.Initiator | None = field(
        default=None,
        metadata={
            "type": "Element",
            "namespace": "http://www.accellera.org/XMLSchema/IPXACT/1685-2022",
        },
    )
    target: BusInterfaceType.Target | None = field(
        default=None,
        metadata={
            "type": "Element",
            "namespace": "http://www.accellera.org/XMLSchema/IPXACT/1685-2022",
        },
    )
    system: BusInterfaceType.System | None = field(
        default=None,
        metadata={
            "type": "Element",
            "namespace": "http://www.accellera.org/XMLSchema/IPXACT/1685-2022",
        },
    )
    mirrored_target: BusInterfaceType.MirroredTarget | None = field(
        default=None,
        metadata={
            "name": "mirroredTarget",
            "type": "Element",
            "namespace": "http://www.accellera.org/XMLSchema/IPXACT/1685-2022",
        },
    )
    mirrored_initiator: object | None = field(
        default=None,
        metadata={
            "name": "mirroredInitiator",
            "type": "Element",
            "namespace": "http://www.accellera.org/XMLSchema/IPXACT/1685-2022",
        },
    )
    mirrored_system: BusInterfaceType.MirroredSystem | None = field(
        default=None,
        metadata={
            "name": "mirroredSystem",
            "type": "Element",
            "namespace": "http://www.accellera.org/XMLSchema/IPXACT/1685-2022",
        },
    )
    monitor: BusInterfaceType.Monitor | None = field(
        default=None,
        metadata={
            "type": "Element",
            "namespace": "http://www.accellera.org/XMLSchema/IPXACT/1685-2022",
        },
    )
    connection_required: bool | None = field(
        default=None,
        metadata={
            "name": "connectionRequired",
            "type": "Element",
            "namespace": "http://www.accellera.org/XMLSchema/IPXACT/1685-2022",
        },
    )
    bits_in_lau: BitsInLau | None = field(
        default=None,
        metadata={
            "name": "bitsInLau",
            "type": "Element",
            "namespace": "http://www.accellera.org/XMLSchema/IPXACT/1685-2022",
        },
    )
    bit_steering: UnsignedBitExpression | None = field(
        default=None,
        metadata={
            "name": "bitSteering",
            "type": "Element",
            "namespace": "http://www.accellera.org/XMLSchema/IPXACT/1685-2022",
        },
    )
    endianness: EndianessType | None = field(
        default=None,
        metadata={
            "type": "Element",
            "namespace": "http://www.accellera.org/XMLSchema/IPXACT/1685-2022",
        },
    )
    parameters: Parameters | None = field(
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
    other_attributes: dict[str, str] = field(
        default_factory=dict,
        metadata={
            "type": "Attributes",
            "namespace": "##other",
        },
    )

    @dataclass
    class Initiator:
        """
        :ivar address_space_ref: If this initiator connects to an
            addressable bus, this element references the address space
            it maps to.
        """

        address_space_ref: BusInterfaceType.Initiator.AddressSpaceRef | None = field(
            default=None,
            metadata={
                "name": "addressSpaceRef",
                "type": "Element",
                "namespace": "http://www.accellera.org/XMLSchema/IPXACT/1685-2022",
            },
        )

        @dataclass
        class AddressSpaceRef(AddrSpaceRefType):
            """
            :ivar base_address: Base of an address space.
            :ivar mode_ref:
            """

            base_address: SignedLongintExpression | None = field(
                default=None,
                metadata={
                    "name": "baseAddress",
                    "type": "Element",
                    "namespace": "http://www.accellera.org/XMLSchema/IPXACT/1685-2022",
                },
            )
            mode_ref: list[
                BusInterfaceType.Initiator.AddressSpaceRef.ModeRef
            ] = field(
                default_factory=list,
                metadata={
                    "name": "modeRef",
                    "type": "Element",
                    "namespace": "http://www.accellera.org/XMLSchema/IPXACT/1685-2022",
                },
            )

            @dataclass
            class ModeRef:
                """
                A reference to a mode.
                """

                value: str = field(
                    default="",
                    metadata={
                        "required": True,
                    },
                )
                id: str | None = field(
                    default=None,
                    metadata={
                        "type": "Attribute",
                        "namespace": "http://www.w3.org/XML/1998/namespace",
                    },
                )

    @dataclass
    class Target:
        """
        :ivar memory_map_ref:
        :ivar transparent_bridge:
        :ivar file_set_ref_group: This reference is used to point the
            filesets that are associated with this target port.
            Depending on the target port function, there may be
            completely different software drivers associated with the
            different ports.
        """

        memory_map_ref: MemoryMapRef | None = field(
            default=None,
            metadata={
                "name": "memoryMapRef",
                "type": "Element",
                "namespace": "http://www.accellera.org/XMLSchema/IPXACT/1685-2022",
            },
        )
        transparent_bridge: list[TransparentBridge] = field(
            default_factory=list,
            metadata={
                "name": "transparentBridge",
                "type": "Element",
                "namespace": "http://www.accellera.org/XMLSchema/IPXACT/1685-2022",
            },
        )
        file_set_ref_group: list[BusInterfaceType.Target.FileSetRefGroup] = (
            field(
                default_factory=list,
                metadata={
                    "name": "fileSetRefGroup",
                    "type": "Element",
                    "namespace": "http://www.accellera.org/XMLSchema/IPXACT/1685-2022",
                },
            )
        )

        @dataclass
        class FileSetRefGroup:
            """
            :ivar group: Abritray name assigned to the collections of
                fileSets.
            :ivar file_set_ref:
            :ivar id:
            """

            group: str | None = field(
                default=None,
                metadata={
                    "type": "Element",
                    "namespace": "http://www.accellera.org/XMLSchema/IPXACT/1685-2022",
                },
            )
            file_set_ref: list[FileSetRef] = field(
                default_factory=list,
                metadata={
                    "name": "fileSetRef",
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

    @dataclass
    class System:
        group: Group | None = field(
            default=None,
            metadata={
                "type": "Element",
                "namespace": "http://www.accellera.org/XMLSchema/IPXACT/1685-2022",
                "required": True,
            },
        )

    @dataclass
    class MirroredTarget:
        """
        :ivar base_addresses: Represents a set of remap base addresses.
        """

        base_addresses: BusInterfaceType.MirroredTarget.BaseAddresses | None = field(
            default=None,
            metadata={
                "name": "baseAddresses",
                "type": "Element",
                "namespace": "http://www.accellera.org/XMLSchema/IPXACT/1685-2022",
            },
        )

        @dataclass
        class BaseAddresses:
            """
            :ivar remap_addresses:
            :ivar range: The address range of mirrored target, expressed
                as the number of bitsInLAU from the containing
                busInterface.
            """

            remap_addresses: list[
                BusInterfaceType.MirroredTarget.BaseAddresses.RemapAddresses
            ] = field(
                default_factory=list,
                metadata={
                    "name": "remapAddresses",
                    "type": "Element",
                    "namespace": "http://www.accellera.org/XMLSchema/IPXACT/1685-2022",
                    "min_occurs": 1,
                },
            )
            range: UnsignedPositiveLongintExpression | None = field(
                default=None,
                metadata={
                    "type": "Element",
                    "namespace": "http://www.accellera.org/XMLSchema/IPXACT/1685-2022",
                    "required": True,
                },
            )

            @dataclass
            class RemapAddresses:
                """
                :ivar remap_address: Base of an address block, expressed
                    as the number of bitsInLAU from the containing
                    busInterface. The modeRef element indicates the name
                    of the mode for which this address is valid.
                :ivar mode_ref:
                :ivar id:
                """

                remap_address: UnsignedLongintExpression | None = field(
                    default=None,
                    metadata={
                        "name": "remapAddress",
                        "type": "Element",
                        "namespace": "http://www.accellera.org/XMLSchema/IPXACT/1685-2022",
                        "required": True,
                    },
                )
                mode_ref: list[ModeRef] = field(
                    default_factory=list,
                    metadata={
                        "name": "modeRef",
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

    @dataclass
    class MirroredSystem:
        group: Group | None = field(
            default=None,
            metadata={
                "type": "Element",
                "namespace": "http://www.accellera.org/XMLSchema/IPXACT/1685-2022",
                "required": True,
            },
        )

    @dataclass
    class Monitor:
        """
        :ivar group: Indicates which system interface is being
            monitored. Name must match a group name present on one or
            more ports in the corresonding bus definition.
        :ivar interface_mode:
        """

        group: Group | None = field(
            default=None,
            metadata={
                "type": "Element",
                "namespace": "http://www.accellera.org/XMLSchema/IPXACT/1685-2022",
            },
        )
        interface_mode: MonitorInterfaceMode | None = field(
            default=None,
            metadata={
                "name": "interfaceMode",
                "type": "Attribute",
                "required": True,
            },
        )
