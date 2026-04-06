# Using OpenMP with C and Fortran

Because a cluster consists of many CPUs, the most effective way to utilize
these resources involves parallel programming. Perhaps the simplest
way to begin parallel programming is through the use of
OpenMP. OpenMP is a compiler-side solution for creating code that runs
on multiple cores/threads. Because OpenMP is built into a compiler, no
external libraries need to be installed in order to compile this
code. If you are new to OpenMP, a good foundational tutorial is available at [https://hpc-tutorials.llnl.gov/openmp/](https://hpc-tutorials.llnl.gov/openmp/).

In this tutorial we will be using the Intel and GCC compilers to create an OpenMP ‘hello world’ program in your choice of C++ or Fortran.  This tutorial assumes the you have experience in both the Linux terminal and C++ or Fortran.  To begin, select the tab for C++ or Fortran.

(tabset-ref-ucb-prog-MPI-types)=
```````{tab-set}
:sync-group: tabset-ucb-prog-MPI-types
``````{tab-item} C++
:sync: ucb-prog-MPI-types-c

## Parallel “Hello, World” Program

In this section we will learn how to make a simple parallel "Hello
World" program in C++. Let’s begin with the creation of a program
titled `parallel_hello_world.cpp`. From the command line, run the
command:

```bash
nano parallel_hello_world.cpp
```

We will begin with include statements we want running at the top of
the program:

```c++
#include <stdio.h>
#include <omp.h>
```

These flags allow us to utilize the `stdio` and `omp` libraries in our
program. The `<omp.h>` header file will provide OpenMP
functionality. The `<stdio.h>` header file will provide us with print
functionality.

Let’s now begin our program by constructing the main function of the
program. We will use `omp_get_thread_num()` to obtain the thread ID of
the process. This will let us identify each of our threads using that
unique ID number.

```c++
#include <stdio.h>
#include <omp.h>

int main(int argc, char** argv){

    printf("Hello from process: %d\n", omp_get_thread_num());

    return 0;
}
```

Let’s compile our code and see what happens. We must first load the
compiler module we want into our environment. We can do so as such:

(tabset-ref-openmp-c-module)=
`````{tab-set}
:sync-group: tabset-openmp-c

````{tab-item} GNU C++ Compiler
:sync: openmp-c-openmpi

```bash
module load gcc
```

````

````{tab-item} Intel C++ Compiler
:sync: openmp-c-intelmpi

```bash
module load intel
```

````
`````

From the command line, where your code is located, run the command:

(tabset-ref-openmp-c-compile)=
`````{tab-set}
:sync-group: tabset-openmp-c

````{tab-item} GCC
:sync: openmp-c-openmpi

```bash
g++ parallel_hello_world.cpp -o parallel_hello_world.exe -fopenmp
```

````

````{tab-item} Intel C/C++ Compiler
:sync: openmp-c-intelmpi

```bash
icc parallel_hello_world.cpp -o parallel_hello_world.exe -qopenmp
```

````
`````

This will give us an executable we can submit as a job to our cluster.
Simply submit the job to Slurm, running the
executable. Your job script should look something like this:

```bash
#!/bin/bash
#SBATCH --nodes=1
#SBATCH --time=00:01:00
#SBATCH --partition=atesting
#SBATCH --qos=testing
#SBATCH --constraint=ib
#SBATCH --ntasks=4
#SBATCH --job-name=CPP_Hello_World
#SBATCH --output=CPP_Hello_World.out

./parallel_hello_world.exe
```

Our output file should look like this:

```
Hello from process: 0
```

As you may have noticed, we only get one thread giving us a Hello
statement.  How do we parallelize the print statement? We parallelize
it with `pragma` !  The `#pragma omp parallel { … }` directive creates
a section of code that will be run in parallel by multiple
threads. Let’s implement it in our code:

```c++
#include <stdio.h>
#include <omp.h>

int main(int argc, char** argv){
    #pragma omp parallel
    {
        printf("Hello from process: %d\n", omp_get_thread_num());
    }
    return 0;
}
```

We must do one more thing before achieving parallelization. To set the
amount of threads we want OpenMP to run, we must set a Linux
environment variable to be specify how many threads we wish to
use. The environment variable `OMP_NUM_THREADS` will store this
information.  Changing this variable does not require recompilation of
the program, so this command can be placed in either the command
line or on your job script:

```bash
export OMP_NUM_THREADS=4
```

```{important}
This environment variable will need to be set
every time you exit your shell.__ If you would like to make this
change permanent, you will need to add these lines to your
`.bash_profile` file in your home directory:

```bash
OMP_NUM_THREADS=4;
export OMP_NUM_THREADS
```



Now let’s re-compile the code and run it to see what happens:

(tabset-ref-openmp-c-recompile)=
`````{tab-set}
:sync-group: tabset-openmp-c

````{tab-item} GCC
:sync: openmp-c-openmpi

```bash
g++ parallel_hello_world.cpp -o parallel_hello_world.exe -fopenmp
```

````

````{tab-item} Intel C/C++ Compiler
:sync: openmp-c-intelmpi

```bash
icc parallel_hello_world.cpp -o parallel_hello_world.exe -qopenmp
```

````
`````

Running our job script, we should end with an output file similar to this one:

```
Hello from process: 3
Hello from process: 0
Hello from process: 2
Hello from process: 1
```

```{note}
Don’t worry about the order of processes that printed, the threads will
print out at varying times.
```

## Private vs. Shared Variables

Memory management is an essential component of any parallel
program that involves data manipulation. In this section, we will
learn about the different variable types in OpenMP, as well as a simple
implementation of these types into the program we made in the previous
section.

OpenMP has a variety of tools that can be utilized to properly
describe how the parallel program should handle variables. These tools
come in the forms of shared and private variable type classifiers.

- Private types create a copy of a variable for each process in the
  parallel system.

- Shared types hold one instance of a variable for all processes to
  share.

To indicate private or shared memory, declare the variable before your
parallel section and annotate the `pragma omp` directive as such:

```c++
#pragma omp shared(shar_Var1) private(priv_Var1, priv_Var2)
```

Variables that are created and assigned inside of a parallel section
of code will be inherently be private, and variables created outside
of parallel sections will be inherently public.


__Example__

Let’s adapt our ‘Hello World’ code to utilize private variables as an
example.  Starting with the code we left off with, let’s create a
variable to store the thread ID of each process.

```c++
#include <stdio.h>
#include <omp.h>

int main(int argc, char** argv){
    int thread_id;

    #pragma omp parallel
    {
        printf("Hello from process: %d\n", omp_get_thread_num());
    }
    return 0;
}
```

Now let’s define `thread_id` as a private variable. Because we want
each task to have a unique thread ID, using the `private(thread_id)`
will create a separate instance of `thread_id` for each task.

```c++
#include <stdio.h>
#include <omp.h>

int main(int argc, char** argv){
    int thread_id;

    #pragma omp parallel private(thread_id)
    {
        printf("Hello from process: %d\n", omp_get_thread_num());
    }
}
```

Lastly, let’s assign the thread id to our private variable and print
out the variable instead of the `omp_get_thread_num()` function call:

```c++
#include <stdio.h>
#include <omp.h>

int main(int argc, char** argv){
    int thread_id;

    #pragma omp parallel private(thread_id)
    {
        thread_id = omp_get_thread_num();
        printf("Hello from process: %d\n", thread_id );
    }

    return 0;
}
```

Compiling and running our code will result in similar output to
our original Hello World:

```
Hello from process: 3
Hello from process: 0
Hello from process: 2
Hello from process: 1
```

## Barrier and Critical Directives

OpenMP has a variety of tools for managing processes. One of the more
prominent forms of control comes with the `barrier`:

```c++
#pragma omp barrier
```

...and the `critical` directives:

```c++
#pragma omp critical { … }
```

The `barrier` directive stops all processes for proceeding to the next
line of code until all processes have reached the barrier. This allows
a programmer to synchronize sequences in the parallel process.

A `critical` directive ensures that a line of code is only run by one
process at a time, ensuring thread safety in the body of code.


__Example__

Let's implement an OpenMP barrier by making our ‘Hello World’ program
print its processes in order. Beginning with the code we created in
the previous section, let’s nest our print statement in a loop which
will iterate from 0 to the max thread count. We will retrieve the max
thread count using the OpenMP function: `omp_get_max_threads()`

Our ‘Hello World’ program will now look like:

```c++
#include <stdio.h>
#include <omp.h>

int main(int argc, char** argv){
    //define loop iterator variable outside parallel region
    int i;
    int thread_id;

    #pragma omp parallel private(thread_id)
    {
        thread_id = omp_get_thread_num();

        //create the loop to have each thread print hello.
        for(i = 0; i < omp_get_max_threads(); i++){
            printf("Hello from process: %d\n", thread_id);
        }
    }
    return 0;
}
```

Now that the loop has been created, let’s create a conditional that
requires the loop to be on the proper iteration to print its thread
number:

```c++
#include <stdio.h>
#include <omp.h>

int main(int argc, char** argv){
    int i;
    int thread_id;

    #pragma omp parallel private(thread_id)
    {
        thread_id = omp_get_thread_num();

        for(i = 0; i < omp_get_max_threads(); i++){
            if(i == thread_ID){
                printf("Hello from process: %d\n", thread_id);
            }
        }
    }
    return 0;
}
```

Lastly, to ensure one process doesn’t get ahead of another, we need to
add a barrier directive in the code. Let’s implement one in our loop:

```c++
#include <stdio.h>
#include <omp.h>

int main(int argc, char** argv){
    int i;
    int thread_id;

    #pragma omp parallel private(thread_id)
    {
        thread_id = omp_get_thread_num();

        for( int i = 0; i < omp_get_max_threads(); i++){
            if(i == omp_get_thread_num()){
                printf("Hello from process: %d\n", thread_id);
            }
            #pragma omp barrier
        }
    }
    return 0;
}
```

Compiling and running our code should order our print statements as
such:

```
Hello from process: 0
Hello from process: 1
Hello from process: 2
Hello from process: 3
```


## Work Sharing Directive: `omp for`

OpenMP’s power comes from easily splitting a larger task into multiple
smaller tasks.  Work-sharing directives allow for simple and effective
splitting of normally serial tasks into fast parallel sections of
code. In this section we will learn how to implement the `omp for`
directive.

The directive `omp for` divides a normally serial for loop into a
parallel task. We can implement this directive as such:

```c++
#pragma omp for { … }
```


__Example__

Let’s write a program to add all the numbers between 1 and 1000. Begin with a `main` function
and the `stdio` and `omp` headers:

```c++
#include <stdio.h>
#include <omp.h>

int main(int argc, char** argv){
    return 0;
}
```

Now let’s go ahead and set up variables for our parallel code. Lets
first create variables `partial_Sum` and `total_Sum` to hold each
thread’s partial summation and to hold the total sum of all threads
respectively.

```c++
#include <stdio.h>
#include <omp.h>

int main(int argc, char** argv){
    int partial_Sum, total_Sum;

    return 0;
}
```

Next let’s begin our parallel section with `pragma omp parallel` . We
will also set `partial_Sum` to be a private variable and `total_Sum`
to be a shared variable. We shall initialize each variable in the
parallel section.

```c++
#include <stdio.h>
#include <omp.h>

int main(int argc, char** argv){
    int partial_Sum, total_Sum;

    #pragma omp parallel private(partial_Sum) shared(total_Sum)
    {
        partial_Sum = 0;
        total_Sum = 0;
    }
    return 0;
}
```

Let’s now set up our work sharing directive. We will use the `#pragma
omp for` to declare the loop as to be work sharing, followed by the
actual C++ loop. Because we want to add all numbers from 1 to 1000, we
will initialize our loop at one and end at 1000.

```c++
#include <stdio.h>
#include <omp.h>

int main(int argc, char** argv){
    int partial_Sum, total_Sum;

    #pragma omp parallel private(partial_Sum) shared(total_Sum)
    {
        partial_Sum = 0;
        total_Sum = 0;

        #pragma omp for
        for(int i = 1; i <= 1000; i++){
            partial_Sum += i;
        }

    }
    return 0;
}
```

Now we must join our threads. To do this, we must use a critical
directive to create a thread safe section of code. We do this with
`#pragma omp critical` directive. Lastly, we add `partial_Sum` to `total_Sum`
 and print out the result outside the parallel section of code.

```c++
#include <stdio.h>
#include <omp.h>

int main(int argc, char** argv){
    int partial_Sum, total_Sum;

    #pragma omp parallel private(partial_Sum) shared(total_Sum)
    {
        partial_Sum = 0;
        total_Sum = 0;

        #pragma omp for
        for(int i = 1; i <= 1000; i++){
            partial_Sum += i;
        }

        //Create thread safe region.
        #pragma omp critical
        {
            //add each threads partial sum to the total sum
            total_Sum += partial_Sum;
        }
    }
    printf("Total Sum: %d\n", total_Sum);
    return 0;
}
```

This will complete our parallel summation. Compiling and running
our code will result in this output:

```
Total Sum: 500500
```

``````

``````{tab-item} Fortran
:sync: ucb-prog-MPI-types-f

## Parallel “Hello, World” Program

In this section we will learn how to make a simple parallel hello
world program in Fortran.  Let’s begin with creation of a program
titled `parallel_hello_world.f90`. From the command line, run the
command:

```bash
nano parallel_hello_world.f90
```
We will begin with the program title and the use statement at the top of the program:

```fortran

PROGRAM Parallel_Hello_World
USE OMP_LIB
```

These flags allow us to utilize the omp library in our program. The
`USE OMP_LIB` line of code will provide OpenMP functionality.

Let’s now begin our program by constructing the main body of the
program. We will use `OMP_GET_THREAD_NUM()` to obtain the thread ID of
the process. This will let us identify each of our threads using that
unique ID number.

```fortran
PROGRAM Parallel_Hello_World
USE OMP_LIB

PRINT *, "Hello from process: ", OMP_GET_THREAD_NUM()

END
```

Let’s compile our code and see what happens. We must first load the
compiler module we want into our environment. We can do so as such:


(tabset-ref-openmp-f-module)=
`````{tab-set}
:sync-group: tabset-openmp-f

````{tab-item} GNU Fortran Compiler
:sync: openmp-f-openmpi

```bash
module load gcc
```

````

````{tab-item} Intel Fortran Compiler
:sync: openmp-f-intelmpi

```bash
module load intel
```

````
`````

From the command line, where your code is located, run the command:


(tabset-ref-openmp-f-compile)=
`````{tab-set}
:sync-group: tabset-openmp-f

````{tab-item} GNU Fortran Compiler
:sync: openmp-f-openmpi

```bash
gfortran parallel_hello_world.f90 -o parallel_hello_world.exe -fopenmp
```

````

````{tab-item} Intel Fortran Compiler
:sync: openmp-f-intelmpi

```bash
ifort parallel_hello_world.f90 -o parallel_hello_world.exe -qopenmp
```

````
`````

This will give us an executable we can run as a job on
a cluster. Simply run the job, telling Slurm to run the
executable. Your job script should look something like this:

```bash
#!/bin/bash

#SBATCH --nodes=1
#SBATCH --time=00:01:00
#SBATCH --partition=atesting
#SBATCH --qos=testing
#SBATCH --constraint=ib
#SBATCH --qos=testing
#SBATCH --ntasks=4
#SBATCH --job-name=Fortran_Hello_World
#SBATCH --output=Fortran_Hello_World.out

./parallel_hello_world.exe
```

Our output file should look like this:

```
Hello from process: 0
```

As you may have noticed, we only get one thread outputting a Hello
statement.

How do we parallelize the print statement? We parallelize it with `omp
parallel`!

The `!$OMP PARALLEL` and `!$OMP END PARALLEL` directives create a
section of code that is run from all available threads.

```fortran
PROGRAM Parallel_Hello_World
USE OMP_LIB

!$OMP PARALLEL

    PRINT *, "Hello from process: ", OMP_GET_THREAD_NUM()

!$OMP END PARALLEL

END
```

We must do one more thing before achieving parallelization. To set the
amount of threads we want OpenMP to run, we must set a Linux
environment variable to be specify how many threads we wish to
use. The environment variable `OMP_NUM_THREADS` will store this
information.  Changing this variable does not require recompilation of
the program, so this command can be placed in either the command
line or on your job script:

```bash
export OMP_NUM_THREADS=4
```

```{important}
This environment variable will need to be set
every time you exit your shell. If you would like to make this
change permanent you will need to add these lines to your
`.bash_profile` file in your home directory:

```bash
OMP_NUM_THREADS=4;
export OMP_NUM_THREADS
```

Now let’s re-compile the code and run it to see what happens:

(tabset-ref-openmp-f-recompile)=
`````{tab-set}
:sync-group: tabset-openmp-f

````{tab-item} GNU Fortran Compiler
:sync: openmp-f-openmpi

```bash
gfortran parallel_hello_world.f90 -o parallel_hello_world.exe -fopenmp
```

````

````{tab-item} Intel Fortran Compiler
:sync: openmp-f-intelmpi

```bash
ifort parallel_hello_world.f90 -o parallel_hello_world.exe -qopenmp
```

````
`````

Running our job script and we should end with an output file similar
to this one:

Hello from process: 3
Hello from process: 0
Hello from process: 2
Hello from process: 1

```{note}
Don’t worry about order of processes that printed, the threads
will print out at varying times.
```

## Private vs. Shared Variables

Memory management is an essential component of any parallel
program that involves data manipulation. In this section, we will
learn about the different variable types in OpenMP, as well as a simple
implementation of these types into the program we made in the previous
section.

OpenMP has a variety of tools that can be utilized to properly
indicate how the parallel program should handle variables. These tools
come in the forms of shared and private variable classifiers.

- Private classifiers create a copy of a variable for each process in
  the parallel system.

- Shared classifiers hold one instance of a variable for all processes
  to share.

To indicate private or shared variables, declare the variable before
your parallel section and annotate the `omp` directive as such:

```bash
!$OMP PARALLEL SHARED(shar_Var1) PRIVATE(priv_Var1, priv_Var2)
```

Variables that are created and assigned inside of a parallel section
of code will be inherently be private, and variables created outside
of parallel sections will be inherently public.

__Example__

Let’s adapt our ‘Hello World’ code to utilize private variables as an
example.  Starting with the code we left off with, let’s create a
variable to store the thread ID of each process. We will also change
the name of the program as good coding practice.

```fortran
PROGRAM Parallel_Stored_Hello
USE OMP_LIB

INTEGER :: thread_id

!$OMP PARALLEL

    PRINT *, "Hello from process: ", OMP_GET_THREAD_NUM()

!$OMP END PARALLEL

END
```

Now let’s define `thread_id` as a private variable. Because we want
each task to have a unique thread ID, using the `private(thread_id)`
will create a separate instance of `thread_id` for each task.

```fortran
PROGRAM Parallel_Stored_Hello
USE OMP_LIB

INTEGER :: thread_id

!$OMP PARALLEL PRIVATE(thread_id)

    PRINT *, "Hello from process: ", OMP_GET_THREAD_NUM()

!$OMP END PARALLEL

END
```

Lastly, let’s assign the thread ID to our private variable and print
out the variable instead of the `OMP_GET_THREAD_NUM()` function call:

```fortran
PROGRAM Parallel_Stored_Hello
USE OMP_LIB

INTEGER :: thread_id

!$OMP PARALLEL PRIVATE(thread_id)

    thread_id = OMP_GET_THREAD_NUM()
    PRINT *, "Hello from process: ", thread_id

!$OMP END PARALLEL

END
```

Compiling and running our code will result in a similar result to
our original Hello World:

```
Hello from process: 3
Hello from process: 0
Hello from process: 2
Hello from process: 1
```

## Barrier and Critical Directives

OpenMP has a variety of tools for managing processes. One of the more
prominent forms of control comes with the `BARRIER`:

```fortran
!$OMP BARRIER
```

...and the `CRITICAL` directives:

```fortran
!$OMP CRITICAL
...
!$OMP END CRITICAL
```

The `BARRIER` directive stops all processes for proceeding to the next
line of code until all processes have reached the barrier. This allows
a programmer to synchronize processes in the parallel program.

A `CRITICAL` directive ensures that a line of code is only run by one
process at a time, ensuring thread safety in the body of code.


__Example__

Let's implement an OpenMP barrier by making our ‘Hello World’ program
print its processes in order. Beginning with the code we created in
the previous section, let’s nest our print statement in a loop which
will iterate from 0 to the max thread count. We will retrieve the max
thread count using the OpenMP function:

```fortran
OMP_GET_MAX_THREADS()
```

Our ‘Hello World’ program will now look like:

```fortran
PROGRAM Parallel_Ordered_Hello
USE OMP_LIB

INTEGER :: thread_id

!$OMP PARALLEL PRIVATE(thread_id)

    thread_id = OMP_GET_THREAD_NUM()
    DO i=0,OMP_GET_MAX_THREADS()
        PRINT *, "Hello from process: ", thread_id
    END DO

!$OMP END PARALLEL

END
```

Now that the loop has been created, let’s create a conditional that
will stop a process from printing its thread number until the loop
iteration matches its thread number:

```fortran
PROGRAM Parallel_Ordered_Hello
USE OMP_LIB

INTEGER :: thread_id

!$OMP PARALLEL PRIVATE(thread_id)

    thread_id = OMP_GET_THREAD_NUM()

    DO i=0,OMP_GET_MAX_THREADS()
        IF (i == thread_id) THEN
            PRINT *, "Hello from process: ", thread_id
        END IF
    END DO
!$OMP END PARALLEL

END
```

Lastly, to ensure one process doesn’t get ahead of another, we need to
add a barrier directive in the code. Let’s implement one in our loop.

```fortran
PROGRAM Parallel_Ordered_Hello
USE OMP_LIB

INTEGER :: thread_id

!$OMP PARALLEL PRIVATE(thread_id)
    thread_id = OMP_GET_THREAD_NUM()

    DO i=0,OMP_GET_MAX_THREADS()
        IF (i == thread_id) THEN
            PRINT *, "Hello from process: ", thread_id
        END IF
        !$OMP BARRIER
    END DO
!$OMP END PARALLEL

END
```

Compiling and running our code should order our print statements as
such:

```fortran
Hello from process: 0
Hello from process: 1
Hello from process: 2
Hello from process: 3
```


## Work Sharing Directive: `omp do`

OpenMP’s power comes from easily splitting a larger task into multiple
smaller tasks.  Work-sharing directives allow for simple and effective
splitting of normally serial tasks into fast parallel sections of
code. In this section we will learn how to implement the `!$OMP DO` directive.
The directive `!$OMP DO` divides a normally serial for loop into a
parallel task. We can implement this directive as such:

```fortran
!$OMP DO
...
!$OMP END DO
```

__Example__

Let’s write a program to add all the numbers between 1 and 1000. Begin
with a program title and the `OMP_LIB` header:

```fortran
PROGRAM Parallel_Do
USE OMP_LIB

END
```

Now let’s go ahead and set up variables for our parallel code. Let’s
first create variables `partial_Sum` and `total_Sum` to hold each
thread’s partial summation and to hold the total sum of all threads
respectively.

```fortran
PROGRAM Parallel_Hello_World
USE OMP_LIB

INTEGER :: partial_Sum, total_Sum

END
```

Next let’s begin our parallel section with `!$OMP PARALLEL` . We will
also set `partial_Sum` to be a private variable and `total_Sum` to be
a shared variable. We shall initialize each variable in the parallel
section.

```fortran
PROGRAM Parallel_Hello_World
USE OMP_LIB

INTEGER :: partial_Sum, total_Sum

!$OMP PARALLEL PRIVATE(partial_Sum) SHARED(total_Sum)

    partial_Sum = 0;
    total_Sum = 0;

!$OMP END PARALLEL

END
```

Let’s now set up our work sharing directive. We will use the `!$OMP
DO` to declare the loop to be work sharing, followed by the actual
Fortran loop. Because we want to add all number from 1 to 1000, we
will initialize our loop at one and end at 1000.

```fortran
PROGRAM Parallel_Hello_World
USE OMP_LIB

INTEGER :: partial_Sum, total_Sum

!$OMP PARALLEL PRIVATE(partial_Sum) SHARED(total_Sum)
    partial_Sum = 0;
    total_Sum = 0;

    !$OMP DO
    DO i=1,1000
        partial_Sum = partial_Sum + i
    END DO

!$OMP END PARALLEL
END
```

Now we must join our threads. To do this we must use a critical
directive to create a thread safe section of code. We do this with the
`!$OMP CRITICAL` directive. Lastly we add `partial_Sum` to `total_Sum` and
print out the result outside the parallel section of code.

```fortran
PROGRAM Parallel_Hello_World
USE OMP_LIB

INTEGER :: partial_Sum, total_Sum

!$OMP PARALLEL PRIVATE(partial_Sum) SHARED(total_Sum)
    partial_Sum = 0;
    total_Sum = 0;

    !$OMP DO
    DO i=1,1000
        partial_Sum = partial_Sum + i
    END DO
    !$OMP END DO

    !$OMP CRITICAL
        total_Sum = total_Sum + partial_Sum
    !$OMP END CRITICAL

!$OMP END PARALLEL
PRINT *, "Total Sum: ", total_Sum

END
```

This will complete our parallel summation. Compiling and running
our code will result in this output:

```
Total Sum: 500500
```

``````
```````
