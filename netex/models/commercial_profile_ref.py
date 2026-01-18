from __future__ import annotations

from dataclasses import dataclass

from .commercial_profile_ref_structure import CommercialProfileRefStructure

__NAMESPACE__ = "http://www.netex.org.uk/netex"


@dataclass
class CommercialProfileRef(CommercialProfileRefStructure):
    class Meta:
        namespace = "http://www.netex.org.uk/netex"
