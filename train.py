# scikit-learn==1.7.0 xgboost==3.1.1
import pickle
import pyreadr
import pandas as pd
import numpy as np
from sklearn.model_selection import train_test_split
from sklearn.feature_extraction import DictVectorizer
import xgboost as xgb
import os

os.chdir(os.path.dirname(os.path.abspath(__file__)))

df = pd.DataFrame(list(pyreadr.read_r('thiomon.rda').values())[0])
df = df.fillna(0)
df.columns = df.columns.str.lower().str.replace(' ', '_')
df.replace(' ', '', regex=True, inplace=True)

df_full_train, df_test = train_test_split(df, test_size=0.2, random_state=1)
y_full_train = df_full_train.days_of_life / 365
y_test = df_test.days_of_life / 365

for i in [df_full_train, df_test]:
    i.drop(columns=['days_of_life', 'active', 'remission'], inplace=True)

dv = DictVectorizer(sparse=True)
X_full_train = dv.fit_transform(df_full_train.to_dict(orient='records'))
X_test = dv.transform(df_test.to_dict(orient='records'))

dv = DictVectorizer(sparse=True)
X_full_train = dv.fit_transform(df_full_train.to_dict(orient='records'))
X_test = dv.transform(df_test.to_dict(orient='records'))

model = xgb.XGBRegressor(
    n_estimators=200,
    reg_lambda=0.1,
    reg_alpha=0.1,
    min_child_weight=7,
    max_depth=8,
    learning_rate=0.05,
    gamma=0.5,
    colsample_bytree=0.6
)

model.fit(X_full_train, y_full_train)

y_pred_test = model.predict(X_test)
print("Final RMSE:", np.sqrt(((y_pred_test - y_test)**2).mean()))

with open('model.pkl', 'wb') as f_out:
    pickle.dump((dv, model), f_out)

print('Model saved...')