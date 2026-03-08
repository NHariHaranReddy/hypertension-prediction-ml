# -*- coding: utf-8 -*-


# **DATA COLLECTION**

---
"""

#importing required libraries
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import seaborn as sns

#loading the datset
data = pd.read_csv("hypertension_data.csv")

#previewing the dataset
data.head()

#size of the dataset
data.shape

#dataset info
data.info()

"""# **DATA PREPARATION**

---

**1. Handling Missing Values**
"""

#checking for missing values
data.isnull().sum()

"""**2. Data Type Correction**"""

#Checking column name
data.columns

#Renaming the column
data.rename(columns={'C':'Gender'}, inplace = True)

#Verification
data.columns

"""**3. Inconsistency Corrections**"""

#checking unqiue values
categorical_cols = [
'Gender','History','Patient','TakeMedication','Severity',
'BreathShortness','VisualChanges','NoseBleeding',
'Whendiagnoused','ControlledDiet','Stages'
]

for col in categorical_cols:
    print(col, ":", data[col].unique())

#remove extra spaces
for col in categorical_cols:
    data[col] = data[col].astype(str).str.strip()

#fix severity spelling
data['Severity'] = data['Severity'].replace('Sever','Severe')

#fix stage labels
data['Stages'] = data['Stages'].replace({
'HYPERTENSION (Stage-2).':'HYPERTENSION (Stage-2)',
'HYPERTENSIVE CRISI':'HYPERTENSIVE CRISIS'
})

#verification
for col in categorical_cols:
    print(col, ":", data[col].unique())

"""**4. Duplicate Removal**"""

#removing duplicates
data.shape

#no. of duplicated row
data.duplicated().sum()

#removing duplicated row
data = data.drop_duplicates()

#verification
data.shape

"""#**CATEGORIAL DATA ENCODING**

---

**1. Defining Features**
"""

#Defining Nominal Features
nominal_features = ['Gender','History','Patient','TakeMedication',
'BreathShortness','VisualChanges','NoseBleeding',
'ControlledDiet']

#Defining Odinal Features
ordinal_features = ['Age','Severity','Whendiagnoused','Systolic','Diastolic']

#Defining Target Featue
target_feature = ['Stages']

"""**2. Encoding Features**"""

#Encoding Binary Features
for col in nominal_features:
    if set(data[col].unique()) == set(['Yes','No']):
        data[col] = data[col].map({'No':0,'Yes':1})

#Encoding Genders
data['Gender'] = data['Gender'].map({'Male':0,'Female':1})

#Encoding Age Groups
data['Age'] = data['Age'].map({'18-34':1,'35-50':2,'51-64':3,'65+':4})

#Encoding Severity
data['Severity'] = data['Severity'].replace({'Mild':0,'Moderate':1,'Severe':2})

#Encoding Diagnosis Time
data['Whendiagnoused'] = data['Whendiagnoused'].map({'<1 Year':1,'1 - 5 Years':2,'>5 Years':3})

#Encoding Blood Pressure
data['Systolic'] = data['Systolic'].map({'100 - 110':0,'111 - 120':1,'121 - 130':2,'130+':3})

data['Diastolic'] = data['Diastolic'].map({'70 - 80':0,'81 - 90':1,'91 - 100':2,'100+':3})

#Encoding Target Variable
data['Stages'] = data['Stages'].map({'NORMAL':0,'HYPERTENSION (Stage-1)':1,'HYPERTENSION (Stage-2)':2,'HYPERTENSIVE CRISIS':3})

"""**3. Aplying and Verfying**"""

#Applying Feature Scaling
from sklearn.preprocessing import MinMaxScaler

scaler = MinMaxScaler()
ordinal_features = ['Age','Severity','Whendiagnoused','Systolic','Diastolic']

data[ordinal_features] = scaler.fit_transform(data[ordinal_features])

#Verification
data.head()
data.dtypes

"""#**Exploratory Data Analysis**

---

