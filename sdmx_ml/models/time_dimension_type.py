from dataclasses import dataclass, field
from typing import Any

from sdmx_ml.models.base_dimension_type import BaseDimensionType
from sdmx_ml.models.time_dimension_representation_type import (
    TimeDimensionRepresentationType,
)

__NAMESPACE__ = "http://www.sdmx.org/resources/sdmxml/schemas/v3_0/structure"


@dataclass(frozen=True)
class TimeDimensionType(BaseDimensionType):
    """
    TimeDimensionType describes the structure of a time dimension.

    The time dimension takes its semantic from its concept identity
    (usually the TIME_PERIOD concept), yet is always has a fixed identifier
    (TIME_PERIOD). The time dimension always has a fixed text format, which
    specifies that its format is always the in the value set of the
    observational time period (see common:ObservationalTimePeriodType). It
    is possible that the format may be a sub-set of the observational time
    period value set. For example, it is possible to state that the
    representation might always be a calendar year. See the enumerations of
    the textType attribute in the LocalRepresentation/TextFormat for more
    details of the possible sub-sets. It is also possible to facet this
    representation with start and end dates. The purpose of such facts is
    to restrict the value of the time dimension to occur within the
    specified range. If the time dimension is expected to allow for the
    standard reporting periods (see common:ReportingTimePeriodType) to be
    used, then it is strongly recommended that the reporting year start day
    attribute also be included in the data structure definition. When the
    reporting year start day attribute is used, any standard reporting
    period values will be assumed to be based on the start day contained in
    this attribute. If the reporting year start day attribute is not
    included and standard reporting periods are used, these values will be
    assumed to be based on a reporting year which begins January 1.

    :ivar concept_role: ConceptRole references concepts which define
        roles which this dimension serves.
    :ivar local_representation:
    :ivar id:
    :ivar position:
    """

    concept_role: Any = field(
        init=False,
        default=None,
        metadata={
            "type": "Ignore",
        },
    )
    local_representation: TimeDimensionRepresentationType | None = field(
        default=None,
        metadata={
            "name": "LocalRepresentation",
            "type": "Element",
            "namespace": "http://www.sdmx.org/resources/sdmxml/schemas/v3_0/structure",
            "required": True,
        },
    )
    id: str = field(
        init=False,
        default="TIME_PERIOD",
        metadata={
            "type": "Attribute",
            "pattern": r"[A-Za-z][A-Za-z0-9_\-]*",
        },
    )
    position: Any = field(
        init=False,
        default=None,
        metadata={
            "type": "Ignore",
        },
    )
