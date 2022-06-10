# Getting Everything Up To Date

If you downloaded and installed your directory and conda environment before the workshop, good for you!  We appreciate
it. However, there may well have been some updates made to the materials we are going to use in the workshop, so...

## 1. Updating your files

### Updating a local repository cloned with `git`

Assuming you cloned the `roman-data-workshop` git repository, open up a terminal, change your location to that
directory, and then run the following:

```shell
cd roman-data-workshop
git pull
```

If there are errors when attempting to update, your best option is to reset your local files to match the remote
(this *will destroy* any local file changes you have made):

```shell
git reset --hard origin/main
```

#### Saving Changes (optional)

**ADVANCED OPTION**: This is not a git workshop, but if you want to keep your file modifications, you can commit your
modified files to the git repository and then create a new branch from the current version on the GitHub server:

```shell
git commit -a "Save my modified files"
git fetch origin
git checkout origin/main -b workshop-main
```

This is probably overkill unless you already use git regularly. When in doubt, please ask the instructors or helpers.

### Updating a local directory downloaded with `Download ZIP`

If you do not have `git` installed and used the `Download ZIP` option instead, you will have to re-download the ZIP and
overwrite your local files to make sure that you have the most recent version.

## 2. Double-checking your Conda environment

Assuming you properly installed your `roman-data-workshop-env` conda environment, you should be able to:

a. activate that conda environment, and b. go to the original installation directory, and then c. check to see if your
environment still meets the requirements.

Let's do that now. Start by activating the `conda` environment:

```shell
conda activate roman-data-workshop-env
```

You may notice a change in your prompt; e.g., `(roman-data-workshop-env)`. Switch to the directory containing the
installer by doing the following (your directory path may be different):

```shell
cd roman-data-workshop
```

Next, we check if the environment is still up-to-date:

```shell
python 00_install/verify_install.py
```

If this check reports no issues, you are done. Otherwise, continue below.

## 3. Updating Python packages

If the `verify_install.py` script reports that some package (for example `numpy`)
is not up-to-date, we need to check where the package came from with `conda list`:

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

Once you have performed the updates, check your installation again using `verify_install.py`:

```shell
python 00_install/verify_install.py
```

You should now be up-to-date.
