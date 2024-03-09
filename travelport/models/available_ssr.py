from __future__ import annotations

from dataclasses import dataclass, field

from travelport.models.industry_standard_ssr_1 import IndustryStandardSsr1
from travelport.models.service_rule_type_1 import ServiceRuleType1
from travelport.models.ssr_1 import Ssr1

__NAMESPACE__ = "http://www.travelport.com/schema/air_v52_0"


@dataclass
class AvailableSsr:
    """
    A wrapper for all the information regarding each of the available SSR.

    Parameters
    ----------
    ssr
    ssrrules
        Holds the rules for selecting the SSR in the itinerary
    industry_standard_ssr
    """

    class Meta:
        name = "AvailableSSR"
        namespace = "http://www.travelport.com/schema/air_v52_0"

    ssr: list[Ssr1] = field(
        default_factory=list,
        metadata={
            "name": "SSR",
            "type": "Element",
            "namespace": "http://www.travelport.com/schema/common_v52_0",
            "max_occurs": 999,
        },
    )
    ssrrules: list[ServiceRuleType1] = field(
        default_factory=list,
        metadata={
            "name": "SSRRules",
            "type": "Element",
            "max_occurs": 999,
        },
    )
    industry_standard_ssr: list[IndustryStandardSsr1] = field(
        default_factory=list,
        metadata={
            "name": "IndustryStandardSSR",
            "type": "Element",
            "namespace": "http://www.travelport.com/schema/common_v52_0",
            "max_occurs": 999,
        },
    )
