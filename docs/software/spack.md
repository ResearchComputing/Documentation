# Spack

*Currently, Spack is only available on Alpine.* [Spack](https://spack.readthedocs.io/en/latest/) is a package manager designed for installing multiple configurations. Spack is designed for Supercomputing clusters, making it easy to install and configure software that may not currently be available in the Alpine software stack. The following documentation demonstrates how to activate & use the CURC Spack module and utilize your own Spack environments to install packages and compilers.

## Using Spack on CURC
You can follow these steps from a Research Computing terminal session via a compile job (`acompile`) or within a batch or interactive job.

### Activate and Use the CURC Spack Module

Run the following command to load the Spack module:  

```
[johndoe@c3cpu-c11-u17-2 ~]$ module load spack
```

You can confirm that spack has been loaded and find a list of useful spack commands by running the `spack help` command: 

```
[johndoe@c3cpu-c11-u17-2 ~]$ spack help --all
```

### Using Spack Environments

Now that you've loaded the Spack module, you'll need to create a spack environment in which you'll install software.

__1. Create a Spack environment.__
You can create a Spack environment with the following command: 

```
[johndoe@c3cpu-c11-u17-2 ~]$ spack env create <environment name>
```

Note that, by default, environment specs are stored in `/projects/$USER/spack/environments/`. This location can be changed by modifying the `environments_root` variable within `~/.spack/config.yaml`.

__2. Activate your Spack environment.__
You can activate your Spack environment with one of the following commands: 

```
[johndoe@c3cpu-c11-u17-2 ~]$ spacktivate <environment name>
```

or

```
[johndoe@c3cpu-c11-u17-2 ~]$ spack env activate <environment name>
```

To deactivate your environment, you can use one of the following commands: 

```
[johndoe@c3cpu-c11-u17-2 ~]$ despacktivate
```

or

```
[johndoe@c3cpu-c11-u17-2 ~]$ spack env deactivate
```

### Installing Software with Spack

Once you've created and activated an environment, you can begin installing software using Spack. To search for available software in Spack easily, you can use [Spack's provided search engine](https://packages.spack.io/). Additionally, you can use the Spack list command `spack list`, however, this command is slow as it lists all 7000+ packages available for installation with Spack. To search for a specific software by name, you can use `spack list <software name>`. For example: 

```
[johndoe@c3cpu-c11-u17-2 ~]$ spack list fastqc
fastqc
==> 1 packages
```

>For additional information about a specific piece of software (available versions, variants, and dependencies), you can use the `spack info <software name>` command. Note that the 'preferred version' is the default version which will be installed if no alternative version is specified. 

Once you've confirmed that a piece of software is available, you can install it in the active environment using the `spack install --add` command:

```
[johndoe@c3cpu-c11-u17-2 ~]$ spack install --add fastqc
```

>__Note:__
>- The `--add` argument is required to add package specs to an environment. You can separately add specs >without installing a package using the `spack add <software name>` command.
>- If no compiler is specified, then a default compiler will be installed and used within the environment.

You can also modify the installation commands to meet your installation needs. You can specify which version you'd like to install using the `@` operator:

```
[johndoe@c3cpu-c11-u17-2 ~]$ spack install --add fastqc@0.11.9
```

Once you have installed a package, you can view what packages are installed in your environment using the `spack find` command. For example, 

```
[johndoe@c3cpu-c11-u17-2 ~]$ spack find
==> In environment my_test_environment
==> Root specs
fastqc@0.11.9

==> Installed packages
-- linux-rhel8-zen / gcc@8.5.0 ----------------------------------
berkeley-db@18.1.40  fastqc@0.11.9  ncurses@6.4        pkgconf@1.9.5
bzip2@1.0.8          gdbm@1.23      openjdk@11.0.17_8  readline@8.2
diffutils@3.9        libiconv@1.17  perl@5.36.0        zlib@1.2.13
==> 12 installed packages
```

>Note that since we did not specify a compiler, the default compiler of `gcc@8.5.0` was used. Please also note that the default compiler may change. 

#### Installation Locations and Specifics

The root of the Spack installation tree, by default, is `/projects/$USER/software/spack` (this can be changed in `~/config.yaml`). From there, executables can be found in subdirectories depending on the OS and compiler used to install the software. Software will be installed here regardless of whether the software was installed in an environment. 

Spack will always check the installation root prior to installing software, in an environment or otherwise. If the software is not found in the installation root, it will be installed there. If the software is found in the installation root, it will not be installed. When attempting to install in an environment, symbolic links to the installation root will be created in `/projects/$USER/spack/environments/<envname>/.spack-env/view`. This behavior means that once a piece of software is installed, it can be linked to any environment without having to perform the installation again. 

The default cache is located at `/scratch/alpine/$USER/spack/cache`. This directory will contain any previously-installed tarballs and repositories, as well as any miscellaneous cache items.  

### Installing and Using Compilers with Spack

In addition to standard software packages, you can use Spack to install compilers which are not currently available in the Alpine software stack. It is highly recommended to __NOT__ install compilers directly within the environment. Instead, we suggest that you first install the compiler outside of the environment. If it is installed directly within an environment, then it will depend on the default compiler within the environment. The following is our recommended way to install a new compiler and set it as the default compiler for your environment. 

1. Install the compiler outside of your environment (only needs to be done once):
    ```
    spack install gcc@13.1.0
    ```

2. Obtain the location of the compiler install and save it into a local environmental variable:
    ```
    gcc_location=$(spack location -i gcc@13.1.0)
    ```

3. Create and activate your environment:
    ```
    spack env create my_test_env
    spack env activate my_test_env
    ```

4. Remove any compilers that are in the environment already:
    ```
    spack compiler remove gcc -a
    ```
    >Note that you can also remove intel compilers using `spack compiler remove intel -a`

5. Add the compiler you installed outside of the environment and install the compiler into the environment:
    ```
    spack compiler add $gcc_location
    spack install --add gcc@13.1.0
    ```

>Note that the install of the compiler within the environment is necessary as it will install all dependencies needed for the compiler. 


Once the compiler is added, you can install any subsequent packages using the compiler you've installed with the `%` operator. For example:

```
[johndoe@c3cpu-c11-u17-2 ~]$ spack install --add fastqc%gcc@13.1.0
```

>Installing compilers can take a long time, so make sure you request enough time with `acompile` using the `--time` directive. Additionally, build times can be reduced by specifying more cores with `acompile -n 4` (or even more cores with sinteractive jobs) in conjunction with `spack install --add -j 4`.

#### Adding a compiler from the CURC stack

You can also add any compilers to spack that are already available in the Alpine software stack. To accomplish this, simply load the module associated with your preferred compiler:

```
[johndoe@c3cpu-c11-u17-2 ~]$ module load aocc/3.2.0
```

From there, you can add the compiler to Spack. All compilers in the Alpine software stack can be located with the environment variable `CURC_<compiler>_BIN`. In the case of `aocc/3.2.0`:

```
[johndoe@c3cpu-c11-u17-2 ~]$ spack compiler add $CURC_AOCC_BIN
```

### Key Spack Terms: 

| Term | Definition |
|---------|----------|
| Spec | Description of the build requirements for an installation. This includes the software, version, compiler, and other variants. |
| Variant | An option or feature that can be toggled for a specific package. These usually correspond to a configuration or compilation setting. |
| Repo | A central location which stores packages. Repo locations can be configured. |
| Environment | A collection of packages and dependencies that are available to a user. In Spack, environments do not interact. |

### Basic Spack commands:

| Command | Function |
|---------|----------|
| `spack list` | Find and search for available packages by name |
| `spack info` | Display detailed information about a package, including versions and dependencies |
| `spack env create <environment name>` | Create a Spack environment |
| `spack env list` | List all of your environments |
| `spack env status` | Check which environment is currently activated |
| `spack remove <environment name>` | Remove an environment |
| `spacktivate <environment name>` | Activates a Spack environment |
| `despacktivate` | Deactivates a Spack environment |
| `spack find` | List and search packages installed in the active environment |
| `spack install --add <software>` | Adds specs for selected package and installs it in the active environment |
| `spack uninstall <software>` | Removes package from the activate environment. Refer to the [spack documentation](https://spack-tutorial.readthedocs.io/en/latest/tutorial_environments.html#uninstalling-packages) for additional information |
| `spack compilers` | Lists available compilers |
| `spack spec <software>` | Shows all dependencies and items that would be installed if `<software>` is installed > |

### Troubleshooting Spack

If an installation fails, there are several ways to troubleshoot the failure. Common issues with installations include: 

* __Building with the wrong compiler:__ Double check if the compiler you are using is compatible with the software you are attempting to build. 
* __Building with an incompatible variant set:__ Confirm that the configuration settings for the software are compatible and as expected. If not, try enabling or disabling variants that may be causing problems. 
    * One can easily see variants and possible conflicts by searching the package using [Spack's provided search engine](https://packages.spack.io/) and viewing the "Variants" and "Conflicts" section of the documentation. Additionally, one can view `package.py` in the "Build System" section to directly view the code that defines variants and conflicts.
* __Building an unexpected version:__ Make sure you are building the intended version of a software. If a new version is failing, try insalling an older version. 
* __Building with an unexpected version of a dependency:__ If there are issues installing a dependency, you can modify the specs of a dependency.

Additionally, Spack will oftentimes output troubleshooting suggestions. To increase the verbosity of `spack install`, use `spack -dv install`. 

__Need additional help?__ Fill out our [help form](https://www.colorado.edu/rc/userservices/contact) to request assistance. We are be happy to help with any questions you may have! 

Suggestions provided in the `Troubleshooting Spack` subsection were based off of Spack documentation written by [NERSC](https://docs.nersc.gov/development/build-tools/spack/).