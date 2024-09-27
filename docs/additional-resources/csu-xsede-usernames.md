# CSU and ACCESS (XSEDE) usernames

Your CURC username, which is represented by the environment variable `$USER`, has an `@` symbol in it (e.g. `janedoe@colostate.edu` or `johndoe@xsede.org`). 

The `@` symbol can occasionally be misinterpreted by environments that employ PERL and cause unexpected behavior or errors. This may occur within a stand-alone PERL application or even within a conda-based application that employs PERL packages. As a workaround, symbolic links to your `/home/$USER`, `/projects/$USER` and `/scratch/alpine/$USER` directories have been created for all CSU and ACCESS (XSEDE) users. These symbolic links do not have `@` symbols within them and therefore will not be misinterpreted by programs that utilize PERL. Below is an example of the symbolic links that are setup for the hypothetical user `janedoe@colostate.edu`:

```
/home/.colostate.edu/janedoe → /home/janedoe@colostate.edu

/projects/.colostate.edu/janedoe → /projects/janedoe@colostate.edu

/scratch/alpine/.colostate.edu/janedoe → /scratch/alpine/janedoe@colostate.edu
```

An easy way to use these alternate usernames is to set a `$USER2` environment variable by adding the following line to your `~/.bashrc` file:

```
export USER2=$(echo $USER |  awk -F@ '{print "."$2"/"$1}')
```

This will yield a `$USER2` value of, for example, `.colostate.edu/janedoe`. This means that a path such as `/projects/$USER2` is equivalent to `/projects/$USER`. Thus, if you are having issues with a conda installation because of the `@` symbol, you can simply utilize `/projects/$USER2` in your `.condarc`. For more information on `.condarc` see our [Configuring Conda and Mamba with .condarc](../software/python.md#configuring-conda-and-mamba-with-condarc) section.

