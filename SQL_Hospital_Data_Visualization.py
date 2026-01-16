import psycopg2 
print(psycopg2.__libpq_version__)
connection = psycopg2.connect(user = "postgres",
                              password = "itmm1315@VZU",
                              host = "localhost",
                              port = "5432",
                              database = "hospital")
cursor = connection.cursor()
cursor.execute("select * from hospital_data")
result = cursor.fetchall()
#print(result)
cursor.close()

import pandas as pd 
df = pd.read_sql_query("select * from hospital_data", connection)
#print(df.describe())

import matplotlib.pyplot as plt
font1 = {'family': 'Times New Roman', 'color': 'blue', 'size': 12}
font2 = {'family': 'Times New Roman', 'color': 'black', 'size': 14}
font3 = {'family': 'Times New Roman', 'color': 'Red', 'size': 16}
## Bar Charts

department_medicalexpenses = df.groupby('department')['medical_expenses'].sum().round(2)
department_medicalexpenses.plot(kind = "bar")
plt.title("Departmental Total Medical Expenses", fontdict=font3)
plt.xlabel("Department", fontdict= font2)
plt.ylabel("Total Medical Expenses", fontdict= font2)
plt.show()
location_medicalexpenses = df.groupby('location')['medical_expenses'].sum().round(2)
location_medicalexpenses.plot(kind = "bar", title= "Location-wise Total Medical Expenses")
plt.show()
hospitalname_medicalexpenses = df.groupby("hospital_name")['medical_expenses'].sum().round(2)
hospitalname_medicalexpenses.plot(kind= "bar", title= "Hospital-Name Verus Medical Expenses")
plt.show()
patientsperdoctors_department = (
    df.groupby('department')['patient_count'].sum()/df.groupby('department')
    ['doctors_count'].sum()).round(2)
patientsperdoctors_department.plot(kind= 'bar', title= 'Patients per Doctor in Each Department')
plt.show()


##Scatter plots

patient_department = df.groupby('department')['patient_count'].sum().round(2)
expenses_department = df.groupby('department')['medical_expenses'].sum().round(2)
plt.figure(figsize=(10,6))
plt.scatter(patient_department,expenses_department, s=100 )
plt.title('Number of Patients vs Total Medical Expenses (Department-Wise)')
plt.xlabel('Number of Patients')
plt.ylabel('Total Medical Expenses')
plt.legend(bbox_to_anchor=(1.05,1))
plt.tight_layout()
plt.show()

## Bar Charts using seaborn

import seaborn as sns
sns.barplot(data=df, x = 'department', y= 'medical_expenses')
plt.xlabel("Department", fontdict=font2)
plt.ylabel("Medical Expenses", fontdict=font2)
plt.title("Medical Expenses at Each Department", fontdict=font3)
plt.show()
sns.barplot(data=df, x ='location', y ='medical_expenses')
plt.title("Medical Expenses at Each Locations")
plt.show()
sns.barplot(data=df, x='hospital_name', y='medical_expenses')
plt.title("Medical Expenses at Each Hospital")
plt.show()

##Scatter plots using Seaborn
sns.scatterplot(data=df, x='location', y='medical_expenses', hue='department')
plt.xlabel("Location", fontdict=font2)
plt.ylabel("Medical Expense", fontdict=font2)
plt.title("Medical Expenses Vs Location", fontdict=font3)
plt.show()
sns.scatterplot(data=df, x='location', y='medical_expenses', hue='department', size='doctors_count')
plt.title("Medical Expenses at Each Locations (Number of Doctors)")
plt.show()
sns.scatterplot(data=df, x='location', y='medical_expenses', hue='department', size='patient_count')
plt.title("Medical Expenses at Each Locations (Number of Patient)")
plt.show()

##Boxplot

sns.boxplot(data=df, x='department', y='medical_expenses')
plt.xticks(rotation=45)
plt.show()


##Heatmap
sns.heatmap(df.select_dtypes('number').corr(), annot=True, cmap='coolwarm')
plt.title('Correlation')
plt.show()

##pairplots

sns.pairplot(df[['doctors_count', 'patient_count', 'medical_expenses', 'department']], 
             hue='department')
plt.suptitle('Pairplot: Doctors, Patients, Expenses (by Department)', y=1.02)
plt.show()



