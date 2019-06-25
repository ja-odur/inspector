## __Introspector__ 
A python package for getting information about a python package such documentation, attributes, methods, method signatures etc.

## ___Prerequisites___

* `Git` [Guide to Git](https://git-scm.com/doc) [Installing Git](https://gist.github.com/derhuerst/1b15ff4652a867391f03)
* `Python 3`
* `Pip` [Guide to installing pip](https://github.com/BurntSushi/nfldb/wiki/Python-&-pip-Windows-installation)


## __Cloning and creating wheel file__
* Clone this [repository's](https://github.com/ja-odur/introspector/) develop branch
using this command **`git clone -b develop https://github.com/ja-odur/introspector.git`**
* Change into the newly cloned repo through `cd instrospector`
* Create the wheel file with **`python3 setup.py bdist_wheel`**

## __Installing the wheel file__
* Using pip, run the command to install the package
* $ **`pip3 install dist/introspector-0.0.1-py3-none-any.whl`**


## __Usage__
* **`from introspector import dump`**
* Call the function **`dump`** with the package or module that you want to introspect e.g
- **`dump(list)`** 

## __Author__

Odur Joseph