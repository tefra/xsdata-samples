from __future__ import annotations

from dataclasses import dataclass

from .reselling_version_structure import ResellingVersionStructure

__NAMESPACE__ = "http://www.netex.org.uk/netex"


@dataclass
class ReplacingVersionStructure(ResellingVersionStructure):
    class Meta:
        name = "Replacing_VersionStructure"
