# 🛰️ Thread GPS Tracking Platform

## ▶️ Lancer le projet (3 commandes)

```bash
git clone <repo>
cd gps-minimal
docker-compose up --build
```

Puis ouvrir : **http://localhost:3000**

---

## 📁 Structure

```

---

## 🔌 Services

| Service | URL | Rôle |
|---------|-----|------|
| WebUI | http://localhost:3000 | Interface utilisateur |
| API + Docs | http://localhost:8000/docs | FastAPI Swagger |
| PostgreSQL | localhost:5432 | Base de données |
| MQTT | localhost:1883 | Broker Mosquitto |

---

## 🌐 Réseau Thread IPv6 simulé

| Rôle | Adresse IPv6 | Ressource CoAP |
|------|-------------|----------------|
| Leader | fd00:db8::1 | — |
| Router | fd00:db8::2 | — |
| End Device GPS | fd00:db8::10 | coap://[fd00:db8::10]:5683/gps |
| End Device Batterie | fd00:db8::11 | coap://[fd00:db8::11]:5683/battery |
| End Device Température | fd00:db8::12 | coap://[fd00:db8::12]:5683/temperature |

---

## 📊 Flux de données

```
Flux 1 : WebUI → POST /api/runners → FastAPI → PostgreSQL
Flux 2 : FastAPI → GET coap://[fd00:db8::10]:5683/gps (simulé)
Flux 3 : FastAPI → MQTT /tracking/{id}/gps → Mosquitto
```

---

## ✅ Validation des plages

| Capteur | Plage |
|---------|-------|
| GPS Latitude | [-90, 90]° |
| GPS Longitude | [-180, 180]° |
| Batterie | [0, 100]% |
| Température | [-40, 60]°C |

---

## 🧪 Tests rapides

```bash
# Health check
curl http://localhost:8000/health

# Créer un coureur
curl -X POST http://localhost:8000/api/runners \
  -H "Content-Type: application/json" \
  -d '{"name":"Alice","email":"alice@test.com"}'

# Démarrer une session
curl -X POST http://localhost:8000/api/sessions \
  -H "Content-Type: application/json" \
  -d '{"runner_id":1}'

# Poll CoAP (simule lecture des 3 noeuds Thread)
curl -X POST http://localhost:8000/api/coap/poll/1
```

---

## 🏗️ Justification PostgreSQL

- Relations claires : Runner → Sessions → Mesures (intégrité FK)
- ACID : données GPS critiques, pas de perte/doublons
- Requêtes complexes : distance totale, historiques par session
