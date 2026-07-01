# what is virtual environment in python ?

  1. virtual environment is a tool to keep dependencies required by different projects in separate places by creating virtual python environment for them.

  2. it solves the "Project Dependency" problem and keeps your global site-packages directory clean and manageable.

  3. virtual environment is used to create a separate projects environment for each project.

  4. virtual environment is a tool to create isolated means of separate python environment. 

## how to create virtual environment in python ?

  1. open command prompt and type the following command to create virtual environment in python.

  ```
  pip install virtualenv

  ```

  2. after installing virtualenv, type the following command to create a virtual environment.

  ```
  virtualenv <name of your virtual environment>
 
  ```

  3. after creating virtual environment, type the following command to activate the virtual environment.

  ```
  <name of your virtual environment>\Scripts\activate
 
  ```

# how to deactivate virtual environment in python ?

  1. after activating the virtual environment, type the following command to deactivate the virtual environment.

  ```
  deactivate
  ```  