
if __name__ == '__main__':
    # 1. Train and save (do this once)
    df_train = pd.read_csv("train_data.csv")
    X_train = df_train.drop(columns=["target"]).to_numpy()
    y_train = df_train["target"].to_numpy()

    model = MyTrainedClassifier(n_estimators=50)
    model.fit(X_train, y_train)
    model.save("my_saved_model.pkl")  # Save trained model

    # 2. Later, load and predict (no retraining needed!)
    loaded_model = MyTrainedClassifier.load("my_saved_model.pkl")
    predictions = loaded_model.predict("competition-test.csv")
    print(predictions)