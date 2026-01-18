from __future__ import annotations

from dataclasses import dataclass, field

from npo.models.abstract_facet_type import AbstractFacetType
from npo.models.facet_order_type_enum import FacetOrderTypeEnum

__NAMESPACE__ = "urn:vpro:api:2013"


@dataclass(kw_only=True)
class TextFacetType(AbstractFacetType):
    class Meta:
        name = "textFacetType"

    threshold: None | int = field(
        default=None,
        metadata={
            "type": "Element",
            "namespace": "urn:vpro:api:2013",
        },
    )
    max: None | int = field(
        default=None,
        metadata={
            "type": "Element",
            "namespace": "urn:vpro:api:2013",
        },
    )
    include: None | str = field(
        default=None,
        metadata={
            "type": "Element",
            "namespace": "urn:vpro:api:2013",
        },
    )
    script: None | str = field(
        default=None,
        metadata={
            "type": "Element",
            "namespace": "urn:vpro:api:2013",
        },
    )
    sort: None | FacetOrderTypeEnum = field(
        default=None,
        metadata={
            "type": "Attribute",
        },
    )
