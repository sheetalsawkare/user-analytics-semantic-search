# User Analytics & Semantic Search System

## Overview

A FastAPI-based backend system for tracking user events, generating embeddings, providing analytics, and performing semantic search.

### Features

* Event Tracking API
* Analytics API
* Semantic Search API
* PostgreSQL Persistence
* Embedding Storage
* Vector Similarity Search
* Pydantic Validation
* Error Handling
* Alembic Database Migrations

---

## Tech Stack

* FastAPI
* PostgreSQL
* SQLAlchemy (Async)
* Alembic
* FastEmbed
* NumPy

---

## Database Design

### events

| Column         | Type     |
| -------------- | -------- |
| id             | UUID     |
| user_id        | String   |
| event          | Text     |
| event_metadata | JSONB    |
| timestamp      | DateTime |
| created_at     | DateTime |

### event_embeddings

| Column     | Type     |
| ---------- | -------- |
| id         | UUID     |
| event_id   | UUID     |
| embedding  | JSONB    |
| created_at | DateTime |

### Design Decision

Embeddings are stored in a separate table instead of the events table.

Benefits:

* Separation of concerns
* Easier migration to FAISS/Pinecone/ChromaDB
* Better scalability
* Cleaner schema

---

## Setup Instructions

### Clone Repository

```bash
git clone <repository-url>
cd user-analytics-semantic-search
```

### Create Virtual Environment

```bash
python -m venv venv
source venv/bin/activate
```

### Install Dependencies

```bash
pip install -r requirements.txt
```

### Configure Database

Create PostgreSQL database:

```sql
CREATE DATABASE user_analytics;
```

Update database configuration if required.

### Run Migrations

```bash
alembic upgrade head
```

### Start Application

```bash
uvicorn app.main:app --reload
```

Application:

```text
http://127.0.0.1:8000
```

Swagger Docs:

```text
http://127.0.0.1:8000/docs
```

---

# APIs

## 1. Track Event

POST /track

Request

```json
{
  "userId": "1",
  "event": "customer opened pricing page",
  "event_metadata": {
    "page": "/pricing"
  }
}
```

Response

```json
{
  "id": "uuid",
  "user_id": "1",
  "event": "customer opened pricing page"
}
```

---

## 2. Analytics

GET /analytics

Response

```json
{
  "total_events": 4,
  "events_per_user": {
    "1": 2,
    "2": 1,
    "3": 1
  },
  "most_active_users": [
    {
      "user_id": "1",
      "event_count": 2
    }
  ]
}
```

Filters

```http
GET /analytics?event=pricing
GET /analytics?from_date=2026-01-01
GET /analytics?to_date=2026-01-31
```

---

## 3. Semantic Search

GET /search?query=pricing

Response

```json
{
  "query": "pricing",
  "total_results": 2,
  "results": [
    {
      "event_id": "uuid",
      "user_id": "1",
      "event": "customer opened pricing page",
      "similarity_score": 0.78
    }
  ]
}
```

---

## Embedding Strategy

FastEmbed is used to generate vector embeddings from event text.

Workflow:

1. User event received
2. Event stored in PostgreSQL
3. Text converted into embedding
4. Embedding stored separately
5. Search query converted to embedding
6. Cosine similarity performed
7. Top matching events returned

---

## Scalability Considerations

Current implementation stores embeddings in PostgreSQL (JSONB).

For production systems:

* FAISS
* Pinecone
* ChromaDB
* pgvector

can replace the current storage/search layer with minimal changes.

---

## Future Improvements

* Similar Users API
* Background embedding generation
* pgvector integration
* Caching
* Pagination
* Authentication & Authorization

---
