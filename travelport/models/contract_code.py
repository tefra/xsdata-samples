from __future__ import annotations
from dataclasses import dataclass, field

__NAMESPACE__ = "http://www.travelport.com/schema/air_v52_0"


@dataclass
class ContractCode:
    """
    Some private fares (non-ATPCO) are secured to a contract code.

    Parameters
    ----------
    code
        The 1-64 character string which uniquely identifies a Contract.
    company_name
        Providers supported : ACH
    provider_code
    supplier_code
    """
    class Meta:
        namespace = "http://www.travelport.com/schema/air_v52_0"

    code: None | str = field(
        default=None,
        metadata={
            "name": "Code",
            "type": "Attribute",
            "required": True,
            "min_length": 1,
            "max_length": 64,
        }
    )
    company_name: None | str = field(
        default=None,
        metadata={
            "name": "CompanyName",
            "type": "Attribute",
        }
    )
    provider_code: None | str = field(
        default=None,
        metadata={
            "name": "ProviderCode",
            "type": "Attribute",
            "min_length": 2,
            "max_length": 5,
        }
    )
    supplier_code: None | str = field(
        default=None,
        metadata={
            "name": "SupplierCode",
            "type": "Attribute",
            "min_length": 1,
            "max_length": 5,
        }
    )
