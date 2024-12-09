from ipxact.models.abstraction_definition import AbstractionDefinition
from ipxact.models.library_ref_type import LibraryRefType
from ipxact.models.on_initiator_initiative import OnInitiatorInitiative
from ipxact.models.on_target_initiative import OnTargetInitiative
from ipxact.models.presence import Presence
from ipxact.models.presence_type import PresenceType
from ipxact.models.protocol import Protocol
from ipxact.models.protocol_type_type import ProtocolTypeType
from ipxact.models.qualifier_type import QualifierType


obj = AbstractionDefinition(
    vendor='spiritconsortium.org',
    library='abstractiondef.tlm',
    name='apb_pv',
    version='1.4',
    bus_type=LibraryRefType(
        vendor='amba.com',
        library='AMBA2',
        name='APB',
        version='r2p0_4'
    ),
    ports=AbstractionDefinition.Ports(
        port=[
            AbstractionDefinition.Ports.Port(
                logical_name='PV_TRANS',
                transactional=AbstractionDefinition.Ports.Port.Transactional(
                    qualifier=QualifierType(
                        is_address=True,
                        is_data=True
                    ),
                    on_initiator=AbstractionDefinition.Ports.Port.Transactional.OnInitiator(
                        presence=Presence(
                            value=PresenceType.REQUIRED
                        ),
                        initiative=OnInitiatorInitiative.REQUIRES,
                        protocol=Protocol(
                            protocol_type=Protocol.ProtocolType(
                                value=ProtocolTypeType.CUSTOM,
                                custom='pv_initiator_port'
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
                                value=ProtocolTypeType.CUSTOM,
                                custom='pv_target_port'
                            )
                        )
                    )
                )
            ),
        ]
    )
)
