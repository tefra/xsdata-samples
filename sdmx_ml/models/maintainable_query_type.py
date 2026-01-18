from dataclasses import dataclass, field

from sdmx_ml.models.versionable_query_type import VersionableQueryType
from sdmx_ml.models.wild_card_value_type import WildCardValueType

__NAMESPACE__ = "http://www.sdmx.org/resources/sdmxml/schemas/v3_0/registry"


@dataclass(frozen=True)
class MaintainableQueryType(VersionableQueryType):
    """
    MaintainableQueryType describes the structure of a query for a
    maintainable object.

    :ivar agency_id: The agencyID attribute is used to query for an
        object based on its maintenance agency's identifier. This is
        either an explicit value, or completely wild cared with the "%"
        value.
    """

    agency_id: str | WildCardValueType = field(
        default=WildCardValueType.PERCENT_SIGN,
        metadata={
            "name": "agencyID",
            "type": "Attribute",
            "pattern": r"[A-Za-z0-9_@$\-]+(\.[A-Za-z0-9_@$\-]+)*",
        },
    )
