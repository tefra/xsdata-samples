from ipxact.models.bus_definition import BusDefinition
from ipxact.models.unsigned_int_expression import UnsignedIntExpression


obj = BusDefinition(
    vendor='amba.com',
    library='AMBA3',
    name='AXI',
    version='r1p0_5',
    direct_connection=True,
    is_addressable=True,
    max_initiators=UnsignedIntExpression(
        value='1'
    ),
    max_targets=UnsignedIntExpression(
        value='1'
    ),
    system_group_names=BusDefinition.SystemGroupNames(
        system_group_name=[
            BusDefinition.SystemGroupNames.SystemGroupName(
                value='axi_clk'
            ),
            BusDefinition.SystemGroupNames.SystemGroupName(
                value='axi_reset'
            ),
            BusDefinition.SystemGroupNames.SystemGroupName(
                value='axi_lowpwr'
            ),
        ]
    )
)
