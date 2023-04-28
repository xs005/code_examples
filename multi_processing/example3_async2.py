import asyncio

async def predict_async(key, input):
    model = models[key]
    processed_input = preprocess(input)
    result = await asyncio.to_thread(model.predict, processed_input)
    return result

async def predict_all_async(inputs):
    tasks = []
    for d in inputs:
        key, input = next(iter(d.items()))
        task = asyncio.create_task(predict_async(key, input))
        tasks.append(task)
    results = await asyncio.gather(*tasks)
    return dict(zip(inputs, results))

if __name__ == '__main__':
    inputs = [{'a': 'input1'}, {'b': 'input2'}, {'c': 'input3'}]
    results = asyncio.run(predict_all_async(inputs))
    print(results)