**1. Gender Distribution**
"""

plt.figure(figsize=(8,4))
sns.countplot(data=data, x="Gender", palette="Set2")
plt.title("Gender Distribution")
plt.show()

# Pie chart
data['Gender'].value_counts().plot.pie(
    autopct='%1.1f%%',
    figsize=(5,5),
    colors=['#66b3ff', '#99ff99']
)

plt.title("Gender Distribution (Pie Chart)")
plt.ylabel("")
plt.show()

"""**2. Hypertension Stages Distribution**"""

plt.figure(figsize=(8,4))

sns.countplot(data=data, x="Stages", palette="coolwarm")

plt.title("Hypertension Stages Distribution")

plt.xticks(rotation=30)

plt.show()

"""**3. Correlation between Systolic and Diastolic Pressure**"""

def range_to_midpoint(val):

    if isinstance(val, str):
        if "-" in val:
            start, end = val.split("-")
            return (int(start.strip()) + int(end.strip())) / 2

        elif "+" in val:
            return int(val.replace("+","").strip())

    return np.nan

data['Systolic_num'] = data['Systolic'].apply(range_to_midpoint)
data['Diastolic_num'] = data['Diastolic'].apply(range_to_midpoint)

plt.figure(figsize=(6,4))

sns.heatmap(
    data[['Systolic_num','Diastolic_num']].corr(),
    annot=True,
    cmap="Blues"
)

plt.title("Correlation between Systolic & Diastolic")

plt.show()

"""**4. TakeMedication vs. Severity**"""

plt.figure(figsize=(8,5))

sns.countplot(
    data=data,
    x="TakeMedication",
    hue="Severity",
    palette="Set1"
)

plt.title("TakeMedication vs Severity")

plt.show()

"""**5. Age Group vs. Hypertension Stages**"""

plt.figure(figsize=(8,5))

sns.countplot(
    data=data,
    x="Age",
    hue="Stages",
    palette="husl"
)

plt.title("Age Group vs Hypertension Stages")

plt.show()

"""**6. Pairplot: Systolic vs. Diastolic across Stages**"""

# Convert BP ranges to numeric midpoint

def range_to_midpoint(val):
    try:
        if isinstance(val, str) and "-" in val:
            start, end = val.split("-")
            return (int(start.strip()) + int(end.strip())) / 2
        elif isinstance(val, str) and "+" in val:
            return int(val.replace("+","").strip())
        else:
            return float(val)
    except:
        return np.nan

data['Systolic_num'] = data['Systolic'].apply(range_to_midpoint)
data['Diastolic_num'] = data['Diastolic'].apply(range_to_midpoint)

# Remove rows with NaN before plotting
pair_data = data[['Systolic_num','Diastolic_num','Stages']].dropna()

sns.pairplot(pair_data, hue="Stages", diag_kind="kde", palette="husl")

plt.suptitle("Pairplot: Systolic vs Diastolic across Stages", y=1.02)

plt.show()

"""#**DATA SPLITTING**

---


"""

#importing Train Test Split
from sklearn.model_selection import train_test_split

#seperating features and target
X = data.drop('Stages', axis=1)
y = data['Stages']

#performing train/test split
X_train , X_test, y_train, y_test = train_test_split(X,y,test_size=0.2, random_state=42, stratify=y)

from sklearn.impute import SimpleImputer

imputer = SimpleImputer(strategy='mean')

X_train = imputer.fit_transform(X_train)
X_test = imputer.transform(X_test)

#Verifying Split
print("Training samples:", X_train.shape[0])
print("Testing samples:", X_test.shape[0])

"""# **Algorithm Implementation and Comparison**

---


