from dataclasses import dataclass
from netex.models.no_info_for_topic_error_structure import NoInfoForTopicErrorStructure

__NAMESPACE__ = "http://www.siri.org.uk/siri"


@dataclass
class NoInfoForTopicError(NoInfoForTopicErrorStructure):
    class Meta:
        namespace = "http://www.siri.org.uk/siri"
