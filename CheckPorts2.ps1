function Obtener-DireccionIP {
    param(
        [string]$url
    )
    try {
        $dominio = $url -replace '^https?://(www\.)?', ''
        $dominio = $dominio -replace '/.*', ''
        $dominio += ".com.mx"
        $direccionIP = [System.Net.Dns]::GetHostAddresses($dominio) | Where-Object {$_.AddressFamily -eq "InterNetwork"} | Select-Object -First 1
        if ($direccionIP) {
            return $direccionIP.IPAddressToString
        } else {
            Write-Host "No se pudo obtener la dirección IP para la URL $url."
        }
    } catch {
        Write-Host "Error al obtener la dirección IP para la URL ${url}: $_"
    }
}

$rutaArchivo = Read-Host "Ingrese la ruta del archivo de texto que contiene las URLs a analizar"
if (Test-Path $rutaArchivo) {
    $urls = Get-Content $rutaArchivo
    $directorioScript = Split-Path -Parent $MyInvocation.MyCommand.Definition
    foreach ($url in $urls) {
        $direccionIP = Obtener-DireccionIP -url $url
        if ($direccionIP -ne $null) {
            $resultados = & "D:\Python\python.exe" "$directorioScript\ScanPorts.py" $direccionIP
            $nombreArchivo = "resultados_puertos_$($direccionIP.Replace('.', '_')).txt"
            $rutaCompleta = Join-Path -Path $directorioScript -ChildPath $nombreArchivo
            $resultados | Out-File -FilePath $rutaCompleta -Append
            Write-Host "Los resultados de los puertos se han guardado en $rutaCompleta."
        } else {
            Write-Host "No se pudo obtener la dirección IP para la URL $url."
        }
    }
} else {
    Write-Host "El archivo especificado no existe."
}
