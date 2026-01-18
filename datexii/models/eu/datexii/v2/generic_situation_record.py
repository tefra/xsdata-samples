from dataclasses import dataclass, field

from datexii.models.eu.datexii.v2.extension_type import ExtensionType
from datexii.models.eu.datexii.v2.situation_record import SituationRecord

__NAMESPACE__ = "http://datex2.eu/schema/2/2_0"


@dataclass
class GenericSituationRecord(SituationRecord):
    """
    A generic SituationRecord for use when adding level B extensions at the
    SituationRecord level.

    :ivar generic_situation_record_name: The name of the
        GenericSituationRecord.
    :ivar generic_situation_record_extension:
    """

    generic_situation_record_name: str | None = field(
        default=None,
        metadata={
            "name": "genericSituationRecordName",
            "type": "Element",
            "namespace": "http://datex2.eu/schema/2/2_0",
            "required": True,
            "max_length": 1024,
        },
    )
    generic_situation_record_extension: ExtensionType | None = field(
        default=None,
        metadata={
            "name": "genericSituationRecordExtension",
            "type": "Element",
            "namespace": "http://datex2.eu/schema/2/2_0",
        },
    )
