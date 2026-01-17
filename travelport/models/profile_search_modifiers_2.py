from __future__ import annotations

from dataclasses import dataclass, field

__NAMESPACE__ = "http://www.travelport.com/schema/uprofile_v37_0"


@dataclass
class ProfileSearchModifiers2:
    """
    Specifies the range of search results.

    If omitted, the default values for each attriubute are used.

    Parameters
    ----------
    max_results
        Limits the number of search results in the response. Note that
        performance may decline when a large number of results is requested.
    start_from_result
        The starting search index of the results returned. Used to browse
        beyond the initial search results.
    """

    class Meta:
        name = "ProfileSearchModifiers"
        namespace = "http://www.travelport.com/schema/uprofile_v37_0"

    max_results: int = field(
        default=20,
        metadata={
            "name": "MaxResults",
            "type": "Attribute",
            "min_inclusive": 1,
            "max_inclusive": 200,
        },
    )
    start_from_result: int = field(
        default=1,
        metadata={
            "name": "StartFromResult",
            "type": "Attribute",
            "min_inclusive": 1,
        },
    )
