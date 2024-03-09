from dataclasses import dataclass

from .other_error_structure import OtherErrorStructure

__NAMESPACE__ = "http://www.siri.org.uk/siri"


@dataclass
class OtherError(OtherErrorStructure):
    class Meta:
        namespace = "http://www.siri.org.uk/siri"
