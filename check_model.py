import os
import sys
import joblib


def main():
    path = os.path.join("models", "performance_model.pkl")
    if not os.path.exists(path):
        print(f"Model file not found at {path}")
        sys.exit(1)
    try:
        model = joblib.load(path)
    except Exception as e:
        print(f"Failed to load model: {e}")
        sys.exit(1)
    if not hasattr(model, "predict"):
        print("Loaded object does not look like a model")
        sys.exit(1)
    print("Model check OK")


if __name__ == "__main__":
    main()
