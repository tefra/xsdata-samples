from ipxact.models.abstraction_definition import AbstractionDefinition
from ipxact.models.direction import Direction
from ipxact.models.library_ref_type import LibraryRefType
from ipxact.models.qualifier_type import QualifierType
from ipxact.models.requires_driver import RequiresDriver
from ipxact.models.requires_driver_driver_type import RequiresDriverDriverType
from ipxact.models.unsigned_bit_vector_expression import UnsignedBitVectorExpression
from ipxact.models.wire import Wire


obj = AbstractionDefinition(
    vendor='amba.com',
    library='AMBA2',
    name='APB_rtl',
    version='r2p0_4',
    bus_type=LibraryRefType(
        vendor='amba.com',
        library='AMBA2',
        name='APB',
        version='r2p0_4'
    ),
    ports=AbstractionDefinition.Ports(
        port=[
            AbstractionDefinition.Ports.Port(
                logical_name='PCLK',
                wire=Wire(
                    qualifier=QualifierType(
                        is_clock=True
                    ),
                    on_system=[
                        Wire.OnSystem(
                            group='apb_clk',
                            width=Wire.OnSystem.Width(
                                value='1'
                            ),
                            direction=Direction.OUT
                        ),
                    ],
                    on_initiator=Wire.OnInitiator(
                        width=Wire.OnInitiator.Width(
                            value='1'
                        ),
                        direction=Direction.IN
                    ),
                    on_target=Wire.OnTarget(
                        width=Wire.OnTarget.Width(
                            value='1'
                        ),
                        direction=Direction.IN
                    ),
                    requires_driver=RequiresDriver(
                        value=True,
                        driver_type=RequiresDriverDriverType.CLOCK
                    )
                )
            ),
            AbstractionDefinition.Ports.Port(
                logical_name='PRESETn',
                wire=Wire(
                    qualifier=QualifierType(
                        is_reset=QualifierType.IsReset(
                            value=True
                        )
                    ),
                    on_system=[
                        Wire.OnSystem(
                            group='apb_reset',
                            width=Wire.OnSystem.Width(
                                value='1'
                            ),
                            direction=Direction.OUT
                        ),
                    ],
                    on_initiator=Wire.OnInitiator(
                        width=Wire.OnInitiator.Width(
                            value='1'
                        ),
                        direction=Direction.IN
                    ),
                    on_target=Wire.OnTarget(
                        width=Wire.OnTarget.Width(
                            value='1'
                        ),
                        direction=Direction.IN
                    ),
                    requires_driver=RequiresDriver(
                        value=True,
                        driver_type=RequiresDriverDriverType.SINGLE_SHOT
                    )
                )
            ),
            AbstractionDefinition.Ports.Port(
                logical_name='PCLKEN',
                wire=Wire(
                    on_system=[
                        Wire.OnSystem(
                            group='apb_clk',
                            width=Wire.OnSystem.Width(
                                value='1'
                            ),
                            direction=Direction.OUT
                        ),
                    ],
                    on_initiator=Wire.OnInitiator(
                        width=Wire.OnInitiator.Width(
                            value='1'
                        ),
                        direction=Direction.IN
                    ),
                    on_target=Wire.OnTarget(
                        width=Wire.OnTarget.Width(
                            value='1'
                        ),
                        direction=Direction.IN
                    ),
                    default_value=UnsignedBitVectorExpression(
                        value='1'
                    )
                )
            ),
            AbstractionDefinition.Ports.Port(
                logical_name='PADDR',
                wire=Wire(
                    qualifier=QualifierType(
                        is_address=True
                    ),
                    on_initiator=Wire.OnInitiator(
                        direction=Direction.OUT
                    ),
                    on_target=Wire.OnTarget(
                        direction=Direction.IN
                    )
                )
            ),
            AbstractionDefinition.Ports.Port(
                logical_name='PSELx',
                wire=Wire(
                    on_initiator=Wire.OnInitiator(
                        direction=Direction.OUT
                    ),
                    on_target=Wire.OnTarget(
                        width=Wire.OnTarget.Width(
                            value='1'
                        ),
                        direction=Direction.IN
                    )
                )
            ),
            AbstractionDefinition.Ports.Port(
                logical_name='PENABLE',
                wire=Wire(
                    on_initiator=Wire.OnInitiator(
                        width=Wire.OnInitiator.Width(
                            value='1'
                        ),
                        direction=Direction.OUT
                    ),
                    on_target=Wire.OnTarget(
                        width=Wire.OnTarget.Width(
                            value='1'
                        ),
                        direction=Direction.IN
                    )
                )
            ),
            AbstractionDefinition.Ports.Port(
                logical_name='PWRITE',
                wire=Wire(
                    on_initiator=Wire.OnInitiator(
                        width=Wire.OnInitiator.Width(
                            value='1'
                        ),
                        direction=Direction.OUT
                    ),
                    on_target=Wire.OnTarget(
                        width=Wire.OnTarget.Width(
                            value='1'
                        ),
                        direction=Direction.IN
                    )
                )
            ),
            AbstractionDefinition.Ports.Port(
                logical_name='PRDATA',
                wire=Wire(
                    qualifier=QualifierType(
                        is_data=True
                    ),
                    on_initiator=Wire.OnInitiator(
                        direction=Direction.IN
                    ),
                    on_target=Wire.OnTarget(
                        direction=Direction.OUT
                    )
                )
            ),
            AbstractionDefinition.Ports.Port(
                logical_name='PWDATA',
                wire=Wire(
                    qualifier=QualifierType(
                        is_data=True
                    ),
                    on_initiator=Wire.OnInitiator(
                        direction=Direction.OUT
                    ),
                    on_target=Wire.OnTarget(
                        direction=Direction.IN
                    )
                )
            ),
        ]
    )
)
