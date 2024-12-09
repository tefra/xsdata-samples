from ipxact.models.abstraction_types import AbstractionTypes
from ipxact.models.abstractor import Abstractor
from ipxact.models.abstractor_bus_interface_type import AbstractorBusInterfaceType
from ipxact.models.abstractor_mode_type import AbstractorModeType
from ipxact.models.abstractor_model_type import AbstractorModelType
from ipxact.models.abstractor_port_transactional_type import AbstractorPortTransactionalType
from ipxact.models.abstractor_port_type import AbstractorPortType
from ipxact.models.abstractor_type import AbstractorType
from ipxact.models.component_instantiation_type import ComponentInstantiationType
from ipxact.models.configurable_library_ref_type import ConfigurableLibraryRefType
from ipxact.models.file import File
from ipxact.models.file_set import FileSet
from ipxact.models.file_set_ref import FileSetRef
from ipxact.models.file_sets import FileSets
from ipxact.models.file_type import FileType
from ipxact.models.initiative import Initiative
from ipxact.models.initiative_type import InitiativeType
from ipxact.models.ipxact_uri import IpxactUri
from ipxact.models.language_type import LanguageType
from ipxact.models.library_ref_type import LibraryRefType
from ipxact.models.port_access_handle import PortAccessHandle
from ipxact.models.port_access_type import PortAccessType
from ipxact.models.port_access_type_1 import PortAccessType1
from ipxact.models.port_path_segment_type import PortPathSegmentType
from ipxact.models.port_slice_type import PortSliceType
from ipxact.models.port_slices_type import PortSlicesType
from ipxact.models.simple_file_type import SimpleFileType
from ipxact.models.simple_port_access_type import SimplePortAccessType
from ipxact.models.trans_type_def import TransTypeDef
from ipxact.models.trans_type_defs import TransTypeDefs
from ipxact.models.type_parameter import TypeParameter
from ipxact.models.type_parameters import ServiceTypeDef
from ipxact.models.type_parameters import TypeParameters
from ipxact.models.value import Value


obj = Abstractor(
    vendor='spiritconsortium.org',
    library='Leon2TLM',
    name='scmlAdaptor',
    version='1.0',
    abstractor_mode=AbstractorType.AbstractorMode(
        value=AbstractorModeType.DIRECT
    ),
    bus_type=LibraryRefType(
        vendor='amba.com',
        library='AMBA2',
        name='APB',
        version='r2p0_4'
    ),
    abstractor_interfaces=AbstractorType.AbstractorInterfaces(
        abstractor_interface=[
            AbstractorBusInterfaceType(
                name='APB_Slave',
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
                                            name='apb_slave_port'
                                        )
                                    ),
                                ]
                            )
                        ),
                    ]
                )
            ),
            AbstractorBusInterfaceType(
                name='ambaAPB',
                abstraction_types=AbstractionTypes(
                    abstraction_type=[
                        AbstractionTypes.AbstractionType(
                            abstraction_ref=ConfigurableLibraryRefType(
                                vendor='coware.com',
                                library='SCML',
                                name='APB_PV',
                                version='1.1'
                            ),
                            port_maps=AbstractionTypes.AbstractionType.PortMaps(
                                port_map=[
                                    AbstractionTypes.AbstractionType.PortMaps.PortMap(
                                        logical_port=AbstractionTypes.AbstractionType.PortMaps.PortMap.LogicalPort(
                                            name='PV'
                                        ),
                                        physical_port=AbstractionTypes.AbstractionType.PortMaps.PortMap.PhysicalPort(
                                            name='scml_master_port'
                                        )
                                    ),
                                ]
                            )
                        ),
                    ]
                )
            ),
        ]
    ),
    model=AbstractorModelType(
        views=AbstractorModelType.Views(
            view=[
                AbstractorModelType.Views.View(
                    name='PVPVT',
                    env_identifier=[
                        AbstractorModelType.Views.View.EnvIdentifier(
                            value=':*Simulation:'
                        ),
                    ],
                    component_instantiation_ref='PVPVT'
                ),
            ]
        ),
        instantiations=AbstractorModelType.Instantiations(
            component_instantiation=[
                ComponentInstantiationType(
                    name='PVPVT',
                    language=LanguageType(
                        value='systemc2.1'
                    ),
                    module_name='scmlAdaptor',
                    file_set_ref=[
                        FileSetRef(
                            local_name='scmlAdaptorFileSet'
                        ),
                    ]
                ),
            ]
        ),
        ports=AbstractorModelType.Ports(
            port=[
                AbstractorPortType(
                    name='apb_slave_port',
                    transactional=AbstractorPortTransactionalType(
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
                AbstractorPortType(
                    name='scml_master_port',
                    transactional=AbstractorPortTransactionalType(
                        initiative=Initiative(
                            value=InitiativeType.REQUIRES
                        ),
                        trans_type_defs=TransTypeDefs(
                            trans_type_def=[
                                TransTypeDef(
                                    type_name=TransTypeDef.TypeName(
                                        value='PVInitiator_port'
                                    ),
                                    type_definition=[
                                        TransTypeDef.TypeDefinition(
                                            value='PV/PV.h'
                                        ),
                                    ],
                                    type_parameters=TypeParameters(
                                        service_type_def=[
                                            ServiceTypeDef(
                                                type_name=ServiceTypeDef.TypeName(
                                                    value='SCML',
                                                    implicit=True
                                                ),
                                                type_parameters=TypeParameters(
                                                    type_parameter=[
                                                        TypeParameter(
                                                            name='DT',
                                                            value=Value(
                                                                value='DATA_TYPE'
                                                            )
                                                        ),
                                                        TypeParameter(
                                                            name='AT',
                                                            value=Value(
                                                                value='ADDRESS_TYPE'
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
                                                            value='scml_master_port'
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
    file_sets=FileSets(
        file_set=[
            FileSet(
                name='scmlAdaptorFileSet',
                file=[
                    File(
                        name=IpxactUri(
                            value='./tlmsrc/inc/scmladaptor.h'
                        ),
                        file_type=[
                            FileType(
                                value=SimpleFileType.SYSTEM_CSOURCE_2_1
                            ),
                        ],
                        is_include_file=File.IsIncludeFile(
                            value=True,
                            external_declarations=True
                        ),
                        logical_name=File.LogicalName(
                            value='uart_scml'
                        )
                    ),
                    File(
                        name=IpxactUri(
                            value='./tlmsrc/inc/scmladaptor.cc'
                        ),
                        file_type=[
                            FileType(
                                value=SimpleFileType.SYSTEM_CSOURCE_2_1
                            ),
                        ],
                        logical_name=File.LogicalName(
                            value='uart_scml'
                        )
                    ),
                ]
            ),
        ]
    )
)
