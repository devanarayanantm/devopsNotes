try
{



    if ( test-path -path "$env:USERPROFILE\Dessssktop")
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
    
    write-host "Error: $error"
}