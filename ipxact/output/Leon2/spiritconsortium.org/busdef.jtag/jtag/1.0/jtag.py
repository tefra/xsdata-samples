from ipxact.models.bus_definition import BusDefinition
from ipxact.models.unsigned_int_expression import UnsignedIntExpression


obj = BusDefinition(
    vendor='spiritconsortium.org',
    library='busdef.jtag',
    name='jtag',
    version='1.0',
    direct_connection=False,
    is_addressable=False,
    max_initiators=UnsignedIntExpression(
        value='1'
    )
)
