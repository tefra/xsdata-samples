from __future__ import annotations

from collections.abc import Sequence
from dataclasses import dataclass, field

from .containment_aggregation_structure import ContainmentAggregationStructure
from .sales_offer_package_substitution import SalesOfferPackageSubstitution
from .sales_offer_package_substitution_ref import (
    SalesOfferPackageSubstitutionRef,
)

__NAMESPACE__ = "http://www.netex.org.uk/netex"


@dataclass(kw_only=True)
class SalesOfferPackageSubstitutionsRelStructure(
    ContainmentAggregationStructure
):
    class Meta:
        name = "salesOfferPackageSubstitutions_RelStructure"

    sales_offer_package_substitution_ref_or_sales_offer_package_substitution: Sequence[
        SalesOfferPackageSubstitutionRef | SalesOfferPackageSubstitution
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
