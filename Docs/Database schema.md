# Database Schema: Visual LLM

## Overview

The Visual LLM system utilizes a graph database, Neo4j, to store and manage the knowledge graph and the relationships between ideas. The database schema is designed to efficiently represent the idea tree structure and facilitate querying and traversal of the knowledge graph.

## Nodes

### Idea Node

- id (UUID): Unique identifier for the idea node.
- text (String): The text content of the idea.
- created_at (Timestamp): Timestamp indicating when the idea was created.
- updated_at (Timestamp): Timestamp indicating when the idea was last updated.
- user_id (UUID): Foreign key referencing the user who created the idea.
- session_id (UUID): Foreign key referencing the brainstorming session the idea belongs to.

### User Node

- id (UUID): Unique identifier for the user node.
- username (String): The username of the user.
- email (String): The email address of the user.
- created_at (Timestamp): Timestamp indicating when the user account was created.

### Session Node

- id (UUID): Unique identifier for the session node.
- name (String): The name or title of the brainstorming session.
- description (String): A brief description of the brainstorming session.
- created_at (Timestamp): Timestamp indicating when the session was created.
- updated_at (Timestamp): Timestamp indicating when the session was last updated.
- owner_id (UUID): Foreign key referencing the user who created the session.

## Relationships

### PARENT_OF

Represents the parent-child relationship between ideas in the idea tree.
Connects an idea node to its parent idea node.

Properties:

- created_at (Timestamp): Timestamp indicating when the relationship was created.

### RELATED_TO

Represents the relationship between ideas that are conceptually related or similar.
Connects an idea node to another idea node.

Properties:

- weight (Float): The strength or relevance of the relationship between the ideas.
- created_at (Timestamp): Timestamp indicating when the relationship was created.

### CREATED_BY

Represents the relationship between an idea and the user who created it.  
Connects an idea node to a user node.

Properties:

- created_at (Timestamp): Timestamp indicating when the idea was created by the user.

### BELONGS_TO

Represents the relationship between an idea and the brainstorming session it belongs to.
Connects an idea node to a session node.

Properties:

- created_at (Timestamp): Timestamp indicating when the idea was added to the session.

### VOTED_ON

Represents the relationship between a user and an idea they voted on.
Connects a user node to an idea node.

Properties:

- vote (Integer): The vote value (e.g., +1 for upvote, -1 for downvote).
- created_at (Timestamp): Timestamp indicating when the user voted on the idea.

### COMMENTED_ON

Represents the relationship between a user and an idea they commented on.  
Connects a user node to an idea node.

Properties:

- comment (String): The text content of the comment.
- created_at (Timestamp): Timestamp indicating when the user commented on the idea.

## Indexes

Create an index on the text property of the Idea node to enable efficient text-based searches.

Create an index on the created_at property of the Idea node to support sorting and filtering based on creation time.

Create indexes on the user_id and session_id properties of the Idea node to optimize queries involving user and session relationships.

## Constraints

Ensure uniqueness of the username and email properties in the User node.

Enforce referential integrity for the user_id and session_id foreign keys in the Idea node.

## Query Examples

Retrieve all ideas in a specific brainstorming session:

```cypher
MATCH (session:Session {id: $sessionId})
MATCH (idea:Idea)-[:BELONGS_TO]->(session)
RETURN idea
```

Find the parent idea of a given idea:

```cypher
MATCH (idea:Idea {id: $ideaId})<-[:PARENT_OF]-(parentIdea:Idea)
RETURN parentIdea
```

Get all child ideas of a given idea:

```cypher
MATCH (idea:Idea
```
