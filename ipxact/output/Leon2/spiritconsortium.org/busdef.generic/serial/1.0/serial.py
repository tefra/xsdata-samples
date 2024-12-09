from ipxact.models.bus_definition import BusDefinition
from ipxact.models.unsigned_int_expression import UnsignedIntExpression


obj = BusDefinition(
    vendor='spiritconsortium.org',
    library='busdef.generic',
    name='serial',
    version='1.0',
    direct_connection=False,
    is_addressable=False,
    max_initiators=UnsignedIntExpression(
        value='2'
    ),
    max_targets=UnsignedIntExpression(
        value='0'
    )
)
