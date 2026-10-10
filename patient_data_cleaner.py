import pandas as pd

data = pd.read_csv("patient_data.csv")

print(data.head(5))
print(data.tail(5))
print(data.shape)
data.info()

missing_counts = data.isna().sum()
missing_percentage = (missing_counts / len(data) * 100)
missing_before = missing_counts.sum()
print(missing_counts)
print(missing_percentage)
print(missing_before)

median_age = data["Age"].median()
data["Age"] = data["Age"].fillna(median_age)
print(median_age)
print(data["Age"].isna().sum())

median_blood_pressure = data["Blood_Pressure"].median()
data["Blood_Pressure"] = data["Blood_Pressure"].fillna(median_blood_pressure)
print(median_blood_pressure)
print(data["Blood_Pressure"].isna().sum())

median_glucose = data["Glucose"].median()
data["Glucose"] = data["Glucose"].fillna(median_glucose)
print(median_glucose)
print(data["Glucose"].isna().sum())

median_bmi = data["BMI"].median()
data["BMI"] = data["BMI"].fillna(median_bmi)
print(median_bmi)
print(data["BMI"].isna().sum())

median_cholesterol = data["Cholesterol"].median()
data["Cholesterol"] = data["Cholesterol"].fillna(median_cholesterol)
print(median_cholesterol)
print(data["Cholesterol"].isna().sum())

print(data.isna().sum())

mode_gender = data["Gender"].mode().iloc[0]
data["Gender"] = data["Gender"].fillna(mode_gender)
print(mode_gender)
print(data.isna().sum())


missing_after = data.isna().sum().sum()
print(missing_before)
print(missing_after)
print(data.shape)

data.to_csv("patient_data_cleaned.csv", index=False)
cleaned_data = pd.read_csv("patient_data_cleaned.csv")
print(cleaned_data.shape)
print(cleaned_data.isna().sum().sum())

total_records = len(data)
rows_removed = total_records - len(data)

if missing_after == 0:
    cleaning_status = "No missing values remaining"
else:
    cleaning_status = "Missing values remain"

report = {
    "Total_Records": total_records,
    "Missing_Values_Before": int(missing_before),
    "Missing_Values_After": int(missing_after),
    "Rows_Removed": rows_removed,
    "Cleaning_Status": cleaning_status
}

for key, value in report.items():
    print(f"{key}: {value}")