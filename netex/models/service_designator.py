from __future__ import annotations

from dataclasses import dataclass

from .service_designator_structure import ServiceDesignatorStructure

__NAMESPACE__ = "http://www.netex.org.uk/netex"


@dataclass(kw_only=True)
class ServiceDesignator(ServiceDesignatorStructure):
    class Meta:
        namespace = "http://www.netex.org.uk/netex"
