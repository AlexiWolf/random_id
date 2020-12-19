#  Copyright (C) 2020  AlexiWolf
#
#  This file is part of random_id.
#
#  random_id is free software: you can redistribute it and/or modify
#  it under the terms of the GNU General Public License as published by
#  the Free Software Foundation, either version 3 of the License, or
#  (at your option) any later version.
#
#  random_id is distributed in the hope that it will be useful,
#  but WITHOUT ANY WARRANTY; without even the implied warranty of
#  MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the
#  GNU General Public License for more details.
#
#  You should have received a copy of the GNU General Public License
#  along with random_id.  If not, see <https://www.gnu.org/licenses/>.

from setuptools import setup, find_packages

from random_id import __version__ as package_version

test_requirements = ["tox", "pytest"]

setup(
    author="AlexiWolf",
    author_email="alexiwolf@pm.me",
    url="https://github.com/AlexiWolf/random_id",
    python_requires=">=3.5",
    description="A simple, flexible random ID generator.",
    name="random_id",
    packages=find_packages(include=["random_id", "random_id.*"]),
    tests_require=test_requirements,
    version=package_version,
    classifiers=[
        "Programming Language :: Python :: 3",
        "Programming Language :: Python :: 3.4",
        "Programming Language :: Python :: 3.5",
        "Programming Language :: Python :: 3.6",
        "Programming Language :: Python :: 3.7",
        "Programming Language :: Python :: 3.8",
    ],
)
