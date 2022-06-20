# Nancy Grace Roman Telescope Data Workshop

To run all the workshop notebooks on your own computer, please be sure your machine is configured with the packages in
the
[installation check file](https://github.com/spacetelescope/roman-data-workshop/blob/main/00_install/). These packages
are the ones we use to verify that the notebooks are working as expected.

These instructions describe setup using `git` and `Miniconda`. It is not strictly necessary to use either of these.

> If you have any problems with any of these steps, please check if your problem has already been reported
> as [an issue](https://github.com/spacetelescope/roman-data-workshop/issues/). If not, please
> [create a new issue](https://github.com/spacetelescope/roman-data-workshop/issues/new?assignees=&labels=workshop-question&template=question-from-workshop-participant.md&title=%5BQuestion%5D+Summarize+your+question+here)
> to ask your question.

## 0. (Only for Windows) Install WSL

> *If you are using Windows, we now recommend using the Windows Subsystem for Linux (WSL) instead of using native
Windows tools. WSL is now fully supported by Microsoft and tends to result in fewer install headaches, and lets you use
tools that were developed for Linux seamlessly in windows. While you still may be able to use the Windows-native
installation of Miniconda, these instructions focus on the WSL approach for the above reasons.*

To install WSL, you should follow the instructions provided by Microsoft:

https://docs.microsoft.com/en-us/windows/wsl/install

While you may choose an alternative Linux distribution from the default Ubuntu, the instructions below have been tested
on Ubuntu, so unless you have a specific reason, we suggest you stick with the default. Once you reach the point in the
instructions with a working Linux terminal prompt, you can proceed to step 1 of these instructions.

> **Optional** While you can run a WSL terminal with the command prompt built into Windows, it's rather bare-bones and
> you
> may not have the best experience. For WSL on Windows you'll probably want
> to [install Windows Terminal](https://docs.microsoft.com/en-us/windows/terminal/install) to have a terminal experience
> closer to what you'd see on Mac or Linux.

## 1. Install Miniconda (if needed)

> *Miniconda is a free minimal installer for `conda`. It is a small, bootstrap version of Anaconda that includes
only `conda`, Python, the packages they depend on, and a small number of other useful packages like `pip`, `zlib` etc.
If you have already installed Miniconda or Anaconda, you can skip to the next step.*

In a terminal window, check if Miniconda is already installed:

```shell
conda info
```

If Miniconda is not already installed, follow these instructions for your operating system:

https://conda.io/projects/conda/en/latest/user-guide/install/index.html

> Please be sure to install a **64-bit version** of Miniconda to ensure that all packages work correctly.

> (On native Windows, you might also
> need [additional compilers](https://github.com/conda/conda-build/wiki/Windows-Compilers), although this should not be
> necessary in WSL).

## 2. Open the conda command prompt

> *Miniconda includes an environment manager called `conda`. An environment manager allows you to have multiple
installations of Python, including packages and versions, installed on your computer. You can create, export, list,
remove, and update environments that have different versions of Python and / or packages installed in them. For this
workshop, we will configure an environment using the `conda` command line utility.*

Open a terminal window and verify that conda is working:

```shell
conda info
```

If you are having trouble, check your shell in a terminal window:

```shell
echo $SHELL
```

then run the initialization, if needed, in that same terminal window:

```shell
conda init $SHELL
```

On Windows, open the `Anaconda Prompt` terminal app.

> *(An alternative to using conda is [mamba](https://github.com/mamba-org/mamba) which is a reimplementation of the
conda package manager in C++.)*

> Note: you will need `conda` version `4.6` or later. You can update your `conda` installation with `conda update conda`

## 3. Install Git (if needed)

At the prompt, check whether Git is already installed:

```shell
git --version
```

If the output shows a Git version, skip to the next step. Otherwise, install Git:

```shell
conda install git
```

## 5. Clone this repository, or download and extract a ZIP file, from GitHub

If using `git`, clone the workshop repository using
[git](https://help.github.com/articles/set-up-git/):

```shell
git clone https://github.com/spacetelescope/roman-data-workshop.git
```

If you elect not to use `git`, you can download the ZIP file by opening the green `Code` button at
https://github.com/spacetelescope/roman-data-workshop and selecting `Download ZIP`.

## 6. Create a `conda` environment for the workshop

> *Miniconda includes an environment manager called conda. Environments allow you to have multiple sets of Python
packages installed at the same time, making reproducibility and upgrades easier. You can create, export, list, remove,
and update environments that have different versions of Python and/or packages installed in them.*

[Create a conda environment for this workshop using a yml file](https://conda.io/docs/user-guide/tasks/manage-environments.html#creating-an-environment-from-an-environment-yml-file)
. The python version and all needed packages are listed in
[`environment.yml`](https://github.com/spacetelescope/roman-data-workshop/blob/main/00_install/environment.yml).

Open a terminal window using the appropriate one for your operating system.

Now navigate to this directory in the terminal:

```shell
cd roman-data-workshop
```

And finally, on any platform, to install and activate the `roman-data-workshop-env` environment, type:

```shell
conda env create --file 00_install/environment.yml
conda activate roman-data-workshop-env
```

The name of the new conda environment created above should now be displayed next to the terminal
prompt: `(roman-data-workshop-env)`

## 7. Check Installation

In the terminal you used in the preceding step, run the `verify_install.py` script to check the Python environment and
some required dependencies:

```shell
python 00_install/verify_install.py
```

If the script reports that some versions do not match for a specific package (for example `numpy`), check first whether
the package was installed using `conda` or `pip` by using `conda list <package>`:

```shell
conda list numpy
```

If the package was installed with `pip`, the `Build` and `Channel` columns will include `pypi`:

```
# packages in environment at /opt/miniconda3/envs/test:
#
# Name                    Version                   Build  Channel
numpy                     1.22.4                   pypi_0    pypi
```

and then you can upgrade with `pip install --upgrade <package>`:

```shell
pip install --upgrade numpy
```

> If you need a pre-release version from PyPI, add `--pre` to the `pip install` command.

Otherwise, if the package is installed with `conda`, it will show something similar to the following:

```
# packages in environment at /opt/miniconda3/envs/test:
#
# Name                    Version                   Build  Channel
numpy                     1.22.3          py310hdcd3fac_0
numpy-base                1.22.3          py310hfd2de13_0
```

and you can update with `conda update <package>`:

```shell
conda update numpy
```

## 8. Starting Jupyter Notebook

Making sure your terminal is in the `roman-data-workshop` directory (you can use `pwd` to check), you can then start the
Jupyter server on your local computer, with which you can view the Jupyter notebooks:

```shell
jupyter notebook
```

If successful, your browser will open a new page / tab pointing to `localhost`, showing a listing of the current
directory (including subdirectories).

Click into one of the notebook directories, double-click on a notebook, and wait for it to launch. In the top right
corner, if you see a blue `Kernel Ready` message appear and disappear, then all is well.

If you see a red `Kernel Error` in the top right corner, click on it and scroll down to see the error message. If it
says `FileNotFoundError`, shut down the notebook server on your terminal and run this command:

```shell
python -m ipykernel install --user
```

Now, try running `jupyter notebook` again as above, and the `Kernel Error`
should be fixed. You can try running the first cell (usually an `import`) to check.

## Additional Resources

- [Set up git](https://help.github.com/articles/set-up-git/)
- [Conda Users Guide](https://docs.conda.io/projects/conda/en/latest/user-guide/)
- [Instructions for keeping this repo up to date](UPDATING.md)
