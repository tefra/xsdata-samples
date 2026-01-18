from __future__ import annotations

from dataclasses import dataclass, field

from .group_of_entities_version_structure import (
    GroupOfEntitiesVersionStructure,
)
from .log_entries_rel_structure import LogEntriesRelStructure

__NAMESPACE__ = "http://www.netex.org.uk/netex"


@dataclass(kw_only=True)
class LogVersionStructure(GroupOfEntitiesVersionStructure):
    class Meta:
        name = "Log_VersionStructure"

    log_entries: None | LogEntriesRelStructure = field(
        default=None,
        metadata={
            "name": "logEntries",
            "type": "Element",
            "namespace": "http://www.netex.org.uk/netex",
        },
    )
    name_of_log_entry_class: None | str = field(
        default=None,
        metadata={
            "name": "nameOfLogEntryClass",
            "type": "Attribute",
        },
    )
