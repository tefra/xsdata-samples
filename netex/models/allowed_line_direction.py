from __future__ import annotations

from dataclasses import dataclass

from .allowed_line_direction_version_structure import (
    AllowedLineDirectionVersionStructure,
)

__NAMESPACE__ = "http://www.netex.org.uk/netex"


@dataclass(kw_only=True)
class AllowedLineDirection(AllowedLineDirectionVersionStructure):
    class Meta:
        namespace = "http://www.netex.org.uk/netex"
