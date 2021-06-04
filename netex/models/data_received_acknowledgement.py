from dataclasses import dataclass
from netex.models.data_received_response_structure import DataReceivedResponseStructure

__NAMESPACE__ = "http://www.siri.org.uk/siri"


@dataclass
class DataReceivedAcknowledgement(DataReceivedResponseStructure):
    class Meta:
        namespace = "http://www.siri.org.uk/siri"
