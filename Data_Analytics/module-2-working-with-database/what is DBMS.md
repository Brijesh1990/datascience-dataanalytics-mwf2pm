# what is DBMS ? 
 1. stands for database management systems
 2. DBMS stored an information of data in form of database 
 3. DBMS used some rules to manage databases 

## Codd's 12 Rules (Relational Database Principles)

Edgar F. Codd defined 12 rules that a DBMS should follow to be considered truly relational. Commonly referred to as Codd's rules:

1. Information rule: All information is represented logically as values in tables.

2. Guaranteed access rule: Every datum is logically accessible by table name, primary key, and column name.

3. Systematic treatment of null values: The DBMS must support a representation of missing information and inapplicable values.

4. Dynamic online catalog based on the relational model: The DBMS catalog (metadata) must be stored relationally and accessible via the same query language.

5. Comprehensive data sublanguage rule: The system must support at least one relational language (e.g., SQL) with data definition, manipulation, and transaction control.

6. View updating rule: All theoretically updatable views must be updatable by the system.

7. High-level insert, update, and delete: The DBMS should support set-at-a-time insert, update, and delete operations.

8. Physical data independence: Application programs and ad hoc programs remain unaffected when physical storage changes.

9. Logical data independence: Application programs and ad hoc programs remain unaffected when logical schema changes (e.g., adding a column).

10. Integrity independence: Integrity constraints must be stored in the catalog and not in application programs.

11. Distribution independence: The user should not be aware of whether the data is distributed across multiple locations.

12. Non-subversion rule: If the system provides a low-level (record-at-a-time) interface, it must not be able to subvert the integrity rules and constraints expressed in the higher-level relational language.

These rules are guiding principles; most commercial RDBMS implement many but not always all rules fully.

 