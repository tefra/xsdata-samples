from ipxact.models.clock_driver import ClockDriver
from ipxact.models.clock_driver_type import ClockDriverType
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
from ipxact.models.format_type import FormatType
from ipxact.models.ipxact_uri import IpxactUri
from ipxact.models.language_type import LanguageType
from ipxact.models.model import Model
from ipxact.models.model_type import ModelType
from ipxact.models.parameter import Parameter
from ipxact.models.parameter_type_resolve import ParameterTypeResolve
from ipxact.models.parameters import Parameters
from ipxact.models.port import Port
from ipxact.models.port_wire_type import PortWireType
from ipxact.models.simple_file_type import SimpleFileType
from ipxact.models.single_shot_driver import SingleShotDriver
from ipxact.models.unsigned_bit_expression import UnsignedBitExpression
from ipxact.models.unsigned_bit_vector_expression import UnsignedBitVectorExpression
from ipxact.models.value import Value
from ipxact.models.wire_type_def import WireTypeDef
from ipxact.models.wire_type_defs import WireTypeDefs


obj = Component(
    vendor='spiritconsortium.org',
    library='Leon2TLM',
    name='Leon2Platform',
    version='1.3',
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
                        version='1.3'
                    )
                ),
            ]
        ),
        ports=ModelType.Ports(
            port=[
                Port(
                    name='clkin',
                    wire=PortWireType(
                        direction=ComponentPortDirectionType.IN,
                        wire_type_defs=WireTypeDefs(
                            wire_type_def=[
                                WireTypeDef(
                                    type_name=WireTypeDef.TypeName(
                                        value='bool'
                                    ),
                                    type_definition=[
                                        WireTypeDef.TypeDefinition(
                                            value='systemc.h'
                                        ),
                                    ],
                                    view_ref=[
                                        WireTypeDef.ViewRef(
                                            value='TLM_PV'
                                        ),
                                    ]
                                ),
                            ]
                        ),
                        drivers=Drivers(
                            driver=[
                                Driver(
                                    clock_driver=ClockDriver(
                                        clock_period=ClockDriverType.ClockPeriod(
                                            value='ClockPeriod'
                                        ),
                                        clock_pulse_offset=ClockDriverType.ClockPulseOffset(
                                            value='ClockPulseOffset'
                                        ),
                                        clock_pulse_value=UnsignedBitExpression(
                                            value='ClockPulseValue'
                                        ),
                                        clock_pulse_duration=ClockDriverType.ClockPulseDuration(
                                            value='ClockPulseDuration'
                                        ),
                                        clock_name='clkin'
                                    )
                                ),
                            ]
                        )
                    )
                ),
                Port(
                    name='rstin_an',
                    wire=PortWireType(
                        direction=ComponentPortDirectionType.IN,
                        wire_type_defs=WireTypeDefs(
                            wire_type_def=[
                                WireTypeDef(
                                    type_name=WireTypeDef.TypeName(
                                        value='sc_logic'
                                    ),
                                    type_definition=[
                                        WireTypeDef.TypeDefinition(
                                            value='systemc.h'
                                        ),
                                    ],
                                    view_ref=[
                                        WireTypeDef.ViewRef(
                                            value='TLM_PV'
                                        ),
                                    ]
                                ),
                            ]
                        ),
                        drivers=Drivers(
                            driver=[
                                Driver(
                                    single_shot_driver=SingleShotDriver(
                                        single_shot_offset=SingleShotDriver.SingleShotOffset(
                                            value='0.0'
                                        ),
                                        single_shot_value=UnsignedBitVectorExpression(
                                            value='0'
                                        ),
                                        single_shot_duration=SingleShotDriver.SingleShotDuration(
                                            value='10.0'
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
    ),
    parameters=Parameters(
        parameter=[
            Parameter(
                name='ClockPulseValue',
                value=Value(
                    value='1'
                ),
                parameter_id='ClockPulseValue',
                prompt='Clock Pulse Value:',
                type_value=FormatType.LONGINT,
                resolve=ParameterTypeResolve.USER
            ),
            Parameter(
                name='ClockPeriod',
                value=Value(
                    value='100.0'
                ),
                parameter_id='ClockPeriod',
                prompt='Clock Pulse Period:',
                type_value=FormatType.REAL,
                resolve=ParameterTypeResolve.USER
            ),
            Parameter(
                name='ClockPulseDuration',
                value=Value(
                    value='50.0'
                ),
                parameter_id='ClockPulseDuration',
                prompt='Clock Pulse Duration:',
                type_value=FormatType.REAL,
                resolve=ParameterTypeResolve.USER
            ),
            Parameter(
                name='ClockPulseOffset',
                value=Value(
                    value='50.0'
                ),
                parameter_id='ClockPulseOffset',
                prompt='Clock Pulse Offset:',
                type_value=FormatType.REAL,
                resolve=ParameterTypeResolve.USER
            ),
        ]
    )
)
