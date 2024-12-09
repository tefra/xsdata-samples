from ipxact.models.abstraction_types import AbstractionTypes
from ipxact.models.access_policies import AccessPolicies
from ipxact.models.access_type import AccessType
from ipxact.models.address_block import AddressBlock
from ipxact.models.address_block_type import AddressBlockType
from ipxact.models.base_address import BaseAddress
from ipxact.models.bus_interface import BusInterface
from ipxact.models.bus_interface_type import BusInterfaceType
from ipxact.models.bus_interfaces import BusInterfaces
from ipxact.models.choices import Choices
from ipxact.models.component import Component
from ipxact.models.component_instantiation_type import ComponentInstantiationType
from ipxact.models.configurable_library_ref_type import ConfigurableLibraryRefType
from ipxact.models.dependency import Dependency
from ipxact.models.description import Description
from ipxact.models.field_type import FieldType
from ipxact.models.file import File
from ipxact.models.file_set import FileSet
from ipxact.models.file_set_ref import FileSetRef
from ipxact.models.file_sets import FileSets
from ipxact.models.file_type import FileType
from ipxact.models.format_type import FormatType
from ipxact.models.initiative import Initiative
from ipxact.models.initiative_type import InitiativeType
from ipxact.models.ipxact_uri import IpxactUri
from ipxact.models.language_type import LanguageType
from ipxact.models.memory_map_ref import MemoryMapRef
from ipxact.models.memory_map_type import MemoryMapType
from ipxact.models.memory_maps import MemoryMaps
from ipxact.models.model import Model
from ipxact.models.model_type import ModelType
from ipxact.models.module_parameter_type import ModuleParameterType
from ipxact.models.module_parameter_type_usage_type import ModuleParameterTypeUsageType
from ipxact.models.parameter import Parameter
from ipxact.models.parameter_type_resolve import ParameterTypeResolve
from ipxact.models.parameters import Parameters
from ipxact.models.port import Port
from ipxact.models.port_access_handle import PortAccessHandle
from ipxact.models.port_access_type import PortAccessType
from ipxact.models.port_access_type_1 import PortAccessType1
from ipxact.models.port_path_segment_type import PortPathSegmentType
from ipxact.models.port_slice_type import PortSliceType
from ipxact.models.port_slices_type import PortSlicesType
from ipxact.models.port_transactional_type import PortTransactionalType
from ipxact.models.reset import Reset
from ipxact.models.simple_file_type import SimpleFileType
from ipxact.models.simple_port_access_type import SimplePortAccessType
from ipxact.models.trans_type_def import TransTypeDef
from ipxact.models.trans_type_defs import TransTypeDefs
from ipxact.models.type_parameter import TypeParameter
from ipxact.models.type_parameters import ServiceTypeDef
from ipxact.models.type_parameters import TypeParameters
from ipxact.models.unsigned_bit_vector_expression import UnsignedBitVectorExpression
from ipxact.models.unsigned_int_expression import UnsignedIntExpression
from ipxact.models.unsigned_longint_expression import UnsignedLongintExpression
from ipxact.models.unsigned_positive_int_expression import UnsignedPositiveIntExpression
from ipxact.models.unsigned_positive_longint_expression import UnsignedPositiveLongintExpression
from ipxact.models.usage_type import UsageType
from ipxact.models.value import Value


