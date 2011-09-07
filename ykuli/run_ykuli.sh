#!/bin/bash

failed=0
xterm &
xpid=$!

cd tests


for t in *.sikuli/
do

	echo -n "testing $t... "
	result=`sikuli -s -r $t 2>&1 `

	if [ $? -ne 255 ]; then
		# starting sikuli failed
		echo FAILED
		failed=`expr $failed + 1`
	else
		echo $result | grep "Error" > /dev/null
		if [ $? -eq 1 ]; then
			# tast passed
			echo okay
		else
			# test failed
			echo FAILED	
			failed=`expr $failed + 1`
			killall y2base
		fi
	fi
done

if [ $failed -eq 0 ]; then
	echo "all tests successfully finished"
else
	echo "$failed tests FAILED"
fi
kill $xpid
