In order to simplify the setup of a common environment for all students on any Operating System, we recommend to run Python using `Docker`. Thanks to `Docker`, you can access the Jupyter Notebook and all of the Python Data Science stack without installing any library on your computer. Just install `Docker` and then download a **container** that packages up all the required libraries and use your browser to connect to the Jupyter Notebook running inside this container.

# 1) Install Docker

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

# 2) Install and run the Scientific Python docker container

## Create a folder on your machine to preserve your work

For example create a folder named `Python4DS` in your home folder. This folder will be available within the container so that you can save your work back to your host Operative System.

On Mac/Linux, open a terminal, type `cd` and enter to make sure you are in your home folder and create a folder with `mkdir Python4DS`.
On Windows, open the `Docker Quickstart Terminal` and create a folder with `mkdir Python4DS`.

## Launch the container for the first time

If you are installing Docker on your personal laptop or desktop, you can run (possibly add `sudo` at the beginning for Linux): 

    docker run -d -p 8888:8888 --name python4ds -v /some/host/folder/for/Python4DS:/home/jovyan/work jupyter/scipy-notebook start-notebook.sh --NotebookApp.token='' 
    
Instead of `/your/home/folder/Python4DS`, use the full path to the folder you created above, generally it will be `/home/yourusername/Python4DS` on Linux, `/Users/yourusername/Python4DS` on Mac and `/c/Users/yourusername/Python4DS` on Windows. This will be mounted in the containter at the location `/home/jovyan/work` which is the starting folder of Jupyter Notebook.
    
Instead if you are using a shared system, launch the same command but remove the keyword `--NotebookApp.token=''`, the Notebook will provide an authentication token to prevent other users from connecting to your Notebook:


Just for the first time, the execution of this command will download more than 1 GB of data and will require 20 or more minutes, depending on the speed of your internet connection and performance of your machine.

After the first execution, the startup will be quick and won't require internet connection.

For more configuration options of the container, see [its homepage on Github](https://github.com/jupyter/docker-stacks/tree/master/scipy-notebook).

## Access the Jupyter Notebook

* Open a browser on your local machine (Chrome recommended, but any browser should work)
* Find the address of the container, for Linux it is `localhost`, for Windows, you can find out by typing `docker-machine ip default` in the `Docker Quickstart Terminal` (generally `192.168.99.100`).
* Type `container_address:8888` on your browser bar, e.g. `192.168.99.100:8888` on Windows, localhost:8888 on Linux.
* You should now visualize the Jupyter Notebook dashboard, in particular you should see the `Python4DS` folder.

## Stop the execution of the container

From the terminal on your host system or the `Docker Quickstart Terminal`, type `docker ps` to check the running containters, then `docker stop python4ds` to stop the execution of the container.

## Launch the container again

Now that the container has already been created, you can launch it with:

    docker start python4ds
    
# 3) Troubleshooting

## Wipe and create again the container

If you have a configuration issue in the container you can delete with:

    docker rm -f python4ds
    
then follow the instructions in "Launch the container for the first time" to create it again.
