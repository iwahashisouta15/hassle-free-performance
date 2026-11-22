# Capture baseline Unreal Insights dan PresentMon dari command prompt.
# Sesuaikan executable dan project path sebelum dipakai.

param(
    [Parameter(Mandatory=$true)]
    [string]$UnrealEditorExe,

    [Parameter(Mandatory=$true)]
    [string]$ProjectPath,

    [string]$MapName = "OutdoorSettlement",
    [int]$DurationSeconds = 90,
    [int]$Runs = 3
)

Write-Host "UE5.4 H-F-P Benchmark"
Write-Host "Map: $MapName"
Write-Host "Duration: $DurationSeconds seconds"
Write-Host "Runs: $Runs"
Write-Host "NOTE: Use the same route and camera for every run."

for ($i = 1; $i -le $Runs; $i++) {
    $timestamp = Get-Date -Format "yyyyMMdd-HHmmss"
    $traceFile = "insights-run-$i-$timestamp.utrace"
    Write-Host "Run $i/$Runs - start Unreal Insights capture"

    & $UnrealEditorExe $ProjectPath -Map=$MapName -statnamedevents -trace=start -tracefile=$traceFile

    Start-Sleep -Seconds $DurationSeconds
}
