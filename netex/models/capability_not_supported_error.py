from dataclasses import dataclass
from .capability_not_supported_error_structure import (
    CapabilityNotSupportedErrorStructure,
)

__NAMESPACE__ = "http://www.siri.org.uk/siri"


@dataclass
class CapabilityNotSupportedError(CapabilityNotSupportedErrorStructure):
    class Meta:
        namespace = "http://www.siri.org.uk/siri"
