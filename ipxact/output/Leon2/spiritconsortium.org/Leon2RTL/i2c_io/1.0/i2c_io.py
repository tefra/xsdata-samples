from ipxact.models.abstraction_types import AbstractionTypes
from ipxact.models.bus_interface import BusInterface
from ipxact.models.bus_interface_type import BusInterfaceType
from ipxact.models.bus_interfaces import BusInterfaces
from ipxact.models.component import Component
from ipxact.models.component_instantiation_type import ComponentInstantiationType
from ipxact.models.component_port_direction_type import ComponentPortDirectionType
from ipxact.models.configurable_library_ref_type import ConfigurableLibraryRefType
from ipxact.models.default_value import DefaultValue
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


obj = Component(
    vendor='spiritconsortium.org',
    library='Leon2RTL',
    name='i2c_io',
    version='1.0',
    bus_interfaces=BusInterfaces(
        bus_interface=[
            BusInterface(
                name='i2c_internal',
                bus_type=ConfigurableLibraryRefType(
                    vendor='spiritconsortium.org',
                    library='busdef.nxp',
                    name='i2c_internal',
                    version='1.0'
                ),
                abstraction_types=AbstractionTypes(
                    abstraction_type=[
                        AbstractionTypes.AbstractionType(
                            abstraction_ref=ConfigurableLibraryRefType(
                                vendor='spiritconsortium.org',
                                library='busdef.nxp',
                                name='i2c_internal_rtl',
                                version='1.0'
                            ),
                            port_maps=AbstractionTypes.AbstractionType.PortMaps(
                                port_map=[
                                    AbstractionTypes.AbstractionType.PortMaps.PortMap(
                                        logical_port=AbstractionTypes.AbstractionType.PortMaps.PortMap.LogicalPort(
                                            name='SCL_IN'
                                        ),
                                        physical_port=AbstractionTypes.AbstractionType.PortMaps.PortMap.PhysicalPort(
                                            name='scl_in'
                                        )
                                    ),
                                    AbstractionTypes.AbstractionType.PortMaps.PortMap(
                                        logical_port=AbstractionTypes.AbstractionType.PortMaps.PortMap.LogicalPort(
                                            name='SCL_OUT'
                                        ),
                                        physical_port=AbstractionTypes.AbstractionType.PortMaps.PortMap.PhysicalPort(
                                            name='scl_out'
                                        )
                                    ),
                                    AbstractionTypes.AbstractionType.PortMaps.PortMap(
                                        logical_port=AbstractionTypes.AbstractionType.PortMaps.PortMap.LogicalPort(
                                            name='SCL_OEN'
                                        ),
                                        physical_port=AbstractionTypes.AbstractionType.PortMaps.PortMap.PhysicalPort(
                                            name='scl_oen'
                                        )
                                    ),
                                    AbstractionTypes.AbstractionType.PortMaps.PortMap(
                                        logical_port=AbstractionTypes.AbstractionType.PortMaps.PortMap.LogicalPort(
                                            name='SDA_IN'
                                        ),
                                        physical_port=AbstractionTypes.AbstractionType.PortMaps.PortMap.PhysicalPort(
                                            name='sda_in'
                                        )
                                    ),
                                    AbstractionTypes.AbstractionType.PortMaps.PortMap(
                                        logical_port=AbstractionTypes.AbstractionType.PortMaps.PortMap.LogicalPort(
                                            name='SDA_OUT'
                                        ),
                                        physical_port=AbstractionTypes.AbstractionType.PortMaps.PortMap.PhysicalPort(
                                            name='sda_out'
                                        )
                                    ),
                                    AbstractionTypes.AbstractionType.PortMaps.PortMap(
                                        logical_port=AbstractionTypes.AbstractionType.PortMaps.PortMap.LogicalPort(
                                            name='SDA_OEN'
                                        ),
                                        physical_port=AbstractionTypes.AbstractionType.PortMaps.PortMap.PhysicalPort(
                                            name='sda_oen'
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
            BusInterface(
                name='i2c',
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
                initiator=BusInterfaceType.Initiator(

                ),
                connection_required=True
            ),
        ]
    ),
    model=Model(
        views=ModelType.Views(
            view=[
                ModelType.Views.View(
                    name='verilogsource',
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
                    component_instantiation_ref='verilogsource'
                ),
                ModelType.Views.View(
                    name='vhdlsource',
                    env_identifier=[
                        ModelType.Views.View.EnvIdentifier(
                            value=':ncsim.cadence.com:'
                        ),
                    ],
                    component_instantiation_ref='vhdlsource'
                ),
            ]
        ),
        instantiations=ModelType.Instantiations(
            component_instantiation=[
                ComponentInstantiationType(
                    name='verilogsource',
                    language=LanguageType(
                        value='verilog'
                    ),
                    module_name='i2c_io',
                    file_set_ref=[
                        FileSetRef(
                            local_name='fs-verilogSource'
                        ),
                    ]
                ),
                ComponentInstantiationType(
                    name='vhdlsource',
                    language=LanguageType(
                        value='vhdl'
                    ),
                    module_name='i2c_io',
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
                        direction=ComponentPortDirectionType.INOUT
                    )
                ),
                Port(
                    name='sda',
                    wire=PortWireType(
                        direction=ComponentPortDirectionType.INOUT
                    )
                ),
                Port(
                    name='scl_in',
                    wire=PortWireType(
                        direction=ComponentPortDirectionType.OUT
                    )
                ),
                Port(
                    name='scl_out',
                    wire=PortWireType(
                        direction=ComponentPortDirectionType.IN,
                        drivers=Drivers(
                            driver=[
                                Driver(
                                    default_value=DefaultValue(
                                        value='0'
                                    )
                                ),
                            ]
                        )
                    )
                ),
                Port(
                    name='scl_oen',
                    wire=PortWireType(
                        direction=ComponentPortDirectionType.IN,
                        drivers=Drivers(
                            driver=[
                                Driver(
                                    default_value=DefaultValue(
                                        value='1'
                                    )
                                ),
                            ]
                        )
                    )
                ),
                Port(
                    name='sda_in',
                    wire=PortWireType(
                        direction=ComponentPortDirectionType.OUT
                    )
                ),
                Port(
                    name='sda_out',
                    wire=PortWireType(
                        direction=ComponentPortDirectionType.IN,
                        drivers=Drivers(
                            driver=[
                                Driver(
                                    default_value=DefaultValue(
                                        value='0'
                                    )
                                ),
                            ]
                        )
                    )
                ),
                Port(
                    name='sda_oen',
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
                name='fs-verilogSource',
                file=[
                    File(
                        name=IpxactUri(
                            value='data/i2c_io/RTL/i2c_io.v'
                        ),
                        file_type=[
                            FileType(
                                value=SimpleFileType.VERILOG_SOURCE
                            ),
                        ],
                        logical_name=File.LogicalName(
                            value='i2c_io_lib'
                        )
                    ),
                ]
            ),
            FileSet(
                name='fs-vhdlWrapper',
                file=[
                    File(
                        name=IpxactUri(
                            value='data/i2c_io/RTL/i2c_io.vhd'
                        ),
                        file_type=[
                            FileType(
                                value=SimpleFileType.VHDL_SOURCE
                            ),
                        ],
                        logical_name=File.LogicalName(
                            value='i2c_io_lib'
                        )
                    ),
                ]
            ),
        ]
    )
)