from collections.abc import Iterable
from dataclasses import dataclass, field
from typing import Union

from .containment_aggregation_structure import ContainmentAggregationStructure
from .sales_offer_package_substitution import SalesOfferPackageSubstitution
from .sales_offer_package_substitution_ref import (
    SalesOfferPackageSubstitutionRef,
)

__NAMESPACE__ = "http://www.netex.org.uk/netex"


@dataclass
class SalesOfferPackageSubstitutionsRelStructure(
    ContainmentAggregationStructure
):
    class Meta:
        name = "salesOfferPackageSubstitutions_RelStructure"

    sales_offer_package_substitution_ref_or_sales_offer_package_substitution: Iterable[
        Union[SalesOfferPackageSubstitutionRef, SalesOfferPackageSubstitution]
    ] = field(
        default_factory=list,
        metadata={
            "type": "Elements",
            "choices": (
                {
                    "name": "SalesOfferPackageSubstitutionRef",
                    "type": SalesOfferPackageSubstitutionRef,
                    "namespace": "http://www.netex.org.uk/netex",
                },
                {
                    "name": "SalesOfferPackageSubstitution",
                    "type": SalesOfferPackageSubstitution,
                    "namespace": "http://www.netex.org.uk/netex",
                },
            ),
        },
    )
