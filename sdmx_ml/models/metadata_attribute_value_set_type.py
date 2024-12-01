from dataclasses import dataclass, field
from typing import Any

from sdmx_ml.models.member_selection_type import MemberSelectionType

__NAMESPACE__ = "http://www.sdmx.org/resources/sdmxml/schemas/v3_0/structure"


@dataclass(frozen=True)
class MetadataAttributeValueSetType(MemberSelectionType):
    """MetadataAttributeValueSetType defines the structure for providing values for
    a metadata attribute.

    If no values are provided, the attribute is implied to
    include/excluded from the region in which it is defined, with no
    regard to the value of the metadata attribute.
    """

    valid_from: Any = field(
        init=False,
        default=None,
        metadata={
            "type": "Ignore",
        },
    )
    valid_to: Any = field(
        init=False,
        default=None,
        metadata={
            "type": "Ignore",
        },
    )
