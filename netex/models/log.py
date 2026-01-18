from __future__ import annotations

from dataclasses import dataclass

from .log_version_structure import LogVersionStructure

__NAMESPACE__ = "http://www.netex.org.uk/netex"


@dataclass(kw_only=True)
class Log(LogVersionStructure):
    class Meta:
        namespace = "http://www.netex.org.uk/netex"
