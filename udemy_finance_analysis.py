# udemy_finance_analysis.py
# -----------------------------------------
# 📊 Udemy Finance & Accounting Course Analysis
# -----------------------------------------

import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns
from sklearn.preprocessing import MinMaxScaler
import os

# -----------------------------------------
# 1️⃣ Load Dataset
# -----------------------------------------
data = pd.read_csv("Finance_Accounting_Courses.csv")

print("\n✅ Data Loaded Successfully!")
print(data.head())

# -----------------------------------------
# 2️⃣ Basic Information
# -----------------------------------------
print("\n📄 Dataset Info:")
print(data.info())

print("\n📊 Missing Values:")
print(data.isnull().sum())

# -----------------------------------------
# 3️⃣ Data Cleaning
# -----------------------------------------
data.dropna(inplace=True)
data.drop_duplicates(inplace=True)

# Remove currency symbols and commas from price/enrollment columns
for col in ["price", "num_subscribers", "num_reviews", "num_lectures"]:
    if col in data.columns:
        data[col] = data[col].astype(str).str.replace(',', '').str.replace('$', '').astype(float)

# -----------------------------------------
# 4️⃣ Normalization (if needed)
# -----------------------------------------
scaler = MinMaxScaler()
if "num_subscribers" in data.columns and "num_reviews" in data.columns:
    data[["num_subscribers", "num_reviews"]] = scaler.fit_transform(
        data[["num_subscribers", "num_reviews"]]
    )

# -----------------------------------------
# 5️⃣ Visualizations Folder
# -----------------------------------------
os.makedirs("graphs", exist_ok=True)

# -----------------------------------------
# 6️⃣ Visualizations
# -----------------------------------------

# 🔹 Average Price by Level
if "level" in data.columns and "price" in data.columns:
    plt.figure(figsize=(6, 4))
    sns.barplot(x="level", y="price", data=data, palette="coolwarm")
    plt.title("Average Course Price by Level")
    plt.tight_layout()
    plt.savefig("graphs/1_avg_price_by_level.png")
    plt.close()

# 🔹 Subscribers vs Reviews
if "num_subscribers" in data.columns and "num_reviews" in data.columns:
    plt.figure(figsize=(6, 4))
    sns.scatterplot(x="num_subscribers", y="num_reviews", data=data, alpha=0.6)
    plt.title("Subscribers vs Reviews")
    plt.tight_layout()
    plt.savefig("graphs/2_subscribers_vs_reviews.png")
    plt.close()

# 🔹 Top 10 Courses by Subscribers
if "course_title" in data.columns and "num_subscribers" in data.columns:
    top_courses = data.sort_values("num_subscribers", ascending=False).head(10)
    plt.figure(figsize=(6, 4))
    sns.barplot(y="course_title", x="num_subscribers", data=top_courses, palette="Blues_r")
    plt.title("Top 10 Courses by Subscribers")
    plt.tight_layout()
    plt.savefig("graphs/3_top10_courses.png")
    plt.close()

# 🔹 Course Distribution by Subject
if "subject" in data.columns:
    plt.figure(figsize=(6, 4))
    data["subject"].value_counts().plot(kind="pie", autopct="%1.1f%%", startangle=90, colors=sns.color_palette("pastel"))
    plt.title("Course Distribution by Subject")
    plt.tight_layout()
    plt.savefig("graphs/4_subject_distribution.png")
    plt.close()

# -----------------------------------------
# 7️⃣ Summary Insights
# -----------------------------------------
print("\n📈 Summary Insights:")
if "price" in data.columns:
    print(f"💰 Average Price: ${data['price'].mean():.2f}")
if "num_subscribers" in data.columns:
    print(f"👥 Average Subscribers: {data['num_subscribers'].mean():.2f}")
if "num_reviews" in data.columns:
    print(f"⭐ Average Reviews: {data['num_reviews'].mean():.2f}")

print("\n✅ Graphs saved in 'graphs' folder.")
print("✅ Udemy Finance & Accounting Course Analysis Completed Successfully.")