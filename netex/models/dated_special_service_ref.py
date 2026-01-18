from __future__ import annotations

from dataclasses import dataclass

from .dated_special_service_ref_structure import (
    DatedSpecialServiceRefStructure,
)

__NAMESPACE__ = "http://www.netex.org.uk/netex"


@dataclass
class DatedSpecialServiceRef(DatedSpecialServiceRefStructure):
    class Meta:
        namespace = "http://www.netex.org.uk/netex"
