# Fabric notebook source

# METADATA ********************

# META {
# META   "kernel_info": {
# META     "name": "synapse_pyspark"
# META   },
# META   "dependencies": {
# META     "lakehouse": {
# META       "default_lakehouse": "6ae86e31-a073-479e-bf88-33d878b1f50e",
# META       "default_lakehouse_name": "lh_01",
# META       "default_lakehouse_workspace_id": "919a2254-27c7-46cd-8ab2-d83819170937",
# META       "known_lakehouses": [
# META         {
# META           "id": "6ae86e31-a073-479e-bf88-33d878b1f50e"
# META         }
# META       ]
# META     }
# META   }
# META }

# CELL ********************

# Welcome to your new notebook
# Type here in the cell editor to add code!


# METADATA ********************

# META {
# META   "language": "python",
# META   "language_group": "synapse_pyspark"
# META }

# CELL ********************

df = spark.read.format("csv").option("header","true").load("Files/Fire_Incidents_20260408.csv")
# df now is a Spark DataFrame containing CSV data from "Files/Fire_Incidents_20260408.csv".
display(df)

# METADATA ********************

# META {
# META   "language": "python",
# META   "language_group": "synapse_pyspark"
# META }

# CELL ********************

df.columns

from pyspark.sql import functions as F

# Replace spaces with underscores in all column names
df_new = df.select([F.col(x).alias(x.replace(' ', '_').lower()) for x in df.columns])

display(df_new)


# METADATA ********************

# META {
# META   "language": "python",
# META   "language_group": "synapse_pyspark"
# META }

# CELL ********************

# Create new column names by formatting each original column string
new_column_names = [col.replace(" ", "_").lower() for col in df.columns]

# Apply the new list of column names back to the DataFrame
df = df.toDF(*new_column_names)
df.write.format("delta").saveAsTable("fire_incidence")

# METADATA ********************

# META {
# META   "language": "python",
# META   "language_group": "synapse_pyspark"
# META }

# CELL ********************

# MAGIC %%sql
# MAGIC 
# MAGIC select * from fire_incidence

# METADATA ********************

# META {
# META   "language": "sparksql",
# META   "language_group": "synapse_pyspark"
# META }
