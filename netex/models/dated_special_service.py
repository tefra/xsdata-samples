from dataclasses import dataclass
from netex.models.dated_special_service_version_structure import DatedSpecialServiceVersionStructure

__NAMESPACE__ = "http://www.netex.org.uk/netex"


@dataclass
class DatedSpecialService(DatedSpecialServiceVersionStructure):
    class Meta:
        namespace = "http://www.netex.org.uk/netex"
