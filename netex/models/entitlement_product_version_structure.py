from dataclasses import dataclass, field
from typing import Optional
from .fare_product_prices_rel_structure import FareProductPricesRelStructure
from .general_organisation_ref import GeneralOrganisationRef
from .service_access_right_version_structure import ServiceAccessRightVersionStructure

__NAMESPACE__ = "http://www.netex.org.uk/netex"


@dataclass
class EntitlementProductVersionStructure(ServiceAccessRightVersionStructure):
    class Meta:
        name = "EntitlementProduct_VersionStructure"

    general_organisation_ref: Optional[GeneralOrganisationRef] = field(
        default=None,
        metadata={
            "name": "GeneralOrganisationRef",
            "type": "Element",
            "namespace": "http://www.netex.org.uk/netex",
        }
    )
    prices: Optional[FareProductPricesRelStructure] = field(
        default=None,
        metadata={
            "type": "Element",
            "namespace": "http://www.netex.org.uk/netex",
        }
    )
