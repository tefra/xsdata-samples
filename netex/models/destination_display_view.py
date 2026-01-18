from __future__ import annotations

from dataclasses import dataclass

from .destination_display_derived_view_structure import (
    DestinationDisplayDerivedViewStructure,
)

__NAMESPACE__ = "http://www.netex.org.uk/netex"


@dataclass
class DestinationDisplayView(DestinationDisplayDerivedViewStructure):
    class Meta:
        namespace = "http://www.netex.org.uk/netex"
