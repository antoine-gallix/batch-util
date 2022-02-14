#!/usr/bin/env fish

# with a command
set command python batch_run.py $INPUTDIR $OUTPUTDIR "command --option {0} {1}"
echo $command
eval $command

# without a command. not yet working
set command python batch_run.py $INPUTDIR $OUTPUTDIR
echo $command
eval $command

# only one dir, no command.
set command python batch_run.py $INPUTDIR
echo $command
eval $command

# only one dir, with command. not yet working
set command "python batch_run.py $INPUTDIR --command 'command --option {}'"
echo $command
eval $command
