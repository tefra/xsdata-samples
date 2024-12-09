from ipxact.models.component import Component
from ipxact.models.component_instantiation_type import ComponentInstantiationType
from ipxact.models.component_port_direction_type import ComponentPortDirectionType
from ipxact.models.extended_vectors_type import ExtendedVectorsType
from ipxact.models.file import File
from ipxact.models.file_set import FileSet
from ipxact.models.file_set_ref import FileSetRef
from ipxact.models.file_sets import FileSets
from ipxact.models.file_type import FileType
from ipxact.models.ipxact_uri import IpxactUri
from ipxact.models.language_type import LanguageType
from ipxact.models.left import Left
from ipxact.models.model import Model
from ipxact.models.model_type import ModelType
from ipxact.models.module_parameter_type import ModuleParameterType
from ipxact.models.parameter import Parameter
from ipxact.models.parameter_type_resolve import ParameterTypeResolve
from ipxact.models.parameters import Parameters
from ipxact.models.port import Port
from ipxact.models.port_wire_type import PortWireType
from ipxact.models.right import Right
from ipxact.models.simple_file_type import SimpleFileType
from ipxact.models.value import Value


obj = Component(
    vendor='spiritconsortium.org',
    library='Leon2RTL',
    name='dac',
    version='1.2',
    model=Model(
        views=ModelType.Views(
            view=[
                ModelType.Views.View(
                    name='vhdlSource',
                    env_identifier=[
                        ModelType.Views.View.EnvIdentifier(
                            value=':modelsim.mentor.com:'
                        ),
                        ModelType.Views.View.EnvIdentifier(
                            value=':ncsim.cadence.com:'
                        ),
                        ModelType.Views.View.EnvIdentifier(
                            value=':vcs.synopsys.com:'
                        ),
                        ModelType.Views.View.EnvIdentifier(
                            value=':designcompiler.synopsys.com:'
                        ),
                    ],
                    component_instantiation_ref='vhdlSource'
                ),
            ]
        ),
        instantiations=ModelType.Instantiations(
            component_instantiation=[
                ComponentInstantiationType(
                    name='vhdlSource',
                    language=LanguageType(
                        value='vhdl'
                    ),
                    module_name='dac',
                    module_parameters=ComponentInstantiationType.ModuleParameters(
                        module_parameter=[
                            ModuleParameterType(
                                name='WIDTH',
                                value=Value(
                                    value='dacwidth'
                                ),
                                minimum='1',
                                maximum='32',
                                data_type='integer'
                            ),
                        ]
                    ),
                    file_set_ref=[
                        FileSetRef(
                            local_name='fs-vhdlSource'
                        ),
                    ]
                ),
            ]
        ),
        ports=ModelType.Ports(
            port=[
                Port(
                    name='data',
                    wire=PortWireType(
                        direction=ComponentPortDirectionType.IN,
                        vectors=ExtendedVectorsType(
                            vector=[
                                ExtendedVectorsType.Vector(
                                    left=Left(
                                        value='dacwidth - 1'
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
                    name='clk',
                    wire=PortWireType(
                        direction=ComponentPortDirectionType.IN
                    )
                ),
            ]
        )
    ),
    file_sets=FileSets(
        file_set=[
            FileSet(
                name='fs-vhdlSource',
                file=[
                    File(
                        name=IpxactUri(
                            value='hdlsrc/dac.vhd'
                        ),
                        file_type=[
                            FileType(
                                value=SimpleFileType.VHDL_SOURCE
                            ),
                        ],
                        logical_name=File.LogicalName(
                            value='dac_lib'
                        )
                    ),
                ]
            ),
        ]
    ),
    parameters=Parameters(
        parameter=[
            Parameter(
                name='WIDTH',
                value=Value(
                    value='24'
                ),
                parameter_id='dacwidth',
                minimum='1',
                maximum='32',
                resolve=ParameterTypeResolve.USER
            ),
        ]
    )
)
