from dataclasses import dataclass

from .check_status_response_structure import CheckStatusResponseStructure

__NAMESPACE__ = "http://www.siri.org.uk/siri"


@dataclass
class CheckStatusResponse(CheckStatusResponseStructure):
    class Meta:
        namespace = "http://www.siri.org.uk/siri"
