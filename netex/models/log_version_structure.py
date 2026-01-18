from dataclasses import dataclass, field
from typing import Optional

from .group_of_entities_version_structure import (
    GroupOfEntitiesVersionStructure,
)
from .log_entries_rel_structure import LogEntriesRelStructure

__NAMESPACE__ = "http://www.netex.org.uk/netex"


@dataclass
class LogVersionStructure(GroupOfEntitiesVersionStructure):
    class Meta:
        name = "Log_VersionStructure"

    log_entries: LogEntriesRelStructure | None = field(
        default=None,
        metadata={
            "name": "logEntries",
            "type": "Element",
            "namespace": "http://www.netex.org.uk/netex",
        },
    )
    name_of_log_entry_class: str | None = field(
        default=None,
        metadata={
            "name": "nameOfLogEntryClass",
            "type": "Attribute",
        },
    )
