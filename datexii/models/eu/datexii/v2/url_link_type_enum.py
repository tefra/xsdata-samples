from enum import Enum

__NAMESPACE__ = "http://datex2.eu/schema/2/2_0"


class UrlLinkTypeEnum(Enum):
    """
    Types of URL links.

    :cvar DOCUMENT_PDF: URL link to a pdf document.
    :cvar HTML: URL link to an html page.
    :cvar IMAGE: URL link to an image.
    :cvar RSS: URL link to an RSS feed.
    :cvar VIDEO_STREAM: URL link to a video stream.
    :cvar VOICE_STREAM: URL link to a voice stream.
    :cvar OTHER: Other than as defined in this enumeration.
    """

    DOCUMENT_PDF = "documentPdf"
    HTML = "html"
    IMAGE = "image"
    RSS = "rss"
    VIDEO_STREAM = "videoStream"
    VOICE_STREAM = "voiceStream"
    OTHER = "other"
