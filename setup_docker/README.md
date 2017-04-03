In order to simplify the setup of a common environment for all students on any Operating System, we recommend to run Python using `Docker`. Thanks to `Docker`, you can access the Jupyter Notebook and all of the Python Data Science stack without installing any library on your computer. Just install `Docker` and then download a **container** that packages up all the required libraries and use your browser to connect to the Jupyter Notebook running inside this container.

# Install Docker

## Windows 10

Docker requires 64bit Windows 10 Pro, Enterprise and Education (1511 November update, Build 10586 or later)
Follow instructions on the Docker official website at https://docs.docker.com/docker-for-windows/install/

* Choose the `Stable` version

## Windows 7 and 8

Docker maintains also the `Docker toolbox`, a legacy system that works on 64bit Windows 7 and 8, follow the instructions here:

<https://docs.docker.com/toolbox/toolbox_install_windows/>

## Mac

Docker for Mac has substantial system requirements, check on the **System requirements** section on this page to check if your machine is supported:

<https://docs.docker.com/docker-for-mac/install/>

* Choose the `Stable` version

## Linux

Check if your distribution is supported on the Docker official website:

https://docs.docker.com/engine/installation/linux/

Then follow the instructions to install the **Community Edition (CE)** and choose the `stable` channel.

# Install and run the Scientific Python docker container

## Create a folder on your machine to preserve your work

For example create a folder named `Python4DS` in your home folder. This folder will be available within the container so that you can save your work back to your host Operative System.

## Launch the container

If you are installing Docker on your personal laptop or desktop, you can run (possibly add `sudo` at the beginning for Linux): 

    docker run -d -p 8888:8888 jupyter/scipy-notebook start-notebook.sh --NotebookApp.token='' -v /some/host/folder/for/Python4DS:/home/jovyan/Python4DS
    
Instead of `/some/host/folder/for/Python4DS`, use the full path to the folder you created above.

**FIXME** how does this work on windows??
    
Instead if you are using a shared system, launch the same command but remove the keyword `--NotebookApp.token='', the Notebook will provide an authentication token to prevent other users from connecting to your Notebook:


Just for the first time, the execution of this command will download more than 1 GB of data and will require 20 or more minutes, depending on the speed of your internet connection and performance of your machine.

After the first execution, the startup will be quick and won't require internet connection.

For more configuration options of the container, see [its homepage on Github](https://github.com/jupyter/docker-stacks/tree/master/scipy-notebook).

# Access the Python Data Science stack

* Open a browser on your local machine (Chrome recommended, but any browser should work)
* Type `localhost:8888` on your browser bar
* You should now visualize the Jupyter Notebook dashboard, in particular you should see the `Python4DS` folder.
