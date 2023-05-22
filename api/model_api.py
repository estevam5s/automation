import pickle
import numpy as np
import pandas as pd
from sklearn.linear_model import LinearRegression
from sklearn.metrics import mean_squared_error
from sklearn.model_selection import train_test_split
from fastapi import FastAPI
from pydantic import BaseModel

# Carregar dados do arquivo CSV
df = pd.read_csv('path_para_o_arquivo.csv')

# Pré-processamento dos dados
df = pd.get_dummies(df)
y = df['price']
X = df.drop(['price'], axis=1)

X_train, X_test, y_train, y_test = train_test_split(X, y)

# Treinar o modelo de regressão linear
model = LinearRegression()
model.fit(X_train, y_train)

# Métricas de avaliação do modelo
mse_train = mean_squared_error(y_train, model.predict(X_train))
mse_test = mean_squared_error(y_test, model.predict(X_test))
model_coefs = model.coef_

y_pred = model.predict(X_train)

# Salvar modelo em arquivo pickle
filename = 'model.pkl'
pickle.dump(model, open(filename, 'wb'))

# Inicialização do FastAPI
app = FastAPI()

# Carregar o modelo a partir do arquivo pickle
pickle_in = open("model.pkl", "rb")
model = pickle.load(pickle_in)


# 1. Método GET
@app.get("/predict")
async def root():
    return {"y": [1, 2, 3]}


# 2. Método POST com modelo base
class Item(BaseModel):
    size: int
    nb_rooms: int
    garden: int
    locations: str  # Est, Sud, Nord, Quest


@app.post("/prediction")
async def do_prediction(data: Item):
    pickle_encoder = open("ohe_orientation.pkl", "rb")
    encoder = pickle.load(pickle_encoder)
    arr = encoder.transform([[data.locations]])
    rem_arr = [[data.size, data.nb_rooms, data.garden]]
    user_input = np.concatenate((rem_arr, arr), axis=1)
    print(user_input.shape)
    prediction = model.predict(user_input)
    print(prediction)
    return (f"Bonjour, The price of your house is predicted to be Euro {prediction[0]:.2f} , Merci ! ")

# Executar o aplicativo FastAPI
if __name__ == "__main__":
    import uvicorn
    uvicorn.run(app, host="0.0.0.0", port=8000)
