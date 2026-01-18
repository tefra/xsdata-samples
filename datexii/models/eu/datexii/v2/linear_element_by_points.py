from __future__ import annotations

from dataclasses import dataclass, field

from datexii.models.eu.datexii.v2.extension_type import ExtensionType
from datexii.models.eu.datexii.v2.intermediate_point_on_linear_element import (
    IntermediatePointOnLinearElement,
)
from datexii.models.eu.datexii.v2.linear_element import LinearElement
from datexii.models.eu.datexii.v2.referent import Referent

__NAMESPACE__ = "http://datex2.eu/schema/2/2_0"


@dataclass
class LinearElementByPoints(LinearElement):
    """
    A linear element along a single linear object defined by its start and
    end points.

    :ivar start_point_of_linear_element: The referent at a known
        location on the linear object which defines the start of the
        linear element.
    :ivar intermediate_point_on_linear_element: A referent at a known
        location on the linear object which is neither the start or end
        of the linear element.
    :ivar end_point_of_linear_element: The referent at a known location
        on the linear object which defines the end of the linear
        element.
    :ivar linear_element_by_points_extension:
    """

    start_point_of_linear_element: None | Referent = field(
        default=None,
        metadata={
            "name": "startPointOfLinearElement",
            "type": "Element",
            "namespace": "http://datex2.eu/schema/2/2_0",
            "required": True,
        },
    )
    intermediate_point_on_linear_element: list[
        IntermediatePointOnLinearElement
    ] = field(
        default_factory=list,
        metadata={
            "name": "intermediatePointOnLinearElement",
            "type": "Element",
            "namespace": "http://datex2.eu/schema/2/2_0",
        },
    )
    end_point_of_linear_element: None | Referent = field(
        default=None,
        metadata={
            "name": "endPointOfLinearElement",
            "type": "Element",
            "namespace": "http://datex2.eu/schema/2/2_0",
            "required": True,
        },
    )
    linear_element_by_points_extension: None | ExtensionType = field(
        default=None,
        metadata={
            "name": "linearElementByPointsExtension",
            "type": "Element",
            "namespace": "http://datex2.eu/schema/2/2_0",
        },
    )
