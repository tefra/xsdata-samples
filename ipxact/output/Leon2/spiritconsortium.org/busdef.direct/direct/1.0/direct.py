from ipxact.models.bus_definition import BusDefinition
from ipxact.models.description import Description
from ipxact.models.unsigned_int_expression import UnsignedIntExpression


obj = BusDefinition(
    vendor='spiritconsortium.org',
    library='busdef.direct',
    name='direct',
    version='1.0',
    description=Description(
        value='Simple definition for testing addressing rule with direct connections'
    ),
    direct_connection=True,
    is_addressable=True,
    max_initiators=UnsignedIntExpression(
        value='1'
    )
)
