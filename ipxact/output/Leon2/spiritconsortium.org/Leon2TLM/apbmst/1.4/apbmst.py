from ipxact.models.abstraction_types import AbstractionTypes
from ipxact.models.address_spaces import AddressSpaces
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
from ipxact.models.signed_longint_expression import SignedLongintExpression
from ipxact.models.simple_file_type import SimpleFileType
from ipxact.models.subspace_map import SubspaceMap
from ipxact.models.trans_type_def import TransTypeDef
from ipxact.models.trans_type_defs import TransTypeDefs
from ipxact.models.type_parameter import TypeParameter
from ipxact.models.type_parameters import ServiceTypeDef
from ipxact.models.type_parameters import TypeParameters
from ipxact.models.unsigned_positive_int_expression import UnsignedPositiveIntExpression
from ipxact.models.unsigned_positive_longint_expression import UnsignedPositiveLongintExpression
from ipxact.models.value import Value


obj = Component(
    vendor='spiritconsortium.org',
    library='Leon2TLM',
    name='apbmst',
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
                                            name='target_port'
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
                ),
                connection_required=True
            ),
            BusInterface(
                name='APB_Master',
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
                                vendor='spiritconsortium.org',
                                library='abstractiondef.tlm',
                                name='apb_pv',
                                version='1.4'
                            ),
                            port_maps=AbstractionTypes.AbstractionType.PortMaps(
                                port_map=[
                                    AbstractionTypes.AbstractionType.PortMaps.PortMap(
                                        logical_port=AbstractionTypes.AbstractionType.PortMaps.PortMap.LogicalPort(
                                            name='PV_TRANS'
                                        ),
                                        physical_port=AbstractionTypes.AbstractionType.PortMaps.PortMap.PhysicalPort(
                                            name='initiator_port'
                                        )
                                    ),
                                ]
                            )
                        ),
                    ]
                ),
                initiator=BusInterfaceType.Initiator(
                    address_space_ref=BusInterfaceType.Initiator.AddressSpaceRef(
                        address_space_ref='APB_AS'
                    )
                )
            ),
        ]
    ),
    address_spaces=AddressSpaces(
        address_space=[
            AddressSpaces.AddressSpace(
                name='APB_AS',
                range=UnsignedPositiveLongintExpression(
                    value='masterRange'
                ),
                width=UnsignedPositiveIntExpression(
                    value='32'
                ),
                parameters=Parameters(
                    parameter=[
                        Parameter(
                            name='masterRange',
                            value=Value(
                                value='1 * (2 ** 20)'
                            ),
                            parameter_id='masterRange',
                            prompt='Master Port Size :',
                            choice_ref='addressWidthChoice',
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
                name='AHB_MM',
                subspace_map=[
                    SubspaceMap(
                        name='ahbMemoryMap',
                        base_address=SignedLongintExpression(
                            value='0'
                        ),
                        initiator_ref='APB_Master'
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
                    module_name='apbmst',
                    module_parameters=ComponentInstantiationType.ModuleParameters(
                        module_parameter=[
                            ModuleParameterType(
                                name='mapfile',
                                value=Value(
                                    value='mapfile'
                                ),
                                data_type='const char*',
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
                    name='target_port',
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
                Port(
                    name='initiator_port',
                    transactional=PortTransactionalType(
                        initiative=Initiative(
                            value=InitiativeType.REQUIRES
                        ),
                        trans_type_defs=TransTypeDefs(
                            trans_type_def=[
                                TransTypeDef(
                                    type_name=TransTypeDef.TypeName(
                                        value='pv_initiator_port'
                                    ),
                                    type_definition=[
                                        TransTypeDef.TypeDefinition(
                                            value='pv_initiator_port.h'
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
                        value='8K',
                        text='8K'
                    ),
                    Choices.Choice.Enumeration(
                        value='16K',
                        text='16K'
                    ),
                    Choices.Choice.Enumeration(
                        value='32K',
                        text='32K'
                    ),
                    Choices.Choice.Enumeration(
                        value='64K',
                        text='64K'
                    ),
                    Choices.Choice.Enumeration(
                        value='128K',
                        text='128K'
                    ),
                    Choices.Choice.Enumeration(
                        value='256K',
                        text='256K'
                    ),
                    Choices.Choice.Enumeration(
                        value='512K',
                        text='512K'
                    ),
                    Choices.Choice.Enumeration(
                        value='1M',
                        text='1M'
                    ),
                    Choices.Choice.Enumeration(
                        value='2M',
                        text='2M'
                    ),
                    Choices.Choice.Enumeration(
                        value='4M',
                        text='4M'
                    ),
                    Choices.Choice.Enumeration(
                        value='8M',
                        text='8M'
                    ),
                    Choices.Choice.Enumeration(
                        value='16M',
                        text='16M'
                    ),
                    Choices.Choice.Enumeration(
                        value='32M',
                        text='32M'
                    ),
                    Choices.Choice.Enumeration(
                        value='64M',
                        text='64M'
                    ),
                    Choices.Choice.Enumeration(
                        value='128M',
                        text='128M'
                    ),
                    Choices.Choice.Enumeration(
                        value='256M',
                        text='256M'
                    ),
                    Choices.Choice.Enumeration(
                        value='1024M',
                        text='1024M'
                    ),
                    Choices.Choice.Enumeration(
                        value='2048M',
                        text='2048M'
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
                            value='tlmsrc/apbmst.h'
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
                            value='apbmst'
                        ),
                        dependency=[
                            Dependency(
                                value='../../PV'
                            ),
                        ]
                    ),
                    File(
                        name=IpxactUri(
                            value='../../PV/pv_router.h'
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
                name='mapfile',
                value=Value(
                    value='apbmstMapFile.map'
                ),
                parameter_id='mapfile',
                resolve=ParameterTypeResolve.USER
            ),
        ]
    )
)
