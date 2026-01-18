from __future__ import annotations

from dataclasses import dataclass, field

from npo.models.association_search_type import AssociationSearchType

__NAMESPACE__ = "urn:vpro:api:2013"


@dataclass(kw_only=True)
class PageAssociationSearchListType:
    class Meta:
        name = "pageAssociationSearchListType"

    search: list[AssociationSearchType] = field(
        default_factory=list,
        metadata={
            "type": "Element",
            "namespace": "urn:vpro:api:2013",
        },
    )
