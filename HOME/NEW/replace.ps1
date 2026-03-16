$file = 'c:\Users\NgocDuong\Downloads\NEW\AR\HOME\NEW\index.html'
$content = [System.IO.File]::ReadAllText($file, [System.Text.Encoding]::UTF8)

$startMarker = '<!-- ======= ÔN TẬP CHỦ ĐỀ SECTION ======= -->'
$endMarker = '</section>'

$startIdx = $content.IndexOf($startMarker)
if ($startIdx -lt 0) {
    Write-Host "Start marker not found"
    exit 1
}

$endIdx = $content.IndexOf($endMarker, $startIdx)
if ($endIdx -lt 0) {
    Write-Host "End marker not found"
    exit 1
}
$endIdx = $endIdx + $endMarker.Length

$newContent = [System.IO.File]::ReadAllText('c:\Users\NgocDuong\Downloads\NEW\AR\HOME\NEW\replace.py', [System.Text.Encoding]::UTF8)
$newContentStart = $newContent.IndexOf($startMarker)
$newContentEnd = $newContent.LastIndexOf($endMarker) + $endMarker.Length

if ($newContentStart -lt 0 -or $newContentEnd -lt 0) {
    Write-Host "Could not extract new content"
    exit 1
}

$replacement = $newContent.Substring($newContentStart, $newContentEnd - $newContentStart)

$finalContent = $content.Substring(0, $startIdx) + $replacement + $content.Substring($endIdx)
[System.IO.File]::WriteAllText($file, $finalContent, [System.Text.Encoding]::UTF8)

Write-Host "Successfully replaced on-tap section"
