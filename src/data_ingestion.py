import pandas as pd
import numpy as np
import os
df = pd.read_csv('https://raw.githubusercontent.com/araj2/customer-database/master/Ecommerce%20Customers.csv')
df = df.iloc[:, 3:]

df = df[df['Length of Membership'] > 3]
# Step 4: Save to CSV
file_path = os.path.join('data', 'customer.csv')
df.to_csv(file_path, index=False)
print(f"✅ Data saved to: {file_path}")
