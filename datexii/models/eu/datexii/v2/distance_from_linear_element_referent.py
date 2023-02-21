from dataclasses import dataclass, field
from typing import Optional
from datexii.models.eu.datexii.v2.distance_along_linear_element import DistanceAlongLinearElement
from datexii.models.eu.datexii.v2.extension_type import ExtensionType
from datexii.models.eu.datexii.v2.referent import Referent

__NAMESPACE__ = "http://datex2.eu/schema/2/2_0"


@dataclass
class DistanceFromLinearElementReferent(DistanceAlongLinearElement):
    """
    Distance of a point along a linear element measured from a "from referent" on
    the linear element, in the sense relative to the linear element definition
    rather than the direction of traffic flow or optionally towards a "towards
    referent".

    :ivar distance_along: A measure of distance along a linear element.
    :ivar from_referent: A known location along the linear element from
        which the distanceAlong is measured, termed the "fromReferent"
        in ISO 19148.
    :ivar towards_referent: A known location along the linear element
        towards which the distanceAlong is measured, termed the
        "towardsReferent" in ISO 19148.
    :ivar distance_from_linear_element_referent_extension:
    """
    distance_along: Optional[float] = field(
        default=None,
        metadata={
            "name": "distanceAlong",
            "type": "Element",
            "namespace": "http://datex2.eu/schema/2/2_0",
            "required": True,
        }
    )
    from_referent: Optional[Referent] = field(
        default=None,
        metadata={
            "name": "fromReferent",
            "type": "Element",
            "namespace": "http://datex2.eu/schema/2/2_0",
            "required": True,
        }
    )
    towards_referent: Optional[Referent] = field(
        default=None,
        metadata={
            "name": "towardsReferent",
            "type": "Element",
            "namespace": "http://datex2.eu/schema/2/2_0",
        }
    )
    distance_from_linear_element_referent_extension: Optional[ExtensionType] = field(
        default=None,
        metadata={
            "name": "distanceFromLinearElementReferentExtension",
            "type": "Element",
            "namespace": "http://datex2.eu/schema/2/2_0",
        }
    )
