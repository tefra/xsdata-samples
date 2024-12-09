from ipxact.models.abstraction_types import AbstractionTypes
from ipxact.models.bus_interface import BusInterface
from ipxact.models.bus_interface_type import BusInterfaceType
from ipxact.models.bus_interfaces import BusInterfaces
from ipxact.models.component import Component
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
from ipxact.models.model import Model
from ipxact.models.model_type import ModelType
from ipxact.models.port import Port
from ipxact.models.port_access_handle import PortAccessHandle
from ipxact.models.port_access_type import PortAccessType
from ipxact.models.port_access_type_1 import PortAccessType1
from ipxact.models.port_path_segment_type import PortPathSegmentType
from ipxact.models.port_slice_type import PortSliceType
from ipxact.models.port_slices_type import PortSlicesType
from ipxact.models.port_transactional_type import PortTransactionalType
from ipxact.models.simple_file_type import SimpleFileType
from ipxact.models.simple_port_access_type import SimplePortAccessType
from ipxact.models.trans_type_def import TransTypeDef
from ipxact.models.trans_type_defs import TransTypeDefs
from ipxact.models.type_parameter import TypeParameter
from ipxact.models.type_parameters import ServiceTypeDef
from ipxact.models.type_parameters import TypeParameters
from ipxact.models.value import Value


obj = Component(
    vendor='spiritconsortium.org',
    library='Leon2TLM',
    name='serial_device',
    version='1.0',
    bus_interfaces=BusInterfaces(
        bus_interface=[
            BusInterface(
                name='SerialOut',
                bus_type=ConfigurableLibraryRefType(
                    vendor='spiritconsortium.org',
                    library='busdef.generic',
                    name='serial',
                    version='1.0'
                ),
                abstraction_types=AbstractionTypes(
                    abstraction_type=[
                        AbstractionTypes.AbstractionType(
                            abstraction_ref=ConfigurableLibraryRefType(
                                vendor='spiritconsortium.org',
                                library='abstractiondef.tlm',
                                name='serial_pv',
                                version='1.0'
                            ),
                            port_maps=AbstractionTypes.AbstractionType.PortMaps(
                                port_map=[
                                    AbstractionTypes.AbstractionType.PortMaps.PortMap(
                                        logical_port=AbstractionTypes.AbstractionType.PortMaps.PortMap.LogicalPort(
                                            name='RW_TRANSACTION'
                                        ),
                                        physical_port=AbstractionTypes.AbstractionType.PortMaps.PortMap.PhysicalPort(
                                            name='pSerialOut'
                                        )
                                    ),
                                ]
                            )
                        ),
                    ]
                ),
                initiator=BusInterfaceType.Initiator(

                ),
                connection_required=True
            ),
            BusInterface(
                name='SerialIn',
                bus_type=ConfigurableLibraryRefType(
                    vendor='spiritconsortium.org',
                    library='busdef.generic',
                    name='serial',
                    version='1.0'
                ),
                abstraction_types=AbstractionTypes(
                    abstraction_type=[
                        AbstractionTypes.AbstractionType(
                            abstraction_ref=ConfigurableLibraryRefType(
                                vendor='spiritconsortium.org',
                                library='abstractiondef.tlm',
                                name='serial_pv',
                                version='1.0'
                            ),
                            port_maps=AbstractionTypes.AbstractionType.PortMaps(
                                port_map=[
                                    AbstractionTypes.AbstractionType.PortMaps.PortMap(
                                        logical_port=AbstractionTypes.AbstractionType.PortMaps.PortMap.LogicalPort(
                                            name='RW_TRANSACTION'
                                        ),
                                        physical_port=AbstractionTypes.AbstractionType.PortMaps.PortMap.PhysicalPort(
                                            name='pSerialIn'
                                        )
                                    ),
                                ]
                            )
                        ),
                    ]
                ),
                target=BusInterfaceType.Target(

                ),
                connection_required=True
            ),
        ]
    ),
    model=Model(
        views=ModelType.Views(
            view=[
                ModelType.Views.View(
                    name='PVPVT',
                    env_identifier=[
                        ModelType.Views.View.EnvIdentifier(
                            value=':*Simulation:'
                        ),
                    ],
                    component_instantiation_ref='PVPVT'
                ),
            ]
        ),
        instantiations=ModelType.Instantiations(
            component_instantiation=[
                ComponentInstantiationType(
                    name='PVPVT',
                    language=LanguageType(
                        value='systemc2.1'
                    ),
                    module_name='SerialDevice',
                    file_set_ref=[
                        FileSetRef(
                            local_name='serialDeviceFileSet'
                        ),
                    ]
                ),
            ]
        ),
        ports=ModelType.Ports(
            port=[
                Port(
                    name='pSerialOut',
                    transactional=PortTransactionalType(
                        initiative=Initiative(
                            value=InitiativeType.REQUIRES
                        ),
                        trans_type_defs=TransTypeDefs(
                            trans_type_def=[
                                TransTypeDef(
                                    type_name=TransTypeDef.TypeName(
                                        value='sc_port'
                                    ),
                                    type_definition=[
                                        TransTypeDef.TypeDefinition(
                                            value='systemc.h'
                                        ),
                                    ],
                                    type_parameters=TypeParameters(
                                        service_type_def=[
                                            ServiceTypeDef(
                                                type_name=ServiceTypeDef.TypeName(
                                                    value='tlm::tlm_blocking_put_if'
                                                ),
                                                type_definition=[
                                                    ServiceTypeDef.TypeDefinition(
                                                        value='tlm_interfaces/tlm_core_ifs.h'
                                                    ),
                                                ],
                                                type_parameters=TypeParameters(
                                                    type_parameter=[
                                                        TypeParameter(
                                                            name='DATATYPE',
                                                            value=Value(
                                                                value='SERIAL_DATA_STRUCTURE'
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
                                                            value='pSerialOut'
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
                    name='pSerialIn',
                    transactional=PortTransactionalType(
                        initiative=Initiative(
                            value=InitiativeType.PROVIDES
                        ),
                        trans_type_defs=TransTypeDefs(
                            trans_type_def=[
                                TransTypeDef(
                                    type_name=TransTypeDef.TypeName(
                                        value='sc_export'
                                    ),
                                    type_definition=[
                                        TransTypeDef.TypeDefinition(
                                            value='systemc.h'
                                        ),
                                    ],
                                    type_parameters=TypeParameters(
                                        service_type_def=[
                                            ServiceTypeDef(
                                                type_name=ServiceTypeDef.TypeName(
                                                    value='tlm::tlm_blocking_put_if'
                                                ),
                                                type_definition=[
                                                    ServiceTypeDef.TypeDefinition(
                                                        value='tlm_interfaces/tlm_core_ifs.h'
                                                    ),
                                                ],
                                                type_parameters=TypeParameters(
                                                    type_parameter=[
                                                        TypeParameter(
                                                            name='DATATYPE',
                                                            value=Value(
                                                                value='SERIAL_DATA_STRUCTURE'
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
                                                            value='pSerialIn'
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
                name='serialDeviceFileSet',
                file=[
                    File(
                        name=IpxactUri(
                            value='./tlmsrc/serial_device.h'
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
                            value='serialDevice'
                        )
                    ),
                ]
            ),
        ]
    )
)
