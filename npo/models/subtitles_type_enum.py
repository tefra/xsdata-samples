from enum import Enum

__NAMESPACE__ = "urn:vpro:shared:2009"


class SubtitlesTypeEnum(Enum):
    """The type of a subtitles object.

    TODO these descriptions are provisional?
    """
    CAPTION = "CAPTION"
    TRANSLATION = "TRANSLATION"
    TRANSCRIPT = "TRANSCRIPT"


SubtitlesTypeEnum.CAPTION.__doc__ = (
    "The subtitles represent a textual version of what is spoken or wat is "
    "happening. They are expected to be in the same language as the video "
    "itself. Teletekst 888 subtitles are captions."
)
SubtitlesTypeEnum.TRANSLATION.__doc__ = (
    "The subtitles represent a translation. They are expected to be in a "
    "different language than the main language that can be heard"
)
SubtitlesTypeEnum.TRANSCRIPT.__doc__ = (
    "The subtitles represent a precise or automatic version of what is being "
    "said."
)
