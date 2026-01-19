import time
import pandas as pd

from stats_engine import compute_statistics
from visualization import analyze_distribution
from normalizer import apply_normalization


def benchmark(func, *args):
    start = time.perf_counter()
    func(*args)
    end = time.perf_counter()
    return end - start


def run_benchmarks():
    # Load dataset once
    df = pd.read_csv("sales.csv")
    numeric_cols = ["Amount", "Discount", "Quantity_Sold"]

    timings = {}

    timings["stats_engine"] = benchmark(
        compute_statistics, df, numeric_cols
    )

    timings["visualization"] = benchmark(
        analyze_distribution, df, numeric_cols
    )

    timings["normalizer"] = benchmark(
        apply_normalization, df, numeric_cols
    )

    print("\nExecution Time Report")
    print("-" * 35)
    for module, t in timings.items():
        print(f"{module:<25} : {t:.6f} sec")


if __name__ == "__main__":
    run_benchmarks()
