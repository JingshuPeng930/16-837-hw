# Local Installation Guide

## General Environment Setup

For all operating systems, use **Conda** to set up the environment. We recommend installing [Miniconda](https://www.anaconda.com/download/success) first.

> **Note:** Miniconda may modify your `PATH` through `.bashrc`. After installation, open a **new terminal** so that `conda` is available.

### 1. Create the Conda environment

Create a new environment with Python 3.10:

```bash
conda create -n rob831 python=3.10
```

### 2. Activate the environment

Activate the environment whenever you open a new terminal and want to run the code:

```bash
conda activate rob831
```

### 3. Install dependencies

From the repository root, install the required packages:

```bash
pip install --user -r requirements.txt
```

### 4. Install the package

Install the project in editable mode so that your code can import `rob831`:

```bash
cd <path_to_hw1>
pip install -e .
```

> **Tip:** Make sure the `rob831` Conda environment is activated before running the code.


## Linux/Ubuntu
To test if the project installation worked correctly run
```
python -c "import gym; env = gym.make('Ant-v2'); print(env.reset().shape); env.close()"
```

If an error appears when installing mujoco-py: `No such file or directory: 'patchelf'`, try installing patchelf first:

```
sudo apt-get install patchelf
```

During mujoco-py install, if `fatal error: GL/osmesa.h: No such file or directory compilation terminated` appears, run:

```
$ sudo apt-get install libosmesa6-dev
```

## Windows
> **Note:** Mujoco-py versions above 2 are now deprecated for Windows. We recommend using Linux or running on colab.

On Windows, install [Windows Subystem for Linux (WSL)](https://learn.microsoft.com/en-us/windows/wsl/install). Setup below has been tested for Ubuntu 22.04. Ensure system comes with the following system packages:

```bash 
sudo apt-get update
sudo apt-get install -y build-essential gcc g++ patchelf libosmesa6-dev libgl1-mesa-dev libglew-dev libglfw3 libglfw3-dev
```

and confirm the osmesa header exists by running the following:

```bash
ls /usr/include/GL/osmesa.h # should return a valid path
```

Perform conda env installation as shown above. To test if the project installation worked correctly run
```
python -c "import gym; env = gym.make('Ant-v2'); print(env.reset().shape); env.close()"
```

If a gcc error occurs, point the build at the system gcc compiler.

```bash
export CC=/usr/bin/gcc
export CFLAGS="-I/usr/include -Wno-incompatible-pointer-types"
export C_INCLUDE_PATH=/usr/include
```

## Mac
To test if the project installation worked correctly run
```
python -c "import gym; env = gym.make('Ant-v2'); print(env.reset().shape); env.close()"
```

If you get the following error: `RuntimeError: Could not find GCC executable`, please run the following

```bash
conda install -c conda-forge gcc 

export CC=$CONDA_PREFIX/bin/gcc
export CFLAGS="-Wno-incompatible-pointer-types"
```

If installing requirements.txt fails to build matplotlib, install it separately without specifying version number:
```
pip uninstall matplotlib
pip install matplotlib
```