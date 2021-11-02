## CSU and XSEDE usernames

Your CURC username, which is represented by the environment variable `$USER`, has an `@` symbol in it (for example, janedoe@colostate.edu or johndoe@xsede.org). 

The `@` symbol can occasionally be misinterpreted by environments that employ PERL. This may occur within a stand-alone PERL application, or within a conda-based application that employs PERL packages. As a workaround symbolic link to your `/home/$USER`, `/projects/$USER` and `/scratch/summit/$USER` directories that do not have `@` symbols have been created for all CSU and XSEDE users. Below is an example of the symbolic links that are setup for the hypothetical user janedoe@colostate.edu:

```
/home/.colostate.edu/janedoe → /home/janedoe@colostate.edu

/projects/.colostate.edu/janedoe → /projects/janedoe@colostate.edu

/scratch/summit/.colostate.edu/janedoe → /scratch/summit/janedoe@colostate.edu
```

An easy way to use these alternate usernames is to set a `$USER2` environment variable by adding the following line in your `~.bashrc` file:

```
export USER2=$(echo $USER |  awk -F@ '{print "."$2"/"$1}')
```

This will yield a `$USER2` value of (e.g.) .colostate.edu/janedoe such that `/home/$USER2` is equivalent to `/home/$USER`, `/projects/$USER2` is equivalent to `/projects/$USER`, an so on.
