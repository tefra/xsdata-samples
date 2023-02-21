from dataclasses import dataclass, field
from typing import Optional
from datexii.models.eu.datexii.v2.extension_type import ExtensionType
from datexii.models.eu.datexii.v2.operator_action import OperatorAction
from datexii.models.eu.datexii.v2.vms_setting import VmsSetting

__NAMESPACE__ = "http://datex2.eu/schema/2/2_0"


@dataclass
class SignSetting(OperatorAction):
    """
    Provides information on message signs and the information currently displayed.
    """
    vms_setting: Optional[VmsSetting] = field(
        default=None,
        metadata={
            "name": "vmsSetting",
            "type": "Element",
            "namespace": "http://datex2.eu/schema/2/2_0",
            "required": True,
        }
    )
    sign_setting_extension: Optional[ExtensionType] = field(
        default=None,
        metadata={
            "name": "signSettingExtension",
            "type": "Element",
            "namespace": "http://datex2.eu/schema/2/2_0",
        }
    )
