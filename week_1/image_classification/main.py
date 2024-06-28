import argparse
import pickle
import os, torch, torchvision
import pandas as pd
import numpy as np
import pylab as plt

from haven import haven_utils as hu


def trainval(exp_dict, savedir, args):
    """
    exp_dict: dictionary defining the hyperparameters of the experiment
    savedir: the directory where the experiment will be saved
    args: arguments passed through the command line
    """
    # Create savedir
    hu.save_json(os.path.join(savedir, "exp_dict.json"), exp_dict)
    print("\nHyperparameters: ")
    print(exp_dict)
    print("================\n")

    result_savedir = os.path.join(savedir, "results.json")

    # (TODO) Step 0 : Check if the experiment has already been run
    if False:
        print("Experiment already exists. Skipping...")

    # (TODO) Step 1: Get train_loader for the MNIST dataset
    # Load the MNIST dataset and create a DataLoader for it
    dataset = None
    train_loader = None

    # (TODO) Step 2: Create Linear Model and Optimizer
    # Define a simple linear model and an Adam optimizer
    model = None
    opt = None
    # Step 3: Train for K Epochs
    for epoch in range(1):
        # (TODO) Step 3.1: Train on train_loader with optimizer and model
        # Iterate over the DataLoader and perform forward and backward passes
        train_dict = []
        for batch in train_loader:
            # Get Images
            X = None

            # Get labels
            y = None

            # Forward pass
            out = None
            loss = None

            # Backpropagate
            None

        # (TODO) Step 3.2: Print Loss every epoch
        print(None)

    # (TODO) Step 4: Evaluate - Get Average Loss and Accuracy on Train Loader
    # Evaluate the model on the training data and calculate average loss and accuracy
    for batch in train_loader:
        # Get Images
        X = None

        # Get labels
        y = None

        # Forward pass
        out = None
        loss = None

        # Get scores for one iteration
        acc = None
        train_dict += [{"loss": None}]

    # (TODO) Get avg scores for one epoch
    # Calculate average loss and accuracy for the epoch
    train_dict_avg = None

    # Step 5: Get Metrics
    result_dict = exp_dict.copy()

    # (TODO) Step 5.1: Include loss and acc into result_dict
    # Add the average loss and accuracy to the result dictionary
    result_dict["loss"] = None
    result_dict["acc"] = None

    # Step 6: Save Results
    hu.save_json(result_savedir, result_dict)
    print(result_dict)

    print("Experiment Completed.\n")

    return result_dict


if __name__ == "__main__":
    # Specify arguments regarding save directory
    parser = argparse.ArgumentParser()
    parser.add_argument(
        "-e",
        "--exp_group",
        required=True,
        help="Define the experiment group to run.",
    )
    parser.add_argument(
        "-sb",
        "--savedir_base",
        default="results/",
        help="Define the base directory where the experiments will be saved.",
    )
    parser.add_argument(
        "-r", "--reset", default=0, type=int, help="Reset or resume the experiment."
    )

    args, others = parser.parse_known_args()
    savedir_base = os.path.join(args.savedir_base, args.exp_group)

    # Define a list of experiments
    if args.exp_group == "image_classifier":
        exp_list = []
        for lr in [1e-3, 1e-4]:
            exp_list += [{"lr": lr, "dataset": "mnist", "model": "linear"}]

    # Initialize result list
    result_list = []

    # Run experiments and create results file
    for exp_dict in exp_list:
        # Get savedir
        savedir = os.path.join(savedir_base, hu.hash_dict(exp_dict))

        # Get results
        result_dict = trainval(exp_dict, savedir, args)

        # Append results to result list
        result_list += [result_dict]

    # (TODO) Step 7: Get DataFrame for the results and save as .csv
    # Convert the result list to a DataFrame and save as a CSV file
    result_df = None
    print(f"Results saved as {os.path.join(savedir_base, 'results.csv')}")

    # (TODO) Step 8: Bar plot the results and save as jpg between "lr" and "acc"
    # Create a bar plot for the results and save as a JPG file
    result_df.plot.bar
    print(f"Bar Plot Saved as {os.path.join(savedir_base, 'results.jpg')}")
