from ipxact.models.component import Component
from ipxact.models.component_instantiation_type import ComponentInstantiationType
from ipxact.models.component_port_direction_type import ComponentPortDirectionType
from ipxact.models.configurable_library_ref_type import ConfigurableLibraryRefType
from ipxact.models.design_instantiation_type import DesignInstantiationType
from ipxact.models.driver import Driver
from ipxact.models.drivers import Drivers
from ipxact.models.file import File
from ipxact.models.file_set import FileSet
from ipxact.models.file_set_ref import FileSetRef
from ipxact.models.file_sets import FileSets
from ipxact.models.file_type import FileType
from ipxact.models.ipxact_uri import IpxactUri
from ipxact.models.language_type import LanguageType
from ipxact.models.model import Model
from ipxact.models.model_type import ModelType
from ipxact.models.port import Port
from ipxact.models.port_wire_type import PortWireType
from ipxact.models.simple_file_type import SimpleFileType
from ipxact.models.single_shot_driver import SingleShotDriver
from ipxact.models.unsigned_bit_vector_expression import UnsignedBitVectorExpression


obj = Component(
    vendor='spiritconsortium.org',
    library='Leon2TLM',
    name='Leon2Platform',
    version='1.1',
    model=Model(
        views=ModelType.Views(
            view=[
                ModelType.Views.View(
                    name='spirit-design',
                    env_identifier=[
                        ModelType.Views.View.EnvIdentifier(
                            value='::Hierarchy'
                        ),
                    ],
                    design_instantiation_ref='spirit-design'
                ),
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
                    module_name='Leon2Platform',
                    file_set_ref=[
                        FileSetRef(
                            local_name='sourceCode'
                        ),
                    ]
                ),
            ],
            design_instantiation=[
                DesignInstantiationType(
                    name='spirit-design',
                    design_ref=ConfigurableLibraryRefType(
                        vendor='spiritconsortium.org',
                        library='Leon2TLM',
                        name='design_Leon2Platform',
                        version='1.1'
                    )
                ),
            ]
        ),
        ports=ModelType.Ports(
            port=[
                Port(
                    name='rstin_an',
                    wire=PortWireType(
                        direction=ComponentPortDirectionType.IN,
                        drivers=Drivers(
                            driver=[
                                Driver(
                                    single_shot_driver=SingleShotDriver(
                                        single_shot_offset=SingleShotDriver.SingleShotOffset(
                                            value='500.0'
                                        ),
                                        single_shot_value=UnsignedBitVectorExpression(
                                            value='1'
                                        ),
                                        single_shot_duration=SingleShotDriver.SingleShotDuration(
                                            value='1000.0'
                                        )
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
                name='sourceCode',
                file=[
                    File(
                        name=IpxactUri(
                            value='tlmsrc/Leon2Platform.h'
                        ),
                        file_type=[
                            FileType(
                                value=SimpleFileType.SYSTEM_CSOURCE
                            ),
                        ],
                        is_include_file=File.IsIncludeFile(
                            value=True
                        ),
                        logical_name=File.LogicalName(
                            value='Leon2Platform'
                        )
                    ),
                ]
            ),
        ]
    )
)
