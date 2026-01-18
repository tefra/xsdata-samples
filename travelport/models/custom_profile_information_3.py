from __future__ import annotations

from dataclasses import dataclass

__NAMESPACE__ = "http://www.travelport.com/schema/common_v33_0"


@dataclass(kw_only=True)
class CustomProfileInformation3:
    """
    Custom Profile Field Data required for File Finishing.
    """

    class Meta:
        name = "CustomProfileInformation"
        namespace = "http://www.travelport.com/schema/common_v33_0"
