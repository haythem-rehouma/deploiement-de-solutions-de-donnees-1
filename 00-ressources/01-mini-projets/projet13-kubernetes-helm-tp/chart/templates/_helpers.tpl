{{/*
Nom complet d'une ressource : "<release>-<composant>".
Usage : {{ include "hedge.fullname" (dict "root" . "composant" "portail") }}
Exemple : release = "hedge-dev", composant = "portail" -> "hedge-dev-portail"
*/}}
{{- define "hedge.fullname" -}}
{{- printf "TODO" .root.Release.Name .composant | trunc 63 | trimSuffix "-" -}}
{{- end -}}


{{/*
Labels communs a toutes les ressources.
Usage : {{ include "hedge.labels" (dict "root" . "composant" "portail") | nindent 4 }}

? Renseignez les 7 labels demandes dans la Mission 3 :
    app.kubernetes.io/name
    app.kubernetes.io/instance
    app.kubernetes.io/component
    app.kubernetes.io/managed-by
    app.kubernetes.io/version
    helm.sh/chart
    hedge/environment
*/}}
{{- define "hedge.labels" -}}
app.kubernetes.io/name: TODO
app.kubernetes.io/instance: TODO
app.kubernetes.io/component: TODO
# ? completez les 4 lignes manquantes
{{- end -}}


{{/*
Selector labels : SOUS-ENSEMBLE STABLE des labels ci-dessus.
Ne JAMAIS y inclure de valeur variable dans le temps (version, revision, env)
sous peine de "spec.selector: field is immutable" au premier upgrade.
Usage : {{ include "hedge.selectorLabels" (dict "root" . "composant" "portail") | nindent 6 }}

? Mettez ici SEULEMENT les 3 labels strictement immuables pour une instance.
*/}}
{{- define "hedge.selectorLabels" -}}
# ? les 3 labels immuables uniquement
{{- end -}}
