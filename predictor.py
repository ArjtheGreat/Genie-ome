def make_prediction(model, input_features):
    print(input_features)
    if len(input_features.shape) == 1:
        input_features = input_features.reshape(1, -1)
    return model.predict(input_features)
