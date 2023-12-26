from __future__ import annotations
from dataclasses import dataclass, field
from travelport.models.base_req_1 import BaseReq1
from travelport.models.type_show_providers_type import TypeShowProvidersType

__NAMESPACE__ = "http://www.travelport.com/schema/util_v52_0"


@dataclass
class ContentProviderRetrieveReq(BaseReq1):
    """
    Retrieves all available providers with their suppliers.

    Parameters
    ----------
    provider_code
        If ProviderCode present, Retruns Data for the ProviderCode
    supplier_code
        Represents SupplierCode or Carrier code. If SupplierCode Presents,
        returns Data for the SupplierCode.
    show_providers
        Enumeration of reqested type of Provider Configuration requested -
        default is "Provisioned". An error may be returned if 'All' is
        requested and the user security level is not allowed this access
    """

    class Meta:
        namespace = "http://www.travelport.com/schema/util_v52_0"

    provider_code: None | str = field(
        default=None,
        metadata={
            "name": "ProviderCode",
            "type": "Attribute",
            "min_length": 2,
            "max_length": 5,
        },
    )
    supplier_code: None | str = field(
        default=None,
        metadata={
            "name": "SupplierCode",
            "type": "Attribute",
            "min_length": 1,
            "max_length": 5,
        },
    )
    show_providers: TypeShowProvidersType = field(
        default=TypeShowProvidersType.PROVISIONED,
        metadata={
            "name": "ShowProviders",
            "type": "Attribute",
        },
    )
