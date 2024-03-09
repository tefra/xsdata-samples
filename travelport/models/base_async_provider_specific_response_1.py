from __future__ import annotations

from dataclasses import dataclass, field

__NAMESPACE__ = "http://www.travelport.com/schema/common_v32_0"


@dataclass
class BaseAsyncProviderSpecificResponse1:
    """
    Identifies pending responses from a specific provider using MoreResults
    attribute.

    Parameters
    ----------
    provider_code
        Provider code of a specific host
    more_results
        Identifies whether more results are available for specific host or
        not.
    """

    class Meta:
        name = "BaseAsyncProviderSpecificResponse"

    provider_code: None | str = field(
        default=None,
        metadata={
            "name": "ProviderCode",
            "type": "Attribute",
            "required": True,
            "min_length": 2,
            "max_length": 5,
        },
    )
    more_results: None | bool = field(
        default=None,
        metadata={
            "name": "MoreResults",
            "type": "Attribute",
            "required": True,
        },
    )
