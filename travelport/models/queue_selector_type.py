from __future__ import annotations

from dataclasses import dataclass, field

__NAMESPACE__ = "http://www.travelport.com/schema/gdsQueue_v52_0"


@dataclass
class QueueSelectorType:
    """
    Parameters
    ----------
    queue
        Queue Number . Possible values are 01, AA , A1 etc.
    category
        Queue Category Number. 2 Character Alpha or Numeric Number. Either
        Alpha or Numeric Number is allowed. If using for Sabre is mandatory
        and is Prefatory Instruction Code value of 0-999.
    date_range
        Date range number where the PNR should be queued. Possible values
        are 1,2,1-4 etc.
    surname
        Surname as in queue ,supports alpha characters only.
    """

    queue: None | str = field(
        default=None,
        metadata={
            "name": "Queue",
            "type": "Attribute",
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
    surname: None | str = field(
        default=None,
        metadata={
            "name": "Surname",
            "type": "Attribute",
        },
    )
