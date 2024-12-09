from ipxact.models.abstraction_types import AbstractionTypes
from ipxact.models.bus_interface import BusInterface
from ipxact.models.bus_interface_type import BusInterfaceType
from ipxact.models.bus_interfaces import BusInterfaces
from ipxact.models.component import Component
from ipxact.models.component_instantiation_type import ComponentInstantiationType
from ipxact.models.component_port_direction_type import ComponentPortDirectionType
from ipxact.models.configurable_library_ref_type import ConfigurableLibraryRefType
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
    name='i2c_gpio',
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

                )
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
                    module_name='i2c_gpio',
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
                    module_name='i2c_gpio',
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
                            value='data/i2c_gpio/RTL/i2c_gpio.v'
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
                            value='data/i2c_gpio/RTL/i2c_gpio.vhd'
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
