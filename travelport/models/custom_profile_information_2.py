from __future__ import annotations
from dataclasses import dataclass

__NAMESPACE__ = "http://www.travelport.com/schema/common_v32_0"


@dataclass
class CustomProfileInformation2:
    """
    Custom Profile Field Data required for File Finishing.
    """

    class Meta:
        name = "CustomProfileInformation"
        namespace = "http://www.travelport.com/schema/common_v32_0"
