from dataclasses import dataclass, field
from typing import Optional

from datexii.models.eu.datexii.v2.cause import Cause
from datexii.models.eu.datexii.v2.extension_type import ExtensionType
from datexii.models.eu.datexii.v2.situation_record_versioned_reference import (
    SituationRecordVersionedReference,
)

__NAMESPACE__ = "http://datex2.eu/schema/2/2_0"


@dataclass
class ManagedCause(Cause):
    """
    A cause of this situation record which is managed by the publication creator,
    i.e. one which is represented by another situation record produced by the same
    publication creator.

    :ivar managed_cause: A reference to another situation record
        produced by the same publication creator which defines a cause
        of the event defined here.
    :ivar managed_cause_extension:
    """

    managed_cause: Optional[SituationRecordVersionedReference] = field(
        default=None,
        metadata={
            "name": "managedCause",
            "type": "Element",
            "namespace": "http://datex2.eu/schema/2/2_0",
        },
    )
    managed_cause_extension: Optional[ExtensionType] = field(
        default=None,
        metadata={
            "name": "managedCauseExtension",
            "type": "Element",
            "namespace": "http://datex2.eu/schema/2/2_0",
        },
    )
