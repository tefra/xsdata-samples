from dataclasses import dataclass, field
from .communications_transport_method_enumeration import CommunicationsTransportMethodEnumeration
from .compression_method_enumeration import CompressionMethodEnumeration

__NAMESPACE__ = "http://www.siri.org.uk/siri"


@dataclass
class TransportDescriptionStructure:
    communications_transport_method: CommunicationsTransportMethodEnumeration = field(
        default=CommunicationsTransportMethodEnumeration.HTTP_POST,
        metadata={
            "name": "CommunicationsTransportMethod",
            "type": "Element",
            "namespace": "http://www.siri.org.uk/siri",
        }
    )
    compression_method: CompressionMethodEnumeration = field(
        default=CompressionMethodEnumeration.NONE,
        metadata={
            "name": "CompressionMethod",
            "type": "Element",
            "namespace": "http://www.siri.org.uk/siri",
        }
    )
