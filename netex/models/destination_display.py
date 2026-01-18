from __future__ import annotations

from dataclasses import dataclass

from .destination_display_version_structure import (
    DestinationDisplayVersionStructure,
)

__NAMESPACE__ = "http://www.netex.org.uk/netex"


@dataclass
class DestinationDisplay(DestinationDisplayVersionStructure):
    class Meta:
        namespace = "http://www.netex.org.uk/netex"
