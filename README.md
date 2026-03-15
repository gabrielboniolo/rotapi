# 🗺️ rotapi

Microservices-based system for Brazilian address management and geospatial distance calculation, built as an MVP for the **Software Architecture** course — **Software Engineering | PUC-Rio**.

---

## 📁 Services

| Directory | Description |
|---|---|
| [`rotapi_address/`](./rotapi_address) | Main API — orchestrates address management, integrates with ViaCEP for ZIP code lookup and delegates distance calculations to `rotapi_calc` |
| [`rotapi_calc/`](./rotapi_calc) | Secondary API — stateless microservice that calculates the geodesic distance between two coordinates using the Haversine formula |

Each service runs independently and has its own documentation, dependencies, and Docker setup. Refer to the `README.md` inside each directory for setup and execution instructions.

---

## 👨‍💻 Author

Developed by **Gabriel Boniolo** | Software Engineering — PUC-Rio
