import os
import joblib


def test_model_file_exists_and_loads():
    path = os.path.join("models", "performance_model.pkl")
    assert os.path.exists(path), f"Model file not found at {path}"
    model = joblib.load(path)
    # basic sanity: model should have predict method
    assert hasattr(model, "predict"), "Loaded object does not look like a model"
