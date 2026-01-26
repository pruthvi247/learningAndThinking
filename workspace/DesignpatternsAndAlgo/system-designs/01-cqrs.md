![[Pasted image 20260104203106.png]]
Here’s how it works:

1. The client sends a command to update the system state. A Command Handler validates and executes logic using the Domain Model.
2. Changes are saved in the Write Database and can also be saved to an Event Store. Events are emitted to update the Read Model asynchronously.
3. The projections are stored in the Read Database. This database is eventually consistent with the Write Database.
4. On the query side, the client sends a query to retrieve data.
5. A Query Handler fetches data from the Read Database, which contains precomputed projections.
6. Results are returned to the client without hitting the write model or the write database.