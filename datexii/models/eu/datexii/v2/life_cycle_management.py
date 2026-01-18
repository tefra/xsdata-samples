from dataclasses import dataclass, field

from datexii.models.eu.datexii.v2.extension_type import ExtensionType

__NAMESPACE__ = "http://datex2.eu/schema/2/2_0"


@dataclass
class LifeCycleManagement:
    """
    Information relating to the life cycle management of the situation
    record.

    :ivar cancel: Indication that all the element information previously
        sent is not considered valid, due to an incorrect content.
    :ivar end: A binary attribute specifying whether the situation
        element is finished (true) or not (false). If finished (i.e. end
        is true) then the overallEndTime in the OverallPeriod class
        associated with the SituationRecord must be populated.
    :ivar life_cycle_management_extension:
    """

    cancel: bool | None = field(
        default=None,
        metadata={
            "type": "Element",
            "namespace": "http://datex2.eu/schema/2/2_0",
        },
    )
    end: bool | None = field(
        default=None,
        metadata={
            "type": "Element",
            "namespace": "http://datex2.eu/schema/2/2_0",
        },
    )
    life_cycle_management_extension: ExtensionType | None = field(
        default=None,
        metadata={
            "name": "lifeCycleManagementExtension",
            "type": "Element",
            "namespace": "http://datex2.eu/schema/2/2_0",
        },
    )
