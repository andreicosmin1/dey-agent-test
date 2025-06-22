# test_flow_data.py

from modules import flow_data

# Tokenul tău Unusual Whales
token = "TOKENUL_TAU"

score, message = flow_data.run(token)
print("Scor:", score)
print("Interpretare:", message)

