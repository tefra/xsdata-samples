from __future__ import annotations

from collections.abc import Sequence
from dataclasses import dataclass, field

from .containment_aggregation_structure import ContainmentAggregationStructure
from .type_of_security_list import TypeOfSecurityList
from .type_of_security_list_ref import TypeOfSecurityListRef

__NAMESPACE__ = "http://www.netex.org.uk/netex"


@dataclass(kw_only=True)
class TypesOfSecurityListRelStructure(ContainmentAggregationStructure):
    class Meta:
        name = "typesOfSecurityList_RelStructure"

    type_of_security_list_ref_or_type_of_security_list: Sequence[
        TypeOfSecurityListRef | TypeOfSecurityList
    ] = field(
        default_factory=list,
        metadata={
            "type": "Elements",
            "choices": (
                {
                    "name": "TypeOfSecurityListRef",
                    "type": TypeOfSecurityListRef,
                    "namespace": "http://www.netex.org.uk/netex",
                },
                {
                    "name": "TypeOfSecurityList",
                    "type": TypeOfSecurityList,
                    "namespace": "http://www.netex.org.uk/netex",
                },
            ),
        },
    )
