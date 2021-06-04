from dataclasses import dataclass
from netex.models.error_code_structure import ErrorCodeStructure

__NAMESPACE__ = "http://www.siri.org.uk/siri"


@dataclass
class ErrorCode(ErrorCodeStructure):
    class Meta:
        namespace = "http://www.siri.org.uk/siri"
