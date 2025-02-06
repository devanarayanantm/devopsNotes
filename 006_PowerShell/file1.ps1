# if ( get-childitem | where-object { $_.name -like "desktop"} )
# {
#     write-host "Desktop folder exists"
# }
# else
# {
#     write-host "Desktop folder does not exist"
# }


try
{


    
    $Path=[Environment]::Getfolderpath("Desktopdirectory")
    echo $Path
     
    if (Test-Path $Path -pathtype container)
    {
        write-host "Desktop folder exists"
    }
    else
    {
        write-host "Desktop folder does not exist"
    }
}
catch
{
    "error in line number $($_.invocationinfo.scriptlinenumber) : $($error[0])"
}