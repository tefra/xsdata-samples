from dataclasses import dataclass
from .authenticated_request_structure import AuthenticatedRequestStructure

__NAMESPACE__ = "http://www.siri.org.uk/siri"


@dataclass
class AuthenticatedRequest(AuthenticatedRequestStructure):
    class Meta:
        namespace = "http://www.siri.org.uk/siri"
