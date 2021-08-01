from dataclasses import dataclass, field
from typing import Optional
from datexii.models.eu.datexii.v2.extension_type import ExtensionType
from datexii.models.eu.datexii.v2.overall_period import OverallPeriod
from datexii.models.eu.datexii.v2.validity_status_enum import ValidityStatusEnum

__NAMESPACE__ = "http://datex2.eu/schema/2/2_0"


@dataclass
class Validity:
    """
    Specification of validity, either explicitly or by a validity time period
    specification which may be discontinuous.

    :ivar validity_status: Specification of validity, either explicitly
        overriding the validity time specification or confirming it.
    :ivar overrunning: The activity or action described by the
        SituationRecord is still in progress, overrunning its planned
        duration as indicated in a previous version of this record.
    :ivar validity_time_specification: A specification of periods of
        validity defined by overall bounding start and end times and the
        possible intersection of valid periods with exception periods
        (exception periods overriding valid periods).
    :ivar validity_extension:
    """
    validity_status: Optional[ValidityStatusEnum] = field(
        default=None,
        metadata={
            "name": "validityStatus",
            "type": "Element",
            "namespace": "http://datex2.eu/schema/2/2_0",
            "required": True,
        }
    )
    overrunning: Optional[bool] = field(
        default=None,
        metadata={
            "type": "Element",
            "namespace": "http://datex2.eu/schema/2/2_0",
        }
    )
    validity_time_specification: Optional[OverallPeriod] = field(
        default=None,
        metadata={
            "name": "validityTimeSpecification",
            "type": "Element",
            "namespace": "http://datex2.eu/schema/2/2_0",
            "required": True,
        }
    )
    validity_extension: Optional[ExtensionType] = field(
        default=None,
        metadata={
            "name": "validityExtension",
            "type": "Element",
            "namespace": "http://datex2.eu/schema/2/2_0",
        }
    )
