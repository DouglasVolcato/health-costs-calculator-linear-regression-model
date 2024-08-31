from Utils.regression_model import RegressionModel
import pandas as pd

model = RegressionModel()

dataset = pd.DataFrame([[18, 'female', 31.9, 0, 'no', 'northeast']], columns=['age', 'sex', 'bmi', 'children', 'smoker', 'region'])
print(f'result = {model.predict(dataset)} // should be 2205.98')

dataset = pd.DataFrame([[50, 'male', 31.0, 3, 'no', 'northwest']], columns=['age', 'sex', 'bmi', 'children', 'smoker', 'region'])
print(f'result = {model.predict(dataset)} // should be 10600.55')