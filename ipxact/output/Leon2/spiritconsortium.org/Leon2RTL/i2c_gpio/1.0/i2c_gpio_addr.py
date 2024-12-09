from ipxact.models.abstraction_types import AbstractionTypes
from ipxact.models.access import Access
from ipxact.models.access_policies import AccessPolicies
from ipxact.models.access_type import AccessType
from ipxact.models.address_block import AddressBlock
from ipxact.models.address_block_type import AddressBlockType
from ipxact.models.base_address import BaseAddress
from ipxact.models.bus_interface import BusInterface
from ipxact.models.bus_interface_type import BusInterfaceType
from ipxact.models.bus_interfaces import BusInterfaces
from ipxact.models.component import Component
from ipxact.models.component_instantiation_type import ComponentInstantiationType
from ipxact.models.component_port_direction_type import ComponentPortDirectionType
from ipxact.models.configurable_library_ref_type import ConfigurableLibraryRefType
from ipxact.models.extended_vectors_type import ExtendedVectorsType
from ipxact.models.field_type import FieldType
from ipxact.models.file import File
from ipxact.models.file_set import FileSet
from ipxact.models.file_set_ref import FileSetRef
from ipxact.models.file_sets import FileSets
from ipxact.models.file_type import FileType
from ipxact.models.ipxact_uri import IpxactUri
from ipxact.models.language_type import LanguageType
from ipxact.models.left import Left
from ipxact.models.memory_map_ref import MemoryMapRef
from ipxact.models.memory_map_type import MemoryMapType
from ipxact.models.memory_maps import MemoryMaps
from ipxact.models.model import Model
from ipxact.models.model_type import ModelType
from ipxact.models.module_parameter_type import ModuleParameterType
from ipxact.models.parameter import Parameter
from ipxact.models.parameter_type_resolve import ParameterTypeResolve
from ipxact.models.parameters import Parameters
from ipxact.models.port import Port
from ipxact.models.port_wire_type import PortWireType
from ipxact.models.reset import Reset
from ipxact.models.right import Right
from ipxact.models.simple_file_type import SimpleFileType
from ipxact.models.unsigned_bit_vector_expression import UnsignedBitVectorExpression
from ipxact.models.unsigned_int_expression import UnsignedIntExpression
from ipxact.models.unsigned_longint_expression import UnsignedLongintExpression
from ipxact.models.unsigned_positive_int_expression import UnsignedPositiveIntExpression
from ipxact.models.unsigned_positive_longint_expression import UnsignedPositiveLongintExpression
from ipxact.models.value import Value


