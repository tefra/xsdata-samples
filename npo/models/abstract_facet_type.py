from __future__ import annotations

from dataclasses import dataclass

__NAMESPACE__ = "urn:vpro:api:2013"


@dataclass
class AbstractFacetType:
    class Meta:
        name = "abstractFacetType"
