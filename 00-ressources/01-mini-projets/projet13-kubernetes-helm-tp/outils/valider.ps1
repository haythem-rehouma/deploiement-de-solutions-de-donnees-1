# ---------------------------------------------------------------------------
# Script de validation projet13 (Helm) — donne un score, JAMAIS la solution.
# Usage :  .\outils\valider.ps1
# ---------------------------------------------------------------------------

$total = 0

function Existe-Release($nom, $namespace) {
    helm status $nom -n $namespace 2>$null | Out-Null
    return $LASTEXITCODE -eq 0
}

function Afficher($libelle, $points, $max, $note) {
    $etat = if ($points -eq $max) { "[OK]    " } else { "[ECHEC] " }
    $ligne = "{0} {1} {2}/{3}" -f $etat, $libelle.PadRight(36, '.'), $points, $max
    if ($note) { $ligne += "   -> $note" }
    Write-Host $ligne
}

Write-Host ""
Write-Host "=== VALIDATION projet13 : Helm multi-environnement ===" -ForegroundColor Cyan
Write-Host ""

# --- Mission 1 : Chart valide -----------------------------------------------
$p = 0; $note = ""
$lint = helm lint .\chart 2>&1
if ($LASTEXITCODE -ne 0) { $note = "helm lint echoue" }
else {
    $chartYaml = Get-Content .\chart\Chart.yaml -Raw -ErrorAction SilentlyContinue
    if (-not $chartYaml) { $note = "Chart.yaml introuvable" }
    elseif ($chartYaml -notmatch "apiVersion:\s*v2") { $note = "Chart.yaml doit etre apiVersion v2" }
    elseif ($chartYaml -notmatch "type:\s*application") { $note = "Chart.yaml doit declarer type: application" }
    else { $p = 10 }
}
Afficher "Mission 1 - Chart valide" $p 10 $note; $total += $p

# --- Mission 2 : templates portail + api -----------------------------------
$p = 0; $note = ""
$rendu = helm template check .\chart -f .\chart\environments\values-dev.yaml 2>&1
if ($LASTEXITCODE -ne 0) { $note = "helm template echoue" }
else {
    $rendu = ($rendu -join "`n")
    if ($rendu -notmatch "kind:\s*Deployment[\s\S]*?name:\s*check-portail") { $note = "Deployment portail : nom attendu 'check-portail'" }
    elseif ($rendu -notmatch "kind:\s*Deployment[\s\S]*?name:\s*check-api") { $note = "Deployment api : nom attendu 'check-api'" }
    elseif ($rendu -notmatch "kind:\s*Service[\s\S]*?name:\s*check-portail") { $note = "Service portail introuvable" }
    elseif ($rendu -notmatch "kind:\s*Service[\s\S]*?name:\s*check-api") { $note = "Service api introuvable" }
    else { $p = 20 }
}
Afficher "Mission 2 - Templating de base" $p 20 $note; $total += $p

# --- Mission 3 : helpers et labels ------------------------------------------
$p = 0; $note = ""
$helpersFile = Get-Content .\chart\templates\_helpers.tpl -Raw -ErrorAction SilentlyContinue
if (-not $helpersFile) { $note = "_helpers.tpl introuvable" }
elseif ($helpersFile -notmatch 'define\s+"hedge\.fullname"') { $note = "helper hedge.fullname manquant" }
elseif ($helpersFile -notmatch 'define\s+"hedge\.labels"') { $note = "helper hedge.labels manquant" }
elseif ($helpersFile -notmatch 'define\s+"hedge\.selectorLabels"') { $note = "helper hedge.selectorLabels manquant" }
else {
    $rendu = helm template check .\chart -f .\chart\environments\values-dev.yaml 2>&1
    $rendu = ($rendu -join "`n")
    if ($rendu -notmatch 'app\.kubernetes\.io/name:\s*hedge') { $note = "label app.kubernetes.io/name absent" }
    elseif ($rendu -notmatch 'app\.kubernetes\.io/component:\s*portail') { $note = "label component=portail absent" }
    elseif ($rendu -notmatch 'app\.kubernetes\.io/component:\s*api') { $note = "label component=api absent" }
    else { $p = 15 }
}
Afficher "Mission 3 - Helpers et labels" $p 15 $note; $total += $p