obj = Component(
    vendor='spiritconsortium.org',
    library='Leon2RTL',
    name='i2c_gpio_addr',
    version='1.0',
    bus_interfaces=BusInterfaces(
        bus_interface=[
            BusInterface(
                name='i2c_slave',
                bus_type=ConfigurableLibraryRefType(
                    vendor='spiritconsortium.org',
                    library='busdef.nxp',
                    name='i2c',
                    version='1.0'
                ),
                abstraction_types=AbstractionTypes(
                    abstraction_type=[
                        AbstractionTypes.AbstractionType(
                            abstraction_ref=ConfigurableLibraryRefType(
                                vendor='spiritconsortium.org',
                                library='busdef.nxp',
                                name='i2c_rtl',
                                version='1.0'
                            ),
                            port_maps=AbstractionTypes.AbstractionType.PortMaps(
                                port_map=[
                                    AbstractionTypes.AbstractionType.PortMaps.PortMap(
                                        logical_port=AbstractionTypes.AbstractionType.PortMaps.PortMap.LogicalPort(
                                            name='SCL'
                                        ),
                                        physical_port=AbstractionTypes.AbstractionType.PortMaps.PortMap.PhysicalPort(
                                            name='scl'
                                        )
                                    ),
                                    AbstractionTypes.AbstractionType.PortMaps.PortMap(
                                        logical_port=AbstractionTypes.AbstractionType.PortMaps.PortMap.LogicalPort(
                                            name='SDA'
                                        ),
                                        physical_port=AbstractionTypes.AbstractionType.PortMaps.PortMap.PhysicalPort(
                                            name='sda'
                                        )
                                    ),
                                ]
                            )
                        ),
                    ]
                ),
                target=BusInterfaceType.Target(
                    memory_map_ref=MemoryMapRef(
                        memory_map_ref='memory'
                    )
                )
            ),
        ]
    ),
    memory_maps=MemoryMaps(
        memory_map=[
            MemoryMapType(
                name='memory',
                address_block=[
                    AddressBlock(
                        name='defaultid4489720',
                        base_address=BaseAddress(
                            value='0'
                        ),
                        range=UnsignedPositiveLongintExpression(
                            value='2'
                        ),
                        width=UnsignedPositiveIntExpression(
                            value='8'
                        ),
                        register=[
                            AddressBlockType.Register(
                                name='inputreg',
                                address_offset=UnsignedLongintExpression(
                                    value="'h0"
                                ),
                                size=UnsignedPositiveIntExpression(
                                    value='8'
                                ),
                                access_policies=AccessPolicies(
                                    access_policy=[
                                        AccessPolicies.AccessPolicy(
                                            access=AccessType.READ_ONLY
                                        ),
                                    ]
                                ),
                                field_value=[
                                    FieldType(
                                        name='inputreg_field',
                                        bit_offset=UnsignedIntExpression(
                                            value='0'
                                        ),
                                        bit_width=UnsignedPositiveIntExpression(
                                            value='gpi'
                                        ),
                                        volatile=True,
                                        field_access_policies=FieldType.FieldAccessPolicies(
                                            field_access_policy=[
                                                FieldType.FieldAccessPolicies.FieldAccessPolicy(
                                                    access=Access(
                                                        value=AccessType.READ_ONLY
                                                    )
                                                ),
                                            ]
                                        )
                                    ),
                                ]
                            ),
                            AddressBlockType.Register(
                                name='outputreg',
                                address_offset=UnsignedLongintExpression(
                                    value="'h1"
                                ),
                                size=UnsignedPositiveIntExpression(
                                    value='8'
                                ),
                                access_policies=AccessPolicies(
                                    access_policy=[
                                        AccessPolicies.AccessPolicy(
                                            access=AccessType.READ_WRITE
                                        ),
                                    ]
                                ),
                                field_value=[
                                    FieldType(
                                        name='outputreg_field',
                                        bit_offset=UnsignedIntExpression(
                                            value='0'
                                        ),
                                        bit_width=UnsignedPositiveIntExpression(
                                            value='gpo'
                                        ),
                                        resets=FieldType.Resets(
                                            reset=[
                                                Reset(
                                                    value=UnsignedBitVectorExpression(
                                                        value="(('h00) >> 0) & {gpo{1'b1}}"
                                                    )
                                                ),
                                            ]
                                        ),
                                        field_access_policies=FieldType.FieldAccessPolicies(
                                            field_access_policy=[
                                                FieldType.FieldAccessPolicies.FieldAccessPolicy(
                                                    access=Access(
                                                        value=AccessType.READ_WRITE
                                                    )
                                                ),
                                            ]
                                        )
                                    ),
                                ]
                            ),
                        ]
                    ),
                ]
            ),
        ]
    ),
    model=Model(
        views=ModelType.Views(
            view=[
                ModelType.Views.View(
                    name='verilogSource',
                    env_identifier=[
                        ModelType.Views.View.EnvIdentifier(
                            value=':modelsim.mentor.com:'
                        ),
                        ModelType.Views.View.EnvIdentifier(
                            value=':vcs.synopsys.com:'
                        ),
                        ModelType.Views.View.EnvIdentifier(
                            value=':designcompiler.synopsys.com:'
                        ),
                    ],
                    component_instantiation_ref='verilogSource'
                ),
                ModelType.Views.View(
                    name='vhdlSource',
                    env_identifier=[
                        ModelType.Views.View.EnvIdentifier(
                            value=':ncsim.cadence.com:'
                        ),
                    ],
                    component_instantiation_ref='vhdlSource'
                ),
            ]
        ),
        instantiations=ModelType.Instantiations(
            component_instantiation=[
                ComponentInstantiationType(
                    name='verilogSource',
                    language=LanguageType(
                        value='verilog'
                    ),
                    module_name='i2c_gpio_addr',
                    module_parameters=ComponentInstantiationType.ModuleParameters(
                        module_parameter=[
                            ModuleParameterType(
                                name='gpibits',
                                value=Value(
                                    value='gpi'
                                ),
                                minimum='1',
                                maximum='8',
                                data_type='integer'
                            ),
                            ModuleParameterType(
                                name='gpobits',
                                value=Value(
                                    value='gpo'
                                ),
                                minimum='1',
                                maximum='8',
                                data_type='integer'
                            ),
                        ]
                    ),
                    file_set_ref=[
                        FileSetRef(
                            local_name='fs-verilogSource'
                        ),
                    ]
                ),
                ComponentInstantiationType(
                    name='vhdlSource',
                    language=LanguageType(
                        value='vhdl'
                    ),
                    module_name='i2c_gpio_addr',
                    module_parameters=ComponentInstantiationType.ModuleParameters(
                        module_parameter=[
                            ModuleParameterType(
                                name='gpibits',
                                value=Value(
                                    value='gpi'
                                ),
                                minimum='1',
                                maximum='8',
                                data_type='integer'
                            ),
                            ModuleParameterType(
                                name='gpobits',
                                value=Value(
                                    value='gpo'
                                ),
                                minimum='1',
                                maximum='8',
                                data_type='integer'
                            ),
                        ]
                    ),
                    file_set_ref=[
                        FileSetRef(
                            local_name='fs-verilogSource'
                        ),
                        FileSetRef(
                            local_name='fs-vhdlWrapper'
                        ),
                    ]
                ),
            ]
        ),
        ports=ModelType.Ports(
            port=[
                Port(
                    name='scl',
                    wire=PortWireType(
                        direction=ComponentPortDirectionType.IN
                    )
                ),
                Port(
                    name='sda',
                    wire=PortWireType(
                        direction=ComponentPortDirectionType.INOUT
                    )
                ),
                Port(
                    name='address',
                    wire=PortWireType(
                        direction=ComponentPortDirectionType.IN,
                        vectors=ExtendedVectorsType(
                            vector=[
                                ExtendedVectorsType.Vector(
                                    left=Left(
                                        value='9'
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
                    name='gpi',
                    wire=PortWireType(
                        direction=ComponentPortDirectionType.IN,
                        vectors=ExtendedVectorsType(
                            vector=[
                                ExtendedVectorsType.Vector(
                                    left=Left(
                                        value='gpi - 1'
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
                    name='gpo',
                    wire=PortWireType(
                        direction=ComponentPortDirectionType.OUT,
                        vectors=ExtendedVectorsType(
                            vector=[
                                ExtendedVectorsType.Vector(
                                    left=Left(
                                        value='gpo - 1'
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
    file_sets=FileSets(
        file_set=[
            FileSet(
                name='fs-verilogSource',
                file=[
                    File(
                        name=IpxactUri(
                            value='data/i2c_gpio/RTL/i2c_gpio_addr.v'
                        ),
                        file_type=[
                            FileType(
                                value=SimpleFileType.VERILOG_SOURCE
                            ),
                        ],
                        logical_name=File.LogicalName(
                            value='i2c_gpio_lib'
                        )
                    ),
                ]
            ),
            FileSet(
                name='fs-vhdlWrapper',
                file=[
                    File(
                        name=IpxactUri(
                            value='data/i2c_gpio/RTL/i2c_gpio_addr.vhd'
                        ),
                        file_type=[
                            FileType(
                                value=SimpleFileType.VHDL_SOURCE
                            ),
                        ],
                        logical_name=File.LogicalName(
                            value='i2c_gpio_lib'
                        )
                    ),
                ]
            ),
        ]
    ),
    parameters=Parameters(
        parameter=[
            Parameter(
                name='gpibits',
                value=Value(
                    value='4'
                ),
                parameter_id='gpi',
                prompt='Number input bits:',
                minimum='1',
                maximum='8',
                resolve=ParameterTypeResolve.USER
            ),
            Parameter(
                name='gpobits',
                value=Value(
                    value='4'
                ),
                parameter_id='gpo',
                prompt='Number output bits:',
                minimum='1',
                maximum='8',
                resolve=ParameterTypeResolve.USER
            ),
        ]
    )
)
