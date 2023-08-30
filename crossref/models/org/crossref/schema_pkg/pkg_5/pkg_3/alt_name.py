from dataclasses import dataclass, field
from typing import List
from crossref.models.org.crossref.schema_pkg.pkg_5.pkg_3.name import Name
from crossref.models.org.crossref.schema_pkg.pkg_5.pkg_3.string_name import StringName

__NAMESPACE__ = "http://www.crossref.org/schema/5.3.1"


@dataclass
class AltName:
    class Meta:
        name = "alt-name"
        namespace = "http://www.crossref.org/schema/5.3.1"

    name: List[Name] = field(
        default_factory=list,
        metadata={
            "type": "Element",
        }
    )
    string_name: List[StringName] = field(
        default_factory=list,
        metadata={
            "name": "string-name",
            "type": "Element",
        }
    )
