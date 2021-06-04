from dataclasses import dataclass
from netex.models.invalid_data_references_error_structure import InvalidDataReferencesErrorStructure

__NAMESPACE__ = "http://www.siri.org.uk/siri"


@dataclass
class InvalidDataReferencesError(InvalidDataReferencesErrorStructure):
    class Meta:
        namespace = "http://www.siri.org.uk/siri"
