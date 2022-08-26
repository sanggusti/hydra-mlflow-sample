## How to run this code

```bash
mlflow run . -P input_artifact="exercise_4/genres_mod.parquet:latest" -P artifact_name="preprocessed_data.csv" -P artifact_type="clean_data" -P artifact_description="Data after preprocessing"
```