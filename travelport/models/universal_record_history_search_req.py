from __future__ import annotations
from dataclasses import dataclass, field
from travelport.models.base_req_1 import BaseReq1
from travelport.models.universal_record_history_search_modifiers import (
    UniversalRecordHistorySearchModifiers,
)

__NAMESPACE__ = "http://www.travelport.com/schema/universal_v52_0"


@dataclass
class UniversalRecordHistorySearchReq(BaseReq1):
    """
    Search the history of a Universal Record.

    Parameters
    ----------
    universal_record_history_search_modifiers
    universal_record_locator_code
        Represents a valid Universal Record locator code
    """

    class Meta:
        namespace = "http://www.travelport.com/schema/universal_v52_0"

    universal_record_history_search_modifiers: None | UniversalRecordHistorySearchModifiers = field(
        default=None,
        metadata={
            "name": "UniversalRecordHistorySearchModifiers",
            "type": "Element",
        },
    )
    universal_record_locator_code: None | str = field(
        default=None,
        metadata={
            "name": "UniversalRecordLocatorCode",
            "type": "Attribute",
            "required": True,
            "min_length": 5,
            "max_length": 8,
        },
    )
