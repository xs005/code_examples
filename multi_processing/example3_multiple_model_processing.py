import multiprocessing

# Define your dictionary of models
models = {'a': model1, 'b': model2, 'c': model3}

# Define a function to perform the prediction for a single input and model
def predict(input_dict):
    key = input_dict['key']
    model = models[key]
    data = input_dict['data']
    prediction = model.predict(data)
    return {key: prediction}

# Define a function to perform the prediction process in parallel
def predict_parallel(inputs):
    with multiprocessing.Pool() as pool:
        results = pool.map(predict, inputs)
    return results

# Example usage
inputs = [{'key': 'a', 'data': input_data_1}, {'key': 'b', 'data': input_data_2}, {'key': 'c', 'data': input_data_3}]
predictions = predict_parallel(inputs)
