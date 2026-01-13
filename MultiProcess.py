import multiprocessing
import time

def square_number(n):
    return n * n

if __name__ == "__main__":
    # Large dataset
    data = list(range(1, 1_000_000))

    start = time.time()

    # Create a pool of worker processes
    with multiprocessing.Pool(processes=multiprocessing.cpu_count()) as pool:
        result = pool.map(square_number, data)

    end = time.time()

    print(f"First 10000 results: {result[:10000]}")
    print(f"Time taken: {end - start:.2f} seconds")
