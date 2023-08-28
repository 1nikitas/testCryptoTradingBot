from pathlib import Path
from pathlib import Path
from typing import Optional

import matplotlib.dates as mdates
import matplotlib.pyplot as plt
import pandas as pd

from Logger import Logger
from bot.dataclasses_ import CandlestickColumns
from .settings import RESAMPLING, AggregationSettings

logger = Logger(__name__)


class CSVAnalyzer:
    """Класс для анализа и обработки CSV файлов."""

    @staticmethod
    def _calculate_ema(data: pd.Series, periods: int) -> pd.Series:
        """Рассчитать экспоненциальное скользящее среднее."""
        sma = data[:periods].mean()
        ema_values = [float('nan')] * (periods - 1)
        multiplier = 2 / (periods + 1)
        for close in data[periods - 1:]:
            if pd.isna(ema_values[-1]):
                ema_prev = sma
            else:
                ema_prev = ema_values[-1]
            ema_current = (close - ema_prev) * multiplier + ema_prev
            ema_values.append(ema_current)
        return pd.Series(index=data.index, data=ema_values)

    @staticmethod
    def compute_candlesticks(df: pd.DataFrame) -> pd.DataFrame:
        """Вычисление свечей из данных."""
        candlesticks = df.resample(RESAMPLING.interval, on=RESAMPLING.column).agg(AggregationSettings)
        candlesticks.columns = [value for _, value in CandlestickColumns.__dict__.items() if not _.startswith("__")]
        return candlesticks

    @classmethod
    def process_csv(cls, file_path: str) -> Optional[plt.Figure]:
        """Обработать CSV файл и вернуть график."""
        file = Path(file_path)
        if not file.exists():
            logger.error(f"File doesn't exist: {file_path}")
            return

        df = pd.read_csv(file_path)
        df['TS'] = pd.to_datetime(df['TS'])
        candlesticks = cls.compute_candlesticks(df)
        ema_14 = cls._calculate_ema(candlesticks[CandlestickColumns.CLOSE], 14)
        candlesticks['EMA_14'] = ema_14

        return cls._generate_chart(candlesticks)

    @staticmethod
    def _generate_chart(data: pd.DataFrame) -> plt.Figure:
        """Создать график на основе данных."""
        subset = data.iloc[-100:]
        fig, ax = plt.subplots(figsize=(15, 7))
        ax.plot(subset.index, subset[CandlestickColumns.CLOSE], label='Цена закрытия', color='blue')
        ax.plot(subset.index, subset['EMA_14'], label='EMA 14', color='red')
        ax.set_title("График свечей с EMA")
        ax.set_ylabel("Цена")
        ax.legend()
        ax.xaxis.set_major_formatter(mdates.DateFormatter('%Y-%m-%d %H:%M'))
        plt.xticks(rotation=45)
        plt.grid(True)
        plt.tight_layout()
        return fig
