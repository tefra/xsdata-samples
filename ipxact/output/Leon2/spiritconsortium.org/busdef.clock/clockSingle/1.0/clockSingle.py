from ipxact.models.bus_definition import BusDefinition
from ipxact.models.description import Description
from ipxact.models.library_ref_type import LibraryRefType
from ipxact.models.unsigned_int_expression import UnsignedIntExpression


obj = BusDefinition(
    vendor='spiritconsortium.org',
    library='busdef.clock',
    name='clockSingle',
    version='1.0',
    description=Description(
        value='Extension of the base clock bus definition for clock architectures that requires the number of clock masters to be limited 1'
    ),
    direct_connection=True,
    is_addressable=False,
    extends=LibraryRefType(
        vendor='spiritconsortium.org',
        library='busdef.clock',
        name='clock',
        version='1.0'
    ),
    max_initiators=UnsignedIntExpression(
        value='1'
    )
)
