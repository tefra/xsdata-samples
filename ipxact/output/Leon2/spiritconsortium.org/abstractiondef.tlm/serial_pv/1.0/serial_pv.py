from ipxact.models.abstraction_definition import AbstractionDefinition
from ipxact.models.library_ref_type import LibraryRefType
from ipxact.models.on_initiator_initiative import OnInitiatorInitiative
from ipxact.models.on_target_initiative import OnTargetInitiative
from ipxact.models.presence import Presence
from ipxact.models.presence_type import PresenceType
from ipxact.models.protocol import Protocol
from ipxact.models.protocol_type_type import ProtocolTypeType


obj = AbstractionDefinition(
    vendor='spiritconsortium.org',
    library='abstractiondef.tlm',
    name='serial_pv',
    version='1.0',
    bus_type=LibraryRefType(
        vendor='spiritconsortium.org',
        library='busdef.generic',
        name='serial',
        version='1.0'
    ),
    ports=AbstractionDefinition.Ports(
        port=[
            AbstractionDefinition.Ports.Port(
                logical_name='RW_TRANSACTION',
                transactional=AbstractionDefinition.Ports.Port.Transactional(
                    on_initiator=AbstractionDefinition.Ports.Port.Transactional.OnInitiator(
                        presence=Presence(
                            value=PresenceType.REQUIRED
                        ),
                        initiative=OnInitiatorInitiative.REQUIRES,
                        protocol=Protocol(
                            protocol_type=Protocol.ProtocolType(
                                value=ProtocolTypeType.TLM
                            )
                        )
                    ),
                    on_target=AbstractionDefinition.Ports.Port.Transactional.OnTarget(
                        presence=Presence(
                            value=PresenceType.REQUIRED
                        ),
                        initiative=OnTargetInitiative.PROVIDES,
                        protocol=Protocol(
                            protocol_type=Protocol.ProtocolType(
                                value=ProtocolTypeType.TLM
                            )
                        )
                    )
                )
            ),
        ]
    )
)
