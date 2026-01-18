from __future__ import annotations

from dataclasses import dataclass

from npo.models.organization_type import OrganizationType

__NAMESPACE__ = "urn:vpro:media:2009"


@dataclass(kw_only=True)
class BroadcasterType(OrganizationType):
    class Meta:
        name = "broadcasterType"
