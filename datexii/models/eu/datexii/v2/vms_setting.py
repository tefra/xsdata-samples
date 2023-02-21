from dataclasses import dataclass, field
from typing import Optional
from datexii.models.eu.datexii.v2.extension_type import ExtensionType

__NAMESPACE__ = "http://datex2.eu/schema/2/2_0"


@dataclass
class VmsSetting:
    """
    Provides information on variable message signs and the information currently
    displayed.
    """
    vms_setting_extension: Optional[ExtensionType] = field(
        default=None,
        metadata={
            "name": "vmsSettingExtension",
            "type": "Element",
            "namespace": "http://datex2.eu/schema/2/2_0",
        }
    )
