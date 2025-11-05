## Jour 1 - Introduction à Kubernetes
- Objectif : Comprendre les concepts de base de Kubernetes.
- Différences entre Docker et Kubernetes.
- Concepts clés :
- Cluster (Maître et nœuds).
- Pod (l'unité de base de déploiement).
- Service (exposition et communication).
- Installation et configuration de Minikube.
- Commandes essentielles : kubectl.

## Jour 2 - Pods et Déploiements
- Objectif : Déployer et gérer des applications de base.
- Création d’un Pod à partir d’un fichier YAML.
- Différence entre Pods et Déploiements.
- Déploiement d’une application simple (par exemple, une application web Nginx).
- Mise à jour d’une application (rolling updates et rollbacks).
- Jour 3 : Services et Réseautage
- Objectif : Exposer des applications et comprendre les réseaux Kubernetes.
- Types de Services :
- ClusterIP
- NodePort
- LoadBalancer
- Exposition d’un Pod à l’extérieur du cluster.
- Utilisation de Minikube pour accéder aux Services.

## Jour 4 - Configuration et Stockage
- Objectif : Gérer les configurations et le stockage dans Kubernetes.
- Variables d’environnement et ConfigMaps.
- Secrets pour les données sensibles.
- Introduction aux volumes :
- Volumes persistants (PersistentVolume, PersistentVolumeClaim).
- Exemple pratique : Ajouter un volume à un Pod.

## Jour 5 è Orchestration Avancée
- Objectif : Automatiser les tâches et gérer des applications complexes.
- Liveness et Readiness Probes.
- Horizontal Pod Autoscaler.
- Utilisation des Jobs et CronJobs.
- Exemple pratique : Orchestrer une tâche périodique avec un CronJob.

## Jour 6 - Surveillance et Logs
- Objectif : Surveiller un cluster Kubernetes et analyser les logs.
- Commandes pour visualiser l’état des Pods, nœuds et ressources : kubectl get, kubectl describe, kubectl logs.
- Introduction aux métriques Kubernetes.
- Intégration avec des outils comme Prometheus et Grafana (en option).

## Jour 7 - Conclusion et Intégration AWX
- Objectif : Intégrer Kubernetes avec AWX et approfondir.
- Déploiement et gestion d’applications via AWX.
- Exploration des extensions Kubernetes :
- Helm Charts.
- Opérateurs.
- Étapes pour aller plus loin :
- Clusters multi-nœuds.
- Kubernetes en production (surveillance, sécurité).
