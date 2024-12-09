from ipxact.models.abstraction_types import AbstractionTypes
from ipxact.models.address_spaces import AddressSpaces
from ipxact.models.address_unit_bits import AddressUnitBits
from ipxact.models.bits_in_lau import BitsInLau
from ipxact.models.bus_interface import BusInterface
from ipxact.models.bus_interface_type import BusInterfaceType
from ipxact.models.bus_interfaces import BusInterfaces
from ipxact.models.choices import Choices
from ipxact.models.component import Component
from ipxact.models.component_port_direction_type import ComponentPortDirectionType
from ipxact.models.component_type import ComponentType
from ipxact.models.configurable_library_ref_type import ConfigurableLibraryRefType
from ipxact.models.endianess_type import EndianessType
from ipxact.models.extended_vectors_type import ExtendedVectorsType
from ipxact.models.format_type import FormatType
from ipxact.models.left import Left
from ipxact.models.memory_map_type import MemoryMapType
from ipxact.models.memory_maps import MemoryMaps
from ipxact.models.model import Model
from ipxact.models.model_type import ModelType
from ipxact.models.parameter import Parameter
from ipxact.models.parameter_type_resolve import ParameterTypeResolve
from ipxact.models.parameters import Parameters
from ipxact.models.port import Port
from ipxact.models.port_wire_type import PortWireType
from ipxact.models.range import Range
from ipxact.models.right import Right
from ipxact.models.signed_longint_expression import SignedLongintExpression
from ipxact.models.subspace_map import SubspaceMap
from ipxact.models.unsigned_bit_expression import UnsignedBitExpression
from ipxact.models.unsigned_positive_int_expression import UnsignedPositiveIntExpression
from ipxact.models.unsigned_positive_longint_expression import UnsignedPositiveLongintExpression
from ipxact.models.value import Value


