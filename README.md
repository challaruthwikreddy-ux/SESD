# Courier and Parcel Tracking Lab

## Sequence diagram

```mermaid
sequenceDiagram
    actor Customer
    participant Website as Tracking Website
    participant System as Tracking System
    participant DB as Parcel Database
    actor Courier

    Customer->>Website: Enter tracking number
    Website->>System: Request parcel status
    System->>DB: Find parcel
    DB-->>System: Return current status
    System-->>Website: Send status
    Website-->>Customer: Display status

    Courier->>System: Submit new parcel status
    System->>DB: Save status update
    DB-->>System: Confirm update
    System-->>Courier: Show update saved
```

## Run the tests

Install pytest and run the unit tests:

```bash
python -m pip install pytest
python -m pytest
```

The GitHub Actions workflow runs pytest automatically whenever code is pushed or a pull request is opened.
