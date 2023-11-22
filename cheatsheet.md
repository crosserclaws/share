# Cheatsheet

## Python

```shell
# virtual environments from pyenv
pyenv install 3.6.9
pyenv virtualenv 3.6.9 new-env
pyenv activate new-env
pyenv deactive
# You can also use `pyenv local`


# virtual environments from conda
conda create -n new-env python=3.6
conda env list
conda activate new-env
conda deactivate
```

## Reference
- Stackoverflow
  - [How can I install Anaconda aside an existing pyenv installation on OSX?](https://stackoverflow.com/questions/57640272/how-can-i-install-anaconda-aside-an-existing-pyenv-installation-on-osx)
