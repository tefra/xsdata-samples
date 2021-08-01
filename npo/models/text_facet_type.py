from dataclasses import dataclass, field
from typing import Optional
from npo.models.abstract_facet_type import AbstractFacetType
from npo.models.facet_order_type_enum import FacetOrderTypeEnum

__NAMESPACE__ = "urn:vpro:api:2013"


@dataclass
class TextFacetType(AbstractFacetType):
    class Meta:
        name = "textFacetType"

    threshold: Optional[int] = field(
        default=None,
        metadata={
            "type": "Element",
            "namespace": "urn:vpro:api:2013",
        }
    )
    max: Optional[int] = field(
        default=None,
        metadata={
            "type": "Element",
            "namespace": "urn:vpro:api:2013",
        }
    )
    include: Optional[str] = field(
        default=None,
        metadata={
            "type": "Element",
            "namespace": "urn:vpro:api:2013",
        }
    )
    script: Optional[str] = field(
        default=None,
        metadata={
            "type": "Element",
            "namespace": "urn:vpro:api:2013",
        }
    )
    sort: Optional[FacetOrderTypeEnum] = field(
        default=None,
        metadata={
            "type": "Attribute",
        }
    )
