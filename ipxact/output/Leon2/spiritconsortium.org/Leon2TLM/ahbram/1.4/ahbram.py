from ipxact.models.abstraction_types import AbstractionTypes
from ipxact.models.access_policies import AccessPolicies
from ipxact.models.access_type import AccessType
from ipxact.models.bank import Bank
from ipxact.models.bank_alignment_type import BankAlignmentType
from ipxact.models.banked_block_type import BankedBlockType
from ipxact.models.base_address import BaseAddress
from ipxact.models.bus_interface import BusInterface
from ipxact.models.bus_interface_type import BusInterfaceType
from ipxact.models.bus_interfaces import BusInterfaces
from ipxact.models.choices import Choices
from ipxact.models.component import Component
from ipxact.models.component_instantiation_type import ComponentInstantiationType
from ipxact.models.configurable_library_ref_type import ConfigurableLibraryRefType
from ipxact.models.dependency import Dependency
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
from ipxact.models.port_transactional_type import PortTransactionalType
from ipxact.models.simple_file_type import SimpleFileType
from ipxact.models.trans_type_def import TransTypeDef
from ipxact.models.trans_type_defs import TransTypeDefs
from ipxact.models.type_parameter import TypeParameter
from ipxact.models.type_parameters import ServiceTypeDef
from ipxact.models.type_parameters import TypeParameters
from ipxact.models.unsigned_positive_int_expression import UnsignedPositiveIntExpression
from ipxact.models.unsigned_positive_longint_expression import UnsignedPositiveLongintExpression
from ipxact.models.usage_type import UsageType
from ipxact.models.value import Value


