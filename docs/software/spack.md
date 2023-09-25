# Spack

[Spack](https://spack.readthedocs.io/en/latest/) is a package manager designed for installing multiple configurations of scientific software within environments. Spack is designed for Supercomputing clusters, making it easy to install and configure software that may not currently be available on the CURC software stack. The following documentation demonstrates how to activate & use the CURC Spack module and utilize your own Spack environments to install packages and compilers.

## Using Spack on CURC
You can follow these steps from a Research Computing terminal session via a compile job (`acompile`) or within a batch or interactive job. *Currently, Spack is only available on Alpine*.

### Activate the CURC Spack Module

Run the following command to load the Spack module:  

```
[johndoe@c3cpu-c11-u17-2 ~]$ module load spack/0.20.1
```

You can confirm that spack has been loaded and find a list of useful spack commands by running the `spack` command: 

```
[johndoe@c3cpu-c11-u17-2 ~]$ spack
```

### Using Spack Environments

Now that you've loaded the Spack module, you'll need to create a spack environment in which you'll install software.

__1. Create a Spack environment__
You can create a Spack environment with the following command: 

```
[johndoe@c3cpu-c11-u17-2 ~]$ spack env create <environment name>
```

Note that, by default, environments are stored in `/projects/$USER/spack/environments/`. This location can be changed by modifying the `environments_root` variable within `~/.spack/config.yaml`.

__2. Activate your Spack environment__
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

Once you've created and activated an environment, you can begin installing software using Spack. To see a list of *all* of the software available, you can use the spack list command: 

```
[johndoe@c3cpu-c11-u17-2 ~]$ spack list
```

To search for a specific software by name, you can use `spack list <software name>`. For example: 

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
>Note that the `--add` argument is required to add package specs to an environment. You can separately add specs without installing a package using the `spack add <software name>` command.

This will install the specified software and all dependencies into your environment. The root of the installation tree is `/projects/$USER/software/spack/`.

You can also modify the installation commands to meet your installation needs. You can specify which version you'd like installed using the `@` operator:

```
[johndoe@c3cpu-c11-u17-2 ~]$ spack install --add fastqc@0.11.9
```

### Installing and Using Compilers with Spack

In addition to standard software packages, you can use Spack to install compilers which are not currently available on the CURC software stack. For example, if you need the newest available version of `gcc`, you can install it into your environment as follows: 

```
[johndoe@c3cpu-c11-u17-2 ~]$ spack install --add gcc@13.1.0
```
Once the installation is complete, you can make it available to Spack with `spack compiler add`:

```
[johndoe@c3cpu-c11-u17-2 ~]$ spack compiler add <path to compiler>
```

>Note that, in this case, you can locate the path of the compiler with `spack location -i gcc@13.1.0`.

Once the compiler is added, you can install any subsequent packages using the compiler you've installed with the `%` operator. For example:

```
[johndoe@c3cpu-c11-u17-2 ~]$ spack install fastqc%gcc@13.1.0
```

### Basic Spack commands:

| Command | Function |
|---------|----------|
| `spack list` | Find and search for available packages by name |
| `spack info` | Display detailed information about a package, including versions and dependencies |
| `spack env create <environment name>` | Create a Spack environment |
| `spacktivate <environment name>` | Activates a Spack environment |
| `despacktivate` | Deactivates a Spack environment |
| `spack find` | List and search packages installed in the active environment |
| `spack install --add <software>` | Adds specs for selected package and installs it in the active environment |
| `spack compilers` | Lists available compilers |
| `spack spec <software>` | Shows all dependencies and items that would be installed if `<software>` is installed > |

---