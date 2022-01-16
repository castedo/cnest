# The .readthedocs.yaml file determines what OCI container is run and what
# software packages are installed by the Read the Docs service.
# This Dockerfile approximates the environment resulting from the
# .readthedocs.yaml file of the cnest documentation.

FROM docker.io/readthedocs/build:ubuntu-20.04-2021.09.23

# The following commands were selected based on readthedocs.org build logs
# and the server code readthedocs/doc_builder/python_environments.py in the
# repository https://github.com/readthedocs/readthedocs.org


# class PythonEnvironment:
#    def install_build_tools(self):

RUN asdf install python 3.8.12
RUN asdf global python 3.8.12
RUN asdf reshim python

RUN python -m pip install --upgrade virtualenv "setuptools<58.3.0"


# class Virtualenv(PythonEnvironment):
#    def setup_base(self):

# pick a shorter virtual environment path than readthedocs.org
ENV RTD_VENV_PATH=/home/docs/venv

RUN python -mvirtualenv $RTD_VENV_PATH


# class Virtualenv(PythonEnvironment):
#    def install_core_requirements(self):

RUN $RTD_VENV_PATH/bin/python -m pip install --upgrade pip "setuptools<58.3.0"

RUN $RTD_VENV_PATH/bin/python -m pip install --upgrade \
    mock==1.0.1 \
    pillow==5.4.1 \
    "alabaster>=0.7,<0.8,!=0.7.5" \
    commonmark==0.8.1 \
    recommonmark==0.5.0 \
    sphinx \
    sphinx-rtd-theme \
    readthedocs-sphinx-ext


# class Virtualenv(PythonEnvironment):
#    def install_requirements_file(self, install):

COPY requirements.txt /tmp/
RUN $RTD_VENV_PATH/bin/python -m pip install --exists-action=w -r /tmp/requirements.txt


# Let new users get the same benefit of the home setup of user docs
USER root
RUN cp /home/docs/.bashrc /etc/skel/
RUN cp /home/docs/.tool-versions /etc/skel/
RUN ln -s /home/docs/.asdf /etc/skel/.asdf

# set image user back like Read the Docs base image
USER docs

