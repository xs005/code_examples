import asyncio

# Define your dictionary of models
models = {'a': model1, 'b': model2, 'c': model3}

# Define a coroutine to perform the prediction for a single input and model
async def predict(input_dict):
    key = input_dict['key']
    model = models[key]
    data = input_dict['data']
    prediction = await asyncio.to_thread(model.predict, data)
    return {key: prediction}

# Define a coroutine to perform the prediction process in parallel
async def predict_async(inputs):
    tasks = [asyncio.create_task(predict(input)) for input in inputs]
    results = await asyncio.gather(*tasks)
    return results

# Example usage
inputs = [{'key': 'a', 'data': input_data_1}, {'key': 'b', 'data': input_data_2}, {'key': 'c', 'data': input_data_3}]
loop = asyncio.get_event_loop()
predictions = loop.run_until_complete(predict_async(inputs))
