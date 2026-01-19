from __future__ import annotations

from dataclasses import dataclass, field

from sdmx_ml.models.wild_card_value_type import WildCardValueType

__NAMESPACE__ = "http://www.sdmx.org/resources/sdmxml/schemas/v3_1/registry"


@dataclass(frozen=True, kw_only=True)
class IdentifiableQueryType:
    """
    IdentifiableQueryType describes the structure of a query for an
    identifiable object.

    :ivar id: The id attribute is used to query for an object based on
        its identifier. This is either an explicit value, or completely
        wildcarded with the "%" value.
    """

    id: str | WildCardValueType = field(
        default=WildCardValueType.PERCENT_SIGN,
        metadata={
            "type": "Attribute",
            "pattern": r"[A-Za-z0-9_@$\-]+",
        },
    )