obj = Component(
    vendor='spiritconsortium.org',
    library='Leon2TLM',
    name='uart_tac',
    version='1.0',
    bus_interfaces=BusInterfaces(
        bus_interface=[
            BusInterface(
                name='ambaAPB',
                bus_type=ConfigurableLibraryRefType(
                    vendor='amba.com',
                    library='AMBA2',
                    name='APB',
                    version='r2p0_4'
                ),
                abstraction_types=AbstractionTypes(
                    abstraction_type=[
                        AbstractionTypes.AbstractionType(
                            abstraction_ref=ConfigurableLibraryRefType(
                                vendor='st.com',
                                library='SPG',
                                name='tlm_tac',
                                version='2.0'
                            ),
                            port_maps=AbstractionTypes.AbstractionType.PortMaps(
                                port_map=[
                                    AbstractionTypes.AbstractionType.PortMaps.PortMap(
                                        logical_port=AbstractionTypes.AbstractionType.PortMaps.PortMap.LogicalPort(
                                            name='tac_if'
                                        ),
                                        physical_port=AbstractionTypes.AbstractionType.PortMaps.PortMap.PhysicalPort(
                                            name='ambaAPB'
                                        )
                                    ),
                                ]
                            )
                        ),
                    ]
                ),
                target=BusInterfaceType.Target(
                    memory_map_ref=MemoryMapRef(
                        memory_map_ref='ambaAPB'
                    )
                )
            ),
        ]
    ),
    memory_maps=MemoryMaps(
        memory_map=[
            MemoryMapType(
                name='ambaAPB',
                address_block=[
                    AddressBlock(
                        name='ambaAPB',
                        base_address=BaseAddress(
                            value='0'
                        ),
                        range=UnsignedPositiveLongintExpression(
                            value='24'
                        ),
                        width=UnsignedPositiveIntExpression(
                            value='32'
                        ),
                        usage=UsageType.REGISTER,
                        register=[
                            AddressBlockType.Register(
                                name='data',
                                description=Description(
                                    value='Data read/write register'
                                ),
                                address_offset=UnsignedLongintExpression(
                                    value="'h0"
                                ),
                                size=UnsignedPositiveIntExpression(
                                    value='32'
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
                                        name='data',
                                        bit_offset=UnsignedIntExpression(
                                            value='0'
                                        ),
                                        bit_width=UnsignedPositiveIntExpression(
                                            value='32'
                                        ),
                                        resets=FieldType.Resets(
                                            reset=[
                                                Reset(
                                                    value=UnsignedBitVectorExpression(
                                                        value="'h0"
                                                    )
                                                ),
                                            ]
                                        )
                                    ),
                                ]
                            ),
                            AddressBlockType.Register(
                                name='status',
                                description=Description(
                                    value='Status register'
                                ),
                                address_offset=UnsignedLongintExpression(
                                    value="'h4"
                                ),
                                size=UnsignedPositiveIntExpression(
                                    value='32'
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
                                        name='status',
                                        bit_offset=UnsignedIntExpression(
                                            value='0'
                                        ),
                                        bit_width=UnsignedPositiveIntExpression(
                                            value='32'
                                        ),
                                        resets=FieldType.Resets(
                                            reset=[
                                                Reset(
                                                    value=UnsignedBitVectorExpression(
                                                        value="'h6"
                                                    )
                                                ),
                                            ]
                                        )
                                    ),
                                ]
                            ),
                            AddressBlockType.Register(
                                name='control',
                                description=Description(
                                    value='Control register'
                                ),
                                address_offset=UnsignedLongintExpression(
                                    value="'h8"
                                ),
                                size=UnsignedPositiveIntExpression(
                                    value='32'
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
                                        name='control',
                                        bit_offset=UnsignedIntExpression(
                                            value='0'
                                        ),
                                        bit_width=UnsignedPositiveIntExpression(
                                            value='32'
                                        ),
                                        resets=FieldType.Resets(
                                            reset=[
                                                Reset(
                                                    value=UnsignedBitVectorExpression(
                                                        value="'h0"
                                                    )
                                                ),
                                            ]
                                        )
                                    ),
                                ]
                            ),
                            AddressBlockType.Register(
                                name='scalarReload',
                                description=Description(
                                    value='Scalar reload register'
                                ),
                                address_offset=UnsignedLongintExpression(
                                    value="'hC"
                                ),
                                size=UnsignedPositiveIntExpression(
                                    value='32'
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
                                        name='scalarReload',
                                        bit_offset=UnsignedIntExpression(
                                            value='0'
                                        ),
                                        bit_width=UnsignedPositiveIntExpression(
                                            value='32'
                                        ),
                                        resets=FieldType.Resets(
                                            reset=[
                                                Reset(
                                                    value=UnsignedBitVectorExpression(
                                                        value="'h0"
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
                    name='PV',
                    env_identifier=[
                        ModelType.Views.View.EnvIdentifier(
                            value='systemCSource::'
                        ),
                    ],
                    component_instantiation_ref='PV'
                ),
            ]
        ),
        instantiations=ModelType.Instantiations(
            component_instantiation=[
                ComponentInstantiationType(
                    name='PV',
                    language=LanguageType(
                        value='systemCSource'
                    ),
                    module_name='Leon2::uart',
                    module_parameters=ComponentInstantiationType.ModuleParameters(
                        module_parameter=[
                            ModuleParameterType(
                                name='module_name',
                                value=Value(
                                    value='moduleName_id'
                                ),
                                data_type='sc_module_name',
                                usage_type=ModuleParameterTypeUsageType.NONTYPED
                            ),
                            ModuleParameterType(
                                name='resetOnInitialize',
                                value=Value(
                                    value='resetOnInitialize_id'
                                ),
                                type_value=FormatType.BIT,
                                data_type='bool',
                                usage_type=ModuleParameterTypeUsageType.NONTYPED
                            ),
                            ModuleParameterType(
                                name='debug_level',
                                value=Value(
                                    value='debug_level_id'
                                ),
                                type_value=FormatType.LONGINT,
                                data_type='unsigned int',
                                usage_type=ModuleParameterTypeUsageType.NONTYPED
                            ),
                            ModuleParameterType(
                                name='endianness',
                                value=Value(
                                    value='endianness_id'
                                ),
                                data_type='tlm_endianness endianness',
                                usage_type=ModuleParameterTypeUsageType.NONTYPED
                            ),
                        ]
                    ),
                    file_set_ref=[
                        FileSetRef(
                            local_name='fs-scSource'
                        ),
                    ]
                ),
            ]
        ),
        ports=ModelType.Ports(
            port=[
                Port(
                    name='ambaAPB',
                    transactional=PortTransactionalType(
                        initiative=Initiative(
                            value=InitiativeType.PROVIDES
                        ),
                        trans_type_defs=TransTypeDefs(
                            trans_type_def=[
                                TransTypeDef(
                                    type_name=TransTypeDef.TypeName(
                                        value='prt_tlm_tac::tac_target_port'
                                    ),
                                    type_definition=[
                                        TransTypeDef.TypeDefinition(
                                            value='tac_target_port.h'
                                        ),
                                    ],
                                    type_parameters=TypeParameters(
                                        service_type_def=[
                                            ServiceTypeDef(
                                                type_name=ServiceTypeDef.TypeName(
                                                    value='TAC',
                                                    implicit=True
                                                ),
                                                type_parameters=TypeParameters(
                                                    type_parameter=[
                                                        TypeParameter(
                                                            name='BFM_ADDRESS_TYPE',
                                                            value=Value(
                                                                value='tlm_uint32_t'
                                                            )
                                                        ),
                                                        TypeParameter(
                                                            name='BFM_DATA_TYPE',
                                                            value=Value(
                                                                value='tlm_uint32_t'
                                                            )
                                                        ),
                                                    ]
                                                )
                                            ),
                                        ]
                                    )
                                ),
                            ]
                        )
                    ),
                    access=PortAccessType1(
                        port_access_type=PortAccessType(
                            value=SimplePortAccessType.REF
                        ),
                        access_handles=PortAccessType1.AccessHandles(
                            access_handle=[
                                PortAccessHandle(
                                    slices=PortSlicesType(
                                        slice=[
                                            PortSliceType(
                                                path_segments=PortSliceType.PathSegments(
                                                    path_segment=[
                                                        PortPathSegmentType(
                                                            value='ambaAPB'
                                                        ),
                                                    ]
                                                )
                                            ),
                                        ]
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
                name='endianness',
                enumeration=[
                    Choices.Choice.Enumeration(
                        value='TLM_BIG_ENDIAN',
                        text='TLM_BIG_ENDIAN'
                    ),
                    Choices.Choice.Enumeration(
                        value='TLM_LITTLE_ENDIAN',
                        text='TLM_LITTLE_ENDIAN'
                    ),
                    Choices.Choice.Enumeration(
                        value='TLM_HOST_ENDIAN',
                        text='TLM_HOST_ENDIAN'
                    ),
                ]
            ),
        ]
    ),
    file_sets=FileSets(
        file_set=[
            FileSet(
                name='fs-scSource',
                file=[
                    File(
                        name=IpxactUri(
                            value='./tlmsrc/src/Leon2_uart.cpp'
                        ),
                        file_type=[
                            FileType(
                                value=SimpleFileType.SYSTEM_CSOURCE
                            ),
                        ],
                        dependency=[
                            Dependency(
                                value='./include'
                            ),
                        ]
                    ),
                    File(
                        name=IpxactUri(
                            value='./tlmsrc/src/tlmreg_Leon2_uart.cpp'
                        ),
                        file_type=[
                            FileType(
                                value=SimpleFileType.SYSTEM_CSOURCE
                            ),
                        ],
                        dependency=[
                            Dependency(
                                value='./include'
                            ),
                        ]
                    ),
                    File(
                        name=IpxactUri(
                            value='./tlmsrc/src/user_specific_Leon2_uart.cpp'
                        ),
                        file_type=[
                            FileType(
                                value=SimpleFileType.SYSTEM_CSOURCE
                            ),
                        ],
                        dependency=[
                            Dependency(
                                value='./include'
                            ),
                        ]
                    ),
                    File(
                        name=IpxactUri(
                            value='./tlmsrc/include/Leon2_uart.h'
                        ),
                        file_type=[
                            FileType(
                                value=SimpleFileType.SYSTEM_CSOURCE
                            ),
                        ],
                        is_include_file=File.IsIncludeFile(
                            value=True,
                            external_declarations=True
                        )
                    ),
                    File(
                        name=IpxactUri(
                            value='./tlmsrc/include/def_Leon2_uart.h'
                        ),
                        file_type=[
                            FileType(
                                value=SimpleFileType.SYSTEM_CSOURCE
                            ),
                        ],
                        is_include_file=File.IsIncludeFile(
                            value=True
                        )
                    ),
                    File(
                        name=IpxactUri(
                            value='./tlmsrc/include/tlmreg_Leon2_uart.h'
                        ),
                        file_type=[
                            FileType(
                                value=SimpleFileType.SYSTEM_CSOURCE
                            ),
                        ],
                        is_include_file=File.IsIncludeFile(
                            value=True
                        )
                    ),
                    File(
                        name=IpxactUri(
                            value='./tlmsrc/include/tlm_field.h'
                        ),
                        file_type=[
                            FileType(
                                value=SimpleFileType.SYSTEM_CSOURCE
                            ),
                        ],
                        is_include_file=File.IsIncludeFile(
                            value=True
                        )
                    ),
                    File(
                        name=IpxactUri(
                            value='./tlmsrc/include/tlm_register.h'
                        ),
                        file_type=[
                            FileType(
                                value=SimpleFileType.SYSTEM_CSOURCE
                            ),
                        ],
                        is_include_file=File.IsIncludeFile(
                            value=True
                        )
                    ),
                ]
            ),
        ]
    ),
    parameters=Parameters(
        parameter=[
            Parameter(
                name='module_name',
                value=Value(
                    value='""'
                ),
                parameter_id='moduleName_id',
                prompt='module name',
                config_groups=[
                    'requiredConfig',
                ],
                resolve=ParameterTypeResolve.GENERATED
            ),
            Parameter(
                name='resetOnInitialize',
                value=Value(
                    value='true'
                ),
                parameter_id='resetOnInitialize_id',
                prompt='whether reset() should be invoked at startup time',
                config_groups=[
                    'requiredConfig',
                ],
                type_value=FormatType.BIT,
                resolve=ParameterTypeResolve.USER
            ),
            Parameter(
                name='debug_level',
                value=Value(
                    value='0'
                ),
                parameter_id='debug_level_id',
                prompt='debug level',
                config_groups=[
                    'requiredConfig',
                ],
                type_value=FormatType.LONGINT,
                resolve=ParameterTypeResolve.USER
            ),
            Parameter(
                name='endianness',
                value=Value(
                    value='TLM_BIG_ENDIAN'
                ),
                parameter_id='endianness_id',
                prompt='use specific endianness',
                choice_ref='endianness',
                config_groups=[
                    'requiredConfig',
                ],
                resolve=ParameterTypeResolve.USER
            ),
        ]
    )
)
