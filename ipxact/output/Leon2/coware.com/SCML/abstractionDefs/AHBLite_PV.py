from ipxact.models.abstraction_definition import AbstractionDefinition
from ipxact.models.library_ref_type import LibraryRefType
from ipxact.models.on_initiator_initiative import OnInitiatorInitiative
from ipxact.models.on_target_initiative import OnTargetInitiative
from ipxact.models.protocol import Protocol
from ipxact.models.protocol_type_type import ProtocolTypeType
from ipxact.models.qualifier_type import QualifierType


obj = AbstractionDefinition(
    vendor='coware.com',
    library='SCML',
    name='AHBLite_PV',
    version='1.1',
    bus_type=LibraryRefType(
        vendor='amba.com',
        library='AMBA3',
        name='AHBLite',
        version='r1p0_6'
    ),
    ports=AbstractionDefinition.Ports(
        port=[
            AbstractionDefinition.Ports.Port(
                logical_name='PV',
                transactional=AbstractionDefinition.Ports.Port.Transactional(
                    qualifier=QualifierType(
                        is_address=True,
                        is_data=True
                    ),
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
