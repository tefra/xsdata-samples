from ipxact.models.abstraction_definition import AbstractionDefinition
from ipxact.models.direction import Direction
from ipxact.models.library_ref_type import LibraryRefType
from ipxact.models.qualifier_type import QualifierType
from ipxact.models.wire import Wire


obj = AbstractionDefinition(
    vendor='spiritconsortium.org',
    library='busdef.amba',
    name='APB_rtl',
    version='1.0',
    bus_type=LibraryRefType(
        vendor='amba.com',
        library='AMBA2',
        name='APB',
        version='r2p0_4'
    ),
    ports=AbstractionDefinition.Ports(
        port=[
            AbstractionDefinition.Ports.Port(
                logical_name='Clock',
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
                        direction=Direction.IN
                    ),
                    on_target=Wire.OnTarget(
                        direction=Direction.IN
                    )
                )
            ),
            AbstractionDefinition.Ports.Port(
                logical_name='Resetn',
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
                        direction=Direction.IN
                    ),
                    on_target=Wire.OnTarget(
                        direction=Direction.IN
                    )
                )
            ),
            AbstractionDefinition.Ports.Port(
                logical_name='Address',
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
                logical_name='Select',
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
                logical_name='Enable',
                wire=Wire(
                    on_initiator=Wire.OnInitiator(
                        direction=Direction.OUT
                    ),
                    on_target=Wire.OnTarget(
                        direction=Direction.IN
                    )
                )
            ),
            AbstractionDefinition.Ports.Port(
                logical_name='Write',
                wire=Wire(
                    on_initiator=Wire.OnInitiator(
                        direction=Direction.OUT
                    ),
                    on_target=Wire.OnTarget(
                        direction=Direction.IN
                    )
                )
            ),
            AbstractionDefinition.Ports.Port(
                logical_name='ReadData',
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
                logical_name='WriteData',
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
            AbstractionDefinition.Ports.Port(
                logical_name='ClockEnable',
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
                    )
                )
            ),
        ]
    )
)
