# User Analytics & Semantic Search System

A backend system built with FastAPI that tracks user events, provides analytics, and enables AI-powered semantic search using embeddings.

## Features

### Event Tracking API

Track user events and store them in PostgreSQL.

**Endpoint**

```http
POST /track
```

**Request**

```json
{
  "userId": "123",
  "event": "user viewed pricing page",
  "event_metadata": {
    "page": "/pricing"
  }
}
```

**Capabilities**

* Store user events
* Generate embeddings using FastEmbed
* Store embeddings separately from event data
* Input validation using Pydantic

---

### Analytics API

Provides aggregated insights from tracked events.

**Endpoint**

```http
GET /analytics
```

**Supported Filters**

```http
GET /analytics?event=pricing
GET /analytics?from=2026-01-01
GET /analytics?to=2026-01-31
```

**Returns**

* Total events
* Events per user
* Most active users

Example Response:

```json
{
  "total_events": 10,
  "events_per_user": {
    "1": 4,
    "2": 6
  },
  "most_active_users": [
    {
      "user_id": "2",
      "event_count": 6
    }
  ]
}
```

---

### Semantic Search API

Search events using semantic similarity instead of exact keyword matching.

**Endpoint**

```http
GET /search?query=pricing
```

**Workflow**

1. Generate embedding for search query
2. Compare with stored event embeddings
3. Calculate cosine similarity
4. Return most relevant events

Example Response:

```json
{
  "query": "pricing",
  "total_results": 2,
  "results": [
    {
      "event_id": "123",
      "user_id": "1",
      "event": "customer opened pricing page",
      "similarity_score": 0.82
    }
  ]
}
```

---

## Tech Stack

* FastAPI
* PostgreSQL
* SQLAlchemy (Async)
* Alembic
* FastEmbed
* NumPy
* Pydantic v2

---

## Project Structure

```text
app/
├── api/
│   ├── track.py
│   ├── analytics.py
│   └── search.py
│
├── core/
│   └── config.py
│
├── db/
│   ├── database.py
│   ├── base.py
│   └── base_imports.py
│
├── models/
│   ├── event.py
│   └── event_embedding.py
│
├── schemas/
│   ├── event.py
│   ├── analytics.py
│   └── search.py
│
├── services/
│   ├── event_service.py
│   ├── event_embedding_service.py
│   ├── embedding_service.py
│   ├── analytics_service.py
│   └── search_service.py
│
├── utils/
│   └── similarity.py
│
└── main.py
```

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

---

## Architecture

```text
POST /track
        │
        ▼
 Store Event
        │
        ▼
 Generate Embedding
   (FastEmbed)
        │
        ▼
 Store Embedding

GET /analytics
        │
        ▼
 Aggregation Queries
        │
        ▼
 Analytics Response

GET /search
        │
        ▼
 Query Embedding
        │
        ▼
 Cosine Similarity
        │
        ▼
 Ranked Results
```

---

## Design Decisions

### Why Separate Event and Embedding Tables?

Event data and vector data serve different purposes.

Keeping embeddings in a separate table:

* Improves maintainability
* Keeps event records lightweight
* Makes migration to a vector database easier
* Follows separation of concerns

### Why FastEmbed?

FastEmbed provides lightweight and efficient embedding generation suitable for semantic search without requiring large model dependencies.

### Why JSONB for Embeddings?

The assignment allowed using a vector database or a similar approach.

For simplicity and portability:

* Embeddings are stored in PostgreSQL JSONB columns
* Semantic search is performed in the application layer
* Architecture can easily migrate to pgvector, FAISS, ChromaDB, Pinecone, or Qdrant

### Similarity Metric

Cosine Similarity is used to compare query embeddings with stored event embeddings.

---

## Error Handling

Implemented:

* Pydantic request validation
* Empty field validation
* Database transaction rollback
* FastAPI exception handling

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

### Configure Environment Variables

Create a `.env` file:

```env
DATABASE_URL=postgresql+asyncpg://postgres:password@localhost:5432/user_analytics
```

### Run Migrations

```bash
alembic upgrade head
```

### Start Server

```bash
uvicorn app.main:app --reload
```

### API Documentation

```text
http://127.0.0.1:8000/docs
```

---

## Future Improvements

* pgvector integration
* FAISS integration
* Similar Users API
* Background embedding generation
* Pagination for search results
* Caching layer
* User management and authentication

---

## Author

Sheetal Sawkare

Backend Assignment Submission
