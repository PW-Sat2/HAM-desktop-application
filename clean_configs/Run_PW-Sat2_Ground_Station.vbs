Set oShell = CreateObject ("Wscript.Shell") 
Dim strArgs
strArgs = "cmd /c main\\main.exe"
oShell.Run strArgs, 0, false
