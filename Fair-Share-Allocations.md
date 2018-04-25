## Table of Contents

- [Overview](#overview)
- [Why Do I Need An Allocation](#why-do-i-need-an-allocation)
- [What is Fair Share](#what-is-fair-share)
- [Fair Share Target Percentage](#fair-share-target-percentage)

# Overview

Allocations are a crucial component of running on an HPC system.  They are required to run on RC resources.  When you receive an account you will automatically be assigned a ucb-general allocation, which is intended for you to use to test and benchmark your code.  After you have done this, you should apply for a [project allocation](https://www.colorado.edu/rc/userservices/allocations) to run on our systems.  

In this document, we will describe the allocation process and how Fair Share works to give priority.

# Why Do I Need An Allocation

Having an account only validates that you are eligible to use RC resources.  An allocation allows us to keep track of your use of the system.  This is important because:
   * We need to make sure we have enough resources to accommodate all of our users
   * Helps for reporting to NSF and the CU Research & Innovation Office

# What is Fair Share?

On some of our older systems, allocations have been treated as a bank account.  You apply for an allocation and receive a certain number of hours based on your benchmark tests, and once you've used those hours they are gone.  If it is Christmas Day and you are ready to run, but have no hours, and the system is under-utilized, our resources and your time are wasted.  Fair share improves upon that, and balances out the load usage in a more appropriate way for all users.

Fair share scheduling starts in the allocation application process.  When you are running in ucb-general, you receive a pre-determined priority (see below).  When you apply for a project allocation, you will still ask for a certain number of hours based on the benchmarking you did in ucb-general.  Fair share scheduling will then use a complex formula to determine your priority in queue, based on these numbers, our determination of your needs, and general utilization.  From this information, you will be assigned a fair share target percentage, and your utilization of your "fair share" on the system will be based on historical usage and how far under or over the fair share target percentage you are.

# Fair Share Target Percentage

For project allocations, your target percentage depends on your priority based on your project proposal (as described above).  Everyone not associated with a project shares a target percentage of 13% (20% of the CU fraction).  Your jobs are likely to have a lower priority if you are running in ucb-general than if you are running with a target percentage assigned from writing a project allocation proposal.

Everyone therefore has an assigned target percentage, and your priority will depend upon how far under or over thatt target percentage you are based on a four week average.  If you are under (over) your four week target percentage, your priority is increased (decreased).  Information on how to check your fair share priority level can be found [here](https://github.com/ResearchComputing/Research-Computing-User-Tutorials/wiki/FAQs#where-is-my-current-fair-share-priority-level-at).

Finally - just a reminder that this only impacts pending jobs.  If there are no other pending jobs and enough resources are available then your job will run regardless of your previous usage!
