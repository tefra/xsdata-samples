from dataclasses import dataclass, field
from typing import Optional

from xsdata.models.datatype import XmlDateTime

from .error_code_structure import ErrorCodeStructure

__NAMESPACE__ = "http://www.siri.org.uk/siri"


@dataclass
class ServiceNotAvailableErrorStructure(ErrorCodeStructure):
    expected_restart_time: Optional[XmlDateTime] = field(
        default=None,
        metadata={
            "name": "ExpectedRestartTime",
            "type": "Element",
            "namespace": "http://www.siri.org.uk/siri",
        },
    )
