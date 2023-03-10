import pandas as pd
from sklearn.neural_network import MLPClassifier
from sklearn.preprocessing import MinMaxScaler
from joblib import load

mlp: MLPClassifier = load('price_analizer.joblib')
transformer: MinMaxScaler = load("transformer.joblib")
while True:
    battery_power = float(input("Battery power: "))
    blue = float(input("Bluetooth [Y/n]: "))
    dual_sim = float(input("Dual SIM [Y/n]: "))
    four_g = float(input("Four G [Y/n]: "))
    int_memory = float(input("Internal memory: Giga Byte "))
    ram = float(input("RAM: Mega Byte "))
    talk_time = float(input("Talk Time: "))
    three_g = float(input("Three G [Y/n]: "))
    touch_screen = float(input("Touch Screen [Y/n]: "))
    wifi = float(input("WiFi [Y/n]: "))
    camera = float(input("Camera: "))
    phone = pd.DataFrame({"battery_power": [battery_power], "blue": [blue], 
    "dual_sim": [dual_sim], "four_g": [four_g], "int_memory": [int_memory], "ram": [ram], 
    "talk_time": [talk_time], "three_g": [three_g], "touch_screen": [touch_screen], 
    "wifi": [wifi], "camera": [camera]})
    
    normalized_phone = transformer.transform(phone)
    prediction = mlp.predict(normalized_phone)

    if prediction[0]==0:
        print("Your phone is in price range [200-350]€")
    elif prediction[0]==1:
        print("Your phone is in price range [351-500]€")
    elif prediction[0]==2:
        print("Your phone is in price range [501-650]€")
    else:
        print("Your phone is in price range [650-800]€")

        
