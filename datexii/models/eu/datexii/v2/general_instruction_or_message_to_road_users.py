from dataclasses import dataclass, field
from typing import Optional
from datexii.models.eu.datexii.v2.extension_type import ExtensionType
from datexii.models.eu.datexii.v2.general_instruction_to_road_users_type_enum import (
    GeneralInstructionToRoadUsersTypeEnum,
)
from datexii.models.eu.datexii.v2.multilingual_string import MultilingualString
from datexii.models.eu.datexii.v2.network_management import NetworkManagement

__NAMESPACE__ = "http://datex2.eu/schema/2/2_0"


@dataclass
class GeneralInstructionOrMessageToRoadUsers(NetworkManagement):
    """
    General instruction and/or message that is issued by the network/road operator
    which is applicable to drivers and sometimes passengers.

    :ivar general_instruction_to_road_users_type: General instruction
        that is issued by the network/road operator which is applicable
        to drivers and sometimes passengers.
    :ivar general_message_to_road_users: General message that is issued
        by the network/road operator which is applicable to drivers and
        sometimes passengers, e.g. details about an amber alert (missing
        or abducted child alert).
    :ivar general_instruction_or_message_to_road_users_extension:
    """

    general_instruction_to_road_users_type: Optional[
        GeneralInstructionToRoadUsersTypeEnum
    ] = field(
        default=None,
        metadata={
            "name": "generalInstructionToRoadUsersType",
            "type": "Element",
            "namespace": "http://datex2.eu/schema/2/2_0",
        },
    )
    general_message_to_road_users: Optional[MultilingualString] = field(
        default=None,
        metadata={
            "name": "generalMessageToRoadUsers",
            "type": "Element",
            "namespace": "http://datex2.eu/schema/2/2_0",
        },
    )
    general_instruction_or_message_to_road_users_extension: Optional[
        ExtensionType
    ] = field(
        default=None,
        metadata={
            "name": "generalInstructionOrMessageToRoadUsersExtension",
            "type": "Element",
            "namespace": "http://datex2.eu/schema/2/2_0",
        },
    )
