from dataclasses import dataclass

from Logger import Logger
from bot.enums import TimeIntervals

logger = Logger(__name__)

@dataclass
class ResamplingSettings:
    interval: str
    column: str


RESAMPLING = ResamplingSettings(
    interval=TimeIntervals.FIVE_MINUTES.value,
    column='TS'
)

AggregationSettings = {
    'PRICE': ['first', 'max', 'min', 'last']
}
