import fileinput
import json
import subprocess
from concurrent.futures import ThreadPoolExecutor
import os
import shutil

def create_project(path,name,domain,description):
    command = f'flutter create "{path+'/'+name}" --org={domain} --project-name={name} --platforms=android --description="{description}"'
   
    subprocess.run(command,shell=True)


def add_permission_to_manifest(manifest_path):
    with fileinput.FileInput(manifest_path, inplace=True) as file:
        for line in file:
            if('<uses-permission android:name="android.permission.INTERNET"/>' in line):
                continue
            else:
                print(line, end='')
            if '<manifest xmlns:android="http://schemas.android.com/apk/res/android">' in line:
                print('    <uses-permission android:name="android.permission.INTERNET"/>')

def generate_icon_folders(icon_path,project_path):
    icon_genrate_path = project_path+"\\dummy"
    run_command(icon_path,icon_genrate_path)

    source_path = icon_genrate_path+"\\android"
    destination_path = project_path+"\\android\\app\\src\\main\\res"
    move_files(source_path, destination_path)

def move_files(source_path, destination_path):
    # Walk through all files and subdirectories in the source path
    for root, dirs, files in os.walk(source_path):
        for file in files:
            source_file_path = os.path.join(root, file)
            
            # Calculate the relative path of the file to the source_path
            relative_path = os.path.relpath(source_file_path, source_path)
            
            # Construct the destination path for the file
            destination_file_path = os.path.join(destination_path, relative_path)
            
            # Make sure the destination directory exists, create if not
            os.makedirs(os.path.dirname(destination_file_path), exist_ok=True)
            
            # Move the file to the destination path
            shutil.move(source_file_path, destination_file_path)

def run_command(icon_path, folder_path):
    command = f'python ./app_icon_genrator.py "{icon_path}" "{folder_path}"'
    print("FOLDER PATH :"+command)
    subprocess.run(command, shell=True)



def move_files(source_path, destination_path):
    # Walk through all files and subdirectories in the source path
    for root, dirs, files in os.walk(source_path):
        for file in files:
            source_file_path = os.path.join(root, file)
            
            # Calculate the relative path of the file to the source_path
            relative_path = os.path.relpath(source_file_path, source_path)
            
            # Construct the destination path for the file
            destination_file_path = os.path.join(destination_path, relative_path)
            
            # Make sure the destination directory exists, create if not
            os.makedirs(os.path.dirname(destination_file_path), exist_ok=True)
            
            # Move the file to the destination path
            shutil.move(source_file_path, destination_file_path)



def update_key_properties(key_properties_path,storePassword=12345678,keyPassword=12345678,storeFile ='C:\\Users\\PMLS\\upload-keystore.jks' ):
    if('\\\\' not in storeFile and '\\' in storeFile ):
        storeFile=storeFile.replace('\\','\\\\')
    if('/' in storeFile):
        storeFile = storeFile.replace('/','\\\\')

    # Replace or add the key properties in key.properties file
    new_properties = f"""
    storePassword={storePassword}
    keyPassword={keyPassword}
    keyAlias=upload
    storeFile={storeFile}
    """
    with open(key_properties_path, 'w') as file:
        file.write(new_properties)

class ConfigChecker:
    def __init__(self, value,exist_value,area_entry, area_exit, is_entered = False,is_exist = False, can_add = True):
        self.value = value
        self.exist_value = exist_value
        self.area_entry = area_entry
        self.area_exit = area_exit
        self.is_entered = is_entered
        self.is_exist = is_exist
        self.can_add = can_add
        self.toReplace = None

    def excecute(self,line):
        if(self.can_add is False):
            return False
        if(self.is_entered is False and  self.area_entry in line):
            self.is_entered = True
            print(line,end='')
            return True
        elif (self.is_entered and self.exist_value in line ):
            self.can_add = False
            print(line,end='')
            return True
        elif (self.is_entered and self.area_exit in line):
            if(self.is_exist is False):
                print(self.value)
            self.can_add = False
            print(line,end='')
            return True
        else :
            return False




def update_build_gradle(build_gradle_path):
    key_properites_value = '''
def keystoreProperties = new Properties()
def keystorePropertiesFile = rootProject.file('key.properties')
if (keystorePropertiesFile.exists()) {
    keystoreProperties.load(new FileInputStream(keystorePropertiesFile))
}
'''
    signing_values = '''
    signingConfigs {
       release {
           keyAlias keystoreProperties['keyAlias']
           keyPassword keystoreProperties['keyPassword']
           storeFile keystoreProperties['storeFile'] ? file(keystoreProperties['storeFile']) : null
           storePassword keystoreProperties['storePassword']
       }
   }'''


    keyProperites = ConfigChecker(  value=key_properites_value,
                                    area_entry='###########',
                                    area_exit='android {',
                                    exist_value='def keystoreProperties = new Properties()',
                                    is_entered=True,
                                    )
    multiDex = ConfigChecker(value='        multiDexEnabled true',
                            area_entry='defaultConfig {',
                            area_exit='}',
                            exist_value= 'multiDexEnabled true'
                            )
    signing = ConfigChecker(value=signing_values,
                            area_entry='android',
                            area_exit='buildTypes {',
                            exist_value='signingConfigs {',
                            is_entered=True,                            
                            )

    with fileinput.FileInput(build_gradle_path, inplace=True) as file:
        for line in file:
            if multiDex.excecute(line):
                continue
            if keyProperites.excecute(line):
                continue
            if signing.excecute(line):
                continue
            if('signingConfig signingConfigs.debug' in line):
                print('           signingConfig signingConfigs.release')
            else:
                print(line, end='')

def build(path):
    import subprocess

def build_flutter_project(project_path):
    # Change to the project directory
    os.chdir(project_path)

    # Run 'flutter clean'
    subprocess.run('flutter clean', shell=True)

    # Run 'flutter pub get'
    subprocess.run('flutter pub get', shell=True)

    # Run 'flutter build apk'
    subprocess.run('flutter build apk', shell=True)

# Example usage

def create_app(path,name,domain,imgPath,url,description):
    project_path = path+'/'+name
    manifest_path = project_path+'/android/app/src/main/AndroidManifest.xml'
    key_path = project_path+'/android/key.properties'
    build_gradle_path = project_path+'/android/app/build.gradle'

    create_project(path=path,name=name,domain=domain,description=description)
    add_permission_to_manifest(manifest_path)
    update_key_properties(key_path)
    update_build_gradle(build_gradle_path)
    generate_icon_folders(imgPath,project_path=path)

    build_flutter_project(project_path) 



# Example usage
path = "C:/Users/PMLS/Desktop/memnnus pk/projects/Ecommerce"
name = 'test1'
domain = 'com.menuspk.test1'
description = 'HI GOOD CODE'
imgPath = path+'/footcap'+'/1.png'
url = ''

create_app(path,name,domain,description,imgPath,url)





