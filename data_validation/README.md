## How to Run tests

```bash
pytest tests/ -vv --reference_artifact exercise_6/data_train.csv:latest --sample_artifact exercise_6/data_test.csv:latest --ks_alpha 0.05 -s
```