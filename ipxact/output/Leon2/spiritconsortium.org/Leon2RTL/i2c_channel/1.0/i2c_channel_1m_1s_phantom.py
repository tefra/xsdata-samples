from ipxact.models.abstraction_types import AbstractionTypes
from ipxact.models.bus_interface import BusInterface
from ipxact.models.bus_interface_type import BusInterfaceType
from ipxact.models.bus_interfaces import BusInterfaces
from ipxact.models.channels import Channels
from ipxact.models.component import Component
from ipxact.models.component_port_direction_type import ComponentPortDirectionType
from ipxact.models.configurable_library_ref_type import ConfigurableLibraryRefType
from ipxact.models.description import Description
from ipxact.models.model import Model
from ipxact.models.model_type import ModelType
from ipxact.models.port import Port
from ipxact.models.port_wire_type import PortWireType


obj = Component(
    vendor='spiritconsortium.org',
    library='Leon2RTL',
    name='i2c_channel_1m_1s_phantom',
    version='1.0',
    description=Description(
        value='1 master, 1 slave i2c channel, with phantom ports'
    ),
    bus_interfaces=BusInterfaces(
        bus_interface=[
            BusInterface(
                name='i2c_master1',
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
                mirrored_initiator=''
            ),
            BusInterface(
                name='i2c_slave1',
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
                mirrored_target=BusInterfaceType.MirroredTarget(

                )
            ),
        ]
    ),
    channels=Channels(
        channel=[
            Channels.Channel(
                name='i2c',
                bus_interface_ref=[
                    Channels.Channel.BusInterfaceRef(
                        local_name='i2c_master1'
                    ),
                    Channels.Channel.BusInterfaceRef(
                        local_name='i2c_slave1'
                    ),
                ]
            ),
        ]
    ),
    model=Model(
        ports=ModelType.Ports(
            port=[
                Port(
                    name='scl',
                    wire=PortWireType(
                        direction=ComponentPortDirectionType.PHANTOM
                    )
                ),
                Port(
                    name='sda',
                    wire=PortWireType(
                        direction=ComponentPortDirectionType.PHANTOM
                    )
                ),
            ]
        )
    )
)
