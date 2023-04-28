import datetime
import multiprocessing
import random
import time


def predict(input_str):
    # Generate a random number based on the current time and a random value
    print(f'input is {input_str}')
    time.sleep(1)
    rand_seed = int(time.time()) + random.randint(0, 100)
    random.seed(rand_seed)
    return random.randint(1, 10) * len(input_str)


def compute_string_lengths(inputs):
    pool = multiprocessing.Pool()
    results = {}
    for input_str in inputs:
        result = pool.apply_async(predict, args=(input_str,))
        results[input_str] = result
    pool.close()
    pool.join()
    return {k: v.get() for k, v in results.items()}


if __name__ == '__main__':
    start_time = datetime.datetime.now()
    inputs = ['fooddddd', 'bar', 'baz', 'qux']
    result = compute_string_lengths(inputs)
    print(result)
    print(datetime.datetime.now() - start_time)
