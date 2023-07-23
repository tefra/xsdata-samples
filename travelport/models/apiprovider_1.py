from __future__ import annotations
from dataclasses import dataclass, field
from travelport.models.transaction_type_1 import TransactionType1

__NAMESPACE__ = "http://www.travelport.com/schema/common_v52_0"


@dataclass
class Apiprovider1:
    """
    Parameters
    ----------
    transaction_type
    available_pseudo_city_code
    provider_code
        The Provider Code of the host
    supplier_code
        The Supplier Code of the host
    iatacode
        Agency IATA or ARC code, used as an ID with airlines.
    """
    class Meta:
        name = "APIProvider"
        namespace = "http://www.travelport.com/schema/common_v52_0"

    transaction_type: None | TransactionType1 = field(
        default=None,
        metadata={
            "name": "TransactionType",
            "type": "Element",
        }
    )
    available_pseudo_city_code: list[Apiprovider1.AvailablePseudoCityCode] = field(
        default_factory=list,
        metadata={
            "name": "AvailablePseudoCityCode",
            "type": "Element",
            "max_occurs": 999,
        }
    )
    provider_code: None | str = field(
        default=None,
        metadata={
            "name": "ProviderCode",
            "type": "Attribute",
            "required": True,
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
    iatacode: None | str = field(
        default=None,
        metadata={
            "name": "IATACode",
            "type": "Attribute",
            "max_length": 8,
        }
    )

    @dataclass
    class AvailablePseudoCityCode:
        """
        Parameters
        ----------
        pseudo_city_code
            The PseudoCityCode used to connect to the host.
        """
        pseudo_city_code: None | str = field(
            default=None,
            metadata={
                "name": "PseudoCityCode",
                "type": "Attribute",
                "min_length": 2,
                "max_length": 10,
            }
        )
