variable "resource_group_name" {
  description = "Nome del Resource Group"
  type        = string
  default     = "rg-hoop-insights"
}

variable "location" {
  description = "Regione di Azure"
  type        = string
  default     = "italynorth"
}

variable "cluster_name" {
  description = "Nome del cluster AKS"
  type        = string
  default     = "aks-hoop-insights"
}

variable "node_count" {
  description = "Numero di nodi nel cluster"
  type        = number
  default     = 2
}

variable "node_vm_size" {
  description = "Dimensione delle macchine virtuali dei nodi"
  type        = string
  default     = "Standard_DS2_v2"
}
