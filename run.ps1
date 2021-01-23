$scriptRoot = $PSScriptRoot
$pythonFile = (ls $scriptRoot\*.py ).FullName
$python     = (ls "$scriptRoot\python*\python.exe" ).FullName

& $python $pythonFile 

explorer $scriptRoot\results
pause
exit