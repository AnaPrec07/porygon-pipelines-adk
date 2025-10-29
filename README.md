# Porygon Pipelines: Enterprise AI Agent for Data Exploration

> **A production-ready AI agent built with Google Cloud's Agent Development Kit (ADK) that accelerates time to insights through a conversational interface for enterprise decision-making.**

[![GitHub Page](https://img.shields.io/badge/GitHub%20Page-More%20Details-blue?style=flat-square)](https://anaprec07.github.io/porygon-pipelines-adk/)
[![Security](https://img.shields.io/badge/Security-Enterprise%20Grade-green?style=flat-square)]()
[![Scalability](https://img.shields.io/badge/Scalability-Petabyte%20Ready-blue?style=flat-square)]()
[![ROI](https://img.shields.io/badge/ROI-%20Time%20Savings-orange?style=flat-square)]()


## Executive Summary 

**Porygon Pipelines ADK** represents a paradigm shift in enterprise data accessibility, transforming the process of performing complex BigQuery analytics into natural language conversations. This production-ready AI agent eliminates technical barriers while maintaining enterprise-grade security, governance, and scalability requirements. It achieves: 

- **Reduction** in time-to-insight for routine analytical queries.
- **Democratization of the data exploration** processes by providing a conversational interface for insight discovery.
- **Increase** in data-driven decision velocity across business units.

---

## The Need Addressed
Before this implementation, the e-commerce company with name **The Look E-commerce** faced the below issues:

- **Data Access Bottlenecks**: Most leaders required analyst intermediaries for basic data exploration, delaying decision making.
- **Lack of resource optimization**: Senior analysts spent valuable time performing routine queries for business stakeholders. This interface liberates senior analyst time. 
- **Compliance & Governance Gaps**: Ad-hoc data sharing increases security risks and regulatory exposure

---

## Technology Stack & Architecture Rationale

### Core Technology Decisions

| Component | Technology | Strategic Rationale |
|-----------|------------|-------------------|
| **AI Foundation** | Google Agent Development Kit (ADK) and Vertex AI | Provides with enterprise-grade LLM orchestration with built-in production monitoring |
| **Data Platform** | BigQuery | Performative, Scalable, Cost-efficient, Seamless integration, Supports analytics|
| **Security Layer** | Google Cloud IAM + Service Accounts | Zero-trust architecture with read-only access and granular permissions |


### Agent Intelligence Architecture
```
┌─────────────────────────────────────────────────────────────┐
│                    User Interface Layer                     │
│  Natural Language Input → Context Understanding → Response  │
├─────────────────────────────────────────────────────────────┤
│                   Gemini Pro Language Model                 │
│  • Query interpretation & business context understanding    │
│  • Multi-turn conversation management                       │
│  • Result summarization & insight generation                │
├─────────────────────────────────────────────────────────────┤
│                      Tool Orchestration                     │
│  BigQueryToolset: SQL execution, schema introspection,      │
│  result formatting, cost optimization, error handling       │
├─────────────────────────────────────────────────────────────┤
│                    Data & Security Layer                    │
│  BigQuery: Enterprise data warehouse with IAM controls      │
└─────────────────────────────────────────────────────────────┘
```

### Project Structure & Scalability

```
.
├── config
│   └── credentials
│       └── service_account.json
├── deployment
│   ├── __ini__.py
│   └── remote.py               # Vertex AI deployment automation
├── docs
├── index.html
├── poetry.lock                 # Dependency management
├── pyproject.toml              # Dependency management
├── README.md
└── root_agent                  # Enterprise agent core
    ├── __init__.py
    ├── agent.py                # Root Agent
    └── tools
        ├── __init__.py
        └── bigquery.py.        # ADK Built-in BigQueryToolset
```

---

## Next Steps

Next steps include: 
1. Definition and implementation of model evaluation, testing and monitoring strategies.
2. Total cost of ownership estimation.
3. Implementation of CI/CD workflows following the Google provided [agent-starter-pack](https://github.com/GoogleCloudPlatform/agent-starter-pack)
4. Creation of backend interface with `Flask` and `Cloud Run`.
5. Creation of front end interface with `Streamlit`.

---

Built with ❤️ using Google Cloud's Agent Development Kit. Inspired by Brandon Hancock's AI tutorial — see
[Brandon Hancock's AI tutorial on YouTube](https://www.youtube.com/watch?v=bPtKnDIVEsg) for more.