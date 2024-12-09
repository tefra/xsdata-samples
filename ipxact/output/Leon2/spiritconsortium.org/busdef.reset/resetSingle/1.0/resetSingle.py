from ipxact.models.bus_definition import BusDefinition
from ipxact.models.description import Description
from ipxact.models.library_ref_type import LibraryRefType
from ipxact.models.unsigned_int_expression import UnsignedIntExpression


obj = BusDefinition(
    vendor='spiritconsortium.org',
    library='busdef.reset',
    name='resetSingle',
    version='1.0',
    description=Description(
        value='Extension of the base reset bus definition for reset architectures that requires the number of reset masters to be limited 1'
    ),
    direct_connection=True,
    is_addressable=False,
    extends=LibraryRefType(
        vendor='spiritconsortium.org',
        library='busdef.reset',
        name='reset',
        version='1.0'
    ),
    max_initiators=UnsignedIntExpression(
        value='1'
    )
)
