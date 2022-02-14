#!/usr/bin/env fish

set testdir (mktemp --tmpdir -d batch-test-XXX)
set inputdir $testdir/input
mkdir $inputdir
set outputdir $testdir/output
mkdir $outputdir
for x in (seq 5)
    touch $inputdir/file-$x.ogg
end
tree $testdir

echo "# use the following directories for testing"
echo "# bash"
echo INPUTDIR=$inputdir
echo OUTPUTDIR=$outputdir
echo
echo "# fish"
echo set INPUTDIR $inputdir
echo set OUTPUTDIR $outputdir