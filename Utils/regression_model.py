from Utils.smoker import Smoker
from Utils.region import Region
from Utils.sex import Sex
import tensorflow as tf
import pandas as pd

class RegressionModel:
    def predict(self, dataset: pd.DataFrame) -> pd.DataFrame:
        model = self.__getModel()
        dataset = self.__handleDataset(dataset)
        predictions = model.predict(dataset)

        return predictions

    def train(self) -> None:
        train_dataset, train_labels, test_dataset, test_labels = self.__getTrainDataset()
        model = self.__createModel(train_dataset)

        model.fit(train_dataset, train_labels, epochs=2000)

        results = model.evaluate(test_dataset, test_labels, batch_size=128)
        print("test loss, test acc:", results)

        model.save('cache/models/model.keras')

    def __getTrainDataset(self) -> pd.DataFrame:
        dataset = pd.read_csv('cache/data/insurance.csv')
        dataset = self.__handleDataset(dataset)

        train_dataset = dataset.sample(frac=0.8, random_state=0)
        train_labels = train_dataset.pop('expenses')

        test_dataset = dataset.drop(train_dataset.index)
        test_labels = test_dataset.pop('expenses')

        return train_dataset, train_labels, test_dataset, test_labels

    def __handleDataset(self, dataset: pd.DataFrame) -> pd.DataFrame:
        dataset['sex'] = dataset['sex'].apply(Sex.encode)
        dataset['smoker'] = dataset['smoker'].apply(Smoker.encode)
        dataset['region'] = dataset['region'].apply(Region.encode)

        return dataset

    def __createModel(self, train_dataset) -> tf.keras.Model:

        model = tf.keras.Sequential([
            tf.keras.layers.Dense(64, activation='relu', input_shape=[
                                  len(train_dataset.keys())]),
            tf.keras.layers.Dense(64, activation='relu'),
            tf.keras.layers.Dense(1)
        ])
        model.compile(loss='mean_absolute_error', optimizer='adam', metrics=[
                      'mean_absolute_error', 'mean_squared_error'])

        return model

    def __getModel(self) -> tf.keras.Model:
        return tf.keras.models.load_model('cache/models/model.keras')
