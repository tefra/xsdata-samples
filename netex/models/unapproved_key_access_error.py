from dataclasses import dataclass
from netex.models.unapproved_key_access_structure import UnapprovedKeyAccessStructure

__NAMESPACE__ = "http://www.siri.org.uk/siri"


@dataclass
class UnapprovedKeyAccessError(UnapprovedKeyAccessStructure):
    class Meta:
        namespace = "http://www.siri.org.uk/siri"
