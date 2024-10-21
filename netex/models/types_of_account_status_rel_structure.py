from collections.abc import Iterable
from dataclasses import dataclass, field
from typing import Union

from .containment_aggregation_structure import ContainmentAggregationStructure
from .customer_account_status import CustomerAccountStatus
from .customer_account_status_ref import CustomerAccountStatusRef

__NAMESPACE__ = "http://www.netex.org.uk/netex"


@dataclass
class TypesOfAccountStatusRelStructure(ContainmentAggregationStructure):
    class Meta:
        name = "typesOfAccountStatus_RelStructure"

    customer_account_status_ref_or_customer_account_status: Iterable[
        Union[CustomerAccountStatusRef, CustomerAccountStatus]
    ] = field(
        default_factory=list,
        metadata={
            "type": "Elements",
            "choices": (
                {
                    "name": "CustomerAccountStatusRef",
                    "type": CustomerAccountStatusRef,
                    "namespace": "http://www.netex.org.uk/netex",
                },
                {
                    "name": "CustomerAccountStatus",
                    "type": CustomerAccountStatus,
                    "namespace": "http://www.netex.org.uk/netex",
                },
            ),
        },
    )
