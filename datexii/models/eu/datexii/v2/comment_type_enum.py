from enum import Enum

__NAMESPACE__ = "http://datex2.eu/schema/2/2_0"


class CommentTypeEnum(Enum):
    """
    Classification of comment types.

    :cvar ABNORMAL_LOAD_MOVEMENT_NOTE: A free text human oriented note
        describing details of abnormal load movements associated with
        the SituationRecord.
    :cvar DATA_PROCESSING_NOTE: A free text human oriented note
        describing the way the information in the SituationRecord has
        been or should be processed.
    :cvar DESCRIPTION: A free text human oriented description of the
        situation element defined by the SituationRecord.
    :cvar INTERNAL_NOTE: A free text human oriented note that supports
        internal traffic control operations relating to the situation
        element defined by the SituationRecord.
    :cvar LOCATION_DESCRIPTOR: A free text human oriented description of
        the location of the situation element defined by the
        SituationRecord.
    :cvar WARNING: A free text human oriented warning relating to the
        SituationRecord, such as advising the recipient that an advanced
        warning on VMS should be activated.
    :cvar OTHER: Other than as defined in this enumeration.
    """
    ABNORMAL_LOAD_MOVEMENT_NOTE = "abnormalLoadMovementNote"
    DATA_PROCESSING_NOTE = "dataProcessingNote"
    DESCRIPTION = "description"
    INTERNAL_NOTE = "internalNote"
    LOCATION_DESCRIPTOR = "locationDescriptor"
    WARNING = "warning"
    OTHER = "other"
