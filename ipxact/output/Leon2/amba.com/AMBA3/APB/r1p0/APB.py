from ipxact.models.bus_definition import BusDefinition
from ipxact.models.library_ref_type import LibraryRefType
from ipxact.models.unsigned_int_expression import UnsignedIntExpression


obj = BusDefinition(
    vendor='amba.com',
    library='AMBA3',
    name='APB',
    version='r1p0_4',
    direct_connection=False,
    is_addressable=True,
    extends=LibraryRefType(
        vendor='amba.com',
        library='AMBA2',
        name='APB',
        version='r2p0_4'
    ),
    max_initiators=UnsignedIntExpression(
        value='1'
    ),
    system_group_names=BusDefinition.SystemGroupNames(
        system_group_name=[
            BusDefinition.SystemGroupNames.SystemGroupName(
                value='apb_clk'
            ),
            BusDefinition.SystemGroupNames.SystemGroupName(
                value='apb_reset'
            ),
        ]
    )
)