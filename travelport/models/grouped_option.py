from __future__ import annotations
from dataclasses import dataclass, field

__NAMESPACE__ = "http://www.travelport.com/schema/air_v52_0"


@dataclass
class GroupedOption:
    """
    Parameters
    ----------
    optional_service_ref
        Reference to a optionalService which is paired with other optional
        services in the parent PairedOptions element.
    """
    class Meta:
        namespace = "http://www.travelport.com/schema/air_v52_0"

    optional_service_ref: None | str = field(
        default=None,
        metadata={
            "name": "OptionalServiceRef",
            "type": "Attribute",
            "required": True,
        }
    )
