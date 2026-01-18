from __future__ import annotations

from dataclasses import dataclass, field

from xsdata.models.datatype import XmlDateTime

from .error_code_structure import ErrorCodeStructure

__NAMESPACE__ = "http://www.siri.org.uk/siri"


@dataclass(kw_only=True)
class ServiceNotAvailableErrorStructure(ErrorCodeStructure):
    expected_restart_time: None | XmlDateTime = field(
        default=None,
        metadata={
            "name": "ExpectedRestartTime",
            "type": "Element",
            "namespace": "http://www.siri.org.uk/siri",
        },
    )
