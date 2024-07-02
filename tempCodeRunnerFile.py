scaler = StandardScaler()
scaler.fit(X)
standardized_data = scaler.transform(X)

print(standardized_data)
