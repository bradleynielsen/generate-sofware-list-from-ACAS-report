Add-Type -AssemblyName PresentationFramework
$scriptRoot  = $PSScriptRoot
$pythonFile  = (ls $scriptRoot\*.py ).FullName
$python      = (ls "$scriptRoot\python*\python.exe" ).FullName
$csvpath     = "$scriptRoot\csv"
$resultspath = "$scriptRoot\results"

if (!(test-path -path $csvpath)){
    mkdir $csvpath
    "Making csv folder"
    [System.Windows.MessageBox]::Show('`csv` folder created. Add your ACAS reports to it before continuing.','Missing CSV files')
}

if (!(test-path -path $resultspath)){
    mkdir $resultspath
    "Making results folder"
}

& $python $pythonFile 

explorer $scriptRoot\results
pause
exit