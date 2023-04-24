# prevents mac from going to sleep until python process exits.
# run this script AFTER running 'python pollevbot/main.py'
py_file="pollevbot/main.py"
pid=$(pgrep -f "$py_file")
if [[ "$pid" == "" ]]
then
  echo "Couldn't find python process id for '$py_file'."
  echo "Make sure you are running this script after already running 'python $py_file'."
else
  echo "Python process $py_file located with pid $pid."
  echo "Preventing sleep until process exits..."
  caffeinate -w "$pid"
  echo "Process exited."
fi