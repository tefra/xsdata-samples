from __future__ import annotations
from dataclasses import dataclass, field
from travelport.models.type_mcostatus import TypeMcostatus
from travelport.models.type_mcotype import TypeMcotype

__NAMESPACE__ = "http://www.travelport.com/schema/util_v52_0"


@dataclass
class McoSearchModifiers:
    """
    Modifiers to narrow the MCO search results.

    Parameters
    ----------
    type_value
        Find all MCOs of a particular type
    status
        Find all MCOs of a particular status.
    max_results
        Used to limit the number of results returned, particularly in more
        200809 searches that may return a large result set.
    start_from_result
        Used to browse beyond the maximum number of results specified with
        the MaxResults parameter. Acts as an offset to skip the specified
        number of items from the begining of the result set.
    include_name
        Should the McoSearchResult include the name on the MCO
    """

    class Meta:
        namespace = "http://www.travelport.com/schema/util_v52_0"

    type_value: None | TypeMcotype = field(
        default=None,
        metadata={
            "name": "Type",
            "type": "Attribute",
        },
    )
    status: None | TypeMcostatus = field(
        default=None,
        metadata={
            "name": "Status",
            "type": "Attribute",
        },
    )
    max_results: int = field(
        default=20,
        metadata={
            "name": "MaxResults",
            "type": "Attribute",
            "min_inclusive": 1,
        },
    )
    start_from_result: int = field(
        default=0,
        metadata={
            "name": "StartFromResult",
            "type": "Attribute",
            "min_inclusive": 0,
        },
    )
    include_name: bool = field(
        default=False,
        metadata={
            "name": "IncludeName",
            "type": "Attribute",
        },
    )
