from __future__ import annotations

from dataclasses import dataclass, field

from sdmx_ml.models.annotable_type import AnnotableType
from sdmx_ml.models.availability_constraint_attachment_type import (
    AvailabilityConstraintAttachmentType,
)
from sdmx_ml.models.cube_region_type import CubeRegionType

__NAMESPACE__ = "http://www.sdmx.org/resources/sdmxml/schemas/v3_1/structure"


@dataclass(frozen=True, kw_only=True)
class AvailabilityConstraintType(AnnotableType):
    """
    AvailabilityConstraintType defines the structure of an availability
    constraint.

    This type of constraint contains the actual data currently present for
    the referenced object and is used to express data availability either
    by listing the available sets of keys (DataKeySet) or a set of
    component values (CubeRegion), e.g., in a data source. Availability
    constraints should not be (semantically) versioned.

    :ivar constraint_attachment: ConstraintAttachment describes the
        Constrainable structure the availability information is for
    :ivar cube_region: CubeRegion defines a slice of the data set
        (dimensions and attribute values) for the constrained artefact.
        A set of included or excluded regions can be described.
    :ivar series_count:
    :ivar obs_count:
    """

    constraint_attachment: AvailabilityConstraintAttachmentType = field(
        metadata={
            "name": "ConstraintAttachment",
            "type": "Element",
            "namespace": "http://www.sdmx.org/resources/sdmxml/schemas/v3_1/structure",
            "required": True,
        }
    )
    cube_region: CubeRegionType = field(
        metadata={
            "name": "CubeRegion",
            "type": "Element",
            "namespace": "http://www.sdmx.org/resources/sdmxml/schemas/v3_1/structure",
            "required": True,
        }
    )
    series_count: None | int = field(
        default=None,
        metadata={
            "name": "seriesCount",
            "type": "Attribute",
        },
    )
    obs_count: None | int = field(
        default=None,
        metadata={
            "name": "obsCount",
            "type": "Attribute",
        },
    )
