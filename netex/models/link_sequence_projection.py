from __future__ import annotations

from dataclasses import dataclass

from .link_sequence_projection_version_structure import (
    LinkSequenceProjectionVersionStructure,
)

__NAMESPACE__ = "http://www.netex.org.uk/netex"


@dataclass(kw_only=True)
class LinkSequenceProjection(LinkSequenceProjectionVersionStructure):
    class Meta:
        namespace = "http://www.netex.org.uk/netex"
