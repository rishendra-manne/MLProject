from setuptools import find_packages,setup
from setuptools.config.expand import find_packages

def get_requirements(file_path:str)->list[str]:
    '''this function returns the list of requirements'''
    req=[]
    with open(file_path) as file_obj:
        req=file_obj.readlines()
        req=[rq.replace("/n",' ') for rq in req]
        if '-e.' in req:
            req.remove('-e.')
    return req




setup(
    name='mlproject',
    version='0.0.1',
    author='rishi',
    author_email='rishe6@gmail.com',
    packages=find_packages(),
    install_requires=get_requirements('requirements.txt')

)