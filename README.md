# Why it is needed for?
Sometime you need to setup Anaconda3 environment on a server that does not have Internet connection or you cannot do download-only due to the error below. In this case you need to use this script.

```
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
(base) [anaconda@sandbox pyspark]$ ll
total 252740
-rw-r----- 1 anaconda anaconda   1033810 Apr 10  2023 abseil-cpp-20210324.2-h9c3ff4c_0.tar.bz2
-rw-r----- 1 anaconda anaconda  24338428 Apr 10  2023 arrow-cpp-5.0.0-py39h247a7eb_8_cpu.tar.bz2
-rw-r----- 1 anaconda anaconda     37458 Apr 10  2023 aws-c-cal-0.5.11-h95a6274_0.tar.bz2
-rw-r----- 1 anaconda anaconda    171606 Apr 10  2023 aws-c-common-0.6.2-h7f98852_0.tar.bz2
-rw-r----- 1 anaconda anaconda     47766 Apr 10  2023 aws-c-event-stream-0.2.7-h3541f99_13.tar.bz2
-rw-r----- 1 anaconda anaconda    124127 Apr 10  2023 aws-c-io-0.10.5-hfb6a706_0.tar.bz2
-rw-r----- 1 anaconda anaconda     51209 Apr 10  2023 aws-checksums-0.1.11-ha31a3da_7.tar.bz2
-rw-r----- 1 anaconda anaconda   4773329 Apr 10  2023 aws-sdk-cpp-1.8.186-hb4091e7_3.tar.bz2
-rw-r----- 1 anaconda anaconda    986033 Apr 10  2023 conda-22.9.0-py39hf3d152e_2.tar.bz2
-rw-r----- 1 anaconda anaconda    116549 Apr 10  2023 gflags-2.2.2-he1b5a44_1004.tar.bz2
-rw-r----- 1 anaconda anaconda    106887 Apr 10  2023 glog-0.5.0-h48cff8f_0.tar.bz2
-rw-r----- 1 anaconda anaconda   3815220 Apr 10  2023 grpc-cpp-1.40.0-h05f19cf_1.tar.bz2
-rw-r----- 1 anaconda anaconda   2692535 Apr 10  2023 libprotobuf-3.18.0-h780b84a_1.tar.bz2
-rw-r----- 1 anaconda anaconda   3851957 Apr 10  2023 libthrift-0.15.0-hcc01f38_0.tar.bz2
-rw-r----- 1 anaconda anaconda     99885 Apr 10  2023 libutf8proc-2.7.0-h7f98852_0.tar.bz2
-rw-r----- 1 anaconda anaconda   1141818 Apr 10  2023 orc-1.7.0-h68e2c4e_0.tar.bz2
-rw-r----- 1 anaconda anaconda      3118 Apr 10  2023 parquet-cpp-1.5.1-2.tar.bz2
-rw-r----- 1 anaconda anaconda    183423 Apr 10  2023 py4j-0.10.9-pyh9f0ad1d_0.tar.bz2
-rw-r----- 1 anaconda anaconda   2971505 Apr 10  2023 pyarrow-5.0.0-py39h3ebc44c_8_cpu.tar.bz2
-rw-r----- 1 anaconda anaconda 211526103 Apr 10  2023 pyspark-3.1.1-pyh44b312d_0.tar.bz2
-rw-r----- 1 anaconda anaconda      3134 Apr 10  2023 pyspark-install.bash
-rw-r----- 1 anaconda anaconda      4017 Apr 10  2023 python_abi-3.9-2_cp39.tar.bz2
-rw-r----- 1 anaconda anaconda    225947 Apr 10  2023 re2-2021.09.01-h9c3ff4c_0.tar.bz2
-rw-r----- 1 anaconda anaconda    452368 Apr 10  2023 s2n-1.0.10-h9b69904_0.tar.bz2
```

### Installation
In the given example for the pyspark script produces bash file that contains conda commands for installation: pkgs/3.9.13/pyspark/pyspark-installation.bash

```
less pkgs/3.9.13/pyspark/pyspark-installation.bash

# Copy & paste commands to terminal
conda install --offline abseil-cpp-20210324.2-h9c3ff4c_0.tar.bz2
# Or execute the script
bash pkgs/3.9.13/pyspark/pyspark-installation.bash
```

