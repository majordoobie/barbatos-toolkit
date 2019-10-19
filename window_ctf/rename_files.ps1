#$path = Read-Host -Prompt 'Tell me your dir path, big boi'
$path = "C:\users\SgtMa\OneDrive\root\Cyberdomains\OSCP\pwk-30962-310211\media\video"

# Just break if the user gives you a file not a directory 
if (-not (test-path -path $path -PathType Container)){
    write-host "Path must be a directory"
    exit
} else {
    write-host "You got yourself a lil directory dude"
}

# Otherwise get the array of file names, obvi check if the array even exists 
$files = Get-ChildItem $path
if ($files.count -gt 0) {
    foreach ($file in $files) {
        #get-member -inputObject $file
        $chapter = $file.name.split('-')[-1].split('.')[0]
        rename-item $file.fullname -NewName $chapter"_OSCP_Video.mp4"
    }
}