obj = Component(
    vendor='spiritconsortium.org',
    library='Leon2TLM',
    name='ahbram',
    version='1.4',
    bus_interfaces=BusInterfaces(
        bus_interface=[
            BusInterface(
                name='AHB_Slave',
                bus_type=ConfigurableLibraryRefType(
                    vendor='amba.com',
                    library='AMBA2',
                    name='AHB',
                    version='r2p0_6'
                ),
                abstraction_types=AbstractionTypes(
                    abstraction_type=[
                        AbstractionTypes.AbstractionType(
                            abstraction_ref=ConfigurableLibraryRefType(
                                vendor='spiritconsortium.org',
                                library='abstractiondef.tlm',
                                name='ahb_pv',
                                version='1.4'
                            ),
                            port_maps=AbstractionTypes.AbstractionType.PortMaps(
                                port_map=[
                                    AbstractionTypes.AbstractionType.PortMaps.PortMap(
                                        logical_port=AbstractionTypes.AbstractionType.PortMaps.PortMap.LogicalPort(
                                            name='PV_TRANS'
                                        ),
                                        physical_port=AbstractionTypes.AbstractionType.PortMaps.PortMap.PhysicalPort(
                                            name='ahb_slave_port'
                                        )
                                    ),
                                ]
                            )
                        ),
                    ]
                ),
                target=BusInterfaceType.Target(
                    memory_map_ref=MemoryMapRef(
                        memory_map_ref='AHB_MM'
                    )
                )
            ),
        ]
    ),
    memory_maps=MemoryMaps(
        memory_map=[
            MemoryMapType(
                name='AHB_MM',
                bank=[
                    Bank(
                        name='ahbMemoryMap',
                        base_address=BaseAddress(
                            value='memoryBaseAddress'
                        ),
                        address_block=[
                            BankedBlockType(
                                name='defaultid4489955',
                                range=UnsignedPositiveLongintExpression(
                                    value="longint'($pow(2, addressBusSize))"
                                ),
                                width=UnsignedPositiveIntExpression(
                                    value='8'
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
                                            name='addressRange0',
                                            value=Value(
                                                value="longint'($pow(2, addressBusSize))"
                                            ),
                                            parameter_id='addressRange0',
                                            type_value=FormatType.LONGINT
                                        ),
                                    ]
                                )
                            ),
                            BankedBlockType(
                                name='defaultid4489979',
                                range=UnsignedPositiveLongintExpression(
                                    value="longint'($pow(2, addressBusSize))"
                                ),
                                width=UnsignedPositiveIntExpression(
                                    value='8'
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
                                            name='addressRange1',
                                            value=Value(
                                                value="longint'($pow(2, addressBusSize))"
                                            ),
                                            parameter_id='addressRange1',
                                            type_value=FormatType.LONGINT
                                        ),
                                    ]
                                )
                            ),
                            BankedBlockType(
                                name='defaultid4490002',
                                range=UnsignedPositiveLongintExpression(
                                    value="longint'($pow(2, addressBusSize))"
                                ),
                                width=UnsignedPositiveIntExpression(
                                    value='8'
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
                                            name='addressRange2',
                                            value=Value(
                                                value="longint'($pow(2, addressBusSize))"
                                            ),
                                            parameter_id='addressRange2',
                                            type_value=FormatType.LONGINT
                                        ),
                                    ]
                                )
                            ),
                            BankedBlockType(
                                name='defaultid4490024',
                                range=UnsignedPositiveLongintExpression(
                                    value="longint'($pow(2, addressBusSize))"
                                ),
                                width=UnsignedPositiveIntExpression(
                                    value='8'
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
                                            name='addressRange3',
                                            value=Value(
                                                value="longint'($pow(2, addressBusSize))"
                                            ),
                                            parameter_id='addressRange3',
                                            type_value=FormatType.LONGINT
                                        ),
                                    ]
                                )
                            ),
                        ],
                        parameters=Parameters(
                            parameter=[
                                Parameter(
                                    name='memoryBaseAddress',
                                    value=Value(
                                        value="'h00000000"
                                    ),
                                    parameter_id='memoryBaseAddress',
                                    prompt='Base address offset:',
                                    config_groups=[
                                        'immediate',
                                    ],
                                    type_value=FormatType.LONGINT,
                                    resolve=ParameterTypeResolve.USER
                                ),
                            ]
                        ),
                        bank_alignment=BankAlignmentType.PARALLEL
                    ),
                ]
            ),
        ]
    ),
    model=Model(
        views=ModelType.Views(
            view=[
                ModelType.Views.View(
                    name='TLM_PV',
                    env_identifier=[
                        ModelType.Views.View.EnvIdentifier(
                            value=':*Simulation:'
                        ),
                    ],
                    component_instantiation_ref='TLM_PV'
                ),
            ]
        ),
        instantiations=ModelType.Instantiations(
            component_instantiation=[
                ComponentInstantiationType(
                    name='TLM_PV',
                    language=LanguageType(
                        value='systemc'
                    ),
                    module_name='ahbram',
                    module_parameters=ComponentInstantiationType.ModuleParameters(
                        module_parameter=[
                            ModuleParameterType(
                                name='addrsize',
                                value=Value(
                                    value='addressBusSize'
                                ),
                                type_value=FormatType.LONGINT,
                                data_type='unsigned long',
                                usage_type=ModuleParameterTypeUsageType.NONTYPED
                            ),
                        ]
                    ),
                    file_set_ref=[
                        FileSetRef(
                            local_name='sourceCode'
                        ),
                    ]
                ),
            ]
        ),
        ports=ModelType.Ports(
            port=[
                Port(
                    name='ahb_slave_port',
                    transactional=PortTransactionalType(
                        initiative=Initiative(
                            value=InitiativeType.PROVIDES
                        ),
                        trans_type_defs=TransTypeDefs(
                            trans_type_def=[
                                TransTypeDef(
                                    type_name=TransTypeDef.TypeName(
                                        value='pv_target_port'
                                    ),
                                    type_definition=[
                                        TransTypeDef.TypeDefinition(
                                            value='pv_target_port.h'
                                        ),
                                    ],
                                    type_parameters=TypeParameters(
                                        service_type_def=[
                                            ServiceTypeDef(
                                                type_name=ServiceTypeDef.TypeName(
                                                    value='OSCI_TLM_PV',
                                                    implicit=True
                                                ),
                                                type_parameters=TypeParameters(
                                                    type_parameter=[
                                                        TypeParameter(
                                                            name='typedef1',
                                                            value=Value(
                                                                value='ADDRESS_TYPE'
                                                            )
                                                        ),
                                                        TypeParameter(
                                                            name='typedef2',
                                                            value=Value(
                                                                value='DATA_TYPE'
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
                    )
                ),
            ]
        )
    ),
    choices=Choices(
        choice=[
            Choices.Choice(
                name='addressWidthChoice',
                enumeration=[
                    Choices.Choice.Enumeration(
                        value='8',
                        text='1K'
                    ),
                    Choices.Choice.Enumeration(
                        value='9',
                        text='2K'
                    ),
                    Choices.Choice.Enumeration(
                        value='10',
                        text='4K'
                    ),
                    Choices.Choice.Enumeration(
                        value='11',
                        text='8K'
                    ),
                    Choices.Choice.Enumeration(
                        value='12',
                        text='16K'
                    ),
                    Choices.Choice.Enumeration(
                        value='13',
                        text='32K'
                    ),
                    Choices.Choice.Enumeration(
                        value='14',
                        text='64K'
                    ),
                    Choices.Choice.Enumeration(
                        value='15',
                        text='128K'
                    ),
                    Choices.Choice.Enumeration(
                        value='16',
                        text='256K'
                    ),
                ]
            ),
        ]
    ),
    file_sets=FileSets(
        file_set=[
            FileSet(
                name='sourceCode',
                file=[
                    File(
                        name=IpxactUri(
                            value='tlmsrc/ahbram.cc'
                        ),
                        file_type=[
                            FileType(
                                value=SimpleFileType.SYSTEM_CSOURCE
                            ),
                        ],
                        dependency=[
                            Dependency(
                                value='tlmsrc'
                            ),
                        ]
                    ),
                    File(
                        name=IpxactUri(
                            value='tlmsrc/ahbram.h'
                        ),
                        file_type=[
                            FileType(
                                value=SimpleFileType.SYSTEM_CSOURCE
                            ),
                        ],
                        is_include_file=File.IsIncludeFile(
                            value=True,
                            external_declarations=True
                        ),
                        logical_name=File.LogicalName(
                            value='ahbram'
                        ),
                        dependency=[
                            Dependency(
                                value='../../PV'
                            ),
                        ]
                    ),
                    File(
                        name=IpxactUri(
                            value='../../PV/pv_slave_base.h'
                        ),
                        file_type=[
                            FileType(
                                value=SimpleFileType.UNKNOWN
                            ),
                        ],
                        is_include_file=File.IsIncludeFile(
                            value=True
                        )
                    ),
                    File(
                        name=IpxactUri(
                            value='../../PV/pv_target_port.h'
                        ),
                        file_type=[
                            FileType(
                                value=SimpleFileType.UNKNOWN
                            ),
                        ],
                        is_include_file=File.IsIncludeFile(
                            value=True
                        )
                    ),
                    File(
                        name=IpxactUri(
                            value='../../PV/user_types.h'
                        ),
                        file_type=[
                            FileType(
                                value=SimpleFileType.UNKNOWN
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
                name='addrsize',
                value=Value(
                    value='16'
                ),
                parameter_id='addressBusSize',
                prompt='RAM Depth (bytes):',
                choice_ref='addressWidthChoice',
                config_groups=[
                    'requiredConfig',
                ],
                type_value=FormatType.LONGINT,
                resolve=ParameterTypeResolve.USER
            ),
        ]
    )
)
