from __future__ import annotations
from dataclasses import dataclass
from travelport.models.type_tax_info_1 import TypeTaxInfo1

__NAMESPACE__ = "http://www.travelport.com/schema/air_v52_0"


@dataclass
class TaxInfo(TypeTaxInfo1):
    """
    The tax information for a.
    """

    class Meta:
        namespace = "http://www.travelport.com/schema/air_v52_0"
