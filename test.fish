#!/usr/bin/env fish

# with a command
python batch_run.py $INPUTDIR $OUTPUTDIR "command --option {0} {1}"

# without a command. not yet working
# python batch_run.py $INPUTDIR $OUTPUTDIR

# only one dir, no command. not yet working
# python batch_run.py $INPUTDIR

# only one dir, with command. not yet working
# python batch_run.py $INPUTDIR "command --option {0} {1}"
