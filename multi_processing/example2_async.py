import asyncio
import datetime
import random
import time


async def predict(input_str):
    # Generate a random number based on the current time and a random value
    print(f'input is {input_str}')
    await asyncio.sleep(1)
    rand_seed = int(time.time()) + random.randint(0, 100)
    random.seed(rand_seed)
    return random.randint(1, 10) * len(input_str)


async def compute_string_lengths(inputs):
    tasks = [asyncio.create_task(predict(input_str)) for input_str in inputs]
    results = await asyncio.gather(*tasks)
    return {k: v for k, v in zip(inputs, results)}


if __name__ == '__main__':
    start_time = datetime.datetime.now()
    inputs = ['foo', 'bar', 'baz', 'qux']
    result = asyncio.run(compute_string_lengths(inputs))
    print(result)
    print(datetime.datetime.now() - start_time)
