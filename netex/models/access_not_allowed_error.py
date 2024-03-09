from dataclasses import dataclass

from .access_not_allowed_error_structure import AccessNotAllowedErrorStructure

__NAMESPACE__ = "http://www.siri.org.uk/siri"


@dataclass
class AccessNotAllowedError(AccessNotAllowedErrorStructure):
    class Meta:
        namespace = "http://www.siri.org.uk/siri"
