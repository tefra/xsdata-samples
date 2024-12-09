from ipxact.models.clock_driver import ClockDriver
from ipxact.models.clock_driver_type import ClockDriverType
from ipxact.models.component import Component
from ipxact.models.component_port_direction_type import ComponentPortDirectionType
from ipxact.models.configurable_library_ref_type import ConfigurableLibraryRefType
from ipxact.models.design_instantiation_type import DesignInstantiationType
from ipxact.models.driver import Driver
from ipxact.models.drivers import Drivers
from ipxact.models.extended_vectors_type import ExtendedVectorsType
from ipxact.models.file import File
from ipxact.models.file_set import FileSet
from ipxact.models.file_sets import FileSets
from ipxact.models.file_type import FileType
from ipxact.models.ipxact_uri import IpxactUri
from ipxact.models.left import Left
from ipxact.models.model import Model
from ipxact.models.model_type import ModelType
from ipxact.models.port import Port
from ipxact.models.port_wire_type import PortWireType
from ipxact.models.right import Right
from ipxact.models.simple_file_type import SimpleFileType
from ipxact.models.single_shot_driver import SingleShotDriver
from ipxact.models.unsigned_bit_expression import UnsignedBitExpression
from ipxact.models.unsigned_bit_vector_expression import UnsignedBitVectorExpression


obj = Component(
    vendor='spiritconsortium.org',
    library='Leon2RTL',
    name='Leon2PlatformSystem',
    version='2.0',
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
            ]
        ),
        instantiations=ModelType.Instantiations(
            design_instantiation=[
                DesignInstantiationType(
                    name='spirit-design',
                    design_ref=ConfigurableLibraryRefType(
                        vendor='spiritconsortium.org',
                        library='Leon2RTL',
                        name='design_Leon2PlatformSystem',
                        version='2.0'
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
                        drivers=Drivers(
                            driver=[
                                Driver(
                                    clock_driver=ClockDriver(
                                        clock_period=ClockDriverType.ClockPeriod(
                                            value='100'
                                        ),
                                        clock_pulse_offset=ClockDriverType.ClockPulseOffset(
                                            value='50'
                                        ),
                                        clock_pulse_value=UnsignedBitExpression(
                                            value='1'
                                        ),
                                        clock_pulse_duration=ClockDriverType.ClockPulseDuration(
                                            value='50'
                                        ),
                                        clock_name='clk'
                                    )
                                ),
                            ]
                        )
                    )
                ),
                Port(
                    name='dac_clk',
                    wire=PortWireType(
                        direction=ComponentPortDirectionType.IN
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
                                        value='3'
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
                    name='i2c_gpio_address',
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
                    name='i2c_memory_address',
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
                    name='rstin_an',
                    wire=PortWireType(
                        direction=ComponentPortDirectionType.IN,
                        drivers=Drivers(
                            driver=[
                                Driver(
                                    single_shot_driver=SingleShotDriver(
                                        single_shot_offset=SingleShotDriver.SingleShotOffset(
                                            value='500'
                                        ),
                                        single_shot_value=UnsignedBitVectorExpression(
                                            value='1'
                                        ),
                                        single_shot_duration=SingleShotDriver.SingleShotDuration(
                                            value='1000'
                                        )
                                    )
                                ),
                            ]
                        )
                    )
                ),
                Port(
                    name='SimDone',
                    wire=PortWireType(
                        direction=ComponentPortDirectionType.OUT
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
                                        value='3'
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
                name='source-code',
                file=[
                    File(
                        name=IpxactUri(
                            value='hdlsrc/Leon2PlatformSystem_ent.vhd'
                        ),
                        file_type=[
                            FileType(
                                value=SimpleFileType.VHDL_SOURCE
                            ),
                        ],
                        logical_name=File.LogicalName(
                            value='work'
                        )
                    ),
                    File(
                        name=IpxactUri(
                            value='hdlsrc/Leon2PlatformSystem_pack.vhd'
                        ),
                        file_type=[
                            FileType(
                                value=SimpleFileType.VHDL_SOURCE
                            ),
                        ],
                        logical_name=File.LogicalName(
                            value='work'
                        )
                    ),
                    File(
                        name=IpxactUri(
                            value='hdlsrc/Leon2PlatformSystem_arch.vhd'
                        ),
                        file_type=[
                            FileType(
                                value=SimpleFileType.VHDL_SOURCE
                            ),
                        ],
                        logical_name=File.LogicalName(
                            value='work'
                        )
                    ),
                ]
            ),
        ]
    )
)
