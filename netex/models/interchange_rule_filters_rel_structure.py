from __future__ import annotations

from collections.abc import Sequence
from dataclasses import dataclass, field

from .containment_aggregation_structure import ContainmentAggregationStructure
from .interchange_rule_filter import InterchangeRuleFilter

__NAMESPACE__ = "http://www.netex.org.uk/netex"


@dataclass(kw_only=True)
class InterchangeRuleFiltersRelStructure(ContainmentAggregationStructure):
    class Meta:
        name = "interchangeRuleFilters_RelStructure"

    interchange_rule_filter: Sequence[InterchangeRuleFilter] = field(
        default_factory=list,
        metadata={
            "name": "InterchangeRuleFilter",
            "type": "Element",
            "namespace": "http://www.netex.org.uk/netex",
            "min_occurs": 1,
        },
    )
