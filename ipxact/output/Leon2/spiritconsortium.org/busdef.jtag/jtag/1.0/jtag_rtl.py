from ipxact.models.abstraction_definition import AbstractionDefinition
from ipxact.models.direction import Direction
from ipxact.models.library_ref_type import LibraryRefType
from ipxact.models.qualifier_type import QualifierType
from ipxact.models.requires_driver import RequiresDriver
from ipxact.models.requires_driver_driver_type import RequiresDriverDriverType
from ipxact.models.wire import Wire


obj = AbstractionDefinition(
    vendor='spiritconsortium.org',
    library='busdef.jtag',
    name='jtag_rtl',
    version='1.0',
    bus_type=LibraryRefType(
        vendor='spiritconsortium.org',
        library='busdef.jtag',
        name='jtag',
        version='1.0'
    ),
    ports=AbstractionDefinition.Ports(
        port=[
            AbstractionDefinition.Ports.Port(
                logical_name='TCK',
                wire=Wire(
                    qualifier=QualifierType(
                        is_clock=True
                    ),
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
                logical_name='NTRST',
                wire=Wire(
                    qualifier=QualifierType(
                        is_reset=QualifierType.IsReset(
                            value=True
                        )
                    ),
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
                logical_name='TDI',
                wire=Wire(
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
            AbstractionDefinition.Ports.Port(
                logical_name='TDO',
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
                        direction=Direction.OUT
                    )
                )
            ),
            AbstractionDefinition.Ports.Port(
                logical_name='TMS',
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
        ]
    )
)
