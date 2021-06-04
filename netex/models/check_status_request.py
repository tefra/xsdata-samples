from dataclasses import dataclass
from netex.models.check_status_request_structure import CheckStatusRequestStructure

__NAMESPACE__ = "http://www.siri.org.uk/siri"


@dataclass
class CheckStatusRequest(CheckStatusRequestStructure):
    class Meta:
        namespace = "http://www.siri.org.uk/siri"
