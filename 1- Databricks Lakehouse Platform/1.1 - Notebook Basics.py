# Databricks notebook source
print("Hello World!")


# COMMAND ----------

# MAGIC %md
# MAGIC ### %run: runs a Python file or a notebook.
# MAGIC ### %sh: executes shell commands on the cluster nodes.
# MAGIC ### %fs: allows you to interact with the Databricks file system.
# MAGIC ### %sql: allows you to run SQL queries.
# MAGIC ### %scala: switches the notebook context to Scala.
# MAGIC ### %python: switches the notebook context to Python.
# MAGIC ### %md: allows you to write markdown text.
# MAGIC ### %r: switches the notebook context to R.
# MAGIC ### %lsmagic: lists all the available magic commands.
# MAGIC ### %jobs: lists all the running jobs.
# MAGIC ### %config: allows you to set configuration options for the notebook.
# MAGIC ### %reload: reloads the contents of a module.
# MAGIC ### %pip: allows you to install Python packages.
# MAGIC ### %load: loads the contents of a file into a cell.
# MAGIC ### %matplotlib: sets up the matplotlib backend.
# MAGIC ### %who: lists all the variables in the current scope.
# MAGIC ### %env: allows you to set environment variables.

# COMMAND ----------

# MAGIC %sql 
# MAGIC SELECT "Hello world from SQL!"
# MAGIC
# MAGIC

# COMMAND ----------

# MAGIC %md
# MAGIC # Title 1
# MAGIC ## Title 2
# MAGIC ### Title 3
# MAGIC
# MAGIC text with a **bold** and *italicized* in it.
# MAGIC
# MAGIC Ordered list
# MAGIC 1. first
# MAGIC 1. second
# MAGIC 1. third
# MAGIC
# MAGIC Unordered list
# MAGIC * coffee
# MAGIC * tea
# MAGIC * milk
# MAGIC
# MAGIC
# MAGIC Images:
# MAGIC ![Associate-badge](https://www.databricks.com/wp-content/uploads/2022/04/associate-badge-eng.svg)
# MAGIC
# MAGIC And of course, tables:
# MAGIC
# MAGIC | user_id | user_name |
# MAGIC |---------|-----------|
# MAGIC |    1    |    Adam   |
# MAGIC |    2    |    Sarah  |
# MAGIC |    3    |    John   |
# MAGIC
# MAGIC Links (or Embedded HTML): <a href="https://docs.databricks.com/notebooks/notebooks-manage.html" target="_blank"> Managing Notebooks documentation</a>

# COMMAND ----------

# MAGIC %md
# MAGIC ### Running setup notebook through %run magic command
# MAGIC

# COMMAND ----------

# MAGIC
# MAGIC %run ../Includes/Setup

# COMMAND ----------

print(full_name)

# COMMAND ----------

# MAGIC %fs ls '/databricks-datasets/'

# COMMAND ----------

dbutils.help()

# COMMAND ----------

dbutils.fs.help()

# COMMAND ----------

files = dbutils.fs.ls('/databricks-datasets')
print(files)

# COMMAND ----------

display(files)

# COMMAND ----------


