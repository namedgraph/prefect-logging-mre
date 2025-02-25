# Steps to reproduce

```shell
prefect server start
prefect worker start --pool "Test pool" --work-queue "default"
prefect config set PREFECT_LOGGING_EXTRA_LOGGERS=logging_mre
prefect config set PREFECT_LOGGING_LEVEL=INFO
poetry run prefect --no-prompt deploy --all --prefect-file ./prefect.yaml
```

# Expected UI log

```
Worker 'ProcessWorker 78137b3b-eb73-442e-9634-ce41d1620346' submitting flow run 'eadb74af-d789-4c0c-be78-cbd9d47922b9'
Opening process...
Completed submission of flow run 'eadb74af-d789-4c0c-be78-cbd9d47922b9'
Beginning flow run 'daffy-marmoset' for flow 'Main Flow'
Starting the main flow
Logging something every second
Logging something every second
Logging something every second
Logging something every second
Logging something every second
Logging something every second
Logging something every second
Logging something every second
Logging something every second
Logging something every second
Main flow completed
Finished in state Completed()
Process 26172 exited cleanly.
```

# Actual UI log

```
Worker 'ProcessWorker 78137b3b-eb73-442e-9634-ce41d1620346' submitting flow run 'eadb74af-d789-4c0c-be78-cbd9d47922b9'
Opening process...
Completed submission of flow run 'eadb74af-d789-4c0c-be78-cbd9d47922b9'
Beginning flow run 'daffy-marmoset' for flow 'Main Flow'
Starting the main flow
Main flow completed
Finished in state Completed()
Process 26172 exited cleanly.
```
