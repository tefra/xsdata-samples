from collections.abc import Iterable
from dataclasses import dataclass, field
from typing import Union

from .containment_aggregation_structure import ContainmentAggregationStructure
from .type_of_fare_contract import TypeOfFareContract
from .type_of_fare_contract_ref import TypeOfFareContractRef

__NAMESPACE__ = "http://www.netex.org.uk/netex"


@dataclass
class TypesOfFareContractRelStructure(ContainmentAggregationStructure):
    class Meta:
        name = "typesOfFareContract_RelStructure"

    type_of_fare_contract_ref_or_type_of_fare_contract: Iterable[
        Union[TypeOfFareContractRef, TypeOfFareContract]
    ] = field(
        default_factory=list,
        metadata={
            "type": "Elements",
            "choices": (
                {
                    "name": "TypeOfFareContractRef",
                    "type": TypeOfFareContractRef,
                    "namespace": "http://www.netex.org.uk/netex",
                },
                {
                    "name": "TypeOfFareContract",
                    "type": TypeOfFareContract,
                    "namespace": "http://www.netex.org.uk/netex",
                },
            ),
        },
    )
