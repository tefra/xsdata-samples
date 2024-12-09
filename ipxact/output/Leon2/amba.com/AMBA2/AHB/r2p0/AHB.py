from ipxact.models.bus_definition import BusDefinition
from ipxact.models.library_ref_type import LibraryRefType


obj = BusDefinition(
    vendor='amba.com',
    library='AMBA2',
    name='AHB',
    version='r2p0_6',
    direct_connection=False,
    is_addressable=True,
    extends=LibraryRefType(
        vendor='amba.com',
        library='AMBA3',
        name='AHBLite',
        version='r1p0_6'
    ),
    system_group_names=BusDefinition.SystemGroupNames(
        system_group_name=[
            BusDefinition.SystemGroupNames.SystemGroupName(
                value='ahb_clk'
            ),
            BusDefinition.SystemGroupNames.SystemGroupName(
                value='ahb_reset'
            ),
        ]
    )
)
