#!/usr/bin/env python3
"""Ringkasan CSV PresentMon untuk H-F-P UE5.4 benchmark."""

import csv
import statistics
import sys


def pct(values, percentile):
    if not values:
        return None
    values = sorted(values)
    rank = (len(values) - 1) * percentile
    lower = int(rank)
    upper = min(lower + 1, len(values) - 1)
    fraction = rank - lower
    return values[lower] * (1 - fraction) + values[upper] * fraction


def analyze(path):
    ms_values = []
    with open(path, newline="", encoding="utf-8-sig") as handle:
        reader = csv.DictReader(handle)
        candidates = [
            "FrameTime",
            "Frame Time",
            "msBetweenPresents",
        ]
        column = next((name for name in candidates if name in reader.fieldnames), None)
        if not column:
            raise RuntimeError("Kolom frame time PresentMon tidak ditemukan")

        for row in reader:
            try:
                value = float(row[column])
                if value > 0:
                    ms_values.append(value)
            except (TypeError, ValueError):
                pass

    if not ms_values:
        raise RuntimeError("Tidak ada frame-time data")

    average_ms = statistics.fmean(ms_values)
    variance = statistics.pvariance(ms_values)
    average_fps = 1000.0 / average_ms
    p99_ms = pct(ms_values, 0.99)

    print("H-F-P Frame Summary")
    print(f"samples={len(ms_values)}")
    print(f"average_ms={average_ms:.3f}")
    print(f"average_fps={average_fps:.2f}")
    print(f"p99_ms={p99_ms:.3f}")
    print(f"frame_time_variance={variance:.3f}")


if __name__ == "__main__":
    if len(sys.argv) != 2:
        print("Usage: python analyze_presentmon.py <presentmon.csv>")
        raise SystemExit(2)
    analyze(sys.argv[1])
