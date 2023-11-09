import os
import sys
import json
import requests

__author__ = 'b0br0ff'
__license__ = 'Free'
__version__ = '1.0.0'
__maintainer__ = 'https://github.com/b0br0ff/'
__status__ = 'Production'


#DRYRUN_FILE = 'packages.json'
DRYRUN_FILE = ''
DOWNLOAD_FOLDER = 'pkgs'
ANACONDA_PYTHON_VERSION = '3.9.13'
PACKAGE_NAME = 'pyspark'
DOWNLOAD_FILE = PACKAGE_NAME +'-install.bash'
SEP = '/'



def prepare_dirs(subpath1, subpath2):
    if os.path.exists(DOWNLOAD_FOLDER) == False:
        os.mkdir(DOWNLOAD_FOLDER)

    if os.path.exists(subpath1) == False:
        os.mkdir(subpath1)

    if os.path.exists(subpath2) == False:
        os.mkdir(subpath2)


def download_package(download_package_path, out_file, pkg_name, url1, url2=''):
    print('Downloading package file  : {}'.format(pkg_name))

    response = requests.get(url1, allow_redirects=True)
    if response.status_code == requests.codes.ok:
        print('URL1 = ' +  url1)
        out_file.write('#' + url1 + os.linesep)
        out_file.write('conda install --offline ' + pkg_name + '.tar.bz2' + os.linesep)

        with open(download_package_path + SEP + pkg_name + '.tar.bz2', 'wb') as dlfile:
            dlfile.write(response.content)
            return True

    else:
        response = requests.get(url2, allow_redirects=True)
        if response.status_code == requests.codes.ok:
            print('URL2 = ' +  url2)
            out_file.write('#' + url2 + os.linesep)
            out_file.write('conda install --offline ' + pkg_name + '.conda' + os.linesep)

            with open(download_package_path + SEP + pkg_name + '.conda', 'wb') as dlfile:
                dlfile.write(response.content)
                return True
            
    print('Falied to download package {}'.format(pkg_name))
    out_file.write('Falied to download package {}'.format(pkg_name) + os.linesep)
    return False


# C:/Users/de000110/AppData/Local/Programs/Python/Python310/python.exe c:/Projects/Python/anaconda_packages_downloader/get_packages.py "3.9.13" pyspark pyspark_pkgs.json
def main():
    if len(sys.argv) != 4:
        print('Usage: {} <PYTHON_VERSION> <PACKAGE_NAME> <DRY_RUN_JSON>'.format(sys.argv[0]))
        exit(1)

    print ('Number of arguments:', len(sys.argv), 'arguments.')
    print ('Argument List:', str(sys.argv))
    #Number of arguments: 4 arguments.
    #Argument List: ['c:/Projects/Python/anaconda_packages_downloader/get_packages.py', '3.9.13', 'pyspark', 'pyspark.json']
    
    ANACONDA_PYTHON_VERSION = sys.argv[1]
    PACKAGE_NAME = sys.argv[2]
    DRYRUN_FILE = sys.argv[3]
    DOWNLOAD_FILE = PACKAGE_NAME +'-install.bash'

    subpath1_list = [DOWNLOAD_FOLDER, ANACONDA_PYTHON_VERSION]
    subpath2_list = [DOWNLOAD_FOLDER, ANACONDA_PYTHON_VERSION, PACKAGE_NAME]
    download_subpath = SEP.join(subpath1_list)
    download_package_path = SEP.join(subpath2_list)
    
    prepare_dirs(download_subpath, download_package_path)

    # Open result file
    res_file = open(download_package_path + SEP + DOWNLOAD_FILE, "w")

    # Opening JSON file
    f = open(DRYRUN_FILE)
    
    # returns JSON object as # a dictionary
    data = json.load(f)

    # Iterating through the json list
    for i in data['actions']['LINK']:
        #print(i)
        path_items=[i["base_url"], i["platform"], i["dist_name"]]
        pkg_url1 = SEP.join(path_items) + '.tar.bz2'
        pkg_url2 = SEP.join(path_items) + '.conda'

        download_package(download_package_path, res_file, i["dist_name"], pkg_url1, pkg_url2)
    
    # Closing file
    f.close()
    res_file.close()


if __name__ == "__main__":
    main()
