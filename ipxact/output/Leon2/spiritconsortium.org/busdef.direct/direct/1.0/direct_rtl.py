from ipxact.models.abstraction_definition import AbstractionDefinition
from ipxact.models.description import Description
from ipxact.models.direction import Direction
from ipxact.models.library_ref_type import LibraryRefType
from ipxact.models.qualifier_type import QualifierType
from ipxact.models.wire import Wire


obj = AbstractionDefinition(
    vendor='spiritconsortium.org',
    library='busdef.direct',
    name='direct_rtl',
    version='1.0',
    description=Description(
        value='Simple definition for testing addressing rule with direct connections'
    ),
    bus_type=LibraryRefType(
        vendor='spiritconsortium.org',
        library='busdef.direct',
        name='direct',
        version='1.0'
    ),
    ports=AbstractionDefinition.Ports(
        port=[
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
