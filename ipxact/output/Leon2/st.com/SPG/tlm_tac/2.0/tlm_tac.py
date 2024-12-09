from ipxact.models.abstraction_definition import AbstractionDefinition
from ipxact.models.library_ref_type import LibraryRefType
from ipxact.models.on_initiator_initiative import OnInitiatorInitiative
from ipxact.models.on_target_initiative import OnTargetInitiative
from ipxact.models.protocol import Protocol
from ipxact.models.protocol_type_type import ProtocolTypeType


obj = AbstractionDefinition(
    vendor='st.com',
    library='SPG',
    name='tlm_tac',
    version='2.0',
    bus_type=LibraryRefType(
        vendor='amba.com',
        library='AMBA2',
        name='APB',
        version='r2p0_4'
    ),
    ports=AbstractionDefinition.Ports(
        port=[
            AbstractionDefinition.Ports.Port(
                logical_name='tac_if',
                transactional=AbstractionDefinition.Ports.Port.Transactional(
                    on_initiator=AbstractionDefinition.Ports.Port.Transactional.OnInitiator(
                        initiative=OnInitiatorInitiative.REQUIRES,
                        protocol=Protocol(
                            protocol_type=Protocol.ProtocolType(
                                value=ProtocolTypeType.TLM
                            )
                        )
                    ),
                    on_target=AbstractionDefinition.Ports.Port.Transactional.OnTarget(
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
