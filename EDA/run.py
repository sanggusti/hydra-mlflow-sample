#!/usr/bin/env python
import argparse
import logging
import pandas as pd
import wandb

import os


logging.basicConfig(level=logging.INFO, format="%(asctime)-15s %(message)s")
logger = logging.getLogger()


def go(args):

    run = wandb.init(project="exercise_5", job_type="process_data")

    ## YOUR CODE HERE
    logger.info(msg="Loading Artifact")
    artifact = run.use_artifact(args.input_artifact)
    artifact_path = artifact.file()

    logger.info(msg="Reading Dataframe")
    df = pd.read_parquet(artifact_path)

    logger.info(msg="Drop Duplicate")
    df = df.drop_duplicates().reset_index(drop=True)
    
    logger.info(msg="Fixing missing values")
    df['title'].fillna(value='', inplace=True)
    df['song_name'].fillna(value='', inplace=True)
    df['text_feature'] = df['title'] + ' ' + df['song_name']

    filename = f"{args.artifact_name}"
    df.to_csv(filename)

    artifact = wandb.Artifact(
        name = args.artifact_name,
        type = args.artifact_type,
        description = args.artifact_description
    )

    artifact.add_file(filename)
    logger.info(msg="Logging Artifact")
    run.log_artifact(artifact)
    os.remove(filename)
    


if __name__ == "__main__":
    parser = argparse.ArgumentParser(
        description="Preprocess a dataset",
        fromfile_prefix_chars="@",
    )

    parser.add_argument(
        "--input_artifact",
        type=str,
        help="Fully-qualified name for the input artifact",
        required=True,
    )

    parser.add_argument(
        "--artifact_name", type=str, help="Name for the artifact", required=True
    )

    parser.add_argument(
        "--artifact_type", type=str, help="Type for the artifact", required=True
    )

    parser.add_argument(
        "--artifact_description",
        type=str,
        help="Description for the artifact",
        required=True,
    )

    args = parser.parse_args()

    go(args)
