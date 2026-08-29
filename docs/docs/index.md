# ECON138-Final-Paper documentation!

## Description

This is a Repo for Business Forecasting, all code and document included.

## Commands

The Makefile contains the central entry points for common tasks related to this project.

### Syncing data to cloud storage

* `make sync_data_up` will use `aws s3 sync` to recursively sync files in `data/` up to `s3://econ-138-business-forecasting-128425593746-us-east-2-an/data/`.
* `make sync_data_down` will use `aws s3 sync` to recursively sync files from `s3://econ-138-business-forecasting-128425593746-us-east-2-an/data/` to `data/`.


