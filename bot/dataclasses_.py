from dataclasses import dataclass

from decouple import config


@dataclass
class Config:
    """Конфигурационные параметры."""
    TOKEN: str = config('TOKEN')


@dataclass
class CandlestickColumns:
    """Колонки для свечей."""
    OPEN: str = 'Open'
    HIGH: str = 'High'
    LOW: str = 'Low'
    CLOSE: str = 'Close'
