from __future__ import annotations
from dataclasses import dataclass, field

__NAMESPACE__ = "http://www.travelport.com/schema/gdsQueue_v52_0"


@dataclass
class QueueAgentRecord:
    """
    The information related to a particular category.

    Parameters
    ----------
    universal_record_locator_code
    pseudo_city_code
    queue_session_token
        Queue Session Token to hold session token for multiple queue
    queue_number
    lastupdated
    target_branch
    category
        Queue Category Number. 2 Character Alpha or Numeric Number. Either
        Alpha or Numeric Number is allowed.
    date_range
        Date range number where the PNR should be queued. Possible values
        are 1,2,1-4 etc.
    """

    class Meta:
        namespace = "http://www.travelport.com/schema/gdsQueue_v52_0"

    universal_record_locator_code: None | str = field(
        default=None,
        metadata={
            "name": "UniversalRecordLocatorCode",
            "type": "Element",
            "required": True,
            "min_length": 5,
            "max_length": 8,
        },
    )
    pseudo_city_code: None | str = field(
        default=None,
        metadata={
            "name": "PseudoCityCode",
            "type": "Attribute",
            "required": True,
            "min_length": 2,
            "max_length": 10,
        },
    )
    queue_session_token: None | str = field(
        default=None,
        metadata={
            "name": "QueueSessionToken",
            "type": "Attribute",
            "required": True,
        },
    )
    queue_number: None | str = field(
        default=None,
        metadata={
            "name": "QueueNumber",
            "type": "Attribute",
            "required": True,
        },
    )
    lastupdated: None | str = field(
        default=None,
        metadata={
            "name": "Lastupdated",
            "type": "Attribute",
            "required": True,
            "pattern": r"[^:Z].*",
        },
    )
    target_branch: None | str = field(
        default=None,
        metadata={
            "name": "TargetBranch",
            "type": "Attribute",
            "required": True,
            "min_length": 1,
            "max_length": 25,
        },
    )
    category: None | str = field(
        default=None,
        metadata={
            "name": "Category",
            "type": "Attribute",
        },
    )
    date_range: None | str = field(
        default=None,
        metadata={
            "name": "DateRange",
            "type": "Attribute",
        },
    )
