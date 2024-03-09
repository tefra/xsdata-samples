from __future__ import annotations

from dataclasses import dataclass, field

from travelport.models.optional_service_applicability_type_5 import (
    OptionalServiceApplicabilityType5,
)

__NAMESPACE__ = "http://www.travelport.com/schema/common_v34_0"


@dataclass
class OptionalServiceApplicationLimitType5:
    """
    The optional service application limit.

    Parameters
    ----------
    applicable_level
        Indicates the applicable level for the option
    provider_defined_applicable_levels
        Indicates the actual provider defined ApplicableLevels which is
        mapped to Other
    maximum_quantity
        The maximum quantity allowed for the type
    minimum_quantity
        Indicates the minimum number of the option that can be selected.
    """

    class Meta:
        name = "OptionalServiceApplicationLimitType"

    applicable_level: None | OptionalServiceApplicabilityType5 = field(
        default=None,
        metadata={
            "name": "ApplicableLevel",
            "type": "Attribute",
            "required": True,
        },
    )
    provider_defined_applicable_levels: None | str = field(
        default=None,
        metadata={
            "name": "ProviderDefinedApplicableLevels",
            "type": "Attribute",
        },
    )
    maximum_quantity: None | int = field(
        default=None,
        metadata={
            "name": "MaximumQuantity",
            "type": "Attribute",
            "required": True,
        },
    )
    minimum_quantity: None | int = field(
        default=None,
        metadata={
            "name": "MinimumQuantity",
            "type": "Attribute",
        },
    )
