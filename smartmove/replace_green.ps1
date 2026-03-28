$files = @(
  'css\style.css',
  'css\fakeLoader.css',
  'e-menu.html',
  'e-menuenglish.html',
  'index.html'
)

foreach ($f in $files) {
  $path = Join-Path (Get-Location) $f
  if (-not (Test-Path $path)) { Write-Host "SKIP: $f"; continue }
  $content = [System.IO.File]::ReadAllText($path, [System.Text.Encoding]::UTF8)

  # rgba — preserve alpha channel
  $content = [regex]::Replace($content, 'rgba\(69,\s*255,\s*23,\s*([^)]+)\)', 'rgba(159, 212, 95, $1)')

  # rgb solid
  $content = [regex]::Replace($content, 'rgb\(69,\s*255,\s*23\)', '#9FD45F')

  # hex variants (case-insensitive)
  $content = [regex]::Replace($content, '(?i)#45FF17', '#9FD45F')
  $content = [regex]::Replace($content, '(?i)#1ad66c', '#9FD45F')

  [System.IO.File]::WriteAllText($path, $content, [System.Text.Encoding]::UTF8)
  Write-Host "DONE: $f"
}
