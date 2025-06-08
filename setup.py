from setuptools import find_packages,setup
from typing import List

def get_requirments()->List[str]:
    requirment_lst:List[str]=[]

    try:
        with open("requirement.txt","r") as file:
            lines=file.readlines()
            for line in lines:
                requirment=line.strip()
                if requirment and requirment!="-e .":
                    requirment_lst.append(requirment)
    except FileNotFoundError:
        print("requirement.txt file is not found")

    return requirment_lst


print(get_requirments())

setup(
    name="Networksecurity",
    version="0.0.1",
    author="Likith",
    author_email="deadpool98763@gmail.com",
    packages=find_packages(),
    install_requires=get_requirments()

)

