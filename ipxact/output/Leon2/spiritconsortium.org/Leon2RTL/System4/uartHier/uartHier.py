from ipxact.models.abstraction_types import AbstractionTypes
from ipxact.models.bus_interface import BusInterface
from ipxact.models.bus_interface_type import BusInterfaceType
from ipxact.models.bus_interfaces import BusInterfaces
from ipxact.models.clock_driver import ClockDriver
from ipxact.models.clock_driver_type import ClockDriverType
from ipxact.models.component import Component
from ipxact.models.component_port_direction_type import ComponentPortDirectionType
from ipxact.models.configurable_library_ref_type import ConfigurableLibraryRefType
from ipxact.models.constraint_set import ConstraintSet
from ipxact.models.constraint_sets import ConstraintSets
from ipxact.models.default_value import DefaultValue
from ipxact.models.design_instantiation_type import DesignInstantiationType
from ipxact.models.driver import Driver
from ipxact.models.drivers import Drivers
from ipxact.models.extended_vectors_type import ExtendedVectorsType
from ipxact.models.file import File
from ipxact.models.file_set import FileSet
from ipxact.models.file_sets import FileSets
from ipxact.models.file_type import FileType
from ipxact.models.format_type import FormatType
from ipxact.models.ipxact_uri import IpxactUri
from ipxact.models.left import Left
from ipxact.models.model import Model
from ipxact.models.model_type import ModelType
from ipxact.models.other_clock_driver import OtherClockDriver
from ipxact.models.other_clocks import OtherClocks
from ipxact.models.parameter import Parameter
from ipxact.models.parameter_type_resolve import ParameterTypeResolve
from ipxact.models.parameters import Parameters
from ipxact.models.port import Port
from ipxact.models.port_wire_type import PortWireType
from ipxact.models.right import Right
from ipxact.models.simple_file_type import SimpleFileType
from ipxact.models.timing_constraint import TimingConstraint
from ipxact.models.unsigned_bit_expression import UnsignedBitExpression
from ipxact.models.value import Value


