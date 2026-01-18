from __future__ import annotations

from dataclasses import dataclass, field
from typing import Optional

from ipxact.models.address_block_ref import AddressBlockRef
from ipxact.models.address_spaces import AddressSpaces
from ipxact.models.address_unit_bits import AddressUnitBits
from ipxact.models.alternate_register_ref import AlternateRegisterRef
from ipxact.models.always_on import AlwaysOn
from ipxact.models.assertions import Assertions
from ipxact.models.bank_ref import BankRef
from ipxact.models.bus_interfaces import BusInterfaces
from ipxact.models.channels import Channels
from ipxact.models.choices import Choices
from ipxact.models.clearbox_element_type import ClearboxElementType
from ipxact.models.component_generators import ComponentGenerators
from ipxact.models.description import Description
from ipxact.models.display_name import DisplayName
from ipxact.models.executable_image import ExecutableImage
from ipxact.models.external_type_definitions import ExternalTypeDefinitions
from ipxact.models.field_ref import FieldRef
from ipxact.models.file_sets import FileSets
from ipxact.models.indirect_interfaces import IndirectInterfaces
from ipxact.models.memory_maps import MemoryMaps
from ipxact.models.memory_remap_ref import MemoryRemapRef
from ipxact.models.model import Model
from ipxact.models.other_clocks import OtherClocks
from ipxact.models.parameters import Parameters
from ipxact.models.part_select import PartSelect
from ipxact.models.range import Range
from ipxact.models.register_file_ref import RegisterFileRef
from ipxact.models.register_ref import RegisterRef
from ipxact.models.short_description import ShortDescription
from ipxact.models.sub_port_reference import SubPortReference
from ipxact.models.unresolved_unsigned_bit_expression import (
    UnresolvedUnsignedBitExpression,
)
from ipxact.models.unsigned_longint_expression import UnsignedLongintExpression
from ipxact.models.unsigned_positive_int_expression import (
    UnsignedPositiveIntExpression,
)
from ipxact.models.unsigned_positive_longint_expression import (
    UnsignedPositiveLongintExpression,
)
from ipxact.models.vendor_extensions import VendorExtensions

__NAMESPACE__ = "http://www.accellera.org/XMLSchema/IPXACT/1685-2022"


