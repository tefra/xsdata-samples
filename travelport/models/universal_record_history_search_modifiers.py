from __future__ import annotations
from dataclasses import dataclass, field
from xsdata.models.datatype import XmlDate

__NAMESPACE__ = "http://www.travelport.com/schema/universal_v52_0"


@dataclass
class UniversalRecordHistorySearchModifiers:
    """
    Controls and switches for the Universal Record history request.

    Parameters
    ----------
    element_type
        The Type of History that is to be searched for.
    modified_date
        Only search for modifications that occured on that date.
    modified_range
        Only search for modifications that occured between the two dates
        (inclusive).
    max_results
    start_from_result
    modified_by
        Agent code that modified the Universal Record
    debug_mode
        Returns Debug info. Travelport Internal Usage Only.
    """
    class Meta:
        namespace = "http://www.travelport.com/schema/universal_v52_0"

    element_type: None | str = field(
        default=None,
        metadata={
            "name": "ElementType",
            "type": "Element",
        }
    )
    modified_date: None | XmlDate = field(
        default=None,
        metadata={
            "name": "ModifiedDate",
            "type": "Element",
        }
    )
    modified_range: None | UniversalRecordHistorySearchModifiers.ModifiedRange = field(
        default=None,
        metadata={
            "name": "ModifiedRange",
            "type": "Element",
        }
    )
    max_results: int = field(
        default=20,
        metadata={
            "name": "MaxResults",
            "type": "Attribute",
            "min_inclusive": 1,
            "max_inclusive": 200,
        }
    )
    start_from_result: int = field(
        default=1,
        metadata={
            "name": "StartFromResult",
            "type": "Attribute",
            "min_inclusive": 1,
        }
    )
    modified_by: None | object = field(
        default=None,
        metadata={
            "name": "ModifiedBy",
            "type": "Attribute",
        }
    )
    debug_mode: bool = field(
        default=False,
        metadata={
            "name": "DebugMode",
            "type": "Attribute",
        }
    )

    @dataclass
    class ModifiedRange:
        modified_start: None | XmlDate = field(
            default=None,
            metadata={
                "name": "ModifiedStart",
                "type": "Element",
                "required": True,
            }
        )
        modified_end: None | XmlDate = field(
            default=None,
            metadata={
                "name": "ModifiedEnd",
                "type": "Element",
                "required": True,
            }
        )