obj = Component(
    vendor='spiritconsortium.org',
    library='Addressing',
    name='directMaster',
    version='1.0',
    bus_interfaces=BusInterfaces(
        bus_interface=[
            BusInterface(
                name='directMaster',
                bus_type=ConfigurableLibraryRefType(
                    vendor='spiritconsortium.org',
                    library='busdef.direct',
                    name='direct',
                    version='1.0'
                ),
                abstraction_types=AbstractionTypes(
                    abstraction_type=[
                        AbstractionTypes.AbstractionType(
                            abstraction_ref=ConfigurableLibraryRefType(
                                vendor='spiritconsortium.org',
                                library='busdef.direct',
                                name='direct_rtl',
                                version='1.0'
                            ),
                            port_maps=AbstractionTypes.AbstractionType.PortMaps(
                                port_map=[
                                    AbstractionTypes.AbstractionType.PortMaps.PortMap(
                                        logical_port=AbstractionTypes.AbstractionType.PortMaps.PortMap.LogicalPort(
                                            name='PRDATA'
                                        ),
                                        physical_port=AbstractionTypes.AbstractionType.PortMaps.PortMap.PhysicalPort(
                                            name='prdata'
                                        )
                                    ),
                                    AbstractionTypes.AbstractionType.PortMaps.PortMap(
                                        logical_port=AbstractionTypes.AbstractionType.PortMaps.PortMap.LogicalPort(
                                            name='PADDR',
                                            range=Range(
                                                left=Left(
                                                    value='addr + 32 - 1'
                                                ),
                                                right=Right(
                                                    value='addr'
                                                )
                                            )
                                        ),
                                        physical_port=AbstractionTypes.AbstractionType.PortMaps.PortMap.PhysicalPort(
                                            name='paddr'
                                        )
                                    ),
                                ]
                            )
                        ),
                    ]
                ),
                initiator=BusInterfaceType.Initiator(
                    address_space_ref=BusInterfaceType.Initiator.AddressSpaceRef(
                        address_space_ref='main',
                        base_address=SignedLongintExpression(
                            value='asBase'
                        )
                    )
                ),
                bits_in_lau=BitsInLau(
                    value='8'
                ),
                bit_steering=UnsignedBitExpression(
                    value='mSteer'
                ),
                endianness=EndianessType.LITTLE,
                parameters=Parameters(
                    parameter=[
                        Parameter(
                            name='addr',
                            value=Value(
                                value='0'
                            ),
                            parameter_id='addr',
                            prompt='Least mapped LSB of the address',
                            type_value=FormatType.LONGINT,
                            resolve=ParameterTypeResolve.USER
                        ),
                        Parameter(
                            name='asBase',
                            value=Value(
                                value='0'
                            ),
                            parameter_id='asBase',
                            prompt='addressSpace Base address:',
                            config_groups=[
                                'requiredConfig',
                            ],
                            type_value=FormatType.LONGINT,
                            resolve=ParameterTypeResolve.USER
                        ),
                        Parameter(
                            name='mSteer',
                            value=Value(
                                value='off'
                            ),
                            parameter_id='mSteer',
                            prompt='bitSteering:',
                            choice_ref='bitSteer',
                            config_groups=[
                                'requiredConfig',
                            ],
                            resolve=ParameterTypeResolve.USER
                        ),
                    ]
                )
            ),
        ]
    ),
    address_spaces=AddressSpaces(
        address_space=[
            AddressSpaces.AddressSpace(
                name='main',
                range=UnsignedPositiveLongintExpression(
                    value='asRange'
                ),
                width=UnsignedPositiveIntExpression(
                    value='asWidth'
                ),
                address_unit_bits=AddressUnitBits(
                    value='8'
                ),
                parameters=Parameters(
                    parameter=[
                        Parameter(
                            name='asRange',
                            value=Value(
                                value='4 * (2 ** 30)'
                            ),
                            parameter_id='asRange',
                            prompt='addressSpace range:',
                            config_groups=[
                                'requiredConfig',
                            ],
                            type_value=FormatType.LONGINT,
                            resolve=ParameterTypeResolve.USER
                        ),
                        Parameter(
                            name='asWidth',
                            value=Value(
                                value='32'
                            ),
                            parameter_id='asWidth',
                            prompt='addressSpace width:',
                            config_groups=[
                                'requiredConfig',
                            ],
                            type_value=FormatType.LONGINT,
                            resolve=ParameterTypeResolve.USER
                        ),
                    ]
                )
            ),
        ]
    ),
    memory_maps=MemoryMaps(
        memory_map=[
            MemoryMapType(
                name='processor_MemoryMap',
                subspace_map=[
                    SubspaceMap(
                        name='main_SubspaceMap',
                        base_address=SignedLongintExpression(
                            value='0'
                        ),
                        initiator_ref='directMaster'
                    ),
                ]
            ),
        ]
    ),
    model=Model(
        ports=ModelType.Ports(
            port=[
                Port(
                    name='prdata',
                    wire=PortWireType(
                        direction=ComponentPortDirectionType.IN,
                        vectors=ExtendedVectorsType(
                            vector=[
                                ExtendedVectorsType.Vector(
                                    left=Left(
                                        value='dataWidth - 1'
                                    ),
                                    right=Right(
                                        value='0'
                                    )
                                ),
                            ]
                        )
                    )
                ),
                Port(
                    name='paddr',
                    wire=PortWireType(
                        direction=ComponentPortDirectionType.OUT,
                        vectors=ExtendedVectorsType(
                            vector=[
                                ExtendedVectorsType.Vector(
                                    left=Left(
                                        value='31'
                                    ),
                                    right=Right(
                                        value='0'
                                    )
                                ),
                            ]
                        )
                    )
                ),
                Port(
                    name='pwdata',
                    wire=PortWireType(
                        direction=ComponentPortDirectionType.OUT,
                        vectors=ExtendedVectorsType(
                            vector=[
                                ExtendedVectorsType.Vector(
                                    left=Left(
                                        value='dataWidth - 1'
                                    ),
                                    right=Right(
                                        value='0'
                                    )
                                ),
                            ]
                        )
                    )
                ),
            ]
        )
    ),
    choices=Choices(
        choice=[
            Choices.Choice(
                name='bitSteer',
                enumeration=[
                    Choices.Choice.Enumeration(
                        value='on',
                        text='on'
                    ),
                    Choices.Choice.Enumeration(
                        value='off',
                        text='off'
                    ),
                ]
            ),
        ]
    ),
    cpus=ComponentType.Cpus(
        cpu=[
            ComponentType.Cpus.Cpu(
                name='processor',
                range=UnsignedPositiveLongintExpression(
                    value='asRange'
                ),
                width=UnsignedPositiveIntExpression(
                    value='asWidth'
                ),
                address_unit_bits=AddressUnitBits(
                    value='8'
                ),
                memory_map_ref='processor_MemoryMap'
            ),
        ]
    ),
    parameters=Parameters(
        parameter=[
            Parameter(
                name='width',
                value=Value(
                    value='32'
                ),
                parameter_id='dataWidth',
                prompt='Data width:',
                config_groups=[
                    'requiredConfig',
                ],
                resolve=ParameterTypeResolve.USER
            ),
        ]
    )
)
