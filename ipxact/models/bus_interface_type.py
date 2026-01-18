from __future__ import annotations

from dataclasses import dataclass, field

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


@dataclass(kw_only=True)
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
    bus_type: ConfigurableLibraryRefType = field(
        metadata={
            "name": "busType",
            "type": "Element",
            "namespace": "http://www.accellera.org/XMLSchema/IPXACT/1685-2022",
            "required": True,
        }
    )
    abstraction_types: None | AbstractionTypes = field(
        default=None,
        metadata={
            "name": "abstractionTypes",
            "type": "Element",
            "namespace": "http://www.accellera.org/XMLSchema/IPXACT/1685-2022",
        },
    )
    initiator: None | BusInterfaceType.Initiator = field(
        default=None,
        metadata={
            "type": "Element",
            "namespace": "http://www.accellera.org/XMLSchema/IPXACT/1685-2022",
        },
    )
    target: None | BusInterfaceType.Target = field(
        default=None,
        metadata={
            "type": "Element",
            "namespace": "http://www.accellera.org/XMLSchema/IPXACT/1685-2022",
        },
    )
    system: None | BusInterfaceType.System = field(
        default=None,
        metadata={
            "type": "Element",
            "namespace": "http://www.accellera.org/XMLSchema/IPXACT/1685-2022",
        },
    )
    mirrored_target: None | BusInterfaceType.MirroredTarget = field(
        default=None,
        metadata={
            "name": "mirroredTarget",
            "type": "Element",
            "namespace": "http://www.accellera.org/XMLSchema/IPXACT/1685-2022",
        },
    )
    mirrored_initiator: None | object = field(
        default=None,
        metadata={
            "name": "mirroredInitiator",
            "type": "Element",
            "namespace": "http://www.accellera.org/XMLSchema/IPXACT/1685-2022",
        },
    )
    mirrored_system: None | BusInterfaceType.MirroredSystem = field(
        default=None,
        metadata={
            "name": "mirroredSystem",
            "type": "Element",
            "namespace": "http://www.accellera.org/XMLSchema/IPXACT/1685-2022",
        },
    )
    monitor: None | BusInterfaceType.Monitor = field(
        default=None,
        metadata={
            "type": "Element",
            "namespace": "http://www.accellera.org/XMLSchema/IPXACT/1685-2022",
        },
    )
    connection_required: None | bool = field(
        default=None,
        metadata={
            "name": "connectionRequired",
            "type": "Element",
            "namespace": "http://www.accellera.org/XMLSchema/IPXACT/1685-2022",
        },
    )
    bits_in_lau: None | BitsInLau = field(
        default=None,
        metadata={
            "name": "bitsInLau",
            "type": "Element",
            "namespace": "http://www.accellera.org/XMLSchema/IPXACT/1685-2022",
        },
    )
    bit_steering: None | UnsignedBitExpression = field(
        default=None,
        metadata={
            "name": "bitSteering",
            "type": "Element",
            "namespace": "http://www.accellera.org/XMLSchema/IPXACT/1685-2022",
        },
    )
    endianness: None | EndianessType = field(
        default=None,
        metadata={
            "type": "Element",
            "namespace": "http://www.accellera.org/XMLSchema/IPXACT/1685-2022",
        },
    )
    parameters: None | Parameters = field(
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
    other_attributes: dict[str, str] = field(
        default_factory=dict,
        metadata={
            "type": "Attributes",
            "namespace": "##other",
        },
    )

    @dataclass(kw_only=True)
    class Initiator:
        """
        :ivar address_space_ref: If this initiator connects to an
            addressable bus, this element references the address space
            it maps to.
        """

        address_space_ref: (
            None | BusInterfaceType.Initiator.AddressSpaceRef
        ) = field(
            default=None,
            metadata={
                "name": "addressSpaceRef",
                "type": "Element",
                "namespace": "http://www.accellera.org/XMLSchema/IPXACT/1685-2022",
            },
        )

        @dataclass(kw_only=True)
        class AddressSpaceRef(AddrSpaceRefType):
            """
            :ivar base_address: Base of an address space.
            :ivar mode_ref:
            """

            base_address: None | SignedLongintExpression = field(
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

            @dataclass(kw_only=True)
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
                id: None | str = field(
                    default=None,
                    metadata={
                        "type": "Attribute",
                        "namespace": "http://www.w3.org/XML/1998/namespace",
                    },
                )

    @dataclass(kw_only=True)
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

        memory_map_ref: None | MemoryMapRef = field(
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

        @dataclass(kw_only=True)
        class FileSetRefGroup:
            """
            :ivar group: Abritray name assigned to the collections of
                fileSets.
            :ivar file_set_ref:
            :ivar id:
            """

            group: None | str = field(
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
            id: None | str = field(
                default=None,
                metadata={
                    "type": "Attribute",
                    "namespace": "http://www.w3.org/XML/1998/namespace",
                },
            )

    @dataclass(kw_only=True)
    class System:
        group: Group = field(
            metadata={
                "type": "Element",
                "namespace": "http://www.accellera.org/XMLSchema/IPXACT/1685-2022",
                "required": True,
            }
        )

    @dataclass(kw_only=True)
    class MirroredTarget:
        """
        :ivar base_addresses: Represents a set of remap base addresses.
        """

        base_addresses: (
            None | BusInterfaceType.MirroredTarget.BaseAddresses
        ) = field(
            default=None,
            metadata={
                "name": "baseAddresses",
                "type": "Element",
                "namespace": "http://www.accellera.org/XMLSchema/IPXACT/1685-2022",
            },
        )

        @dataclass(kw_only=True)
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
            range: UnsignedPositiveLongintExpression = field(
                metadata={
                    "type": "Element",
                    "namespace": "http://www.accellera.org/XMLSchema/IPXACT/1685-2022",
                    "required": True,
                }
            )

            @dataclass(kw_only=True)
            class RemapAddresses:
                """
                :ivar remap_address: Base of an address block, expressed
                    as the number of bitsInLAU from the containing
                    busInterface. The modeRef element indicates the name
                    of the mode for which this address is valid.
                :ivar mode_ref:
                :ivar id:
                """

                remap_address: UnsignedLongintExpression = field(
                    metadata={
                        "name": "remapAddress",
                        "type": "Element",
                        "namespace": "http://www.accellera.org/XMLSchema/IPXACT/1685-2022",
                        "required": True,
                    }
                )
                mode_ref: list[ModeRef] = field(
                    default_factory=list,
                    metadata={
                        "name": "modeRef",
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

    @dataclass(kw_only=True)
    class MirroredSystem:
        group: Group = field(
            metadata={
                "type": "Element",
                "namespace": "http://www.accellera.org/XMLSchema/IPXACT/1685-2022",
                "required": True,
            }
        )

    @dataclass(kw_only=True)
    class Monitor:
        """
        :ivar group: Indicates which system interface is being
            monitored. Name must match a group name present on one or
            more ports in the corresonding bus definition.
        :ivar interface_mode:
        """

        group: None | Group = field(
            default=None,
            metadata={
                "type": "Element",
                "namespace": "http://www.accellera.org/XMLSchema/IPXACT/1685-2022",
            },
        )
        interface_mode: MonitorInterfaceMode = field(
            metadata={
                "name": "interfaceMode",
                "type": "Attribute",
                "required": True,
            }
        )
