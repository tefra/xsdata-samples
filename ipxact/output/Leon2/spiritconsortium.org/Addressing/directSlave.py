from ipxact.models.abstraction_types import AbstractionTypes
from ipxact.models.access_policies import AccessPolicies
from ipxact.models.access_type import AccessType
from ipxact.models.address_block import AddressBlock
from ipxact.models.base_address import BaseAddress
from ipxact.models.bits_in_lau import BitsInLau
from ipxact.models.bus_interface import BusInterface
from ipxact.models.bus_interface_type import BusInterfaceType
from ipxact.models.bus_interfaces import BusInterfaces
from ipxact.models.choices import Choices
from ipxact.models.component import Component
from ipxact.models.component_port_direction_type import ComponentPortDirectionType
from ipxact.models.configurable_library_ref_type import ConfigurableLibraryRefType
from ipxact.models.endianess_type import EndianessType
from ipxact.models.extended_vectors_type import ExtendedVectorsType
from ipxact.models.format_type import FormatType
from ipxact.models.left import Left
from ipxact.models.memory_map_ref import MemoryMapRef
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
from ipxact.models.unsigned_bit_expression import UnsignedBitExpression
from ipxact.models.unsigned_positive_int_expression import UnsignedPositiveIntExpression
from ipxact.models.unsigned_positive_longint_expression import UnsignedPositiveLongintExpression
from ipxact.models.usage_type import UsageType
from ipxact.models.value import Value


obj = Component(
    vendor='spiritconsortium.org',
    library='Addressing',
    name='directSlave',
    version='1.0',
    bus_interfaces=BusInterfaces(
        bus_interface=[
            BusInterface(
                name='directSlave',
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
                                            name='paddr_s'
                                        )
                                    ),
                                    AbstractionTypes.AbstractionType.PortMaps.PortMap(
                                        logical_port=AbstractionTypes.AbstractionType.PortMaps.PortMap.LogicalPort(
                                            name='PWDATA'
                                        ),
                                        physical_port=AbstractionTypes.AbstractionType.PortMaps.PortMap.PhysicalPort(
                                            name='pwdata_s'
                                        )
                                    ),
                                    AbstractionTypes.AbstractionType.PortMaps.PortMap(
                                        logical_port=AbstractionTypes.AbstractionType.PortMaps.PortMap.LogicalPort(
                                            name='PRDATA'
                                        ),
                                        physical_port=AbstractionTypes.AbstractionType.PortMaps.PortMap.PhysicalPort(
                                            name='prdata_s'
                                        )
                                    ),
                                ]
                            )
                        ),
                    ]
                ),
                target=BusInterfaceType.Target(
                    memory_map_ref=MemoryMapRef(
                        memory_map_ref='ambaDirect'
                    )
                ),
                bits_in_lau=BitsInLau(
                    value='8'
                ),
                bit_steering=UnsignedBitExpression(
                    value='sSteer'
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
                            name='sSteer',
                            value=Value(
                                value='off'
                            ),
                            parameter_id='sSteer',
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
    memory_maps=MemoryMaps(
        memory_map=[
            MemoryMapType(
                name='ambaDirect',
                address_block=[
                    AddressBlock(
                        name='defaultid4489935',
                        base_address=BaseAddress(
                            value='mmBase'
                        ),
                        range=UnsignedPositiveLongintExpression(
                            value='mmRange'
                        ),
                        width=UnsignedPositiveIntExpression(
                            value='mmWidth'
                        ),
                        usage=UsageType.MEMORY,
                        access_policies=AccessPolicies(
                            access_policy=[
                                AccessPolicies.AccessPolicy(
                                    access=AccessType.READ_WRITE
                                ),
                            ]
                        ),
                        parameters=Parameters(
                            parameter=[
                                Parameter(
                                    name='mmBase',
                                    value=Value(
                                        value="'h00000000"
                                    ),
                                    parameter_id='mmBase',
                                    prompt='memoryMap Base address:',
                                    config_groups=[
                                        'requiredConfig',
                                    ],
                                    type_value=FormatType.LONGINT,
                                    resolve=ParameterTypeResolve.USER
                                ),
                                Parameter(
                                    name='mmRange',
                                    value=Value(
                                        value="'h100"
                                    ),
                                    parameter_id='mmRange',
                                    prompt='memoryMap Range (bytes):',
                                    config_groups=[
                                        'requiredConfig',
                                    ],
                                    type_value=FormatType.LONGINT,
                                    resolve=ParameterTypeResolve.USER
                                ),
                                Parameter(
                                    name='mmWidth',
                                    value=Value(
                                        value='32'
                                    ),
                                    parameter_id='mmWidth',
                                    prompt='memoryMap Width:',
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
        ]
    ),
    model=Model(
        ports=ModelType.Ports(
            port=[
                Port(
                    name='paddr_s',
                    wire=PortWireType(
                        direction=ComponentPortDirectionType.IN,
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
                    name='pwdata_s',
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
                    name='prdata_s',
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
