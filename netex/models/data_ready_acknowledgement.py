from dataclasses import dataclass
from netex.models.data_ready_response_structure import DataReadyResponseStructure

__NAMESPACE__ = "http://www.siri.org.uk/siri"


@dataclass
class DataReadyAcknowledgement(DataReadyResponseStructure):
    class Meta:
        namespace = "http://www.siri.org.uk/siri"
