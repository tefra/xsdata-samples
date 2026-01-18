from __future__ import annotations

from dataclasses import dataclass

from .dated_special_service_version_structure import (
    DatedSpecialServiceVersionStructure,
)

__NAMESPACE__ = "http://www.netex.org.uk/netex"


@dataclass(kw_only=True)
class DatedSpecialService(DatedSpecialServiceVersionStructure):
    class Meta:
        namespace = "http://www.netex.org.uk/netex"