obj = Component(
    vendor='spiritconsortium.org',
    library='Leon2RTL',
    name='uartHier',
    version='1.0',
    bus_interfaces=BusInterfaces(
        bus_interface=[
            BusInterface(
                name='APBClk',
                bus_type=ConfigurableLibraryRefType(
                    vendor='spiritconsortium.org',
                    library='busdef.clock',
                    name='clock',
                    version='1.0'
                ),
                abstraction_types=AbstractionTypes(
                    abstraction_type=[
                        AbstractionTypes.AbstractionType(
                            abstraction_ref=ConfigurableLibraryRefType(
                                vendor='spiritconsortium.org',
                                library='busdef.clock',
                                name='clock_rtl',
                                version='1.0'
                            ),
                            port_maps=AbstractionTypes.AbstractionType.PortMaps(
                                port_map=[
                                    AbstractionTypes.AbstractionType.PortMaps.PortMap(
                                        logical_port=AbstractionTypes.AbstractionType.PortMaps.PortMap.LogicalPort(
                                            name='CLK'
                                        ),
                                        physical_port=AbstractionTypes.AbstractionType.PortMaps.PortMap.PhysicalPort(
                                            name='clk'
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
            BusInterface(
                name='APBReset',
                bus_type=ConfigurableLibraryRefType(
                    vendor='spiritconsortium.org',
                    library='busdef.reset',
                    name='reset',
                    version='1.0'
                ),
                abstraction_types=AbstractionTypes(
                    abstraction_type=[
                        AbstractionTypes.AbstractionType(
                            abstraction_ref=ConfigurableLibraryRefType(
                                vendor='spiritconsortium.org',
                                library='busdef.reset',
                                name='reset_rtl',
                                version='1.0'
                            ),
                            port_maps=AbstractionTypes.AbstractionType.PortMaps(
                                port_map=[
                                    AbstractionTypes.AbstractionType.PortMaps.PortMap(
                                        logical_port=AbstractionTypes.AbstractionType.PortMaps.PortMap.LogicalPort(
                                            name='RESETn'
                                        ),
                                        physical_port=AbstractionTypes.AbstractionType.PortMaps.PortMap.PhysicalPort(
                                            name='rst'
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
            BusInterface(
                name='ambaAPB',
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
                                library='busdef.amba',
                                name='APB_rtl',
                                version='1.0'
                            ),
                            port_maps=AbstractionTypes.AbstractionType.PortMaps(
                                port_map=[
                                    AbstractionTypes.AbstractionType.PortMaps.PortMap(
                                        logical_port=AbstractionTypes.AbstractionType.PortMaps.PortMap.LogicalPort(
                                            name='Select'
                                        ),
                                        physical_port=AbstractionTypes.AbstractionType.PortMaps.PortMap.PhysicalPort(
                                            name='psel'
                                        )
                                    ),
                                    AbstractionTypes.AbstractionType.PortMaps.PortMap(
                                        logical_port=AbstractionTypes.AbstractionType.PortMaps.PortMap.LogicalPort(
                                            name='Enable'
                                        ),
                                        physical_port=AbstractionTypes.AbstractionType.PortMaps.PortMap.PhysicalPort(
                                            name='penable'
                                        )
                                    ),
                                    AbstractionTypes.AbstractionType.PortMaps.PortMap(
                                        logical_port=AbstractionTypes.AbstractionType.PortMaps.PortMap.LogicalPort(
                                            name='Address'
                                        ),
                                        physical_port=AbstractionTypes.AbstractionType.PortMaps.PortMap.PhysicalPort(
                                            name='paddr'
                                        )
                                    ),
                                    AbstractionTypes.AbstractionType.PortMaps.PortMap(
                                        logical_port=AbstractionTypes.AbstractionType.PortMaps.PortMap.LogicalPort(
                                            name='Write'
                                        ),
                                        physical_port=AbstractionTypes.AbstractionType.PortMaps.PortMap.PhysicalPort(
                                            name='pwrite'
                                        )
                                    ),
                                    AbstractionTypes.AbstractionType.PortMaps.PortMap(
                                        logical_port=AbstractionTypes.AbstractionType.PortMaps.PortMap.LogicalPort(
                                            name='WriteData'
                                        ),
                                        physical_port=AbstractionTypes.AbstractionType.PortMaps.PortMap.PhysicalPort(
                                            name='pwdata'
                                        )
                                    ),
                                    AbstractionTypes.AbstractionType.PortMaps.PortMap(
                                        logical_port=AbstractionTypes.AbstractionType.PortMaps.PortMap.LogicalPort(
                                            name='ReadData'
                                        ),
                                        physical_port=AbstractionTypes.AbstractionType.PortMaps.PortMap.PhysicalPort(
                                            name='prdata'
                                        )
                                    ),
                                    AbstractionTypes.AbstractionType.PortMaps.PortMap(
                                        logical_port=AbstractionTypes.AbstractionType.PortMaps.PortMap.LogicalPort(
                                            name='Clock'
                                        ),
                                        physical_port=AbstractionTypes.AbstractionType.PortMaps.PortMap.PhysicalPort(
                                            name='clk'
                                        )
                                    ),
                                    AbstractionTypes.AbstractionType.PortMaps.PortMap(
                                        logical_port=AbstractionTypes.AbstractionType.PortMaps.PortMap.LogicalPort(
                                            name='Resetn'
                                        ),
                                        physical_port=AbstractionTypes.AbstractionType.PortMaps.PortMap.PhysicalPort(
                                            name='rst'
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
                name='Interrupt',
                bus_type=ConfigurableLibraryRefType(
                    vendor='spiritconsortium.org',
                    library='busdef.interrupt',
                    name='interrupt',
                    version='1.0'
                ),
                abstraction_types=AbstractionTypes(
                    abstraction_type=[
                        AbstractionTypes.AbstractionType(
                            abstraction_ref=ConfigurableLibraryRefType(
                                vendor='spiritconsortium.org',
                                library='busdef.interrupt',
                                name='interrupt_rtl',
                                version='1.0'
                            ),
                            port_maps=AbstractionTypes.AbstractionType.PortMaps(
                                port_map=[
                                    AbstractionTypes.AbstractionType.PortMaps.PortMap(
                                        logical_port=AbstractionTypes.AbstractionType.PortMaps.PortMap.LogicalPort(
                                            name='IRQ'
                                        ),
                                        physical_port=AbstractionTypes.AbstractionType.PortMaps.PortMap.PhysicalPort(
                                            name='irq'
                                        )
                                    ),
                                ]
                            )
                        ),
                    ]
                ),
                initiator=BusInterfaceType.Initiator(

                )
            ),
            BusInterface(
                name='serial',
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
                                library='busdef.generic',
                                name='serial_rtl',
                                version='1.0'
                            ),
                            port_maps=AbstractionTypes.AbstractionType.PortMaps(
                                port_map=[
                                    AbstractionTypes.AbstractionType.PortMaps.PortMap(
                                        logical_port=AbstractionTypes.AbstractionType.PortMaps.PortMap.LogicalPort(
                                            name='RxD'
                                        ),
                                        physical_port=AbstractionTypes.AbstractionType.PortMaps.PortMap.PhysicalPort(
                                            name='rxd'
                                        )
                                    ),
                                    AbstractionTypes.AbstractionType.PortMaps.PortMap(
                                        logical_port=AbstractionTypes.AbstractionType.PortMaps.PortMap.LogicalPort(
                                            name='TxD'
                                        ),
                                        physical_port=AbstractionTypes.AbstractionType.PortMaps.PortMap.PhysicalPort(
                                            name='txd'
                                        )
                                    ),
                                    AbstractionTypes.AbstractionType.PortMaps.PortMap(
                                        logical_port=AbstractionTypes.AbstractionType.PortMaps.PortMap.LogicalPort(
                                            name='CTSn'
                                        ),
                                        physical_port=AbstractionTypes.AbstractionType.PortMaps.PortMap.PhysicalPort(
                                            name='ctsn'
                                        )
                                    ),
                                    AbstractionTypes.AbstractionType.PortMaps.PortMap(
                                        logical_port=AbstractionTypes.AbstractionType.PortMaps.PortMap.LogicalPort(
                                            name='RTSn'
                                        ),
                                        physical_port=AbstractionTypes.AbstractionType.PortMaps.PortMap.PhysicalPort(
                                            name='rtsn'
                                        )
                                    ),
                                    AbstractionTypes.AbstractionType.PortMaps.PortMap(
                                        logical_port=AbstractionTypes.AbstractionType.PortMaps.PortMap.LogicalPort(
                                            name='DTRn'
                                        ),
                                        physical_port=AbstractionTypes.AbstractionType.PortMaps.PortMap.PhysicalPort(
                                            name='rxen'
                                        )
                                    ),
                                ]
                            )
                        ),
                    ]
                ),
                initiator=BusInterfaceType.Initiator(

                )
            ),
        ]
    ),
    model=Model(
        views=ModelType.Views(
            view=[
                ModelType.Views.View(
                    name='RTLHierarchical',
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
                    ],
                    design_instantiation_ref='RTLHierarchical'
                ),
            ]
        ),
        instantiations=ModelType.Instantiations(
            design_instantiation=[
                DesignInstantiationType(
                    name='RTLHierarchical',
                    design_ref=ConfigurableLibraryRefType(
                        vendor='spiritconsortium.org',
                        library='Leon2RTL',
                        name='uartHierDesignConfig',
                        version='1.0'
                    )
                ),
            ]
        ),
        ports=ModelType.Ports(
            port=[
                Port(
                    name='clk',
                    wire=PortWireType(
                        direction=ComponentPortDirectionType.IN,
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
                                        clock_name='clk'
                                    )
                                ),
                            ]
                        )
                    )
                ),
                Port(
                    name='rst',
                    wire=PortWireType(
                        direction=ComponentPortDirectionType.IN,
                        constraint_sets=ConstraintSets(
                            constraint_set=[
                                ConstraintSet(
                                    timing_constraint=[
                                        TimingConstraint(
                                            value=50.0,
                                            clock_name='virtual_clk'
                                        ),
                                    ]
                                ),
                            ]
                        )
                    )
                ),
                Port(
                    name='psel',
                    wire=PortWireType(
                        direction=ComponentPortDirectionType.IN,
                        constraint_sets=ConstraintSets(
                            constraint_set=[
                                ConstraintSet(
                                    timing_constraint=[
                                        TimingConstraint(
                                            value=50.0,
                                            clock_name='virtual_clk'
                                        ),
                                    ]
                                ),
                            ]
                        )
                    )
                ),
                Port(
                    name='penable',
                    wire=PortWireType(
                        direction=ComponentPortDirectionType.IN,
                        constraint_sets=ConstraintSets(
                            constraint_set=[
                                ConstraintSet(
                                    timing_constraint=[
                                        TimingConstraint(
                                            value=50.0,
                                            clock_name='virtual_clk'
                                        ),
                                    ]
                                ),
                            ]
                        )
                    )
                ),
                Port(
                    name='paddr',
                    wire=PortWireType(
                        direction=ComponentPortDirectionType.IN,
                        vectors=ExtendedVectorsType(
                            vector=[
                                ExtendedVectorsType.Vector(
                                    left=Left(
                                        value='31'
                                    ),
                                    right=Right(
                                        value='0'
                                    )
                                ),
                            ]
                        ),
                        constraint_sets=ConstraintSets(
                            constraint_set=[
                                ConstraintSet(
                                    timing_constraint=[
                                        TimingConstraint(
                                            value=50.0,
                                            clock_name='virtual_clk'
                                        ),
                                    ]
                                ),
                            ]
                        )
                    )
                ),
                Port(
                    name='pwrite',
                    wire=PortWireType(
                        direction=ComponentPortDirectionType.IN,
                        constraint_sets=ConstraintSets(
                            constraint_set=[
                                ConstraintSet(
                                    timing_constraint=[
                                        TimingConstraint(
                                            value=50.0,
                                            clock_name='virtual_clk'
                                        ),
                                    ]
                                ),
                            ]
                        )
                    )
                ),
                Port(
                    name='pwdata',
                    wire=PortWireType(
                        direction=ComponentPortDirectionType.IN,
                        vectors=ExtendedVectorsType(
                            vector=[
                                ExtendedVectorsType.Vector(
                                    left=Left(
                                        value='31'
                                    ),
                                    right=Right(
                                        value='0'
                                    )
                                ),
                            ]
                        ),
                        constraint_sets=ConstraintSets(
                            constraint_set=[
                                ConstraintSet(
                                    timing_constraint=[
                                        TimingConstraint(
                                            value=50.0,
                                            clock_name='virtual_clk'
                                        ),
                                    ]
                                ),
                            ]
                        )
                    )
                ),
                Port(
                    name='prdata',
                    wire=PortWireType(
                        direction=ComponentPortDirectionType.OUT,
                        vectors=ExtendedVectorsType(
                            vector=[
                                ExtendedVectorsType.Vector(
                                    left=Left(
                                        value='31'
                                    ),
                                    right=Right(
                                        value='0'
                                    )
                                ),
                            ]
                        ),
                        constraint_sets=ConstraintSets(
                            constraint_set=[
                                ConstraintSet(
                                    timing_constraint=[
                                        TimingConstraint(
                                            value=90.0,
                                            clock_name='virtual_clk'
                                        ),
                                    ]
                                ),
                            ]
                        )
                    )
                ),
                Port(
                    name='irq',
                    wire=PortWireType(
                        direction=ComponentPortDirectionType.OUT,
                        constraint_sets=ConstraintSets(
                            constraint_set=[
                                ConstraintSet(
                                    timing_constraint=[
                                        TimingConstraint(
                                            value=80.0,
                                            clock_name='virtual_clk'
                                        ),
                                    ]
                                ),
                            ]
                        )
                    )
                ),
                Port(
                    name='scaler',
                    wire=PortWireType(
                        direction=ComponentPortDirectionType.IN,
                        vectors=ExtendedVectorsType(
                            vector=[
                                ExtendedVectorsType.Vector(
                                    left=Left(
                                        value='7'
                                    ),
                                    right=Right(
                                        value='0'
                                    )
                                ),
                            ]
                        ),
                        drivers=Drivers(
                            driver=[
                                Driver(
                                    default_value=DefaultValue(
                                        value='sigdefVal_scaler'
                                    )
                                ),
                            ]
                        ),
                        constraint_sets=ConstraintSets(
                            constraint_set=[
                                ConstraintSet(
                                    timing_constraint=[
                                        TimingConstraint(
                                            value=75.0,
                                            clock_name='virtual_clk'
                                        ),
                                    ]
                                ),
                            ]
                        )
                    )
                ),
                Port(
                    name='rxd',
                    wire=PortWireType(
                        direction=ComponentPortDirectionType.IN,
                        drivers=Drivers(
                            driver=[
                                Driver(
                                    default_value=DefaultValue(
                                        value='sigdefVal_rxd'
                                    )
                                ),
                            ]
                        ),
                        constraint_sets=ConstraintSets(
                            constraint_set=[
                                ConstraintSet(
                                    timing_constraint=[
                                        TimingConstraint(
                                            value=75.0,
                                            clock_name='virtual_clk'
                                        ),
                                    ]
                                ),
                            ]
                        )
                    )
                ),
                Port(
                    name='rxen',
                    wire=PortWireType(
                        direction=ComponentPortDirectionType.OUT,
                        constraint_sets=ConstraintSets(
                            constraint_set=[
                                ConstraintSet(
                                    timing_constraint=[
                                        TimingConstraint(
                                            value=60.0,
                                            clock_name='virtual_clk'
                                        ),
                                    ]
                                ),
                            ]
                        )
                    )
                ),
                Port(
                    name='txd',
                    wire=PortWireType(
                        direction=ComponentPortDirectionType.OUT,
                        constraint_sets=ConstraintSets(
                            constraint_set=[
                                ConstraintSet(
                                    timing_constraint=[
                                        TimingConstraint(
                                            value=60.0,
                                            clock_name='virtual_clk'
                                        ),
                                    ]
                                ),
                            ]
                        )
                    )
                ),
                Port(
                    name='txen',
                    wire=PortWireType(
                        direction=ComponentPortDirectionType.OUT,
                        constraint_sets=ConstraintSets(
                            constraint_set=[
                                ConstraintSet(
                                    timing_constraint=[
                                        TimingConstraint(
                                            value=60.0,
                                            clock_name='virtual_clk'
                                        ),
                                    ]
                                ),
                            ]
                        )
                    )
                ),
                Port(
                    name='flow',
                    wire=PortWireType(
                        direction=ComponentPortDirectionType.OUT,
                        constraint_sets=ConstraintSets(
                            constraint_set=[
                                ConstraintSet(
                                    timing_constraint=[
                                        TimingConstraint(
                                            value=60.0,
                                            clock_name='virtual_clk'
                                        ),
                                    ]
                                ),
                            ]
                        )
                    )
                ),
                Port(
                    name='rtsn',
                    wire=PortWireType(
                        direction=ComponentPortDirectionType.OUT,
                        constraint_sets=ConstraintSets(
                            constraint_set=[
                                ConstraintSet(
                                    timing_constraint=[
                                        TimingConstraint(
                                            value=60.0,
                                            clock_name='virtual_clk'
                                        ),
                                    ]
                                ),
                            ]
                        )
                    )
                ),
                Port(
                    name='ctsn',
                    wire=PortWireType(
                        direction=ComponentPortDirectionType.IN,
                        drivers=Drivers(
                            driver=[
                                Driver(
                                    default_value=DefaultValue(
                                        value='sigdefVal_ctsn'
                                    )
                                ),
                            ]
                        ),
                        constraint_sets=ConstraintSets(
                            constraint_set=[
                                ConstraintSet(
                                    timing_constraint=[
                                        TimingConstraint(
                                            value=75.0,
                                            clock_name='virtual_clk'
                                        ),
                                    ]
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
                            value='hdlsrc/uartHier.vhd'
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
    ),
    other_clock_drivers=OtherClocks(
        other_clock_driver=[
            OtherClockDriver(
                clock_period=ClockDriverType.ClockPeriod(
                    value='VirtualClockPeriod'
                ),
                clock_pulse_offset=ClockDriverType.ClockPulseOffset(
                    value='VirtualClockPulseOffset'
                ),
                clock_pulse_value=UnsignedBitExpression(
                    value='VirtualClockPulseValue'
                ),
                clock_pulse_duration=ClockDriverType.ClockPulseDuration(
                    value='VirtualClockPulseDuration'
                ),
                clock_name='virtual_clock'
            ),
        ]
    ),
    parameters=Parameters(
        parameter=[
            Parameter(
                name='sigdefVal_scaler',
                value=Value(
                    value="'h0"
                ),
                parameter_id='sigdefVal_scaler',
                type_value=FormatType.LONGINT
            ),
            Parameter(
                name='sigdefVal_rxd',
                value=Value(
                    value='0'
                ),
                parameter_id='sigdefVal_rxd',
                type_value=FormatType.LONGINT
            ),
            Parameter(
                name='sigdefVal_ctsn',
                value=Value(
                    value='0'
                ),
                parameter_id='sigdefVal_ctsn',
                type_value=FormatType.LONGINT
            ),
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
                    value='8'
                ),
                parameter_id='ClockPeriod',
                prompt='Clock Pulse Period:',
                type_value=FormatType.REAL,
                resolve=ParameterTypeResolve.USER
            ),
            Parameter(
                name='ClockPulseDuration',
                value=Value(
                    value='4'
                ),
                parameter_id='ClockPulseDuration',
                prompt='Clock Pulse Duration:',
                type_value=FormatType.REAL,
                resolve=ParameterTypeResolve.USER
            ),
            Parameter(
                name='ClockPulseOffset',
                value=Value(
                    value='4'
                ),
                parameter_id='ClockPulseOffset',
                prompt='Clock Pulse Offset:',
                type_value=FormatType.REAL,
                resolve=ParameterTypeResolve.USER
            ),
            Parameter(
                name='VirtualClockPeriod',
                value=Value(
                    value='8'
                ),
                parameter_id='VirtualClockPeriod',
                prompt='Virtual Clock Period:',
                type_value=FormatType.REAL,
                resolve=ParameterTypeResolve.USER
            ),
            Parameter(
                name='VirtualClockPulseDuration',
                value=Value(
                    value='4'
                ),
                parameter_id='VirtualClockPulseDuration',
                prompt='Virtual Clock Pulse Duration:',
                type_value=FormatType.REAL,
                resolve=ParameterTypeResolve.USER
            ),
            Parameter(
                name='VirtualClockPulseValue',
                value=Value(
                    value='1'
                ),
                parameter_id='VirtualClockPulseValue',
                prompt='Virtual Clock Pulse Value:',
                type_value=FormatType.LONGINT,
                resolve=ParameterTypeResolve.USER
            ),
            Parameter(
                name='VirtualClockPulseOffset',
                value=Value(
                    value='4'
                ),
                parameter_id='VirtualClockPulseOffset',
                prompt='Virtual Clock Pulse Offset:',
                type_value=FormatType.REAL,
                resolve=ParameterTypeResolve.USER
            ),
        ]
    )
)