"""

#importing libraries
from sklearn.linear_model import LogisticRegression, RidgeClassifier
from sklearn.tree import DecisionTreeClassifier
from sklearn.ensemble import RandomForestClassifier
from sklearn.svm import SVC
from sklearn.neighbors import KNeighborsClassifier
from sklearn.naive_bayes import GaussianNB

from sklearn.metrics import accuracy_score, classification_report, confusion_matrix

#accuracy dictionary
accuracy = {}

"""**1. Logistic Regression**"""

from sklearn.impute import SimpleImputer
from sklearn.linear_model import LogisticRegression
from sklearn.metrics import accuracy_score, classification_report, confusion_matrix

# Fix NaN values without changing dataset structure
imputer = SimpleImputer(strategy='mean')

X_train_clean = imputer.fit_transform(X_train)
X_test_clean = imputer.transform(X_test)

log_reg = LogisticRegression(max_iter=1000)

log_reg.fit(X_train_clean, y_train)

y_pred = log_reg.predict(X_test_clean)

print("Logistic Regression:")
print("Accuracy:", accuracy_score(y_test, y_pred))
print("Classification Report:\n", classification_report(y_test, y_pred))
print("Confusion Matrix:\n", confusion_matrix(y_test, y_pred))

accuracy['Logistic Regression'] = accuracy_score(y_test, y_pred)

"""**2. Decision Tree**"""

decisionTree = DecisionTreeClassifier()

decisionTree.fit(X_train, y_train)

y_pred = decisionTree.predict(X_test)

print("Decision Tree:")
print("Accuracy:", accuracy_score(y_test, y_pred))
print("Classification Report:\n", classification_report(y_test, y_pred))
print("Confusion Matrix:\n", confusion_matrix(y_test, y_pred))

accuracy['Decision Tree'] = accuracy_score(y_test, y_pred)

"""**3. Random Forest**"""

randomforest = RandomForestClassifier()

randomforest.fit(X_train, y_train)

y_pred = randomforest.predict(X_test)

print("Random Forest:")
print("Accuracy:", accuracy_score(y_test, y_pred))
print("Classification Report:\n", classification_report(y_test, y_pred))
print("Confusion Matrix:\n", confusion_matrix(y_test, y_pred))

accuracy['Random Forest'] = accuracy_score(y_test, y_pred)

"""**4. Support Vector Machine (SVM)**"""

svm = SVC()

svm.fit(X_train, y_train)

y_pred = svm.predict(X_test)

print("SVM:")

print("Accuracy:", accuracy_score(y_test, y_pred))

print("Classification Report:\n", classification_report(y_test, y_pred))

print("Confusion Matrix:\n", confusion_matrix(y_test, y_pred))

accuracy['SVM'] = accuracy_score(y_test, y_pred)

"""**5. K-Nearest Neighbors (KNN)**"""

knn = KNeighborsClassifier(n_neighbors=5)

knn.fit(X_train, y_train)

y_pred = knn.predict(X_test)

print("KNN:")
print("Accuracy:", accuracy_score(y_test, y_pred))
print("Classification Report:\n", classification_report(y_test, y_pred))
print("Confusion Matrix:\n", confusion_matrix(y_test, y_pred))

accuracy['KNN'] = accuracy_score(y_test, y_pred)

"""**6. Ridge Classifier**"""

RC = RidgeClassifier()

RC.fit(X_train, y_train)

y_pred = RC.predict(X_test)

print("RidgeClassifier:")
print("Accuracy:", accuracy_score(y_test, y_pred))
print("Classification Report:\n", classification_report(y_test, y_pred))
print("Confusion Matrix:\n", confusion_matrix(y_test, y_pred))

accuracy['RidgeClassifier'] = accuracy_score(y_test, y_pred)

"""**7. Gaussian Naive Bayes (Selected Model)**"""

naive_bayes = GaussianNB()

naive_bayes.fit(X_train, y_train)

y_pred = naive_bayes.predict(X_test)

print("Naive Bayes:")
print("Accuracy:", accuracy_score(y_test, y_pred))
print("Classification Report:\n", classification_report(y_test, y_pred))
print("Confusion Matrix:\n", confusion_matrix(y_test, y_pred))

accuracy['Naive Bayes'] = accuracy_score(y_test, y_pred)

"""#**MODEL COMPARISION TABLE**"""

accuracy_df = pd.DataFrame(list(accuracy.items()), columns=['Model','Accuracy'])

accuracy_df = accuracy_df.sort_values(by='Accuracy', ascending=False)

accuracy_df

accuracy_df["Generalization Assessment"] = [
"Overfitted",
"Overfitted",
"Overfitted",
"Good",
"Excellent",
"Good",
"Good"
]

accuracy_df["Selection Status"] = [
"Rejected",
"Rejected",
"Rejected",
"Considered",
"Selected",
"Considered",
"Considered"
]

accuracy_df

#computing testing and taining accuracy for logistic regression
from sklearn.metrics import accuracy_score

train_pred_lr = log_reg.predict(X_train)
test_pred_lr = log_reg.predict(X_test)

train_acc_lr = accuracy_score(y_train, train_pred_lr)
test_acc_lr = accuracy_score(y_test, test_pred_lr)

print("Logistic Regression Training Accuracy:", train_acc_lr)
print("Logistic Regression Testing Accuracy:", test_acc_lr)

#computing testing and training accuracy for overfitted decision tree
train_pred_dt = decisionTree.predict(X_train)
test_pred_dt = decisionTree.predict(X_test)

train_acc_dt = accuracy_score(y_train, train_pred_dt)
test_acc_dt = accuracy_score(y_test, test_pred_dt)

print("Decision Tree Training Accuracy:", train_acc_dt)
print("Decision Tree Testing Accuracy:", test_acc_dt)

from sklearn.metrics import classification_report

print(classification_report(y_test, log_reg.predict(X_test)))

from sklearn.metrics import confusion_matrix
import seaborn as sns
import matplotlib.pyplot as plt

cm = confusion_matrix(y_test, log_reg.predict(X_test))

sns.heatmap(cm, annot=True, fmt='d', cmap='Blues')
plt.xlabel("Predicted")
plt.ylabel("Actual")
plt.title("Confusion Matrix - Logistic Regression")

plt.show()

plt.savefig("confusion_matrix.png", bbox_inches="tight")
plt.savefig("model_accuracy.png", bbox_inches="tight")

"""#**Model Persistence**

---


"""

import joblib

#saving trained model

joblib.dump(log_reg, "logreg_model.pkl")
print("Model saved as logreg_model.pkl")
