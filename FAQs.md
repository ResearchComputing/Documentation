Questions:

[How do I check how full my Summit directories are?](#how-do-i-check-how-full-my-summit-directories-are?)

### How do I check how full my Summit directories are?

You have three directories allocated to your username ($USER).  These include `/home/$USER` (2 G), `/projects/$USER` (250 G) and `/scratch/summit/$USER` (10 T).  To see how much space you've used in each, from a Summit 'scompile' node, type `curc-quota` as follows:

`[janedoe@shas0136 ~]$ curc-quota`<cr>
`------------------------------------------------------------------------`<cr>
                                       ``Used         Avail    Quota Limit`
`------------------------------------------------------------------------`
`/home/janedoe                          1.7G          339M           2.0G`
`/projects/janedoe                       67G          184G           250G`
`/scratch/summit                         29G        10211G         10240G`