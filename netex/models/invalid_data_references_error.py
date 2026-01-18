from __future__ import annotations

from dataclasses import dataclass

from .invalid_data_references_error_structure import (
    InvalidDataReferencesErrorStructure,
)

__NAMESPACE__ = "http://www.siri.org.uk/siri"


@dataclass
class InvalidDataReferencesError(InvalidDataReferencesErrorStructure):
    class Meta:
        namespace = "http://www.siri.org.uk/siri"
