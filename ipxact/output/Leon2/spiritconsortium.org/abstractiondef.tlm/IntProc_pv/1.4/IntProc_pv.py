from ipxact.models.abstraction_definition import AbstractionDefinition
from ipxact.models.direction import Direction
from ipxact.models.library_ref_type import LibraryRefType
from ipxact.models.unsigned_bit_vector_expression import UnsignedBitVectorExpression
from ipxact.models.wire import Wire


obj = AbstractionDefinition(
    vendor='spiritconsortium.org',
    library='abstractiondef.tlm',
    name='IntProc_pv',
    version='1.4',
    bus_type=LibraryRefType(
        vendor='spiritconsortium.org',
        library='busdef.leon2',
        name='IntProc',
        version='v1.0'
    ),
    ports=AbstractionDefinition.Ports(
        port=[
            AbstractionDefinition.Ports.Port(
                logical_name='IRL',
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
                    ),
                    default_value=UnsignedBitVectorExpression(
                        value='0'
                    )
                )
            ),
            AbstractionDefinition.Ports.Port(
                logical_name='IRQVEC',
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
                        direction=Direction.OUT
                    )
                )
            ),
            AbstractionDefinition.Ports.Port(
                logical_name='INTack',
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
                        direction=Direction.OUT
                    )
                )
            ),
        ]
    )
)
