import pandas as pd
import numpy as np
n = 100

data = pd.DataFrame({
    "fever": np.random.randint(0, 2, n),
    "diarrhea": np.random.randint(0, 2, n),
    "vomiting": np.random.randint(0, 2, n)
    
})

# simple rule to decide risk
data["risk"] = (
    data["fever"] +
    data["diarrhea"] +
    data["vomiting"]
   
)
data.to_csv("data/health_data.csv", index=False)

print("Health data created")
