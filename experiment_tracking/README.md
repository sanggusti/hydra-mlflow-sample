# How to run this Project

See this projects on this [link](https://wandb.ai/gustiwinata/exercise_11)
See the model deployed on this [link](https://wandb.ai/gustiwinata/exercise_12/artifacts/model_export/model_export/587af97d2ae82823fd63)

Experiment 1 For config of `max_depth` on `config.yaml`

```bash
> mlflow run . \
  -P hydra_options="random_forest_pipeline.random_forest.max_depth=5"
```

Experiment 2 For config of `n_estimators` on `config.yaml`

```bash
> mlflow run . \
  -P hydra_options="random_forest_pipeline.random_forest.n_estimators=10"
```

Experiment 3 Sweep multiple parameters

```bash
> mlflow run . \
  -P hydra_options="-m random_forest_pipeline.random_forest.max_depth=1,5,10"
```

Experiment 4 Sweep multiple parameters using range

```bash
> mlflow run . \
  -P hydra_options="-m random_forest_pipeline.random_forest.max_depth=range(1,10,2)"
```

Experiment 5 Sweep multiple parameters Parallels using Joblib

```bash
> mlflow run . \
  -P hydra_options="-m random_forest_pipeline.random_forest.max_depth=range(10,50,3) random_forest_pipeline.tfidf.max_features=range(50,200,50) hydra/launcher=joblib"
```

Exporting model

```bash
> cd export_model
> mlflow run . -P test_data="exercise_6/data_test.csv:latest" -P model_export="exercise_12/model_export:latest" 
```