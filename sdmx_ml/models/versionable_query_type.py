from dataclasses import dataclass, field
from typing import Union

from sdmx_ml.models.identifiable_query_type import IdentifiableQueryType
from sdmx_ml.models.wild_card_value_type import WildCardValueType
from sdmx_ml.models.wildcard_type import WildcardType

__NAMESPACE__ = "http://www.sdmx.org/resources/sdmxml/schemas/v3_0/registry"


@dataclass(frozen=True)
class VersionableQueryType(IdentifiableQueryType):
    """
    VersionableQueryType describes the structure of a query for a
    versionable object.

    :ivar version: The version attribute is used to query for an object
        based on its version. This can be and explicit value, wild-
        carded ("%"), or late-bound ("*"). A wild carded version will
        match any version of the object where as a late-bound version
        will only match the latest version.
    """

    version: Union[str, WildcardType, WildCardValueType] = field(
        default=WildcardType.ASTERISK,
        metadata={
            "type": "Attribute",
            "pattern": r"(0|[1-9]\d*)(\.(0|[1-9]\d*))?",
        },
    )
