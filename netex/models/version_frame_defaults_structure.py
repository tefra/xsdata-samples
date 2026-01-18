from __future__ import annotations

from dataclasses import dataclass, field

from .codespace_ref_structure import CodespaceRefStructure
from .data_source_ref_structure import DataSourceRefStructure
from .locale_structure import LocaleStructure
from .responsibility_set_ref_structure import ResponsibilitySetRefStructure
from .system_of_units import SystemOfUnits

__NAMESPACE__ = "http://www.netex.org.uk/netex"


@dataclass
class VersionFrameDefaultsStructure:
    default_codespace_ref: CodespaceRefStructure | None = field(
        default=None,
        metadata={
            "name": "DefaultCodespaceRef",
            "type": "Element",
            "namespace": "http://www.netex.org.uk/netex",
        },
    )
    default_data_source_ref: DataSourceRefStructure | None = field(
        default=None,
        metadata={
            "name": "DefaultDataSourceRef",
            "type": "Element",
            "namespace": "http://www.netex.org.uk/netex",
        },
    )
    default_responsibility_set_ref: ResponsibilitySetRefStructure | None = (
        field(
            default=None,
            metadata={
                "name": "DefaultResponsibilitySetRef",
                "type": "Element",
                "namespace": "http://www.netex.org.uk/netex",
            },
        )
    )
    default_locale: LocaleStructure | None = field(
        default=None,
        metadata={
            "name": "DefaultLocale",
            "type": "Element",
            "namespace": "http://www.netex.org.uk/netex",
        },
    )
    default_location_system: str | None = field(
        default=None,
        metadata={
            "name": "DefaultLocationSystem",
            "type": "Element",
            "namespace": "http://www.netex.org.uk/netex",
        },
    )
    default_system_of_units: SystemOfUnits | None = field(
        default=None,
        metadata={
            "name": "DefaultSystemOfUnits",
            "type": "Element",
            "namespace": "http://www.netex.org.uk/netex",
        },
    )
    default_currency: str | None = field(
        default=None,
        metadata={
            "name": "DefaultCurrency",
            "type": "Element",
            "namespace": "http://www.netex.org.uk/netex",
            "min_length": 3,
            "max_length": 3,
            "pattern": r"[A-Z][A-Z][A-Z]",
        },
    )
