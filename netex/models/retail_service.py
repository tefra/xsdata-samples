from dataclasses import dataclass

from .retail_service_version_structure import RetailServiceVersionStructure

__NAMESPACE__ = "http://www.netex.org.uk/netex"


@dataclass
class RetailService(RetailServiceVersionStructure):
    class Meta:
        namespace = "http://www.netex.org.uk/netex"
