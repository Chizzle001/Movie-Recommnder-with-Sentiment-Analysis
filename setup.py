from setuptools import find_packages,setuptools
from typing import List



HYPEN_E_DOT="-e ."
def get_requirements(file_path:str)->List[str]:
    '''
    This Function will return the List of Requirements
    '''
    requirements = []
    with open(file_path) as file_obj:
        requirements = file_obj.readlines()
        requirements = [req.replace('\n','') for req in requirements]

        if HYPEN_E_DOT in requirements:
            requirements.remove(HYPEN_E_DOT)
            
            
    return requirements

setup(
    
    name = 'Movie-Recommender-System',
    version = '0.0.1',
    author = 'Chirag',
    author_email = 'chirag1346@gmail.com'
    packages = find_packages,
    install_requirements = get_requirements ('requirements.txt')
    

)