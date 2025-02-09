output "aks_name" {
  description = "Nome del cluster AKS"
  value       = azurerm_kubernetes_cluster.aks.name
}

output "kube_config" {
  description = "Configurazione per connettersi al cluster AKS"
  value       = azurerm_kubernetes_cluster.aks.kube_config_raw
  sensitive   = true
}
