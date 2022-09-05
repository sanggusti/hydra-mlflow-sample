## How to Run tests


Via shell pytest
```bash
pytest tests/ -vv --reference_artifact exercise_6/data_train.csv:latest --sample_artifact exercise_6/data_test.csv:latest --ks_alpha 0.05 -s
```

Via MLFlow
```bash
mlflow run . -P reference_artifact="exercise_6/data_train.csv:latest" -P sample_artifact="exercise_6/data_test.csv:latest" -P ks_alpha=0.05
```