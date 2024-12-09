from ipxact.models.abstraction_definition import AbstractionDefinition
from ipxact.models.description import Description
from ipxact.models.direction import Direction
from ipxact.models.library_ref_type import LibraryRefType
from ipxact.models.qualifier_type import QualifierType
from ipxact.models.wire import Wire


obj = AbstractionDefinition(
    vendor='spiritconsortium.org',
    library='busdef.clock',
    name='clockSingle_rtl',
    version='1.0',
    description=Description(
        value='Wire type abstraction definition for a single master(output) multiple slave(input) clock bus definition'
    ),
    bus_type=LibraryRefType(
        vendor='spiritconsortium.org',
        library='busdef.clock',
        name='clockSingle',
        version='1.0'
    ),
    extends=LibraryRefType(
        vendor='spiritconsortium.org',
        library='busdef.clock',
        name='clock_rtl',
        version='1.0'
    ),
    ports=AbstractionDefinition.Ports(
        port=[
            AbstractionDefinition.Ports.Port(
                logical_name='CLK',
                wire=Wire(
                    qualifier=QualifierType(
                        is_clock=True
                    ),
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
