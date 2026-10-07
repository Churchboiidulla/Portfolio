param(
    [string]$Name = "World"
)

$repoRoot = Split-Path -Parent $MyInvocation.MyCommand.Path
$venv = Join-Path $repoRoot ".venv"
$pythonExe = Join-Path $venv "Scripts\python.exe"

if (-not (Test-Path $pythonExe)) {
    Write-Host "Virtual environment not found. Creating venv at $venv..."
    python -m venv $venv
}

if (-not (Test-Path $pythonExe)) {
    Write-Error "Python executable not found in venv. Ensure Python is installed and on PATH."
    exit 1
}

& $pythonExe (Join-Path $repoRoot "scripts\hello.py") --name $Name
