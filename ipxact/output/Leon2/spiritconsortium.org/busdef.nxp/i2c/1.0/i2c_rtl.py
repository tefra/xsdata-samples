from ipxact.models.abstraction_definition import AbstractionDefinition
from ipxact.models.library_ref_type import LibraryRefType
from ipxact.models.wire import Wire


obj = AbstractionDefinition(
    vendor='spiritconsortium.org',
    library='busdef.nxp',
    name='i2c_rtl',
    version='1.0',
    bus_type=LibraryRefType(
        vendor='spiritconsortium.org',
        library='busdef.nxp',
        name='i2c',
        version='1.0'
    ),
    ports=AbstractionDefinition.Ports(
        port=[
            AbstractionDefinition.Ports.Port(
                logical_name='SDA',
                wire=Wire(

                )
            ),
            AbstractionDefinition.Ports.Port(
                logical_name='SCL',
                wire=Wire(

                )
            ),
        ]
    )
)
