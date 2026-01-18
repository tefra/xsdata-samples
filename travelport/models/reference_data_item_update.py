from __future__ import annotations

from dataclasses import dataclass

__NAMESPACE__ = "http://www.travelport.com/schema/util_v52_0"


@dataclass(kw_only=True)
class ReferenceDataItemUpdate:
    """
    To add or update reference data items for a particular type.
    """

    class Meta:
        namespace = "http://www.travelport.com/schema/util_v52_0"
