from __future__ import annotations

from dataclasses import dataclass

from .destination_display_variant_ref_structure import (
    DestinationDisplayVariantRefStructure,
)

__NAMESPACE__ = "http://www.netex.org.uk/netex"


@dataclass(kw_only=True)
class DestinationDisplayVariantRef(DestinationDisplayVariantRefStructure):
    class Meta:
        namespace = "http://www.netex.org.uk/netex"
