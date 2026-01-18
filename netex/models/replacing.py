from __future__ import annotations

from dataclasses import dataclass

from .replacing_version_structure import ReplacingVersionStructure

__NAMESPACE__ = "http://www.netex.org.uk/netex"


@dataclass
class Replacing(ReplacingVersionStructure):
    class Meta:
        namespace = "http://www.netex.org.uk/netex"
