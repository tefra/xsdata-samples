from __future__ import annotations

from dataclasses import dataclass

from .infrastructure_link_restriction_ref_structure import (
    InfrastructureLinkRestrictionRefStructure,
)

__NAMESPACE__ = "http://www.netex.org.uk/netex"


@dataclass(kw_only=True)
class MeetingRestrictionRefStructure(
    InfrastructureLinkRestrictionRefStructure
):
    pass
