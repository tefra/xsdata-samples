from dataclasses import dataclass, field
from typing import Optional

from xsdata.models.datatype import XmlDateTime

from datexii.models.eu.datexii.v2.coded_reason_for_setting_message_enum import (
    CodedReasonForSettingMessageEnum,
)
from datexii.models.eu.datexii.v2.extension_type import ExtensionType
from datexii.models.eu.datexii.v2.multilingual_string import MultilingualString
from datexii.models.eu.datexii.v2.text_page import TextPage
from datexii.models.eu.datexii.v2.versioned_reference import VersionedReference
from datexii.models.eu.datexii.v2.vms_message_information_type_enum import (
    VmsMessageInformationTypeEnum,
)
from datexii.models.eu.datexii.v2.vms_message_pictogram_display_area_index_vms_pictogram_display_area import (
    VmsMessagePictogramDisplayAreaIndexVmsPictogramDisplayArea,
)

__NAMESPACE__ = "http://datex2.eu/schema/2/2_0"


@dataclass
class VmsMessage:
    """A message displayed on a VMS which may comprise one or more sequentially
    displayed text pages and/or pictograms with supplementary details.

    When in a sequence of displayed messages sequencing of text pages
    and pictograms within a message are prohibited.

    :ivar associated_management_or_diversion_plan: The identification of
        the traffic management plan or diversion plan with which the
        message is associated.
    :ivar message_set_by: The organisation or authority which set the
        message currently being displayed.
    :ivar set_by_system: Indicates whether the message has been set
        automatically by a system. True =  automatically set.
    :ivar reason_for_setting: The reason why the sign has been set.
    :ivar coded_reason_for_setting: The reason, in terms of a high level
        coded classification, why the sign has been set.
    :ivar vms_message_information_type: Type of information being
        displayed.
    :ivar primary_setting: Identifies whether the message setting is
        primary (explicitly requested) or is secondary (derived
        according to an algorthm as the result of setting other signs).
        True = a primary setting.
    :ivar mare_nostrum_compliant: Indication that the displayed message
        (text and pictogram) conforms with the formulation recommended
        by the Mare Nostrum project.
    :ivar time_last_set: The date/time at which the sign was last set.
    :ivar requested_by: The authority, organisation or system which
        requested the setting of the message. This may be different from
        the authority or system which actually set the message on behalf
        of the requestor.
    :ivar situation_to_which_message_is_related: A reference to the
        managed situation to which the set message relates.
    :ivar situation_record_to_which_message_is_related: A reference to
        the situation record/element within a managed situation to which
        the set message relates.
    :ivar distance_from_situation_record: Distance of the VMS from the
        location of the related situation record/element. If the VMS is
        located within the extent of the situation record/element this
        should be set to zero.
    :ivar text_pictogram_sequencing_interval: The time duration that
        each text page or pictogram within a message is displayed for
        before the VMS displays the next text page and/or pictogram in
        the message.
    :ivar text_page:
    :ivar vms_pictogram_display_area:
    :ivar vms_message_extension:
    """

    associated_management_or_diversion_plan: Optional[str] = field(
        default=None,
        metadata={
            "name": "associatedManagementOrDiversionPlan",
            "type": "Element",
            "namespace": "http://datex2.eu/schema/2/2_0",
            "max_length": 1024,
        },
    )
    message_set_by: Optional[MultilingualString] = field(
        default=None,
        metadata={
            "name": "messageSetBy",
            "type": "Element",
            "namespace": "http://datex2.eu/schema/2/2_0",
        },
    )
    set_by_system: Optional[bool] = field(
        default=None,
        metadata={
            "name": "setBySystem",
            "type": "Element",
            "namespace": "http://datex2.eu/schema/2/2_0",
        },
    )
    reason_for_setting: Optional[MultilingualString] = field(
        default=None,
        metadata={
            "name": "reasonForSetting",
            "type": "Element",
            "namespace": "http://datex2.eu/schema/2/2_0",
        },
    )
    coded_reason_for_setting: Optional[CodedReasonForSettingMessageEnum] = (
        field(
            default=None,
            metadata={
                "name": "codedReasonForSetting",
                "type": "Element",
                "namespace": "http://datex2.eu/schema/2/2_0",
            },
        )
    )
    vms_message_information_type: list[VmsMessageInformationTypeEnum] = field(
        default_factory=list,
        metadata={
            "name": "vmsMessageInformationType",
            "type": "Element",
            "namespace": "http://datex2.eu/schema/2/2_0",
        },
    )
    primary_setting: Optional[bool] = field(
        default=None,
        metadata={
            "name": "primarySetting",
            "type": "Element",
            "namespace": "http://datex2.eu/schema/2/2_0",
        },
    )
    mare_nostrum_compliant: Optional[bool] = field(
        default=None,
        metadata={
            "name": "mareNostrumCompliant",
            "type": "Element",
            "namespace": "http://datex2.eu/schema/2/2_0",
        },
    )
    time_last_set: Optional[XmlDateTime] = field(
        default=None,
        metadata={
            "name": "timeLastSet",
            "type": "Element",
            "namespace": "http://datex2.eu/schema/2/2_0",
            "required": True,
        },
    )
    requested_by: Optional[MultilingualString] = field(
        default=None,
        metadata={
            "name": "requestedBy",
            "type": "Element",
            "namespace": "http://datex2.eu/schema/2/2_0",
        },
    )
    situation_to_which_message_is_related: Optional[VersionedReference] = (
        field(
            default=None,
            metadata={
                "name": "situationToWhichMessageIsRelated",
                "type": "Element",
                "namespace": "http://datex2.eu/schema/2/2_0",
            },
        )
    )
    situation_record_to_which_message_is_related: Optional[
        VersionedReference
    ] = field(
        default=None,
        metadata={
            "name": "situationRecordToWhichMessageIsRelated",
            "type": "Element",
            "namespace": "http://datex2.eu/schema/2/2_0",
        },
    )
    distance_from_situation_record: Optional[float] = field(
        default=None,
        metadata={
            "name": "distanceFromSituationRecord",
            "type": "Element",
            "namespace": "http://datex2.eu/schema/2/2_0",
        },
    )
    text_pictogram_sequencing_interval: Optional[float] = field(
        default=None,
        metadata={
            "name": "textPictogramSequencingInterval",
            "type": "Element",
            "namespace": "http://datex2.eu/schema/2/2_0",
        },
    )
    text_page: list[TextPage] = field(
        default_factory=list,
        metadata={
            "name": "textPage",
            "type": "Element",
            "namespace": "http://datex2.eu/schema/2/2_0",
        },
    )
    vms_pictogram_display_area: list[
        VmsMessagePictogramDisplayAreaIndexVmsPictogramDisplayArea
    ] = field(
        default_factory=list,
        metadata={
            "name": "vmsPictogramDisplayArea",
            "type": "Element",
            "namespace": "http://datex2.eu/schema/2/2_0",
        },
    )
    vms_message_extension: Optional[ExtensionType] = field(
        default=None,
        metadata={
            "name": "vmsMessageExtension",
            "type": "Element",
            "namespace": "http://datex2.eu/schema/2/2_0",
        },
    )