# --- Mission 4 : trois environnements ---------------------------------------
$p = 0; $notes = @()
foreach ($env in @(
    @{ nom="dev";     port="30130"; replicas="1"; couleur="#2563eb" },
    @{ nom="staging"; port="30131"; replicas="2"; couleur="#ea580c" },
    @{ nom="prod";    port="30132"; replicas="3"; couleur="#16a34a" })) {

    $fichier = ".\chart\environments\values-$($env.nom).yaml"
    if (-not (Test-Path $fichier)) { $notes += "$($env.nom) : $fichier manquant"; continue }
    $c = Get-Content $fichier -Raw
    if ($c -notmatch "environment:\s*$($env.nom)") { $notes += "$($env.nom) : environment mal defini" }
    elseif ($c -notmatch "nodePort:\s*$($env.port)") { $notes += "$($env.nom) : nodePort attendu $($env.port)" }
    elseif ($c -notmatch "replicas:\s*$($env.replicas)") { $notes += "$($env.nom) : replicas attendu $($env.replicas)" }
    elseif ($c -notmatch [regex]::Escape($env.couleur)) { $notes += "$($env.nom) : couleur attendue $($env.couleur)" }
    else { $p += 5 }

    # bonus : release deployee ?
    if (Existe-Release "hedge-$($env.nom)" "hedge-$($env.nom)") { $p += 2 }
}
if ($p -gt 20) { $p = 20 }
Afficher "Mission 4 - Trois environnements" $p 20 ($notes -join " | "); $total += $p

# --- Mission 5 : upgrade + rollback ------------------------------------------
$p = 0; $note = ""
if (-not (Existe-Release "hedge-dev" "hedge-dev")) { $note = "release hedge-dev absente : impossible de verifier" }
else {
    $hist = helm history hedge-dev -n hedge-dev -o json 2>$null
    if (-not $hist) { $note = "impossible de lire l'historique" }
    else {
        $revisions = ($hist | ConvertFrom-Json)
        if ($revisions.Count -lt 2) { $note = "moins de 2 revisions : faites au moins un helm upgrade" }
        else {
            $aRollback = $revisions | Where-Object { $_.description -like "*Rollback*" }
            if (-not $aRollback) { $note = "aucun rollback detecte dans l'historique" }
            else { $p = 10 }
        }
    }
}
Afficher "Mission 5 - Upgrade + rollback" $p 10 $note; $total += $p

# --- Mission 6 : reparations des 3 pannes -----------------------------------
$p = 0; $notes = @()
$tpldir = ".\chart\templates"

# 6.1 : ConfigMap doit contenir Release.Name (soit inclure via helper, soit .Release.Name direct)
$cm = Get-ChildItem $tpldir -Filter "*configmap*" -File -ErrorAction SilentlyContinue | Select-Object -First 1
if (-not $cm) { $notes += "casse-1 : ConfigMap non deploye" }
else {
    $c = Get-Content $cm.FullName -Raw
    if ($c -match 'name:\s*hedge-config\s*$' -or $c -match 'name:\s*"hedge-config"') { $notes += "casse-1 : nom toujours en dur" }
    elseif ($c -match '\.Release\.Name' -or $c -match 'hedge\.fullname') { $p += 7 }
    else { $notes += "casse-1 : nom non prefixe par la release" }
}

# 6.2 : worker deployment ne doit PAS contenir hedge/environment dans matchLabels
$wk = Get-ChildItem $tpldir -Filter "*worker*" -File -ErrorAction SilentlyContinue | Select-Object -First 1
if (-not $wk) { $notes += "casse-2 : worker non deploye" }
else {
    $c = Get-Content $wk.FullName -Raw
    # Isoler le bloc matchLabels (jusqu'a la prochaine cle YAML au meme niveau ou moins)
    $m = [regex]::Match($c, 'matchLabels:\s*\r?\n((?:[ \t]{6,}.+\r?\n)+)')
    $bloc = if ($m.Success) { $m.Groups[1].Value } else { "" }
    if ($bloc -match 'hedge/environment' -or $bloc -match '\.Values\.environment') {
        $notes += "casse-2 : label variable toujours dans matchLabels"
    } else { $p += 7 }
}

# 6.3 : cache deployment doit utiliser .Values.portail (pas portal)
$ca = Get-ChildItem $tpldir -Filter "*cache*" -File -ErrorAction SilentlyContinue | Select-Object -First 1
if (-not $ca) { $notes += "casse-3 : cache non deploye" }
else {
    $c = Get-Content $ca.FullName -Raw
    if ($c -match '\.Values\.portal\.') { $notes += "casse-3 : typo .Values.portal toujours present" }
    else { $p += 6 }
}
if ($p -gt 20) { $p = 20 }
Afficher "Mission 6 - Reparations (3 pannes)" $p 20 ($notes -join " | "); $total += $p

Write-Host ""
$couleur = if ($total -ge 90) { "Green" } elseif ($total -ge 50) { "Yellow" } else { "Red" }
Write-Host ("SCORE AUTOMATIQUE : {0} / 95" -f $total) -ForegroundColor $couleur
Write-Host "   (+5 pour la qualite du rapport, +5 de bonus : evalues manuellement)" -ForegroundColor DarkGray
Write-Host ""
Write-Host "Ouvrez les 3 tableaux de bord dans votre navigateur :" -ForegroundColor DarkGray
Write-Host "  DEV     -> http://localhost:30130" -ForegroundColor DarkGray
Write-Host "  STAGING -> http://localhost:30131" -ForegroundColor DarkGray
Write-Host "  PROD    -> http://localhost:30132" -ForegroundColor DarkGray
Write-Host ""
