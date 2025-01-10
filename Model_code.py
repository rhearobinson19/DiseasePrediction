import pandas as pd
import numpy as np

# Define diseases and symptoms
diseases = [f'Disease_{i+1}' for i in range(41)]
symptoms = [f'Symptom_{i+1}' for i in range(17)]

# Generate synthetic data
np.random.seed(42)
data = {
    **{symptom: np.random.randint(0, 2, 4940) for symptom in symptoms},  # Random 0/1 for symptoms
    'disease': np.random.choice(diseases, 4940)  # Random disease assignment
}

# Create DataFrame
df = pd.DataFrame(data)

# Save to CSV
df.to_csv('disease_data.csv', index=False)

print("Dataset created and saved as 'disease_data.csv'.")
