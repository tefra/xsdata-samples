from __future__ import annotations

from dataclasses import dataclass, field
from typing import Any

from sdmx_ml.models.member_selection_type import MemberSelectionType

__NAMESPACE__ = "http://www.sdmx.org/resources/sdmxml/schemas/v3_0/structure"


@dataclass(frozen=True, kw_only=True)
class DataKeyValueType(MemberSelectionType):
    """
    DataKeyValueType is a type for providing a dimension value for the
    purpose of defining a distinct data key.

    Only a single value can be provided for the dimension.

    :ivar time_range: TimeValue provides a value for a component which
        has a time representation. This is repeatable to allow for a
        range to be specified, although a single value can also be
        provided. An operator is available on this to indicate whether
        the specified value indicates an exact value or the
        beginning/end of a range (inclusive or exclusive).
    :ivar include:
    :ivar valid_from:
    :ivar valid_to:
    """

    time_range: Any = field(
        init=False,
        default=None,
        metadata={
            "type": "Ignore",
        },
    )
    include: bool = field(
        init=False,
        default=True,
        metadata={
            "type": "Attribute",
        },
    )
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
