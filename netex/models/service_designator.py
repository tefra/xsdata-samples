from dataclasses import dataclass

from .service_designator_structure import ServiceDesignatorStructure

__NAMESPACE__ = "http://www.netex.org.uk/netex"


@dataclass
class ServiceDesignator(ServiceDesignatorStructure):
    class Meta:
        namespace = "http://www.netex.org.uk/netex"
