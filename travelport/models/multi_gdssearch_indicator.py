from __future__ import annotations
from dataclasses import dataclass, field

__NAMESPACE__ = "http://www.travelport.com/schema/air_v52_0"


@dataclass
class MultiGdssearchIndicator:
    """
    Indicates whether public fares and/or private fares should be returned.

    Parameters
    ----------
    type_value
        Indicates whether only public fares or both public and private fares
        should be returned or a specific type of private fares. Examples of
        valid values are PublicFaresOnly, PrivateFaresOnly,
        AirlinePrivateFaresOnly, AgencyPrivateFaresOnly,
        PublicandPrivateFares, and NetFaresOnly.
    provider_code
    default_provider
        Use the value “true” if the provider is the default (primary)
        provider.  Use the value “false” if the provider is the alternate
        (secondary).  Use of this attribute requires specifically
        provisioned credentials.
    private_fare_code
        The code of the corporate private fare.  This is the same as an
        account code.  Use of this attribute requires specifically
        provisioned credentials.
    private_fare_code_only
        :  Indicates whether or not the private fares returned should be
        restricted to only those specific to the PrivateFareCode in the
        previous attribute.  This has the same validation as the
        AccountCodeFaresOnly attribute.  Use of this attribute requires
        specifically provisioned credentials.
    """

    class Meta:
        name = "MultiGDSSearchIndicator"
        namespace = "http://www.travelport.com/schema/air_v52_0"

    type_value: None | str = field(
        default=None,
        metadata={
            "name": "Type",
            "type": "Attribute",
        },
    )
    provider_code: None | str = field(
        default=None,
        metadata={
            "name": "ProviderCode",
            "type": "Attribute",
            "min_length": 2,
            "max_length": 5,
        },
    )
    default_provider: None | bool = field(
        default=None,
        metadata={
            "name": "DefaultProvider",
            "type": "Attribute",
        },
    )
    private_fare_code: None | str = field(
        default=None,
        metadata={
            "name": "PrivateFareCode",
            "type": "Attribute",
        },
    )
    private_fare_code_only: None | bool = field(
        default=None,
        metadata={
            "name": "PrivateFareCodeOnly",
            "type": "Attribute",
        },
    )
