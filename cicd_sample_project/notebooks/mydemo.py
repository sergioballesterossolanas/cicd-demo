# Databricks notebook source
from cicd_sample_project.jobs.sample.entrypoint import SampleJob

# COMMAND ----------

job = SampleJob()

# COMMAND ----------

job.launch()
