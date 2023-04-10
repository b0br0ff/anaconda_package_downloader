# Why it is needed for?
Sometime you need to setup Anaconda3 environment on a server that does not have Internet connection or you cannot do download-only due to the error below. In this case you need to use this script.

....
Downloading and Extracting Packages
CondaExitZero: Package caches prepared. UnlinkLinkTransaction cancelled with --download-only option.
```
# Test environment
- Windows 10, Python 3.10
- Anaconda 3 2022.10

# General steps
- Perform dry run and get list of packages for download (output as JSON);
- Using JSON file obtained on previous step download packages;
- Copy download packages to the offline server and install

## Detailed steps
### Do dry run for a specific package, for instance pyspark
```
conda install --dry-run --channel conda-forge pyspark=3.1.1 --json > pyspark_pkgs.json
conda install --dry-run --channel conda-forge jupyterhub --json > jupyterhub_pkgs.json
conda install --dry-run --channel conda-forge sparkmagic --json > sparkmagic_pkgs.json
conda install --dry-run --channel conda-forge jupyterhub-idle-culler --json > jupyterhub-idle-culler_pkgs.json
conda install --dry-run --channel conda-forge sudospawner --json > sudospawner_pkgs.json
conda install --dry-run --channel conda-forge elasticsearch --json > elasticsearch_pkgs.json
conda install --dry-run --channel conda-forge elasticsearch-dsl --json > elasticsearch-dsl_pkgs.json
conda install --dry-run --channel conda-forge eland --json > eland_pkgs.json
conda install --dry-run --channel conda-forge apscheduler --json > apscheduler_pkgs.json
conda install --dry-run --channel conda-forge xgboost --json > xgboost_pkgs.json
conda install --dry-run --channel conda-forge pingouin --json > pingouin_pkgs.json
conda install --dry-run --channel conda-forge lightgbm --json > lightgbm_pkgs.json
conda install --dry-run --channel conda-forge tpot-imblearn --json > tpot-imblearn_pkgs.json
conda install --dry-run --channel conda-forge pytorch --json > pytorch_pkgs.json
```

### Download packages
```
# Win
python.exe get_packages.py 3.9.13 pyspark pyspark_pkgs.json
# Centos
python get_packages.py 3.9.13 pyspark pyspark_pkgs.json
```

### Verify downloaded files
```
ls -al pkgs/3.9.13/pyspark
```


