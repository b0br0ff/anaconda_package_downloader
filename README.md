# Why it is needed for?
Sometime you need to setup Anaconda3 environment on a server that does not have Internet connection or you cannot do download-only due to the error below. In this case you need to use this script.

```
conda install --download-only -c conda-forge pyspark=3.1.1 -y
....
Downloading and Extracting Packages
CondaExitZero: Package caches prepared. UnlinkLinkTransaction cancelled with --download-only option.
```

# General steps
- Perform dry run and get list of packages for download (output as JSON);
- Using JSON file obtained on previous step download packages;

## Detailed steps

### Prepare environment
Folder where scrip resides must contain 
```
ls -al 


```

### Do dry run for a specific package, for instance pyspark
```
conda install --dry-run --channel conda-forge pyspark=3.1.1 --json > pyspark_pkgs.json
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