@dataclass
class ComponentType:
    """
    Component-specific extension to componentType.

    :ivar vendor: Name of the vendor who supplies this file.
    :ivar library: Name of the logical library this element belongs to.
    :ivar name: The name of the object.
    :ivar version: Indicates the version of the named element.
    :ivar display_name: Name for display purposes. Typically a few words
        providing a more detailed and/or user-friendly name than the
        vlnv.
    :ivar short_description:
    :ivar description:
    :ivar type_definitions:
    :ivar power_domains:
    :ivar bus_interfaces:
    :ivar indirect_interfaces:
    :ivar channels:
    :ivar modes: A list of user defined component modes.
    :ivar address_spaces:
    :ivar memory_maps:
    :ivar model:
    :ivar component_generators: Generator list is tools-specific.
    :ivar choices:
    :ivar file_sets:
    :ivar clearbox_elements: A list of clearboxElements
    :ivar cpus: cpu's in the component
    :ivar other_clock_drivers: Defines a set of clock drivers that are
        not directly associated with an input port of the component.
    :ivar reset_types: A list of user defined resetTypes applicable to
        this component.
    :ivar parameters:
    :ivar assertions:
    :ivar vendor_extensions:
    :ivar id:
    """

    class Meta:
        name = "componentType"

    vendor: str | None = field(
        default=None,
        metadata={
            "type": "Element",
            "namespace": "http://www.accellera.org/XMLSchema/IPXACT/1685-2022",
            "required": True,
        },
    )
    library: str | None = field(
        default=None,
        metadata={
            "type": "Element",
            "namespace": "http://www.accellera.org/XMLSchema/IPXACT/1685-2022",
            "required": True,
        },
    )
    name: str | None = field(
        default=None,
        metadata={
            "type": "Element",
            "namespace": "http://www.accellera.org/XMLSchema/IPXACT/1685-2022",
            "required": True,
        },
    )
    version: str | None = field(
        default=None,
        metadata={
            "type": "Element",
            "namespace": "http://www.accellera.org/XMLSchema/IPXACT/1685-2022",
            "required": True,
        },
    )
    display_name: str | None = field(
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
    type_definitions: ComponentType.TypeDefinitions | None = field(
        default=None,
        metadata={
            "name": "typeDefinitions",
            "type": "Element",
            "namespace": "http://www.accellera.org/XMLSchema/IPXACT/1685-2022",
        },
    )
    power_domains: ComponentType.PowerDomains | None = field(
        default=None,
        metadata={
            "name": "powerDomains",
            "type": "Element",
            "namespace": "http://www.accellera.org/XMLSchema/IPXACT/1685-2022",
        },
    )
    bus_interfaces: BusInterfaces | None = field(
        default=None,
        metadata={
            "name": "busInterfaces",
            "type": "Element",
            "namespace": "http://www.accellera.org/XMLSchema/IPXACT/1685-2022",
        },
    )
    indirect_interfaces: IndirectInterfaces | None = field(
        default=None,
        metadata={
            "name": "indirectInterfaces",
            "type": "Element",
            "namespace": "http://www.accellera.org/XMLSchema/IPXACT/1685-2022",
        },
    )
    channels: Channels | None = field(
        default=None,
        metadata={
            "type": "Element",
            "namespace": "http://www.accellera.org/XMLSchema/IPXACT/1685-2022",
        },
    )
    modes: ComponentType.Modes | None = field(
        default=None,
        metadata={
            "type": "Element",
            "namespace": "http://www.accellera.org/XMLSchema/IPXACT/1685-2022",
        },
    )
    address_spaces: AddressSpaces | None = field(
        default=None,
        metadata={
            "name": "addressSpaces",
            "type": "Element",
            "namespace": "http://www.accellera.org/XMLSchema/IPXACT/1685-2022",
        },
    )
    memory_maps: MemoryMaps | None = field(
        default=None,
        metadata={
            "name": "memoryMaps",
            "type": "Element",
            "namespace": "http://www.accellera.org/XMLSchema/IPXACT/1685-2022",
        },
    )
    model: Model | None = field(
        default=None,
        metadata={
            "type": "Element",
            "namespace": "http://www.accellera.org/XMLSchema/IPXACT/1685-2022",
        },
    )
    component_generators: ComponentGenerators | None = field(
        default=None,
        metadata={
            "name": "componentGenerators",
            "type": "Element",
            "namespace": "http://www.accellera.org/XMLSchema/IPXACT/1685-2022",
        },
    )
    choices: Choices | None = field(
        default=None,
        metadata={
            "type": "Element",
            "namespace": "http://www.accellera.org/XMLSchema/IPXACT/1685-2022",
        },
    )
    file_sets: FileSets | None = field(
        default=None,
        metadata={
            "name": "fileSets",
            "type": "Element",
            "namespace": "http://www.accellera.org/XMLSchema/IPXACT/1685-2022",
        },
    )
    clearbox_elements: ComponentType.ClearboxElements | None = field(
        default=None,
        metadata={
            "name": "clearboxElements",
            "type": "Element",
            "namespace": "http://www.accellera.org/XMLSchema/IPXACT/1685-2022",
        },
    )
    cpus: ComponentType.Cpus | None = field(
        default=None,
        metadata={
            "type": "Element",
            "namespace": "http://www.accellera.org/XMLSchema/IPXACT/1685-2022",
        },
    )
    other_clock_drivers: OtherClocks | None = field(
        default=None,
        metadata={
            "name": "otherClockDrivers",
            "type": "Element",
            "namespace": "http://www.accellera.org/XMLSchema/IPXACT/1685-2022",
        },
    )
    reset_types: ComponentType.ResetTypes | None = field(
        default=None,
        metadata={
            "name": "resetTypes",
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
    assertions: Assertions | None = field(
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

    @dataclass
    class TypeDefinitions:
        external_type_definitions: list[ExternalTypeDefinitions] = field(
            default_factory=list,
            metadata={
                "name": "externalTypeDefinitions",
                "type": "Element",
                "namespace": "http://www.accellera.org/XMLSchema/IPXACT/1685-2022",
            },
        )

    @dataclass
    class PowerDomains:
        power_domain: list[ComponentType.PowerDomains.PowerDomain] = field(
            default_factory=list,
            metadata={
                "name": "powerDomain",
                "type": "Element",
                "namespace": "http://www.accellera.org/XMLSchema/IPXACT/1685-2022",
                "min_occurs": 1,
            },
        )

        @dataclass
        class PowerDomain:
            """
            :ivar name: Unique name
            :ivar display_name:
            :ivar short_description:
            :ivar description:
            :ivar always_on:
            :ivar sub_domain_of: Reference to a power domain defined on
                this component
            :ivar parameters:
            :ivar vendor_extensions:
            :ivar id:
            """

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
            always_on: AlwaysOn | None = field(
                default=None,
                metadata={
                    "name": "alwaysOn",
                    "type": "Element",
                    "namespace": "http://www.accellera.org/XMLSchema/IPXACT/1685-2022",
                },
            )
            sub_domain_of: str | None = field(
                default=None,
                metadata={
                    "name": "subDomainOf",
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

    @dataclass
    class Modes:
        mode: list[ComponentType.Modes.Mode] = field(
            default_factory=list,
            metadata={
                "type": "Element",
                "namespace": "http://www.accellera.org/XMLSchema/IPXACT/1685-2022",
                "min_occurs": 1,
            },
        )

        @dataclass
        class Mode:
            """
            :ivar name: Unique name
            :ivar display_name:
            :ivar short_description:
            :ivar description:
            :ivar port_slice:
            :ivar field_slice: Reference to a register field slice
            :ivar condition:
            :ivar vendor_extensions:
            :ivar id:
            """

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
            port_slice: list[ComponentType.Modes.Mode.PortSlice] = field(
                default_factory=list,
                metadata={
                    "name": "portSlice",
                    "type": "Element",
                    "namespace": "http://www.accellera.org/XMLSchema/IPXACT/1685-2022",
                },
            )
            field_slice: list[ComponentType.Modes.Mode.FieldSlice] = field(
                default_factory=list,
                metadata={
                    "name": "fieldSlice",
                    "type": "Element",
                    "namespace": "http://www.accellera.org/XMLSchema/IPXACT/1685-2022",
                },
            )
            condition: UnresolvedUnsignedBitExpression | None = field(
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

            @dataclass
            class PortSlice:
                """
                :ivar name: Unique name
                :ivar display_name:
                :ivar short_description:
                :ivar description:
                :ivar port_ref:
                :ivar sub_port_reference:
                :ivar part_select:
                :ivar id:
                """

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
                port_ref: ComponentType.Modes.Mode.PortSlice.PortRef | None = field(
                    default=None,
                    metadata={
                        "name": "portRef",
                        "type": "Element",
                        "namespace": "http://www.accellera.org/XMLSchema/IPXACT/1685-2022",
                        "required": True,
                    },
                )
                sub_port_reference: list[SubPortReference] = field(
                    default_factory=list,
                    metadata={
                        "name": "subPortReference",
                        "type": "Element",
                        "namespace": "http://www.accellera.org/XMLSchema/IPXACT/1685-2022",
                    },
                )
                part_select: PartSelect | None = field(
                    default=None,
                    metadata={
                        "name": "partSelect",
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
                class PortRef:
                    port_ref: str | None = field(
                        default=None,
                        metadata={
                            "name": "portRef",
                            "type": "Attribute",
                            "required": True,
                            "white_space": "collapse",
                            "pattern": r"\i[\p{L}\p{N}\.\-:_]*",
                        },
                    )

            @dataclass
            class FieldSlice:
                """
                :ivar name: Unique name
                :ivar display_name:
                :ivar short_description:
                :ivar description:
                :ivar address_space_ref:
                :ivar memory_map_ref:
                :ivar memory_remap_ref:
                :ivar bank_ref:
                :ivar address_block_ref:
                :ivar register_file_ref:
                :ivar register_ref:
                :ivar alternate_register_ref:
                :ivar field_ref:
                :ivar range:
                :ivar id:
                """

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
                address_space_ref: ComponentType.Modes.Mode.FieldSlice.AddressSpaceRef | None = field(
                    default=None,
                    metadata={
                        "name": "addressSpaceRef",
                        "type": "Element",
                        "namespace": "http://www.accellera.org/XMLSchema/IPXACT/1685-2022",
                    },
                )
                memory_map_ref: ComponentType.Modes.Mode.FieldSlice.MemoryMapRef | None = field(
                    default=None,
                    metadata={
                        "name": "memoryMapRef",
                        "type": "Element",
                        "namespace": "http://www.accellera.org/XMLSchema/IPXACT/1685-2022",
                    },
                )
                memory_remap_ref: MemoryRemapRef | None = field(
                    default=None,
                    metadata={
                        "name": "memoryRemapRef",
                        "type": "Element",
                        "namespace": "http://www.accellera.org/XMLSchema/IPXACT/1685-2022",
                    },
                )
                bank_ref: list[BankRef] = field(
                    default_factory=list,
                    metadata={
                        "name": "bankRef",
                        "type": "Element",
                        "namespace": "http://www.accellera.org/XMLSchema/IPXACT/1685-2022",
                    },
                )
                address_block_ref: AddressBlockRef | None = field(
                    default=None,
                    metadata={
                        "name": "addressBlockRef",
                        "type": "Element",
                        "namespace": "http://www.accellera.org/XMLSchema/IPXACT/1685-2022",
                        "required": True,
                    },
                )
                register_file_ref: list[RegisterFileRef] = field(
                    default_factory=list,
                    metadata={
                        "name": "registerFileRef",
                        "type": "Element",
                        "namespace": "http://www.accellera.org/XMLSchema/IPXACT/1685-2022",
                    },
                )
                register_ref: RegisterRef | None = field(
                    default=None,
                    metadata={
                        "name": "registerRef",
                        "type": "Element",
                        "namespace": "http://www.accellera.org/XMLSchema/IPXACT/1685-2022",
                        "required": True,
                    },
                )
                alternate_register_ref: AlternateRegisterRef | None = field(
                    default=None,
                    metadata={
                        "name": "alternateRegisterRef",
                        "type": "Element",
                        "namespace": "http://www.accellera.org/XMLSchema/IPXACT/1685-2022",
                    },
                )
                field_ref: FieldRef | None = field(
                    default=None,
                    metadata={
                        "name": "fieldRef",
                        "type": "Element",
                        "namespace": "http://www.accellera.org/XMLSchema/IPXACT/1685-2022",
                        "required": True,
                    },
                )
                range: Range | None = field(
                    default=None,
                    metadata={
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
                class AddressSpaceRef:
                    address_space_ref: str | None = field(
                        default=None,
                        metadata={
                            "name": "addressSpaceRef",
                            "type": "Attribute",
                            "required": True,
                        },
                    )

                @dataclass
                class MemoryMapRef:
                    memory_map_ref: str | None = field(
                        default=None,
                        metadata={
                            "name": "memoryMapRef",
                            "type": "Attribute",
                            "required": True,
                        },
                    )

    @dataclass
    class ClearboxElements:
        """
        :ivar clearbox_element: A clearboxElement is a useful way to
            identify elements of a component that can not be identified
            through other means such as internal signals and non-
            software accessible registers.
        """

        clearbox_element: list[ClearboxElementType] = field(
            default_factory=list,
            metadata={
                "name": "clearboxElement",
                "type": "Element",
                "namespace": "http://www.accellera.org/XMLSchema/IPXACT/1685-2022",
                "min_occurs": 1,
            },
        )

    @dataclass
    class Cpus:
        """
        :ivar cpu: Describes a processor in this component.
        """

        cpu: list[ComponentType.Cpus.Cpu] = field(
            default_factory=list,
            metadata={
                "type": "Element",
                "namespace": "http://www.accellera.org/XMLSchema/IPXACT/1685-2022",
                "min_occurs": 1,
            },
        )

        @dataclass
        class Cpu:
            """
            :ivar name: Unique name
            :ivar display_name:
            :ivar short_description:
            :ivar description:
            :ivar range: The address range of an address block.
                Expressed as the number of addressable units accessible
                to the block. The range and the width are related by the
                following formulas: number_of_bits_in_block =
                ipxact:addressUnitBits * ipxact:range
                number_of_rows_in_block = number_of_bits_in_block /
                ipxact:width
            :ivar width: The bit width of a row in the address block.
                The range and the width are related by the following
                formulas: number_of_bits_in_block =
                ipxact:addressUnitBits * ipxact:range
                number_of_rows_in_block = number_of_bits_in_block /
                ipxact:width
            :ivar regions: Address regions within a cpu system address
                map.
            :ivar address_unit_bits:
            :ivar executable_image:
            :ivar memory_map_ref: Indicates which memory maps into this
                cpu.
            :ivar parameters: Data specific to the cpu.
            :ivar vendor_extensions:
            :ivar id:
            """

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
            range: UnsignedPositiveLongintExpression | None = field(
                default=None,
                metadata={
                    "type": "Element",
                    "namespace": "http://www.accellera.org/XMLSchema/IPXACT/1685-2022",
                    "required": True,
                },
            )
            width: UnsignedPositiveIntExpression | None = field(
                default=None,
                metadata={
                    "type": "Element",
                    "namespace": "http://www.accellera.org/XMLSchema/IPXACT/1685-2022",
                    "required": True,
                },
            )
            regions: ComponentType.Cpus.Cpu.Regions | None = field(
                default=None,
                metadata={
                    "type": "Element",
                    "namespace": "http://www.accellera.org/XMLSchema/IPXACT/1685-2022",
                },
            )
            address_unit_bits: AddressUnitBits | None = field(
                default=None,
                metadata={
                    "name": "addressUnitBits",
                    "type": "Element",
                    "namespace": "http://www.accellera.org/XMLSchema/IPXACT/1685-2022",
                },
            )
            executable_image: list[ExecutableImage] = field(
                default_factory=list,
                metadata={
                    "name": "executableImage",
                    "type": "Element",
                    "namespace": "http://www.accellera.org/XMLSchema/IPXACT/1685-2022",
                },
            )
            memory_map_ref: str | None = field(
                default=None,
                metadata={
                    "name": "memoryMapRef",
                    "type": "Element",
                    "namespace": "http://www.accellera.org/XMLSchema/IPXACT/1685-2022",
                    "required": True,
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

            @dataclass
            class Regions:
                """
                :ivar region: Address region within a system address
                    map.
                """

                region: list[ComponentType.Cpus.Cpu.Regions.Region] = field(
                    default_factory=list,
                    metadata={
                        "type": "Element",
                        "namespace": "http://www.accellera.org/XMLSchema/IPXACT/1685-2022",
                        "min_occurs": 1,
                    },
                )

                @dataclass
                class Region:
                    """
                    :ivar name: Unique name
                    :ivar display_name:
                    :ivar short_description:
                    :ivar description:
                    :ivar address_offset: Address offset of the region
                        within the system address map.
                    :ivar range: The address range of region. Expressed
                        as the number of addressable units accessible to
                        the region.
                    :ivar vendor_extensions:
                    :ivar id:
                    """

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
                    address_offset: UnsignedLongintExpression | None = (
                        field(
                            default=None,
                            metadata={
                                "name": "addressOffset",
                                "type": "Element",
                                "namespace": "http://www.accellera.org/XMLSchema/IPXACT/1685-2022",
                                "required": True,
                            },
                        )
                    )
                    range: UnsignedPositiveLongintExpression | None = field(
                        default=None,
                        metadata={
                            "type": "Element",
                            "namespace": "http://www.accellera.org/XMLSchema/IPXACT/1685-2022",
                            "required": True,
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

    @dataclass
    class ResetTypes:
        """
        :ivar reset_type: A user defined reset policy
        """

        reset_type: list[ComponentType.ResetTypes.ResetType] = field(
            default_factory=list,
            metadata={
                "name": "resetType",
                "type": "Element",
                "namespace": "http://www.accellera.org/XMLSchema/IPXACT/1685-2022",
                "min_occurs": 1,
            },
        )

        @dataclass
        class ResetType:
            """
            :ivar name: Unique name
            :ivar display_name:
            :ivar short_description:
            :ivar description:
            :ivar vendor_extensions:
            :ivar id:
            """

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
